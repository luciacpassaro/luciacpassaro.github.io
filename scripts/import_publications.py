from pathlib import Path
import re
import shutil
import bibtexparser
from bibtexparser.bibdatabase import BibDatabase
import bibtexparser
from bibtexparser.bparser import BibTexParser


ROOT = Path(__file__).resolve().parents[1]
BIB_FILE = ROOT / "publications.bib"
OUT_DIR = ROOT / "content" / "publications"


def clean_text(value):
    if not value:
        return ""
    value = value.replace("\n", " ")
    value = value.replace("{", "").replace("}", "")
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def slugify(value):
    value = clean_text(value).lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    return value[:90] or "publication"


def yaml_quote(value):
    value = clean_text(value)
    value = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{value}"'


def split_authors(author_field):
    author_field = clean_text(author_field)
    if not author_field:
        return []
    return [a.strip() for a in author_field.split(" and ") if a.strip()]


def venue(entry):
    for field in ["journal", "booktitle", "publisher", "school"]:
        if entry.get(field):
            return clean_text(entry[field])
    return ""


def publication_type(entry_type):
    mapping = {
        "article": "journal-article",
        "inproceedings": "conference-paper",
        "conference": "conference-paper",
        "incollection": "book-chapter",
        "book": "book",
        "phdthesis": "thesis",
        "mastersthesis": "thesis",
        "misc": "preprint",
    }
    return mapping.get(entry_type.lower(), "publication")


def write_single_bib(entry, path):
    db = BibDatabase()
    db.entries = [entry]
    path.write_text(bibtexparser.dumps(db), encoding="utf-8")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # cancella le pubblicazioni generate, ma NON cancella _index.md
    for item in OUT_DIR.iterdir():
        if item.name == "_index.md":
            continue
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()

    with BIB_FILE.open(encoding="utf-8") as f:
        parser = BibTexParser(common_strings=True)
        db = bibtexparser.load(f, parser=parser)

    entries = db.entries
    print(f"Loaded {len(entries)} entries")

    used_slugs = set()

    for entry in entries:
        title = clean_text(entry.get("title", "Untitled publication"))
        year = clean_text(entry.get("year", ""))
        authors = split_authors(entry.get("author", ""))
        pub_venue = venue(entry)
        doi = clean_text(entry.get("doi", ""))
        url = clean_text(entry.get("url", ""))
        abstract = clean_text(entry.get("abstract", ""))
        entry_type = publication_type(entry.get("ENTRYTYPE", ""))

        base_slug = slugify(f"{year}-{title}")
        slug = base_slug
        counter = 2

        while slug in used_slugs:
            slug = f"{base_slug}-{counter}"
            counter += 1

        used_slugs.add(slug)

        pub_dir = OUT_DIR / slug
        pub_dir.mkdir(parents=True, exist_ok=True)

        date = f"{year}-01-01" if year else "1900-01-01"

        lines = [
            "---",
            f"title: {yaml_quote(title)}",
            f"date: {date}",
            "publication_types:",
            f"  - {yaml_quote(entry_type)}",
            "authors:",
        ]

        if authors:
            lines.extend([f"  - {yaml_quote(author)}" for author in authors])
        else:
            lines.append('  - "Unknown"')

        if pub_venue:
            lines.append("publication:")
            lines.append(f"  name: {yaml_quote(pub_venue)}")

        if doi:
            lines.append("hugoblox:")
            lines.append("  ids:")
            lines.append(f"    doi: {yaml_quote(doi)}")

        if url:
            lines.append(f"url: {yaml_quote(url)}")
    
        lines.extend([
            "draft: false",
            "share: false",
            "profile: false",
            "reading_time: false",
            "show_reading_time: false",
            "links: []",
            "---",
            "",
        ])

        if abstract:
            lines.extend([
                "## Abstract",
                "",
                abstract,
                "",
            ])

        (pub_dir / "index.md").write_text("\n".join(lines), encoding="utf-8")
        write_single_bib(entry, pub_dir / "cite.bib")

    print(f"Generated {len(entries)} publication pages in {OUT_DIR}")


if __name__ == "__main__":
    main()