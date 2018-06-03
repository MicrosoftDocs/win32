---
title: Getting Group Information
description: The following table lists group-related information and objects and the recommended API elements for obtaining them. If the specified API element does not have an example, look in the Index of Examples for a similar API element.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 37fbce00-5513-4476-8e36-955d2c871605
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- groups Failover Cluster , retrieving information
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Getting Group Information

The following table lists [group](groups.md)-related information and objects and the recommended API elements for obtaining them. If the specified API element does not have an example, look in the [Index of Examples](index-of-examples.md) for a similar API element.



| Information or object to get            | API element to use                                                                                                                                                                                                                                                                                                                                                |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cluster that contains the group         | [**GetClusterFromGroup**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_from_group)                                                                                                                                                                                                                                                                                                                |
| GUID identifying the group              | [CLUSCTL\_GROUP\_GET\_ID](clusctl-group-get-id.md)                                                                                                                                                                                                                                                                                                               |
| Name of the group                       | [CLUSCTL\_GROUP\_GET\_NAME](clusctl-group-get-name.md)                                                                                                                                                                                                                                                                                                           |
| Properties of the group                 | [CLUSCTL\_GROUP\_GET\_COMMON\_PROPERTIES](clusctl-group-get-common-properties.md), [CLUSCTL\_GROUP\_GET\_RO\_COMMON\_PROPERTIES](clusctl-group-get-ro-common-properties.md), [CLUSCTL\_GROUP\_GET\_PRIVATE\_PROPERTIES](clusctl-group-get-private-properties.md), [CLUSCTL\_GROUP\_GET\_RO\_PRIVATE\_PROPERTIES](clusctl-group-get-ro-private-properties.md), |
| Property names                          | [CLUSCTL\_GROUP\_ENUM\_COMMON\_PROPERTIES](clusctl-group-enum-common-properties.md), [CLUSCTL\_GROUP\_ENUM\_PRIVATE\_PROPERTIES](clusctl-group-enum-private-properties.md)                                                                                                                                                                                      |
| Preferred owner nodes                   | [**ClusterGroupOpenEnum**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_group_open_enum), [**ClusterGroupEnum**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_group_enum), [**ClusterGroupCloseEnum**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_group_close_enum)                                                                                                                                                                                                        |
| [Resources](resources.md) in the group | [**ClusterGroupOpenEnum**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_group_open_enum), [**ClusterGroupEnum**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_group_enum), [**ClusterGroupCloseEnum**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_group_close_enum)                                                                                                                                                                                                        |
| State of the group                      | [**GetClusterGroupState**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_group_state)                                                                                                                                                                                                                                                                                                              |



 

For additional group-related API elements, see [Group Management Functions](group-management-functions.md) and [Group Control Codes](group-control-codes.md).

 

 




