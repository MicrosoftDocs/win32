---
title: Features of the Replication Model for Active Directory Domain Services
description: The replication model used in Active Directory Domain Services is called multi-master loose consistency with convergence.
ms.assetid: 8fd63871-68b4-4ed6-8165-145cbc90c213
ms.tgt_platform: multiple
keywords:
- Active Directory Domain Services, Replication Model
- Replication Model Features Active Directory
ms.topic: article
ms.date: 05/31/2018
---

# Features of the Replication Model for Active Directory Domain Services

The replication model used in Active Directory Domain Services is called *multi-master loose consistency with convergence*. In this model, the directory can have many replicas; a replication system propagates changes made at any given replica to all other replicas. The replicas are not guaranteed to be consistent with each other at any particular time ("loose consistency"), because changes can be applied to any replica at any time ("multi-master"). If the system is allowed to reach a steady state, in which no new updates are occurring and all previous updates have been completely replicated, all replicas are guaranteed to converge on the same set of values ("convergence").

 

 




