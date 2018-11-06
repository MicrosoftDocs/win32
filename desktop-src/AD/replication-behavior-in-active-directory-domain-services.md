---
title: Replication Behavior in Active Directory Domain Services
description: Replication behavior is consistent and predictable; given a set of changes to a given replica, the outcome can be predicted \ 8212;the changes will be propagated to all other replicas.
ms.assetid: 4e9f2e43-6375-4663-93ca-55112fd00abe
ms.tgt_platform: multiple
keywords:
- Active Directory Domain Services Active Directory , Replication
ms.topic: article
ms.date: 05/31/2018
---

# Replication Behavior in Active Directory Domain Services

Replication behavior is consistent and predictable; given a set of changes to a given replica, the outcome can be predicted—the changes will be propagated to all other replicas. Devising a reliable general model for predicting when the changes will be applied at all other replicas, or at a particular replica, is impossible, because the future state of the distributed system as a whole cannot be known. This is called "nondeterministic latency," and applications that use the directory must understand and allow for it.

The situation is not as complex at it might appear. There are only three states that an application must accommodate:

-   Version Skew: None of the changes that are applied to a given source replica have propagated to a given destination replica. An application reading the source replica sees the new version of the information, while an application reading the destination sees the old version (or nothing, if the new information was added for the first time). Version skew applies to all directory service consumers.
-   Partial Update: Some of the changes that are applied to a given source replica have propagated to a given destination replica. An application reading the source replica sees the new information, while an application reading the destination sees a mix of old and new information (or only some of the new information, if the new information was added for the first time). Partial update applies to directory service consumers that use two or more related objects to store their information.
-   Fully Replicated State: All of the changes that are applied to a given source replica have propagated to a given destination replica. Applications at the source and destination replicas see the same information.

 

 




