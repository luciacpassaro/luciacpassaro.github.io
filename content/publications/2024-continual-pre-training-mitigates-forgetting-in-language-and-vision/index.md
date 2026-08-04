---
title: "Continual Pre-Training Mitigates Forgetting in Language and Vision"
date: 2024-01-01
publication_types:
  - "journal-article"
authors:
  - "Cossu, Andrea"
  - "Carta, Antonio"
  - "Passaro, Lucia"
  - "Lomonaco, Vincenzo"
  - "Tuytelaars, Tinne"
  - "Bacciu, Davide"
publication:
  name: "NEURAL NETWORKS"
hugoblox:
  ids:
    doi: "10.1016/j.neunet.2024.106492"
draft: false
---

## Abstract

: Pre-trained models are commonly used in Continual Learning to initialize the model before training on the stream of non-stationary data. However, pre-training is rarely applied during Continual Learning. We investigate the characteristics of the Continual Pre-Training scenario, where a model is continually pre-trained on a stream of incoming data and only later fine-tuned to different downstream tasks. We introduce an evaluation protocol for Continual Pre-Training which monitors forgetting against a Forgetting Control dataset not present in the continual stream. We disentangle the impact on forgetting of 3 main factors: the input modality (NLP, Vision), the architecture type (Transformer, ResNet) and the pre-training protocol (supervised, self-supervised). Moreover, we propose a Sample-Efficient Pre-training method (SEP) that speeds up the pre-training phase. We show that the pre-training protocol is the most important factor accounting for forgetting. Surprisingly, we discovered that self-supervised continual pre-training in both NLP and Vision is sufficient to mitigate forgetting without the use of any Continual Learning strategy. Other factors, like model depth, input modality and architecture type are not as crucial.
