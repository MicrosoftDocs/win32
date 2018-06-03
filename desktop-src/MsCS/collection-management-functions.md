---
title: GroupSet Management Functions
description: The groupset management functions manage groupsets.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: D208CA56-29C5-4CC6-95AA-FA40CF775A49
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GroupSet Management Functions

The groupset management functions manage groupsets.

## In this section

<dl> <dt>

[*AddClusterGroupSetDependency*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_add_cluster_group_groupset_dependency)
</dt> <dd>

Adds a dependency between two cluster groupsets.

</dd> <dt>

[*AddClusterGroupToGroupSetDependency*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_add_cluster_group_to_group_groupset_dependency)
</dt> <dd>

Adds a dependency between a cluster group and a cluster groupset.

</dd> <dt>

[**AddCrossClusterGroupSetToGroupSetDependency**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dd>

TBD

</dd> <dt>

[**AddCrossClusterGroupToGroupDependency**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dd>

TBD

</dd> <dt>

[**AddCrossClusterGroupToGroupSetDependency**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dd>

TBD

</dd> <dt>

[**CloseClusterGroupSet**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-closeclustergroupset)
</dt> <dd>

Closes a groupset handle returned from [**OpenClusterGroupSet**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_open_cluster_group_groupset).

</dd> <dt>

[*ClusterAddGroupToGroupSet*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_add_group_to_group_groupset)
</dt> <dd>

Adds the specified group to a groupset in the cluster.

</dd> <dt>

[*ClusterGroupSetCloseEnum*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_close_cluster_group_groupset)
</dt> <dd>

Closes an open enumeration for a groupset.

</dd> <dt>

[**ClusterGroupSetEnum**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustergroupsetenum)
</dt> <dd>

Returns the next enumerable object.

</dd> <dt>

[**ClusterGroupSetGetEnumCount**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustergroupsetgetenumcount)
</dt> <dd>

Gets the number of items contained the enumerator's collection.

</dd> <dt>

[**ClusterGroupSetOpenEnum**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustergroupsetopenenum)
</dt> <dd>

Starts the enumeration of groupset for a cluster.

</dd> <dt>

[*ClusterRemoveGroupFromGroupSet*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_remove_group_from_group_groupset)
</dt> <dd>

Removes the specified group from the groupset to which it is currently a member.

</dd> <dt>

[*CreateClusterGroupSet*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_create_cluster_group_groupset)
</dt> <dd>

Adds a groupset to a [cluster](https://www.bing.com/search?q=cluster) and returns a handle to the newly added groupset.

</dd> <dt>

[*DeleteClusterGroupSet*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_delete_cluster_group_groupset)
</dt> <dd>

Deletes the specified groupset from the cluster.

</dd> <dt>

[*GetClusterFromGroupSet*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_from_group_groupset)
</dt> <dd>

TBD

</dd> <dt>

[*OpenClusterGroupSet*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_open_cluster_group_groupset)
</dt> <dd>

Opens a handle to the specified groupset.

</dd> <dt>

[*RemoveClusterGroupSetDependency*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_remove_cluster_group_groupset_dependency)
</dt> <dd>

Removes a groupset from a groupset's dependency expression.

</dd> <dt>

[*RemoveClusterGroupToGroupSetDependency*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_remove_cluster_group_to_group_groupset_dependency)
</dt> <dd>

Removes a groupset from a group's dependency expression.

</dd> <dt>

[**RemoveCrossClusterGroupSetToGroupSetDependency**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dd>

TBD

</dd> <dt>

[**RemoveCrossClusterGroupToGroupDependency**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dd>

TBD

</dd> <dt>

[**RemoveCrossClusterGroupToGroupSetDependency**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dd>

TBD

</dd> <dt>

[*SetClusterGroupSetDependencyExpression*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_set_cluster_group_groupset_dependency_expression)
</dt> <dd>

Sets the dependency expression for a cluster groupset.

</dd> </dl>

 

 




