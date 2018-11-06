---
title: What Can You Know, and When Can You Know It
description: Applications that are sensitive to latency-induced states must recognize problem states and take appropriate action.
ms.assetid: d1d0135e-2d67-47dd-82ac-4869203ce85e
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# What Can You Know, and When Can You Know It?

Applications that are sensitive to latency-induced states must recognize problem states and take appropriate action. There are two problem states: version skew and partial update. Version skew is not detectable by examining the Directory Service (remember the axiom of distributed computing stated in [Why Active Directory Domain Services Use This Replication Model](why-active-directory-domain-services-uses-this-replication-model.md)). Partial update can be detected by adding metadata to the objects that compose the related set. Suggestions for such metadata appear in subsequent sections of this document. There are avoidance strategies applications can take to reduce the possibility of both version skew and partial update. These strategies are also discussed in subsequent sections of this document.

 

 




