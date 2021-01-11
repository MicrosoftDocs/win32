---
description: The system administrator can set quotas for specific users on a volume. The administrator can also set default quotas for the volume.
ms.assetid: e8fa6a7b-f4b9-48af-9538-d41c12b7c3b6
title: System-level Administration of Disk Quotas
ms.topic: article
ms.date: 05/31/2018
---

# System-level Administration of Disk Quotas

The system administrator can set quotas for specific users on a volume. The administrator can also set default quotas for the volume. A new user on the volume receives the default quota unless the administrator established a quota specifically for that user.

The administrator can query the level of quota tracking and enforcement (or quota states), the default quota limits, and the per-user quota information. The per-user quota information contains the user's hard quota limit, warning threshold, and the quota usage. The administrator can also enable or disable quota enforcement.

There are three quota states, as shown in the following table.



| State          | Description                                                                                                                                                                              |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Quota disabled | Quota usage changes are not tracked, but the quota limits are not removed. In this state, performance is not affected by disk quotas. This is the default state.                         |
| Quota tracked  | Quota usage changes are tracked, but quota limits are not enforced. In this state, no quota violation events are generated and no file operations fail because of disk quota violations. |
| Quota enforced | Quota usage changes are tracked and quota limits are enforced.                                                                                                                           |



 

 

 



