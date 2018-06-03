---
title: LPC and RPC Handles
description: Most of the operations implemented by the Failover Cluster API take object handles as parameters. The Cluster API creates two different types of object handles.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0fdb2024-9b04-4a38-baf9-3cdabba9bf8c
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- LPC and RPC handles Failover Cluster
- RPC handles Failover Cluster
- handles Failover Cluster
- handles Failover Cluster , LPC and RPC
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LPC and RPC Handles

Most of the operations implemented by the [Failover Cluster API](the-server-cluster-api.md) take object handles as parameters. The [Cluster API](cluster-api.md) creates two different types of object handles.

-   Handles created using local procedure calls (LPC handles).
-   Handles created using remote procedure calls (RPC handles).

To obtain any cluster object handle, the first step is acquiring a handle to the cluster that contains the object. How that handle is obtained determines the type of handles that can be obtained from it.

-   If **NULL** is passed to the [**OpenCluster**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_open_cluster) call, the Failover Cluster API creates an LPC cluster handle. All object handles created with that handle are LPC.
-   If a name is specified in the [**OpenCluster**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_open_cluster) call, the [Cluster service](cluster-service.md) creates an RPC cluster handle. All object handles created with that handle are RPC.

If the Cluster service fails on a node, LPC handles to objects that fail over become invalid, while RPC handles to the same objects remain valid. For example, an LPC handle to a group will become invalid if the group fails over due to a failure of the Cluster service, but an RPC handle will remain valid.

Some Failover Cluster API functions take more than one object handle as input parameters. Mixing LPC and RPC handles in the same call will generate an exception at minimum and can have other unpredictable effects. When using functions that take multiple object handles as parameters, be very certain that all handles are either LPC or RPC.

The following functions require multiple object handles,

-   [**AddClusterResourceDependency**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_add_cluster_resource_dependency)
-   [**AddClusterResourceNode**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_add_cluster_resource_node)
-   All [Control Code Functions](control-code-functions.md)
-   [**CanResourceBeDependent**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_can_resource_be_dependent)
-   [**ChangeClusterResourceGroup**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_change_cluster_resource_group)
-   [**OnlineClusterGroup**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_online_cluster_group)
-   [**RemoveClusterResourceDependency**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_remove_cluster_resource_dependency)
-   [**RemoveClusterResourceNode**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_remove_cluster_resource_node)
-   [**ResUtilResourcesEqual**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_resources_equal)
-   [**SetClusterGroupNodeList**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_set_cluster_group_node_list)
-   [**SetClusterNetworkPriorityOrder**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_set_cluster_network_priority_order)

 

 




