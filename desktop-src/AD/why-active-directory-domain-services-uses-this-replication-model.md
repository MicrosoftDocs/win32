---
title: Why Active Directory Domain Services Uses This Replication Model
description: This topic explains the reasons for the free-form system used by Active Directory Domain Services for a replication model.
ms.assetid: 202df900-6d03-4aa8-9099-016238059ef4
ms.tgt_platform: multiple
keywords:
- Replication Model Active Directory ,advantages
ms.topic: article
ms.date: 05/31/2018
---

# Why Active Directory Domain Services Uses This Replication Model

This topic explains the reasons for the free-form system used by Active Directory Domain Services for a replication model.

Active Directory Domain Services are a free-form system for the following reasons:

-   Customers require a highly distributed solution in which parts of the directory can be spread across their networks and administered locally.
-   Large customers often grow to millions of objects, hundreds or thousands of replicas, or both.
-   Many customer networks provide only intermittent connectivity to some locations; for example, remote oil drilling platforms and ships at sea, so the system must be tolerant of partly connected or disconnected operations.

There is no way to guarantee complete awareness of the current or future state of a distributed system because knowledge of state changes must be propagated and propagation takes time, during which more state changes may occur.

Tightly coupled systems handle uncertainty by attempting to eliminate it. This is accomplished through constraints on updates, requiring all nodes or some majority of nodes to be available before updates can be performed, using distributed locking schemes or single-mastering for critical resources, constraining all nodes to be well-connected, or some combination of these techniques. The more tightly coupled the computing nodes in a distributed system are, the lower the scaling limit.

Free-form systems handle uncertainty by tolerating it. A free-form system enables the nodes to have differing views of the overall system state and provides algorithms for resolving conflicts.

Tightly coupled solutions were rejected as unsuitable for Active Directory Domain Services because of the requirements for local administration, disconnected operation, and scalability to very large numbers of nodes. The loosely coupled model chosen, multi-master loose consistency with convergence, satisfies all requirements.

 

 




