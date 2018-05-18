---
title: Failover Cluster Resource Management Functions
description: The failover cluster resource management functions manage cluster resources.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd1f7360d-f592-49fb-b3b4-60d93afd7c6f'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["cluster object management functions Failover Cluster ,resource management functions", "failover cluster object management functions Failover Cluster ,resource management functions", "resource management functions Failover Cluster", "resources Failover Cluster ,management functions"]
---

# Failover Cluster Resource Management Functions

The failover cluster resource management functions manage [cluster resources](resources.md).

## In this section

<dl> <dt>

[*AddClusterResourceDependency*](addclusterresourcedependency.md)
</dt> <dd>

Creates a [dependency](resource-dependencies.md) relationship between two [resources](resources.md).

</dd> <dt>

[*AddClusterResourceNode*](addclusterresourcenode.md)
</dt> <dd>

Adds a [node](nodes.md) to the list of possible nodes that a [resource](resources.md) can run on.

</dd> <dt>

[*AddResourceToClusterSharedVolumes*](addresourcetoclustersharedvolumes.md)
</dt> <dd>

Adds storage to Cluster Shared Volumes.

</dd> <dt>

[*CanResourceBeDependent*](canresourcebedependent.md)
</dt> <dd>

Determines if one [resource](resources.md) can be [dependent](resource-dependencies.md) upon another resource.

</dd> <dt>

[*ChangeClusterResourceGroup*](changeclusterresourcegroup.md)
</dt> <dd>

Moves a [resource](resources.md) from one [group](groups.md) to another.

</dd> <dt>

[*CloseClusterResource*](closeclusterresource.md)
</dt> <dd>

Closes a [resource](resources.md) handle.

</dd> <dt>

[*ClusterResourceCloseEnum*](clusterresourcecloseenum.md)
</dt> <dd>

Closes a [resource](resources.md) enumeration handle.

</dd> <dt>

[*ClusterResourceCloseEnumEx*](clusterresourcecloseenumex.md)
</dt> <dd>

Closes a handle to a resource enumeration.

</dd> <dt>

[*ClusterResourceEnum*](clusterresourceenum.md)
</dt> <dd>

Enumerates a [resource's](resources.md) dependent resources, [nodes](nodes.md), or both.

</dd> <dt>

[*ClusterResourceEnumEx*](clusterresourceenumex.md)
</dt> <dd>

Enumerates a resource and then returns a pointer to the current dependent resource or node.

</dd> <dt>

[*ClusterResourceGetEnumCount*](clusterresourcegetenumcount.md)
</dt> <dd>

Returns the number of [cluster objects](cluster-objects.md) associated with a [resource](resources.md) enumeration handle.

</dd> <dt>

[*ClusterResourceGetEnumCountEx*](clusterresourcegetenumcountex.md)
</dt> <dd>

Returns the number of [cluster objects](cluster-objects.md) that are associated with a [resource](resources.md) enumeration handle.

</dd> <dt>

[*ClusterResourceOpenEnum*](clusterresourceopenenum.md)
</dt> <dd>

Opens an enumerator for iterating through a [resource's](resources.md) [dependencies](resource-dependencies.md) and [nodes](nodes.md).

</dd> <dt>

[*ClusterResourceOpenEnumEx*](clusterresourceopenenumex.md)
</dt> <dd>

Opens a handle to a resource enumeration that enables iteration through a resource's dependencies and nodes.

</dd> <dt>

[*ClusterSharedVolumeSetSnapshotState*](clustersharedvolumesetsnapshotstate.md)
</dt> <dd>

Updates the state of a snapshot of a cluster shared volume.

</dd> <dt>

[*CreateClusterResource*](createclusterresource.md)
</dt> <dd>

Creates a [resource](resources.md) in a [cluster](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

[*DeleteClusterResource*](deleteclusterresource.md)
</dt> <dd>

Removes an offline [resource](resources.md) from a [cluster](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

[*FailClusterResource*](failclusterresource.md)
</dt> <dd>

Initiates a [resource failure](resource-failure.md).

</dd> <dt>

[*GetClusterFromResource*](getclusterfromresource.md)
</dt> <dd>

Returns a handle to the [cluster](c-gly.md#-wolf-cluster-gly) associated with a [resource](resources.md).

</dd> <dt>

[*GetClusterResourceDependencyExpression*](getclusterresourcedependencyexpression.md)
</dt> <dd>

Retrieves the dependency expression associated with the specified resource.

</dd> <dt>

[*GetClusterResourceNetworkName*](getclusterresourcenetworkname.md)
</dt> <dd>

Retrieves the [**Name**](network-names-name.md) private property of the [Network Name](network-name.md) resource on which a [resource](resources.md) is [dependent](resource-dependencies.md).

</dd> <dt>

[*GetClusterResourceState*](getclusterresourcestate.md)
</dt> <dd>

Returns the current state of a [resource](resources.md).

</dd> <dt>

[*IsFileOnClusterSharedVolume*](isfileonclustersharedvolume.md)
</dt> <dd>

Specifies whether the file is on the cluster shared volume.

</dd> <dt>

[*OfflineClusterResource*](offlineclusterresource.md)
</dt> <dd>

Takes a [resource](resources.md) offline.

</dd> <dt>

[**OfflineClusterResourceEx**](offlineclusterresourceex.md)
</dt> <dd>

Extends the [**OfflineClusterResource**](offlineclusterresource.md) method. The client can use the flags to control policies of the resource and the input buffer to send specific instructions for the offline operation to the resource. For instance, the input buffer can be used to instruct a VM to go offline by saving its state as opposed to shutting down.

</dd> <dt>

[*OnlineClusterResource*](onlineclusterresource.md)
</dt> <dd>

Brings an offline or failed [resource](resources.md) online.

</dd> <dt>

[**OnlineClusterResourceEx**](onlineclusterresourceex.md)
</dt> <dd>

Brings an offline or failed [resource](resources.md) online.

</dd> <dt>

[*OpenClusterResource*](openclusterresource.md)
</dt> <dd>

Opens a [resource](resources.md) and returns a handle to it.

</dd> <dt>

[*OpenClusterResourceEx*](openclusterresourceex.md)
</dt> <dd>

Opens a [resource](resources.md) and returns a handle to it.

</dd> <dt>

[*RemoveClusterResourceDependency*](removeclusterresourcedependency.md)
</dt> <dd>

Removes a [dependency](resource-dependencies.md) relationship between two [resources](resources.md).

</dd> <dt>

[*RemoveClusterResourceNode*](removeclusterresourcenode.md)
</dt> <dd>

Removes a [node](nodes.md) from the list of nodes that can host a [resource](resources.md).

</dd> <dt>

[*RemoveResourceFromClusterSharedVolumes*](removeresourcefromclustersharedvolumes.md)
</dt> <dd>

Removes storage from Cluster Shared Volumes.

</dd> <dt>

[*RestartClusterResource*](restartclusterresource.md)
</dt> <dd>

Restarts a cluster resource.

</dd> <dt>

[*SetClusterResourceDependencyExpression*](setclusterresourcedependencyexpression.md)
</dt> <dd>

Specifies the dependency expression to be associated with the resource referred to by *hResource*. Any existing dependency relationships for the resource will be overwritten.

</dd> <dt>

[*SetClusterResourceName*](setclusterresourcename.md)
</dt> <dd>

Sets the name for a [resource](resources.md).

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Object Management Functions](cluster-object-management-functions.md)
</dt> </dl>

 

 




