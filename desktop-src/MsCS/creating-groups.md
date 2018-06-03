---
title: Creating Groups
description: Creating a group involves adding and configuring the individual resources in the group and adjusting the group's properties so that the group is ready to be brought online.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c6309c0e-fe81-4946-a333-efc5d2a7cb48
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- groups Failover Cluster ,creating
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating Groups

Creating a [group](groups.md) involves adding and configuring the individual resources in the group and adjusting the group's properties so that the group is ready to be brought online.

Administrators can create groups manually through [cluster management applications](cluster-management-applications.md) such as [Cluster Administrator](cluster-administrator.md), but [*cluster-aware applications*](https://www.bing.com/search?q=*cluster-aware applications*) can ease the burden on administrators by automating group creation as much as possible.

The following sections describe the tasks associated with creating groups.

**To create a group**

1.  Obtain a cluster handle. (See [Using Object Handles](using-object-handles.md).)
2.  Obtain a unique group name. To list the names of groups currently defined in the cluster, see [Enumerating Objects](enumerating-objects.md).
3.  Create the group by calling [**CreateClusterGroup**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_create_cluster_group).
4.  Add resources to the group. To move existing resources into the group, call [**ChangeClusterResourceGroup**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_change_cluster_resource_group). To create new resources in the group, see [Creating Resources](creating-resources.md).
5.  Set properties, checkpoints, possible owners, and dependencies for the resources. (See [Configuring Resources](configuring-resources.md).)
6.  Adjust the group's failover policies. (For the properties that affect failover, see [Failover](failover.md) and [Failback](failback.md). For information on changing properties, see [Setting Properties](setting-properties.md).)
7.  If necessary, modify the group's preferred owner nodes list by calling [**SetClusterGroupNodeList**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_set_cluster_group_node_list).

## Example Code

See [Creating Failover Cluster Instances](creating-virtual-servers.md).

 

 




