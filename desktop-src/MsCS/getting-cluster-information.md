---
title: Getting Cluster Information
description: Cluster information is data that pertains to the state or configuration of the cluster as a whole.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 60780f74-43bd-447d-897f-3f24911d1828
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- clusters Failover Cluster , retrieving state and configuration
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Getting Cluster Information

Cluster information is data that pertains to the state or configuration of the cluster as a whole.



| Information to get.         | API                                                                                                                                                                                                                                                                                                                                                                              |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name of the cluster         | [**GetClusterInformation**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_information?branch=master)                                                                                                                                                                                                                                                                                                                           |
| Properties of the cluster   | [CLUSCTL\_CLUSTER\_GET\_COMMON\_PROPERTIES](clusctl-cluster-get-common-properties.md), [CLUSCTL\_CLUSTER\_GET\_RO\_COMMON\_PROPERTIES](clusctl-cluster-get-ro-common-properties.md), [CLUSCTL\_CLUSTER\_GET\_RO\_PRIVATE\_PROPERTIES](clusctl-cluster-get-ro-private-properties.md), [CLUSCTL\_CLUSTER\_GET\_PRIVATE\_PROPERTIES](clusctl-cluster-get-private-properties.md) |
| Property names              | [CLUSCTL\_CLUSTER\_ENUM\_COMMON\_PROPERTIES](clusctl-cluster-enum-common-properties.md), [CLUSCTL\_CLUSTER\_ENUM\_PRIVATE\_PROPERTIES](clusctl-cluster-enum-private-properties.md)                                                                                                                                                                                             |
| Quorum resource information | [**GetClusterQuorumResource**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_quorum_resource?branch=master)                                                                                                                                                                                                                                                                                                                     |
| Version of the cluster      | [**GetClusterInformation**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_information?branch=master)                                                                                                                                                                                                                                                                                                                           |



 

For additional cluster-related API elements, see [Cluster Management Functions](cluster-management-functions.md) and [Cluster Control Codes](cluster-control-codes.md).

 

 




