---
title: "Embracing Diversity: A Multi-Perspective Approach with Soft Labels"
date: 2025-01-01
publication_types:
  - "conference-paper"
authors:
  - "Muscato, Benedetta"
  - "Bushipaka, Praveen"
  - "Gezici, Gizem"
  - "Passaro, Lucia"
  - "Giannotti, Fosca"
  - "Cucinotta, Tommaso"
publication:
  name: "Proceedings of HHAI 2025: The 4th International Conference Series on Hybrid Human-Artificial Intelligence"
hugoblox:
  ids:
    doi: "10.3233/FAIA250654"
draft: false
---

## Abstract

In subjective tasks like stance detection, diverse human perspectives are often simplified into a single ground truth through label aggregation i.e. majority voting, potentially marginalizing minority viewpoints. This paper presents a Multi-Perspective framework for stance detection that explicitly incorporates annotation diversity by using soft labels derived from both human and large language model (LLM) annotations. Building on a stance detection dataset focused on controversial topics, we augment it with document summaries and new LLM-generated labels. We then compare two approaches: a baseline using aggregated hard labels, and a multi-perspective model trained on disaggregated soft labels that capture annotation distributions. Our findings show that multi-perspective models consistently outperform traditional baselines (higher F1-scores), with lower model confidence, reflecting task subjectivity. This work highlights the importance of modeling disagreement and promotes a shift toward more inclusive, perspective-aware NLP systems.
