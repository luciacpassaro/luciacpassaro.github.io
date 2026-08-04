---
title: "Deep Continual Learning for Medical Call Incidents Text Classification under the Presence of Dataset Shifts"
date: 2024-01-01
publication_types:
  - "journal-article"
authors:
  - "Ferri, Pablo"
  - "Lomonaco, Vincenzo"
  - "Passaro, Lucia C."
  - "F\\'elix-De Castro, Antonio"
  - "S\\'anchez-Cuesta, Purificaci\\'on"
  - "S\\'aez, Carlos"
  - "Garc\\'ia-G\\'omez, Juan M."
publication:
  name: "COMPUTERS IN BIOLOGY AND MEDICINE"
hugoblox:
  ids:
    doi: "10.1016/j.compbiomed.2024.108548"
draft: false
---

## Abstract

The aim of this work is to develop and evaluate a deep classifier that can effectively prioritize Emergency Medical Call Incidents (EMCI) according to their life-threatening level under the presence of dataset shifts. We utilized a dataset consisting of 1982746 independent EMCI instances obtained from the Health Services Department of the Region of Valencia (Spain), with a time span from 2009 to 2019 (excluding 2013). The dataset includes free text dispatcher observations recorded during the call, as well as a binary variable indicating whether the event was life-threatening. To evaluate the presence of dataset shifts, we examined prior probability shifts, covariate shifts, and concept shifts. Subsequently, we designed and implemented four deep Continual Learning (CL) strategies-cumulative learning, continual fine-tuning, experience replay, and synaptic intelligence-alongside three deep CL baselines-joint training, static approach, and single fine-tuning-based on DistilBERT models. Our results demonstrated evidence of prior probability shifts, covariate shifts, and concept shifts in the data. Applying CL techniques had a statistically significant ($\alpha$=0.05) positive impact on both backward and forward knowledge transfer, as measured by the F1-score, compared to non-continual approaches. We can argue that the utilization of CL techniques in the context of EMCI is effective in adapting deep learning classifiers to changes in data distributions, thereby maintaining the stability of model performance over time. To our knowledge, this study represents the first exploration of a CL approach using real EMCI data.
