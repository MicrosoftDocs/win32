---
title: Multiple and Simultaneous Property Updates
description: Order of changes when multiple properties are set with a single Failover Cluster API function call.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0e6051a8-0d1a-4b5e-abce-113e24ec96ca'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["updates to properties Failover Cluster", "properties Failover Cluster ,update process"]
---

# Multiple and Simultaneous Property Updates

When you use a single function call to set multiple properties for a single object, the cluster applies the changes as follows:

-   For [networks](networks.md) and [network interfaces](network-interfaces.md), the change is applied as a single atomic unit. Either all of the property changes will be applied or none will be applied.
-   For [groups](groups.md), [nodes](nodes.md), [resources](resources.md), and [resource types](resource-types.md), the change is not atomic. If a problem occurs during processing, the results are unpredictable. Some or none of the properties may be changed.

When the cluster receives simultaneous property change requests from multiple nodes, it applies the changes as follows:

-   For networks and network interfaces, each change is applied individually as an atomic unit. One request will either succeed or fail, then the next will succeed or fail, and so on. The order in which the requests are resolved is first come, first served.
-   Simultaneous property changes to groups, nodes, resources, and resource types are applied in an unpredictable order. For changes involving multiple properties, the order of resolution can change from property to property.

For example: Application A on Node A requests that Group N's [**AutoFailbackType**](groups-autofailbacktype.md) and [**PersistentState**](groups-persistentstate.md) properties be set to value A. At the same time, Application B on Node B requests that the same properties be changed to value B. Each individual property change request can be resolved in any order, resulting in the following possible outcomes.



| Result of A's request | Result of B's request | Final value of [**AutoFailbackType**](groups-autofailbacktype.md) | Final value of [**PersistentState**](groups-persistentstate.md) |
|-----------------------|-----------------------|--------------------------------------------------------------------|------------------------------------------------------------------|
| Error                 | Error                 | A                                                                  | B                                                                |
| Error                 | Error                 | A                                                                  | no update                                                        |
| Error                 | Error                 | B                                                                  | A                                                                |
| Error                 | Error                 | B                                                                  | no update                                                        |
| Error                 | Error                 | no update                                                          | A                                                                |
| Error                 | Error                 | no update                                                          | B                                                                |
| Error                 | Error                 | no update                                                          | no update                                                        |
| Error                 | Success               | A                                                                  | B                                                                |
| Error                 | Success               | B                                                                  | B                                                                |
| Error                 | Success               | B                                                                  | A                                                                |
| Success               | Error                 | A                                                                  | A                                                                |
| Success               | Error                 | A                                                                  | B                                                                |
| Success               | Error                 | B                                                                  | A                                                                |
| Success               | Success               | A                                                                  | A                                                                |
| Success               | Success               | A                                                                  | B                                                                |
| Success               | Success               | B                                                                  | A                                                                |
| Success               | Success               | B                                                                  | B                                                                |



 

Be sure to verify the results of a property change before relying on the value of the property in subsequent operations.

 

 




