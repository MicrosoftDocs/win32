---
description: Priority inversion occurs when two or more threads with different priorities are in contention to be scheduled.
ms.assetid: 1cb2f3c9-4641-40d8-892c-768abaf6affb
title: Priority Inversion
ms.topic: article
ms.date: 05/31/2018
---

# Priority Inversion

Priority inversion is a phenomenon where a high–priority thread is indefinitely delayed while awaiting a resource held by a low–priority thread. Often, the low–priority thread cannot proceed due to the presence of an unrelated medium–priority thread. As a result, the high–priority thread is effectively denied the CPU by the lower medium–priority thread.

Imagine a scenario where a thread T1 running at priority 4 gets preempted by a higher-priority thread T2 with a priority of 8 after acquiring a lock. Subsequently, a thread T3 with a priority of 12 arrives, preempts T2, and gets blocked trying to acquire the lock held by T1. At this point, both T1 and T2 are ready to run, but since T2 has a higher priority, it continues to execute, effectively preventing T3, a higher–priority thread, from making progress because T1 is unable to run and release the lock.

The thread scheduler combats this phenomenon through a facility called AutoBoost. AutoBoost automatically tracks resource reservations and adjusts thread priorities by applying priority floors, below which a thread must never fall. For example, if a low–priority thread acquires a critical section and a higher–priority thread is blocked waiting for the critical section, the priority of the owner is raised to the maximum priority of the waiter until it releases the resource.



 



