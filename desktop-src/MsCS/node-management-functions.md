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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Node Management Functions

The node management functions manage [cluster nodes](nodes.md).

## In this section

<dl> <dt>

[*AddClusterNode*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_add_cluster_node?branch=master)
</dt> <dd>

Adds a [node](nodes.md) to an existing cluster.

</dd> <dt>

[*CloseClusterNode*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_close_cluster_node?branch=master)
</dt> <dd>

Closes a [node](nodes.md) handle.

</dd> <dt>

[*ClusterNodeCloseEnum*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_node_close_enum?branch=master)
</dt> <dd>

Closes a [node](nodes.md) enumeration handle.

</dd> <dt>

[*ClusterNodeCloseEnumEx*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_node_close_enum_ex?branch=master)
</dt> <dd>

Closes a node enumeration handle.

</dd> <dt>

[*ClusterNodeEnum*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_node_enum?branch=master)
</dt> <dd>

Enumerates the [network interfaces](network-interfaces.md) or [groups](groups.md) installed on a [node](nodes.md), returning the name of each with each call.

</dd> <dt>

[*ClusterNodeEnumEx*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_node_enum_ex?branch=master)
</dt> <dd>

Retrieves the specified cluster node from a [**CLUSTER\_ENUM\_ITEM**](/windows/previous-versions/ClusApi/ns-clusapi-_cluster_enum_item?branch=master) enumeration.

</dd> <dt>

[*ClusterNodeGetEnumCount*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_node_get_enum_count?branch=master)
</dt> <dd>

Returns the number of [cluster objects](cluster-objects.md) associated with a [node](nodes.md) enumeration handle.

</dd> <dt>

[*ClusterNodeGetEnumCountEx*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_node_get_enum_count_ex?branch=master)
</dt> <dd>

Returns the number of cluster objects that are associated with a node enumeration handle.

</dd> <dt>

[*ClusterNodeOpenEnum*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_node_open_enum?branch=master)
</dt> <dd>

Opens an enumerator for iterating through the [network interfaces](network-interfaces.md) or [groups](groups.md) installed on a [node](nodes.md).

</dd> <dt>

[*ClusterNodeOpenEnumEx*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_node_open_enum_ex?branch=master)
</dt> <dd>

Opens an enumerator that can iterate through the network interfaces or groups that are installed on a node.

</dd> <dt>

[*EvictClusterNode*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_evict_cluster_node?branch=master)
</dt> <dd>

Deletes a [node](nodes.md) from the [cluster database](cluster-database.md).

</dd> <dt>

[*EvictClusterNodeEx*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_evict_cluster_node_ex?branch=master)
</dt> <dd>

Evicts a [node](nodes.md) from the [cluster](c-gly.md#-wolf-cluster-gly) and initiates cleanup operations on the node.

</dd> <dt>

[*GetClusterFromNode*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_from_node?branch=master)
</dt> <dd>

Returns a handle to the [cluster](c-gly.md#-wolf-cluster-gly) associated with a [node](nodes.md).

</dd> <dt>

[*GetClusterNodeId*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_node_id?branch=master)
</dt> <dd>

Returns the unique identifier of a cluster [node](nodes.md).

</dd> <dt>

[*GetClusterNodeState*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_node_state?branch=master)
</dt> <dd>

Returns the current state of a [node](nodes.md).

</dd> <dt>

[**GetCurrentClusterNodeId**](/windows/previous-versions/ClusAPI/nf-clusapi-getcurrentclusternodeid?branch=master)
</dt> <dd>

Returns the unique identifier of the current cluster [node](nodes.md).

</dd> <dt>

[*GetNodeClusterState*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_node_cluster_state?branch=master)
</dt> <dd>

Determines whether the [Cluster service](cluster-service.md) is installed and running on a [node](nodes.md).

</dd> <dt>

[*OpenClusterNode*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_open_cluster_node?branch=master)
</dt> <dd>

Opens a [node](nodes.md) and returns a handle to it.

</dd> <dt>

[*OpenClusterNodeEx*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_open_cluster_node_ex?branch=master)
</dt> <dd>

Opens a [node](nodes.md) and returns a handle to it.

</dd> <dt>

[*PauseClusterNode*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_pause_cluster_node?branch=master)
</dt> <dd>

Requests that a [node](nodes.md) temporarily suspend its [cluster](c-gly.md#-wolf-cluster-gly) activity. The **PCLUSAPI\_PAUSE\_CLUSTER\_NODE** type defines a pointer to this function.

</dd> <dt>

[*PauseClusterNodeEx*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_pause_cluster_node_ex?branch=master)
</dt> <dd>

Requests that a node temporarily suspends its cluster activity.

</dd> <dt>

[*ResumeClusterNode*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_resume_cluster_node?branch=master)
</dt> <dd>

Requests that a paused [node](nodes.md) resume its [cluster](c-gly.md#-wolf-cluster-gly) activity. The **PCLUSAPI\_RESUME\_CLUSTER\_NODE** type defines a pointer to this function.

</dd> <dt>

[*ResumeClusterNodeEx*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_resume_cluster_node_ex?branch=master)
</dt> <dd>

Initiates the specified failback operation, and then requests that a paused node resumes cluster activity.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Object Management Functions](cluster-object-management-functions.md)
</dt> </dl>

 

 




