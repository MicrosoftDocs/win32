---
title: Core Resources
description: A cluster requires that a set of resources be online in order to operate.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '46b71882-be37-4c3f-a328-a394c1310958'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["core resources Failover Cluster", "resources Failover Cluster , core"]
---

# Core Resources

A [*cluster*](c-gly.md#-wolf-cluster-gly) requires that a set of [resources](resources.md) be online in order to operate. These resources are called the core resources, and consist of:

-   An [IP Address](ip-address.md) resource, an [IPv6 Address](ipv6-address.md) resource, and/or an [IPv6 Tunnel Address](ipv6-tunnel-address.md) resource that provides the cluster IP address.
-   A [Network Name](network-name.md) resource that provides the cluster name. This resource depends on the [IP Address](ip-address.md) resource, [IPv6 Address](ipv6-address.md) resource, and/or [IPv6 Tunnel Address](ipv6-tunnel-address.md) resource to create a failover cluster instance.
-   A quorum resource that ensures cluster integrity and the persistence of accurate state information.

The core resources reside in a single [group](groups.md) called (by default) the cluster group. The cluster group is created automatically during cluster setup.

If the core resources cannot be brought online, the cluster will not form and no resources in any group will be online. Therefore it is not necessary to create resources in the cluster group and set dependencies on the core resources in order to ensure that the cluster will be up and running before your resources are brought online.

In fact, there are good reasons for not creating resources in the cluster group. By default (as determined by the [**RestartAction**](resources-restartaction.md) property), if a resource fails the cluster initiates failover for the entire group. Failing over a group means taking all the resources in the group offline—which, for the core resources, means taking the cluster offline.

The cluster identifies the core resources by the **CLUS\_FLAG\_CORE** flag of the [**CLUS\_FLAGS**](clus-flags.md) enumeration. For information on how to get the flags for a resource, see [CLUSCTL\_RESOURCE\_GET\_FLAGS](clusctl-resource-get-flags.md).

 

 




