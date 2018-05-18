---
title: Group Management Functions
description: The group management functions manage cluster groups.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a2336594-ac24-476e-94e8-460a31c1f643'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["failover cluster object management functions Failover Cluster ,group management functions", "cluster object management functions Failover Cluster ,group management functions", "group management functions Failover Cluster", "groups Failover Cluster , management functions"]
---

# Group Management Functions

The group management functions manage [cluster groups](groups.md).

## In this section

<dl> <dt>

[*AddClusterGroupDependency*](addclustergroupdependency.md)
</dt> <dd>

Adds a dependency between two cluster groups.

</dd> <dt>

[**CancelClusterGroupOperation**](cancelclustergroupoperation.md)
</dt> <dd>

Enables a client to cancel a [**MoveClusterGroup**](moveclustergroup.md) or [**MoveClusterGroupEx**](moveclustergroupex.md) operation that is pending for a group. The group is then returned to its persistent state.

</dd> <dt>

[*CloseClusterGroup*](closeclustergroup.md)
</dt> <dd>

Closes a [group](groups.md) handle.

</dd> <dt>

[*ClusterGroupCloseEnum*](clustergroupcloseenum.md)
</dt> <dd>

Closes a [group](groups.md) enumeration handle.

</dd> <dt>

[*ClusterGroupCloseEnumEx*](clustergroupcloseenumex.md)
</dt> <dd>

Closes the enumeration and frees any memory held by the *hGroupEnumEx* handle.

</dd> <dt>

[*ClusterGroupEnum*](clustergroupenum.md)
</dt> <dd>

Enumerates the [resources](resources.md) in a [group](groups.md) or the [nodes](nodes.md) that are the preferred owners of a group, returning the name of the resource or node with each call.

</dd> <dt>

[*ClusterGroupEnumEx*](clustergroupenumex.md)
</dt> <dd>

Retrieves an item in the enumeration.

</dd> <dt>

[*ClusterGroupGetEnumCount*](clustergroupgetenumcount.md)
</dt> <dd>

Returns the number of [cluster objects](cluster-objects.md) associated with a [group](groups.md) enumeration handle.

</dd> <dt>

[*ClusterGroupGetEnumCountEx*](clustergroupgetenumcountex.md)
</dt> <dd>

Returns the number of elements in the enumeration.

</dd> <dt>

[*ClusterGroupOpenEnum*](clustergroupopenenum.md)
</dt> <dd>

Opens an enumerator for iterating through a [group's](groups.md) [resources](resources.md) and/or the [nodes](nodes.md) that are included in its list of preferred owners.

</dd> <dt>

[*ClusterGroupOpenEnumEx*](clustergroupopenenumex.md)
</dt> <dd>

Opens a handle to the group enumeration.

</dd> <dt>

[*CreateClusterGroup*](createclustergroup.md)
</dt> <dd>

Adds a [group](groups.md) to a [cluster](c-gly.md#-wolf-cluster-gly) and returns a handle to the newly added group.

</dd> <dt>

[*CreateClusterGroupEx*](createclustergroupex.md)
</dt> <dd>

Creates a new cluster group with the options specified in the **CLUSTER\_CREATE\_GROUP\_INFO** structure in a single operation.

</dd> <dt>

[*DeleteClusterGroup*](deleteclustergroup.md)
</dt> <dd>

Removes an offline and empty [group](groups.md) from a [cluster](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

[*DestroyClusterGroup*](destroyclustergroup.md)
</dt> <dd>

Deletes the specified [group](groups.md) from a [cluster](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

[*GetClusterFromGroup*](getclusterfromgroup.md)
</dt> <dd>

Returns a handle to the [cluster](c-gly.md#-wolf-cluster-gly) associated with a [group](groups.md).

</dd> <dt>

[*GetClusterGroupState*](getclustergroupstate.md)
</dt> <dd>

Returns the current state of a [group](groups.md).

</dd> <dt>

[*MoveClusterGroup*](moveclustergroup.md)
</dt> <dd>

Moves a [group](groups.md) and all of its [resources](resources.md) from one [node](nodes.md) to another.

</dd> <dt>

[**MoveClusterGroupEx**](moveclustergroupex.md)
</dt> <dd>

Extends the existing [**MoveClusterGroup**](moveclustergroup.md) method with the addition of flags and a buffer.

</dd> <dt>

[*OfflineClusterGroup*](offlineclustergroup.md)
</dt> <dd>

Takes a [group](groups.md) offline.

</dd> <dt>

[**OfflineClusterGroupEx**](offlineclustergroupex.md)
</dt> <dd>

Extends the [**OfflineClusterGroup**](offlineclustergroup.md) method. The client can use the flags to control failover policies of the group and the input buffer to send specific instructions for the offline operation to the resources in the target group. For instance, the input buffer can be used to instruct a virtual machine to go offline by saving its state as opposed to shutting down.

</dd> <dt>

[*OnlineClusterGroup*](onlineclustergroup.md)
</dt> <dd>

Brings a [group](groups.md) online.

</dd> <dt>

[**OnlineClusterGroupEx**](onlineclustergroupex.md)
</dt> <dd>

Brings a [group](groups.md) online.

</dd> <dt>

[*OpenClusterGroup*](openclustergroup.md)
</dt> <dd>

Opens a failover cluster [group](groups.md) and returns a handle to it.

</dd> <dt>

[*OpenClusterGroupEx*](openclustergroupex.md)
</dt> <dd>

Opens a failover cluster [group](groups.md) and returns a handle to it.

</dd> <dt>

[*RemoveClusterGroupDependency*](removeclustergroupdependency.md)
</dt> <dd>

Removes a dependency between two cluster groups.

</dd> <dt>

[*SetClusterGroupName*](setclustergroupname.md)
</dt> <dd>

Sets the name for a [group](groups.md).

</dd> <dt>

[*SetClusterGroupNodeList*](setclustergroupnodelist.md)
</dt> <dd>

Sets the preferred [node](nodes.md) list for a [group](groups.md).

</dd> <dt>

[*SetGroupDependencyExpression*](setgroupdependencyexpression.md)
</dt> <dd>

Sets the dependency expression for a cluster group.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Object Management Functions](cluster-object-management-functions.md)
</dt> </dl>

 

 




