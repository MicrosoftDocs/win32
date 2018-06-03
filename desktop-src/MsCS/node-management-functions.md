---
title: Node Management Functions
description: The node management functions manage cluster nodes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 18981eec-42c0-4e31-8e5c-b79d8ff89fc8
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- cluster object management functions Failover Cluster ,node management functions
- node management functions Failover Cluster
- nodes Failover Cluster ,management functions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Node Management Functions

The node management functions manage [cluster nodes](nodes.md).

## In this section

<dl> <dt>

[*AddClusterNode*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_add_cluster_node)
</dt> <dd>

Adds a [node](nodes.md) to an existing cluster.

</dd> <dt>

[*CloseClusterNode*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_close_cluster_node)
</dt> <dd>

Closes a [node](nodes.md) handle.

</dd> <dt>

[*ClusterNodeCloseEnum*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_node_close_enum)
</dt> <dd>

Closes a [node](nodes.md) enumeration handle.

</dd> <dt>

[*ClusterNodeCloseEnumEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_node_close_enum_ex)
</dt> <dd>

Closes a node enumeration handle.

</dd> <dt>

[*ClusterNodeEnum*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_node_enum)
</dt> <dd>

Enumerates the [network interfaces](network-interfaces.md) or [groups](groups.md) installed on a [node](nodes.md), returning the name of each with each call.

</dd> <dt>

[*ClusterNodeEnumEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_node_enum_ex)
</dt> <dd>

Retrieves the specified cluster node from a [**CLUSTER\_ENUM\_ITEM**](/previous-versions/windows/desktop/api/ClusApi/ns-clusapi-_cluster_enum_item) enumeration.

</dd> <dt>

[*ClusterNodeGetEnumCount*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_node_get_enum_count)
</dt> <dd>

Returns the number of [cluster objects](cluster-objects.md) associated with a [node](nodes.md) enumeration handle.

</dd> <dt>

[*ClusterNodeGetEnumCountEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_node_get_enum_count_ex)
</dt> <dd>

Returns the number of cluster objects that are associated with a node enumeration handle.

</dd> <dt>

[*ClusterNodeOpenEnum*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_node_open_enum)
</dt> <dd>

Opens an enumerator for iterating through the [network interfaces](network-interfaces.md) or [groups](groups.md) installed on a [node](nodes.md).

</dd> <dt>

[*ClusterNodeOpenEnumEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_node_open_enum_ex)
</dt> <dd>

Opens an enumerator that can iterate through the network interfaces or groups that are installed on a node.

</dd> <dt>

[*EvictClusterNode*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_evict_cluster_node)
</dt> <dd>

Deletes a [node](nodes.md) from the [cluster database](cluster-database.md).

</dd> <dt>

[*EvictClusterNodeEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_evict_cluster_node_ex)
</dt> <dd>

Evicts a [node](nodes.md) from the [cluster](https://www.bing.com/search?q=cluster) and initiates cleanup operations on the node.

</dd> <dt>

[*GetClusterFromNode*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_from_node)
</dt> <dd>

Returns a handle to the [cluster](https://www.bing.com/search?q=cluster) associated with a [node](nodes.md).

</dd> <dt>

[*GetClusterNodeId*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_node_id)
</dt> <dd>

Returns the unique identifier of a cluster [node](nodes.md).

</dd> <dt>

[*GetClusterNodeState*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_node_state)
</dt> <dd>

Returns the current state of a [node](nodes.md).

</dd> <dt>

[**GetCurrentClusterNodeId**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-getcurrentclusternodeid)
</dt> <dd>

Returns the unique identifier of the current cluster [node](nodes.md).

</dd> <dt>

[*GetNodeClusterState*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_node_cluster_state)
</dt> <dd>

Determines whether the [Cluster service](cluster-service.md) is installed and running on a [node](nodes.md).

</dd> <dt>

[*OpenClusterNode*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_open_cluster_node)
</dt> <dd>

Opens a [node](nodes.md) and returns a handle to it.

</dd> <dt>

[*OpenClusterNodeEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_open_cluster_node_ex)
</dt> <dd>

Opens a [node](nodes.md) and returns a handle to it.

</dd> <dt>

[*PauseClusterNode*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_pause_cluster_node)
</dt> <dd>

Requests that a [node](nodes.md) temporarily suspend its [cluster](https://www.bing.com/search?q=cluster) activity. The **PCLUSAPI\_PAUSE\_CLUSTER\_NODE** type defines a pointer to this function.

</dd> <dt>

[*PauseClusterNodeEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_pause_cluster_node_ex)
</dt> <dd>

Requests that a node temporarily suspends its cluster activity.

</dd> <dt>

[*ResumeClusterNode*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_resume_cluster_node)
</dt> <dd>

Requests that a paused [node](nodes.md) resume its [cluster](https://www.bing.com/search?q=cluster) activity. The **PCLUSAPI\_RESUME\_CLUSTER\_NODE** type defines a pointer to this function.

</dd> <dt>

[*ResumeClusterNodeEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_resume_cluster_node_ex)
</dt> <dd>

Initiates the specified failback operation, and then requests that a paused node resumes cluster activity.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Object Management Functions](cluster-object-management-functions.md)
</dt> </dl>

 

 




