---
title: Group Management Functions
description: The group management functions manage cluster groups.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a2336594-ac24-476e-94e8-460a31c1f643
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- failover cluster object management functions Failover Cluster ,group management functions
- cluster object management functions Failover Cluster ,group management functions
- group management functions Failover Cluster
- groups Failover Cluster , management functions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Group Management Functions

The group management functions manage [cluster groups](groups.md).

## In this section

<dl> <dt>

[*AddClusterGroupDependency*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_add_cluster_group_dependency)
</dt> <dd>

Adds a dependency between two cluster groups.

</dd> <dt>

[**CancelClusterGroupOperation**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-cancelclustergroupoperation)
</dt> <dd>

Enables a client to cancel a [**MoveClusterGroup**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_move_cluster_group) or [**MoveClusterGroupEx**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-moveclustergroupex) operation that is pending for a group. The group is then returned to its persistent state.

</dd> <dt>

[*CloseClusterGroup*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_close_cluster_group)
</dt> <dd>

Closes a [group](groups.md) handle.

</dd> <dt>

[*ClusterGroupCloseEnum*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_group_close_enum)
</dt> <dd>

Closes a [group](groups.md) enumeration handle.

</dd> <dt>

[*ClusterGroupCloseEnumEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_group_close_enum_ex)
</dt> <dd>

Closes the enumeration and frees any memory held by the *hGroupEnumEx* handle.

</dd> <dt>

[*ClusterGroupEnum*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_group_enum)
</dt> <dd>

Enumerates the [resources](resources.md) in a [group](groups.md) or the [nodes](nodes.md) that are the preferred owners of a group, returning the name of the resource or node with each call.

</dd> <dt>

[*ClusterGroupEnumEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_group_enum_ex)
</dt> <dd>

Retrieves an item in the enumeration.

</dd> <dt>

[*ClusterGroupGetEnumCount*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_group_get_enum_count)
</dt> <dd>

Returns the number of [cluster objects](cluster-objects.md) associated with a [group](groups.md) enumeration handle.

</dd> <dt>

[*ClusterGroupGetEnumCountEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_group_get_enum_count_ex)
</dt> <dd>

Returns the number of elements in the enumeration.

</dd> <dt>

[*ClusterGroupOpenEnum*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_group_open_enum)
</dt> <dd>

Opens an enumerator for iterating through a [group's](groups.md) [resources](resources.md) and/or the [nodes](nodes.md) that are included in its list of preferred owners.

</dd> <dt>

[*ClusterGroupOpenEnumEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_group_open_enum_ex)
</dt> <dd>

Opens a handle to the group enumeration.

</dd> <dt>

[*CreateClusterGroup*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_create_cluster_group)
</dt> <dd>

Adds a [group](groups.md) to a [cluster](https://www.bing.com/search?q=cluster) and returns a handle to the newly added group.

</dd> <dt>

[*CreateClusterGroupEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_create_cluster_groupex)
</dt> <dd>

Creates a new cluster group with the options specified in the **CLUSTER\_CREATE\_GROUP\_INFO** structure in a single operation.

</dd> <dt>

[*DeleteClusterGroup*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_delete_cluster_group)
</dt> <dd>

Removes an offline and empty [group](groups.md) from a [cluster](https://www.bing.com/search?q=cluster).

</dd> <dt>

[*DestroyClusterGroup*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_destroy_cluster_group)
</dt> <dd>

Deletes the specified [group](groups.md) from a [cluster](https://www.bing.com/search?q=cluster).

</dd> <dt>

[*GetClusterFromGroup*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_from_group)
</dt> <dd>

Returns a handle to the [cluster](https://www.bing.com/search?q=cluster) associated with a [group](groups.md).

</dd> <dt>

[*GetClusterGroupState*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_group_state)
</dt> <dd>

Returns the current state of a [group](groups.md).

</dd> <dt>

[*MoveClusterGroup*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_move_cluster_group)
</dt> <dd>

Moves a [group](groups.md) and all of its [resources](resources.md) from one [node](nodes.md) to another.

</dd> <dt>

[**MoveClusterGroupEx**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-moveclustergroupex)
</dt> <dd>

Extends the existing [**MoveClusterGroup**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_move_cluster_group) method with the addition of flags and a buffer.

</dd> <dt>

[*OfflineClusterGroup*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_offline_cluster_group)
</dt> <dd>

Takes a [group](groups.md) offline.

</dd> <dt>

[**OfflineClusterGroupEx**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-offlineclustergroupex)
</dt> <dd>

Extends the [**OfflineClusterGroup**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_offline_cluster_group) method. The client can use the flags to control failover policies of the group and the input buffer to send specific instructions for the offline operation to the resources in the target group. For instance, the input buffer can be used to instruct a virtual machine to go offline by saving its state as opposed to shutting down.

</dd> <dt>

[*OnlineClusterGroup*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_online_cluster_group)
</dt> <dd>

Brings a [group](groups.md) online.

</dd> <dt>

[**OnlineClusterGroupEx**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-onlineclustergroupex)
</dt> <dd>

Brings a [group](groups.md) online.

</dd> <dt>

[*OpenClusterGroup*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_open_cluster_group)
</dt> <dd>

Opens a failover cluster [group](groups.md) and returns a handle to it.

</dd> <dt>

[*OpenClusterGroupEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_open_cluster_group_ex)
</dt> <dd>

Opens a failover cluster [group](groups.md) and returns a handle to it.

</dd> <dt>

[*RemoveClusterGroupDependency*](/previous-versions/windows/desktop/api/clusapi/nc-clusapi-pclusapi_remove_cluster_group_dependency)
</dt> <dd>

Removes a dependency between two cluster groups.

</dd> <dt>

[*SetClusterGroupName*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_set_cluster_group_name)
</dt> <dd>

Sets the name for a [group](groups.md).

</dd> <dt>

[*SetClusterGroupNodeList*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_set_cluster_group_node_list)
</dt> <dd>

Sets the preferred [node](nodes.md) list for a [group](groups.md).

</dd> <dt>

[*SetGroupDependencyExpression*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_set_group_dependency_expression)
</dt> <dd>

Sets the dependency expression for a cluster group.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Object Management Functions](cluster-object-management-functions.md)
</dt> </dl>

 

 




