---
title: LPC and RPC Handles
description: Most of the operations implemented by the Failover Cluster API take object handles as parameters. The Cluster API creates two different types of object handles.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0fdb2024-9b04-4a38-baf9-3cdabba9bf8c'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["LPC and RPC handles Failover Cluster", "RPC handles Failover Cluster", "handles Failover Cluster", "handles Failover Cluster , LPC and RPC"]
---

# LPC and RPC Handles

Most of the operations implemented by the [Failover Cluster API](the-server-cluster-api.md) take object handles as parameters. The [Cluster API](cluster-api.md) creates two different types of object handles.

-   Handles created using local procedure calls (LPC handles).
-   Handles created using remote procedure calls (RPC handles).

To obtain any cluster object handle, the first step is acquiring a handle to the cluster that contains the object. How that handle is obtained determines the type of handles that can be obtained from it.

-   If **NULL** is passed to the [**OpenCluster**](opencluster.md) call, the Failover Cluster API creates an LPC cluster handle. All object handles created with that handle are LPC.
-   If a name is specified in the [**OpenCluster**](opencluster.md) call, the [Cluster service](cluster-service.md) creates an RPC cluster handle. All object handles created with that handle are RPC.

If the Cluster service fails on a node, LPC handles to objects that fail over become invalid, while RPC handles to the same objects remain valid. For example, an LPC handle to a group will become invalid if the group fails over due to a failure of the Cluster service, but an RPC handle will remain valid.

Some Failover Cluster API functions take more than one object handle as input parameters. Mixing LPC and RPC handles in the same call will generate an exception at minimum and can have other unpredictable effects. When using functions that take multiple object handles as parameters, be very certain that all handles are either LPC or RPC.

The following functions require multiple object handles,

-   [**AddClusterResourceDependency**](addclusterresourcedependency.md)
-   [**AddClusterResourceNode**](addclusterresourcenode.md)
-   All [Control Code Functions](control-code-functions.md)
-   [**CanResourceBeDependent**](canresourcebedependent.md)
-   [**ChangeClusterResourceGroup**](changeclusterresourcegroup.md)
-   [**OnlineClusterGroup**](onlineclustergroup.md)
-   [**RemoveClusterResourceDependency**](removeclusterresourcedependency.md)
-   [**RemoveClusterResourceNode**](removeclusterresourcenode.md)
-   [**ResUtilResourcesEqual**](resutilresourcesequal.md)
-   [**SetClusterGroupNodeList**](setclustergroupnodelist.md)
-   [**SetClusterNetworkPriorityOrder**](setclusternetworkpriorityorder.md)

 

 




