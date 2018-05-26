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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Group Management Functions

The group management functions manage [cluster groups](groups.md).

## In this section

<dl> <dt>

[*AddClusterGroupDependency*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_add_cluster_group_dependency?branch=master)
</dt> <dd>

Adds a dependency between two cluster groups.

</dd> <dt>

[**CancelClusterGroupOperation**](/windows/previous-versions/ClusAPI/nf-clusapi-cancelclustergroupoperation?branch=master)
</dt> <dd>

Enables a client to cancel a [**MoveClusterGroup**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_move_cluster_group?branch=master) or [**MoveClusterGroupEx**](/windows/previous-versions/ClusAPI/nf-clusapi-moveclustergroupex?branch=master) operation that is pending for a group. The group is then returned to its persistent state.

</dd> <dt>

[*CloseClusterGroup*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_close_cluster_group?branch=master)
</dt> <dd>

Closes a [group](groups.md) handle.

</dd> <dt>

[*ClusterGroupCloseEnum*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_group_close_enum?branch=master)
</dt> <dd>

Closes a [group](groups.md) enumeration handle.

</dd> <dt>

[*ClusterGroupCloseEnumEx*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_group_close_enum_ex?branch=master)
</dt> <dd>

Closes the enumeration and frees any memory held by the *hGroupEnumEx* handle.

</dd> <dt>

[*ClusterGroupEnum*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_group_enum?branch=master)
</dt> <dd>

Enumerates the [resources](resources.md) in a [group](groups.md) or the [nodes](nodes.md) that are the preferred owners of a group, returning the name of the resource or node with each call.

</dd> <dt>

[*ClusterGroupEnumEx*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_group_enum_ex?branch=master)
</dt> <dd>

Retrieves an item in the enumeration.

</dd> <dt>

[*ClusterGroupGetEnumCount*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_group_get_enum_count?branch=master)
</dt> <dd>

Returns the number of [cluster objects](cluster-objects.md) associated with a [group](groups.md) enumeration handle.

</dd> <dt>

[*ClusterGroupGetEnumCountEx*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_group_get_enum_count_ex?branch=master)
</dt> <dd>

Returns the number of elements in the enumeration.

</dd> <dt>

[*ClusterGroupOpenEnum*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_group_open_enum?branch=master)
</dt> <dd>

Opens an enumerator for iterating through a [group's](groups.md) [resources](resources.md) and/or the [nodes](nodes.md) that are included in its list of preferred owners.

</dd> <dt>

[*ClusterGroupOpenEnumEx*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_group_open_enum_ex?branch=master)
</dt> <dd>

Opens a handle to the group enumeration.

</dd> <dt>

[*CreateClusterGroup*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_create_cluster_group?branch=master)
</dt> <dd>

Adds a [group](groups.md) to a [cluster](c-gly.md#-wolf-cluster-gly) and returns a handle to the newly added group.

</dd> <dt>

[*CreateClusterGroupEx*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_create_cluster_groupex?branch=master)
</dt> <dd>

Creates a new cluster group with the options specified in the **CLUSTER\_CREATE\_GROUP\_INFO** structure in a single operation.

</dd> <dt>

[*DeleteClusterGroup*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_delete_cluster_group?branch=master)
</dt> <dd>

Removes an offline and empty [group](groups.md) from a [cluster](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

[*DestroyClusterGroup*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_destroy_cluster_group?branch=master)
</dt> <dd>

Deletes the specified [group](groups.md) from a [cluster](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

[*GetClusterFromGroup*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_from_group?branch=master)
</dt> <dd>

Returns a handle to the [cluster](c-gly.md#-wolf-cluster-gly) associated with a [group](groups.md).

</dd> <dt>

[*GetClusterGroupState*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_group_state?branch=master)
</dt> <dd>

Returns the current state of a [group](groups.md).

</dd> <dt>

[*MoveClusterGroup*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_move_cluster_group?branch=master)
</dt> <dd>

Moves a [group](groups.md) and all of its [resources](resources.md) from one [node](nodes.md) to another.

</dd> <dt>

[**MoveClusterGroupEx**](/windows/previous-versions/ClusAPI/nf-clusapi-moveclustergroupex?branch=master)
</dt> <dd>

Extends the existing [**MoveClusterGroup**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_move_cluster_group?branch=master) method with the addition of flags and a buffer.

</dd> <dt>

[*OfflineClusterGroup*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_offline_cluster_group?branch=master)
</dt> <dd>

Takes a [group](groups.md) offline.

</dd> <dt>

[**OfflineClusterGroupEx**](/windows/previous-versions/ClusAPI/nf-clusapi-offlineclustergroupex?branch=master)
</dt> <dd>

Extends the [**OfflineClusterGroup**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_offline_cluster_group?branch=master) method. The client can use the flags to control failover policies of the group and the input buffer to send specific instructions for the offline operation to the resources in the target group. For instance, the input buffer can be used to instruct a virtual machine to go offline by saving its state as opposed to shutting down.

</dd> <dt>

[*OnlineClusterGroup*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_online_cluster_group?branch=master)
</dt> <dd>

Brings a [group](groups.md) online.

</dd> <dt>

[**OnlineClusterGroupEx**](/windows/previous-versions/ClusAPI/nf-clusapi-onlineclustergroupex?branch=master)
</dt> <dd>

Brings a [group](groups.md) online.

</dd> <dt>

[*OpenClusterGroup*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_open_cluster_group?branch=master)
</dt> <dd>

Opens a failover cluster [group](groups.md) and returns a handle to it.

</dd> <dt>

[*OpenClusterGroupEx*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_open_cluster_group_ex?branch=master)
</dt> <dd>

Opens a failover cluster [group](groups.md) and returns a handle to it.

</dd> <dt>

[*RemoveClusterGroupDependency*](/windows/previous-versions/clusapi/nc-clusapi-pclusapi_remove_cluster_group_dependency?branch=master)
</dt> <dd>

Removes a dependency between two cluster groups.

</dd> <dt>

[*SetClusterGroupName*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_set_cluster_group_name?branch=master)
</dt> <dd>

Sets the name for a [group](groups.md).

</dd> <dt>

[*SetClusterGroupNodeList*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_set_cluster_group_node_list?branch=master)
</dt> <dd>

Sets the preferred [node](nodes.md) list for a [group](groups.md).

</dd> <dt>

[*SetGroupDependencyExpression*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_set_group_dependency_expression?branch=master)
</dt> <dd>

Sets the dependency expression for a cluster group.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Object Management Functions](cluster-object-management-functions.md)
</dt> </dl>

 

 




