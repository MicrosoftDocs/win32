---
title: Failover Cluster Network Management Functions
description: The failover cluster network management functions manage cluster networks.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7908db54-f432-4aee-aaf4-91f763ffa3a0
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- cluster object management functions Failover Cluster ,network management functions
- failover cluster object management functions Failover Cluster ,network management functions
- network management functions Failover Cluster
- networks Failover Cluster ,management functions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Failover Cluster Network Management Functions

The failover cluster network management functions manage [cluster networks](networks.md).

## In this section

<dl> <dt>

[*CloseClusterNetwork*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_close_cluster_network)
</dt> <dd>

Closes a [network](networks.md) handle.

</dd> <dt>

[*ClusterNetworkCloseEnum*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_network_close_enum)
</dt> <dd>

Closes a [network](networks.md) enumeration handle.

</dd> <dt>

[*ClusterNetworkEnum*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_network_enum)
</dt> <dd>

Enumerates [cluster objects](cluster-objects.md) on a [network](networks.md), returning the name of one object with each call.

</dd> <dt>

[*ClusterNetworkGetEnumCount*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_network_get_enum_count)
</dt> <dd>

Returns the number of [cluster objects](cluster-objects.md) associated with a [network](networks.md) enumeration handle.

</dd> <dt>

[*ClusterNetworkOpenEnum*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_network_open_enum)
</dt> <dd>

Opens an enumerator for iterating through [objects](cluster-objects.md) on a [network](networks.md).

</dd> <dt>

[*GetClusterFromNetwork*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_from_network)
</dt> <dd>

Returns a handle to the [cluster](https://www.bing.com/search?q=cluster) associated with a [network](networks.md).

</dd> <dt>

[*GetClusterNetworkId*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_network_id)
</dt> <dd>

Returns the identifier of a [network](networks.md).

</dd> <dt>

[*GetClusterNetworkState*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_network_state)
</dt> <dd>

current state of a [network](networks.md).

</dd> <dt>

[*OpenClusterNetwork*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_open_cluster_network)
</dt> <dd>

Opens a connection to a [network](networks.md) and returns a handle to it.

</dd> <dt>

[*OpenClusterNetworkEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_open_cluster_network_ex)
</dt> <dd>

Opens a connection to a [network](networks.md) and returns a handle to it.

</dd> <dt>

[*SetClusterNetworkName*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_set_cluster_network_name)
</dt> <dd>

Sets the name for a [network](networks.md).

</dd> <dt>

[*SetClusterNetworkPriorityOrder*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_set_cluster_network_priority_order)
</dt> <dd>

Sets the priority order for the set of [networks](networks.md) used for internal communication between cluster [nodes](nodes.md).

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Object Management Functions](cluster-object-management-functions.md)
</dt> </dl>

 

 




