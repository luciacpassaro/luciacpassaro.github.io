function normalizePublicationText(text) {
  return (text || "")
    .toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .trim();
}

function setupPublicationFilters() {
  const searchInput = document.getElementById("pub-search");
  const yearSelect = document.getElementById("pub-year");
  const items = Array.from(document.querySelectorAll(".pub-item"));

  if (!searchInput || !yearSelect || items.length === 0) {
    return;
  }

  function filterPublications() {
    const query = normalizePublicationText(searchInput.value);
    const selectedYear = yearSelect.value;

    items.forEach(function (item) {
      const text = normalizePublicationText(item.textContent || "");
      const year = item.getAttribute("data-year") || "";

      const matchesSearch = query === "" || text.includes(query);
      const matchesYear = selectedYear === "all" || year === selectedYear;

      if (matchesSearch && matchesYear) {
        item.style.setProperty("display", "grid", "important");
      } else {
        item.style.setProperty("display", "none", "important");
      }
    });
  }

  searchInput.addEventListener("input", filterPublications);
  searchInput.addEventListener("change", filterPublications);
  searchInput.addEventListener("search", filterPublications);
  yearSelect.addEventListener("change", filterPublications);

  filterPublications();
}

window.addEventListener("load", setupPublicationFilters);