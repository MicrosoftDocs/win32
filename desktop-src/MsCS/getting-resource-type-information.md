---
title: Getting Resource Type Information
description: The following table lists resource type \ 8211;related information and objects and the recommended API elements for obtaining them. If the specified API element does not have an example, look in the Index of Examples for a similar element.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6f855b1a-6acc-4f96-9462-9421c362d522
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource types Failover Cluster ,retrieving information
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Getting Resource Type Information

The following table lists [resource type](resource-types.md)–related information and objects and the recommended API elements for obtaining them. If the specified API element does not have an example, look in the [Index of Examples](index-of-examples.md) for a similar element.



| Information to get                        | API element to use                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Available disks                           | [CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_AVAILABLE\_DISKS](clusctl-resource-type-storage-get-available-disks.md)                                                                                                                                                                                                                                                                                                                     |
| Characteristics of the resource type      | [CLUSCTL\_RESOURCE\_TYPE\_GET\_CHARACTERISTICS](clusctl-resource-type-get-characteristics.md)                                                                                                                                                                                                                                                                                                                                       |
| Checkpoints defined for the resource type | [CLUSCTL\_RESOURCE\_TYPE\_GET\_CRYPTO\_CHECKPOINTS](clusctl-resource-type-get-crypto-checkpoints.md), [CLUSCTL\_RESOURCE\_TYPE\_GET\_REGISTRY\_CHECKPOINTS](clusctl-resource-type-get-registry-checkpoints.md)                                                                                                                                                                                                                     |
| Name                                      | [CLUSCTL\_RESOURCE\_GET\_NAME](clusctl-resource-get-name.md)                                                                                                                                                                                                                                                                                                                                                                        |
| Possible owner nodes                      | [**ClusterResourceTypeEnum**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_resource_type_enum)                                                                                                                                                                                                                                                                                                                                                                           |
| Properties                                | [CLUSCTL\_RESOURCE\_TYPE\_GET\_COMMON\_PROPERTIES](clusctl-resource-type-get-common-properties.md), [CLUSCTL\_RESOURCE\_TYPE\_GET\_RO\_COMMON\_PROPERTIES](clusctl-resource-type-get-ro-common-properties.md), [CLUSCTL\_RESOURCE\_TYPE\_GET\_RO\_PRIVATE\_PROPERTIES](clusctl-resource-type-get-ro-private-properties.md), [CLUSCTL\_RESOURCE\_TYPE\_GET\_PRIVATE\_PROPERTIES](clusctl-resource-type-get-private-properties.md) |
| Property names                            | [CLUSCTL\_RESOURCE\_TYPE\_ENUM\_COMMON\_PROPERTIES](clusctl-resource-type-enum-common-properties.md), [CLUSCTL\_RESOURCE\_TYPE\_ENUM\_PRIVATE\_PROPERTIES](clusctl-resource-type-enum-private-properties.md)                                                                                                                                                                                                                       |
| Required dependencies                     | [CLUSCTL\_RESOURCE\_TYPE\_GET\_REQUIRED\_DEPENDENCIES](clusctl-resource-type-get-required-dependencies.md)                                                                                                                                                                                                                                                                                                                          |



 

For additional resource type–related API elements, see [Resource Type Management Functions](resource-type-management-functions.md) and [Resource Type Control Codes](resource-type-control-codes.md).

 

 




