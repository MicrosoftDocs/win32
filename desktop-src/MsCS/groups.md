---
title: Groups
description: List of characteristics of a Failover Cluster group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1e0680ba-87d0-4bf0-808c-d80485e4daa3
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- cluster objects Failover Cluster ,groups
- groups Failover Cluster
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Groups

A group is a container for cluster [resources](resources.md) with the following characteristics:

-   Groups define the units of [*failover*](f-gly.md#-wolf-failover-gly). That is, when one resource in a group fails and it is necessary to move the resource to an alternate [node](nodes.md), all of the resources in the group are moved to the alternate node.
-   A group is always owned by one node at any point in time. Likewise, a resource is always owned by a single group. These relationships ensure that all of a group's members reside on the same node.
-   Groups define dependency boundaries. A resource can establish a dependency on another resource only if both resources are in the same group. This has the effect of requiring groups to be self-sufficient units.

Groups enable resources to be combined into larger logical units. Typically a group is made up of related or dependent resources, such as an application and its associated peripherals and data. However, groups can also be established with resources that are unrelated and nondependent to balance the load or for administrative convenience.

Every group maintains a prioritized list of the nodes that can and should act as its host. The preferred nodes list is generated from two sources.

-   The Cluster service produces a list of preferred nodes for a group from the possible owners lists maintained by the resources that are members of the group.
-   Developers and administrators can add nodes to the list through the [**SetClusterGroupNodeList**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_set_cluster_group_node_list?branch=master) function.

The following topics discuss important concepts related to groups.



| Topic                                             | Information                                                                                                                                                                         |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Failover Cluster Instances](virtual-servers.md) | Describes a special kind of group that can act as a server, yet fails over like any other group.                                                                                    |
| [Failover](failover.md)                          | Provides a detailed description of how the [Cluster service](cluster-service.md) fails over groups and identifies ways that administrators and developers can affect that process. |
| [Failback](failback.md)                          | Describes how the Cluster service fails groups back to their original nodes and identifies ways to affect the process.                                                              |



 

 

 




