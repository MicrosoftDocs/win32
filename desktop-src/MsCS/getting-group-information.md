---
title: Getting Group Information
description: The following table lists group-related information and objects and the recommended API elements for obtaining them. If the specified API element does not have an example, look in the Index of Examples for a similar API element.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '37fbce00-5513-4476-8e36-955d2c871605'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["groups Failover Cluster , retrieving information"]
---

# Getting Group Information

The following table lists [group](groups.md)-related information and objects and the recommended API elements for obtaining them. If the specified API element does not have an example, look in the [Index of Examples](index-of-examples.md) for a similar API element.



| Information or object to get            | API element to use                                                                                                                                                                                                                                                                                                                                                |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cluster that contains the group         | [**GetClusterFromGroup**](getclusterfromgroup.md)                                                                                                                                                                                                                                                                                                                |
| GUID identifying the group              | [CLUSCTL\_GROUP\_GET\_ID](clusctl-group-get-id.md)                                                                                                                                                                                                                                                                                                               |
| Name of the group                       | [CLUSCTL\_GROUP\_GET\_NAME](clusctl-group-get-name.md)                                                                                                                                                                                                                                                                                                           |
| Properties of the group                 | [CLUSCTL\_GROUP\_GET\_COMMON\_PROPERTIES](clusctl-group-get-common-properties.md), [CLUSCTL\_GROUP\_GET\_RO\_COMMON\_PROPERTIES](clusctl-group-get-ro-common-properties.md), [CLUSCTL\_GROUP\_GET\_PRIVATE\_PROPERTIES](clusctl-group-get-private-properties.md), [CLUSCTL\_GROUP\_GET\_RO\_PRIVATE\_PROPERTIES](clusctl-group-get-ro-private-properties.md), |
| Property names                          | [CLUSCTL\_GROUP\_ENUM\_COMMON\_PROPERTIES](clusctl-group-enum-common-properties.md), [CLUSCTL\_GROUP\_ENUM\_PRIVATE\_PROPERTIES](clusctl-group-enum-private-properties.md)                                                                                                                                                                                      |
| Preferred owner nodes                   | [**ClusterGroupOpenEnum**](clustergroupopenenum.md), [**ClusterGroupEnum**](clustergroupenum.md), [**ClusterGroupCloseEnum**](clustergroupcloseenum.md)                                                                                                                                                                                                        |
| [Resources](resources.md) in the group | [**ClusterGroupOpenEnum**](clustergroupopenenum.md), [**ClusterGroupEnum**](clustergroupenum.md), [**ClusterGroupCloseEnum**](clustergroupcloseenum.md)                                                                                                                                                                                                        |
| State of the group                      | [**GetClusterGroupState**](getclustergroupstate.md)                                                                                                                                                                                                                                                                                                              |



 

For additional group-related API elements, see [Group Management Functions](group-management-functions.md) and [Group Control Codes](group-control-codes.md).

 

 




