---
title: Replication and Data Integrity
description: Active Directory Domain Services provide multi-master update.
ms.assetid: 99d35e16-9d1e-40d9-b1b0-600966165e45
ms.tgt_platform: multiple
keywords:
- Active Directory,using,replication and data integrity
ms.topic: article
ms.date: 05/31/2018
---

# Replication and Data Integrity

Active Directory Domain Services provide *multi-master update*. Multi-master update means that all full replicas of a given partition are writable (the partial replicas on global catalog servers are not writable.) Multi-master update means that updates are not blocked even when some replicas are inoperable. The Active Directory server propagates the changes from the updated replica to all other replicas. Replication is automatic and transparent.

For more information, see the following topics.

-   [The Replication Model in Active Directory Domain Services](replication-model-in-active-directory-domain-services.md)
-   [Replication Behavior in Active Directory Domain Services](replication-behavior-in-active-directory-domain-services.md)
-   [Detecting and Avoiding Replication Latency](detecting-and-avoiding-replication-latency.md)

 

 




