---
title: Node Management Functions
description: The node management functions manage cluster nodes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '18981eec-42c0-4e31-8e5c-b79d8ff89fc8'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["cluster object management functions Failover Cluster ,node management functions", "node management functions Failover Cluster", "nodes Failover Cluster ,management functions"]
---

# Node Management Functions

The node management functions manage [cluster nodes](nodes.md).

## In this section

<dl> <dt>

[*AddClusterNode*](addclusternode.md)
</dt> <dd>

Adds a [node](nodes.md) to an existing cluster.

</dd> <dt>

[*CloseClusterNode*](closeclusternode.md)
</dt> <dd>

Closes a [node](nodes.md) handle.

</dd> <dt>

[*ClusterNodeCloseEnum*](clusternodecloseenum.md)
</dt> <dd>

Closes a [node](nodes.md) enumeration handle.

</dd> <dt>

[*ClusterNodeCloseEnumEx*](clusternodecloseenumex.md)
</dt> <dd>

Closes a node enumeration handle.

</dd> <dt>

[*ClusterNodeEnum*](clusternodeenum.md)
</dt> <dd>

Enumerates the [network interfaces](network-interfaces.md) or [groups](groups.md) installed on a [node](nodes.md), returning the name of each with each call.

</dd> <dt>

[*ClusterNodeEnumEx*](clusternodeenumex.md)
</dt> <dd>

Retrieves the specified cluster node from a [**CLUSTER\_ENUM\_ITEM**](cluster-enum-item.md) enumeration.

</dd> <dt>

[*ClusterNodeGetEnumCount*](clusternodegetenumcount.md)
</dt> <dd>

Returns the number of [cluster objects](cluster-objects.md) associated with a [node](nodes.md) enumeration handle.

</dd> <dt>

[*ClusterNodeGetEnumCountEx*](clusternodegetenumcountex.md)
</dt> <dd>

Returns the number of cluster objects that are associated with a node enumeration handle.

</dd> <dt>

[*ClusterNodeOpenEnum*](clusternodeopenenum.md)
</dt> <dd>

Opens an enumerator for iterating through the [network interfaces](network-interfaces.md) or [groups](groups.md) installed on a [node](nodes.md).

</dd> <dt>

[*ClusterNodeOpenEnumEx*](clusternodeopenenumex.md)
</dt> <dd>

Opens an enumerator that can iterate through the network interfaces or groups that are installed on a node.

</dd> <dt>

[*EvictClusterNode*](evictclusternode.md)
</dt> <dd>

Deletes a [node](nodes.md) from the [cluster database](cluster-database.md).

</dd> <dt>

[*EvictClusterNodeEx*](evictclusternodeex.md)
</dt> <dd>

Evicts a [node](nodes.md) from the [cluster](c-gly.md#-wolf-cluster-gly) and initiates cleanup operations on the node.

</dd> <dt>

[*GetClusterFromNode*](getclusterfromnode.md)
</dt> <dd>

Returns a handle to the [cluster](c-gly.md#-wolf-cluster-gly) associated with a [node](nodes.md).

</dd> <dt>

[*GetClusterNodeId*](getclusternodeid.md)
</dt> <dd>

Returns the unique identifier of a cluster [node](nodes.md).

</dd> <dt>

[*GetClusterNodeState*](getclusternodestate.md)
</dt> <dd>

Returns the current state of a [node](nodes.md).

</dd> <dt>

[**GetCurrentClusterNodeId**](getcurrentclusternodeid.md)
</dt> <dd>

Returns the unique identifier of the current cluster [node](nodes.md).

</dd> <dt>

[*GetNodeClusterState*](getnodeclusterstate.md)
</dt> <dd>

Determines whether the [Cluster service](cluster-service.md) is installed and running on a [node](nodes.md).

</dd> <dt>

[*OpenClusterNode*](openclusternode.md)
</dt> <dd>

Opens a [node](nodes.md) and returns a handle to it.

</dd> <dt>

[*OpenClusterNodeEx*](openclusternodeex.md)
</dt> <dd>

Opens a [node](nodes.md) and returns a handle to it.

</dd> <dt>

[*PauseClusterNode*](pauseclusternode.md)
</dt> <dd>

Requests that a [node](nodes.md) temporarily suspend its [cluster](c-gly.md#-wolf-cluster-gly) activity. The **PCLUSAPI\_PAUSE\_CLUSTER\_NODE** type defines a pointer to this function.

</dd> <dt>

[*PauseClusterNodeEx*](pauseclusternodeex.md)
</dt> <dd>

Requests that a node temporarily suspends its cluster activity.

</dd> <dt>

[*ResumeClusterNode*](resumeclusternode.md)
</dt> <dd>

Requests that a paused [node](nodes.md) resume its [cluster](c-gly.md#-wolf-cluster-gly) activity. The **PCLUSAPI\_RESUME\_CLUSTER\_NODE** type defines a pointer to this function.

</dd> <dt>

[*ResumeClusterNodeEx*](resumeclusternodeex.md)
</dt> <dd>

Initiates the specified failback operation, and then requests that a paused node resumes cluster activity.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Object Management Functions](cluster-object-management-functions.md)
</dt> </dl>

 

 




