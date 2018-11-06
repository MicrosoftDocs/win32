---
title: Effective Date and Time
description: Effective date and time is an avoidance strategy that prevents version skew and partial updates by deferring the effective data of information to some point in the future when the change has a high probability of being fully replicated.
ms.assetid: 5e24f90a-dd53-4720-815e-9a1db51847a3
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Effective Date and Time

*Effective date and time* is an avoidance strategy that prevents version skew and partial updates by deferring the effective data of information to some point in the future when the change has a high probability of being fully replicated. To implement effective dates, the application objects must include an effective date timestamp, which is filled in when the object is created or changed. Consumers of the objects verify the timestamp and defer use of the objects until that date and time are reached.

Some important considerations:

-   Applications that choose this approach must ensure that there is a set of applicable data to use until the updated objects become effective.
-   Distributed time service in Windows NT 4.0 keeps the clocks of the connected Windows 2000 synchronized. No time service is perfect, however, so there is a small window for version skew.
-   Setting a good effective date presumes knowledge of the overall replication latency for the distributed system in question. In a stable network a good rule of thumb for effective dates is the (time of the update) + (2\*(average overall latency)). So, for a system whose overall latency averages 4 hours, a delay of 8 hours is reasonable.
-   In an unstable network, determining a "good" value for effective dates is much more difficult, since the latency may be highly variable. Effective date is most "effective" in an unstable network when combined with other avoidance or detection strategies such as checksums or consistency GUIDs. For more information, see [Checksums and Object Counts](checksums-and-object-counts.md).

 

 




