---
title: Getting Node Information
description: The following table lists node-related information and objects and the recommended API elements for obtaining them. If the specified API element does not have an example, look in the Index of Examples for a similar API element.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b8d0884a-8239-4f71-b86b-a2ae29e5c92b
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- nodes Failover Cluster ,retrieving information
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Getting Node Information

The following table lists [node](nodes.md)-related information and objects and the recommended API elements for obtaining them. If the specified API element does not have an example, look in the [Index of Examples](index-of-examples.md) for a similar API element.



| Information or object to get               | API element to use                                                                                                                                                                                                                                                                                                                                        |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cluster that contains the node             | [**GetClusterFromNode**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_from_node?branch=master)                                                                                                                                                                                                                                                                                                          |
| GUID identifying the node                  | [CLUSCTL\_NODE\_GET\_ID](clusctl-node-get-id.md)                                                                                                                                                                                                                                                                                                         |
| Name of the node                           | [CLUSCTL\_NODE\_GET\_NAME](clusctl-node-get-name.md)                                                                                                                                                                                                                                                                                                     |
| Network interfaces in the node             | [**ClusterNodeOpenEnum**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_node_open_enum?branch=master), [**ClusterNodeEnum**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_node_enum?branch=master), [**ClusterNodeCloseEnum**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_node_close_enum?branch=master)                                                                                                                                                                                                      |
| Properties of the node                     | [CLUSCTL\_NODE\_GET\_COMMON\_PROPERTIES](clusctl-node-get-common-properties.md), [CLUSCTL\_NODE\_GET\_RO\_COMMON\_PROPERTIES](clusctl-node-get-ro-common-properties.md), [CLUSCTL\_NODE\_GET\_PRIVATE\_PROPERTIES](clusctl-node-get-private-properties.md), [CLUSCTL\_NODE\_GET\_RO\_PRIVATE\_PROPERTIES](clusctl-node-get-ro-private-properties.md), |
| Property names                             | [CLUSCTL\_NODE\_ENUM\_COMMON\_PROPERTIES](clusctl-node-enum-common-properties.md), [CLUSCTL\_NODE\_ENUM\_PRIVATE\_PROPERTIES](clusctl-node-enum-private-properties.md)                                                                                                                                                                                  |
| State of the Cluster service on the node   | [**GetNodeClusterState**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_node_cluster_state?branch=master)                                                                                                                                                                                                                                                                                                        |
| State of the node                          | [**GetClusterNodeState**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_node_state?branch=master)                                                                                                                                                                                                                                                                                                        |
| Version of the Cluster service on the node | [**GetClusterInformation**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_information?branch=master)                                                                                                                                                                                                                                                                                                    |



 

For additional node-related APIs, see [Node Management Functions](node-management-functions.md) and [Node Control Codes](node-control-codes.md).

 

 




