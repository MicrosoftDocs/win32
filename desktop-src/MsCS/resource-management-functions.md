---
title: Failover Cluster Resource Management Functions
description: The failover cluster resource management functions manage cluster resources.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d1f7360d-f592-49fb-b3b4-60d93afd7c6f
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- cluster object management functions Failover Cluster ,resource management functions
- failover cluster object management functions Failover Cluster ,resource management functions
- resource management functions Failover Cluster
- resources Failover Cluster ,management functions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Failover Cluster Resource Management Functions

The failover cluster resource management functions manage [cluster resources](resources.md).

## In this section

<dl> <dt>

[*AddClusterResourceDependency*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_add_cluster_resource_dependency)
</dt> <dd>

Creates a [dependency](resource-dependencies.md) relationship between two [resources](resources.md).

</dd> <dt>

[*AddClusterResourceNode*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_add_cluster_resource_node)
</dt> <dd>

Adds a [node](nodes.md) to the list of possible nodes that a [resource](resources.md) can run on.

</dd> <dt>

[*AddResourceToClusterSharedVolumes*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_add_resource_to_cluster_shared_volumes)
</dt> <dd>

Adds storage to Cluster Shared Volumes.

</dd> <dt>

[*CanResourceBeDependent*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_can_resource_be_dependent)
</dt> <dd>

Determines if one [resource](resources.md) can be [dependent](resource-dependencies.md) upon another resource.

</dd> <dt>

[*ChangeClusterResourceGroup*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_change_cluster_resource_group)
</dt> <dd>

Moves a [resource](resources.md) from one [group](groups.md) to another.

</dd> <dt>

[*CloseClusterResource*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_close_cluster_resource)
</dt> <dd>

Closes a [resource](resources.md) handle.

</dd> <dt>

[*ClusterResourceCloseEnum*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_resource_close_enum)
</dt> <dd>

Closes a [resource](resources.md) enumeration handle.

</dd> <dt>

[*ClusterResourceCloseEnumEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_resource_close_enum_ex)
</dt> <dd>

Closes a handle to a resource enumeration.

</dd> <dt>

[*ClusterResourceEnum*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_resource_enum)
</dt> <dd>

Enumerates a [resource's](resources.md) dependent resources, [nodes](nodes.md), or both.

</dd> <dt>

[*ClusterResourceEnumEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_resource_enum_ex)
</dt> <dd>

Enumerates a resource and then returns a pointer to the current dependent resource or node.

</dd> <dt>

[*ClusterResourceGetEnumCount*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_resource_get_enum_count)
</dt> <dd>

Returns the number of [cluster objects](cluster-objects.md) associated with a [resource](resources.md) enumeration handle.

</dd> <dt>

[*ClusterResourceGetEnumCountEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_resource_get_enum_count_ex)
</dt> <dd>

Returns the number of [cluster objects](cluster-objects.md) that are associated with a [resource](resources.md) enumeration handle.

</dd> <dt>

[*ClusterResourceOpenEnum*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_resource_open_enum)
</dt> <dd>

Opens an enumerator for iterating through a [resource's](resources.md) [dependencies](resource-dependencies.md) and [nodes](nodes.md).

</dd> <dt>

[*ClusterResourceOpenEnumEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_resource_open_enum_ex)
</dt> <dd>

Opens a handle to a resource enumeration that enables iteration through a resource's dependencies and nodes.

</dd> <dt>

[*ClusterSharedVolumeSetSnapshotState*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_shared_volume_set_snapshot_state)
</dt> <dd>

Updates the state of a snapshot of a cluster shared volume.

</dd> <dt>

[*CreateClusterResource*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_create_cluster_resource)
</dt> <dd>

Creates a [resource](resources.md) in a [cluster](https://www.bing.com/search?q=cluster).

</dd> <dt>

[*DeleteClusterResource*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_delete_cluster_resource)
</dt> <dd>

Removes an offline [resource](resources.md) from a [cluster](https://www.bing.com/search?q=cluster).

</dd> <dt>

[*FailClusterResource*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_fail_cluster_resource)
</dt> <dd>

Initiates a [resource failure](resource-failure.md).

</dd> <dt>

[*GetClusterFromResource*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_from_resource)
</dt> <dd>

Returns a handle to the [cluster](https://www.bing.com/search?q=cluster) associated with a [resource](resources.md).

</dd> <dt>

[*GetClusterResourceDependencyExpression*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_resource_dependency_expression)
</dt> <dd>

Retrieves the dependency expression associated with the specified resource.

</dd> <dt>

[*GetClusterResourceNetworkName*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_resource_network_name)
</dt> <dd>

Retrieves the [**Name**](network-names-name.md) private property of the [Network Name](network-name.md) resource on which a [resource](resources.md) is [dependent](resource-dependencies.md).

</dd> <dt>

[*GetClusterResourceState*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_resource_state)
</dt> <dd>

Returns the current state of a [resource](resources.md).

</dd> <dt>

[*IsFileOnClusterSharedVolume*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_is_file_on_cluster_shared_volume)
</dt> <dd>

Specifies whether the file is on the cluster shared volume.

</dd> <dt>

[*OfflineClusterResource*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_offline_cluster_resource)
</dt> <dd>

Takes a [resource](resources.md) offline.

</dd> <dt>

[**OfflineClusterResourceEx**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-offlineclusterresourceex)
</dt> <dd>

Extends the [**OfflineClusterResource**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_offline_cluster_resource) method. The client can use the flags to control policies of the resource and the input buffer to send specific instructions for the offline operation to the resource. For instance, the input buffer can be used to instruct a VM to go offline by saving its state as opposed to shutting down.

</dd> <dt>

[*OnlineClusterResource*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_online_cluster_resource)
</dt> <dd>

Brings an offline or failed [resource](resources.md) online.

</dd> <dt>

[**OnlineClusterResourceEx**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-onlineclusterresourceex)
</dt> <dd>

Brings an offline or failed [resource](resources.md) online.

</dd> <dt>

[*OpenClusterResource*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_open_cluster_resource)
</dt> <dd>

Opens a [resource](resources.md) and returns a handle to it.

</dd> <dt>

[*OpenClusterResourceEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_open_cluster_resource_ex)
</dt> <dd>

Opens a [resource](resources.md) and returns a handle to it.

</dd> <dt>

[*RemoveClusterResourceDependency*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_remove_cluster_resource_dependency)
</dt> <dd>

Removes a [dependency](resource-dependencies.md) relationship between two [resources](resources.md).

</dd> <dt>

[*RemoveClusterResourceNode*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_remove_cluster_resource_node)
</dt> <dd>

Removes a [node](nodes.md) from the list of nodes that can host a [resource](resources.md).

</dd> <dt>

[*RemoveResourceFromClusterSharedVolumes*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_remove_resource_from_cluster_shared_volumes)
</dt> <dd>

Removes storage from Cluster Shared Volumes.

</dd> <dt>

[*RestartClusterResource*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_restart_cluster_resource)
</dt> <dd>

Restarts a cluster resource.

</dd> <dt>

[*SetClusterResourceDependencyExpression*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_set_cluster_resource_dependency_expression)
</dt> <dd>

Specifies the dependency expression to be associated with the resource referred to by *hResource*. Any existing dependency relationships for the resource will be overwritten.

</dd> <dt>

[*SetClusterResourceName*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_set_cluster_resource_name)
</dt> <dd>

Sets the name for a [resource](resources.md).

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Object Management Functions](cluster-object-management-functions.md)
</dt> </dl>

 

 




