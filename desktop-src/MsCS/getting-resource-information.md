---
title: Getting Resource Information
description: The following table lists resource-related information and the API elements that obtain the information. If the specified API element does not have an example, look in the Index of Examples for a similar API element.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 51eeafa6-3e00-4e99-a0b0-7d75145ef4f1
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resources Failover Cluster ,retrieving information
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Getting Resource Information

The following table lists [resource](resources.md)-related information and the API elements that obtain the information. If the specified API element does not have an example, look in the [Index of Examples](index-of-examples.md) for a similar API element.



| Information to get                    | API                                                                                                                                                                                                                                                                                                                                                                                      |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Characteristics of the resource       | [CLUSCTL\_RESOURCE\_GET\_CHARACTERISTICS](clusctl-resource-get-characteristics.md)                                                                                                                                                                                                                                                                                                      |
| Checkpoints defined for the resource  | [CLUSCTL\_RESOURCE\_GET\_CRYPTO\_CHECKPOINTS](clusctl-resource-get-crypto-checkpoints.md), [CLUSCTL\_RESOURCE\_GET\_REGISTRY\_CHECKPOINTS](clusctl-resource-get-registry-checkpoints.md)                                                                                                                                                                                               |
| Cluster that contains the resource.   | [**GetClusterFromResource**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_from_resource?branch=master)                                                                                                                                                                                                                                                                                                                                 |
| Dependencies                          | [**ClusterResourceEnum**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_resource_enum?branch=master), [**ResUtilGetResourceDependency**](/windows/previous-versions/ResApi/nc-resapi-presutil_get_resource_dependency?branch=master), [**ResUtilGetResourceDependencyByClass**](/windows/previous-versions/ResApi/nc-resapi-presutil_get_resource_dependency_by_class?branch=master), [**ResUtilGetResourceDependencyByName**](/windows/previous-versions/ResApi/nc-resapi-presutil_get_resource_dependency_by_name?branch=master), [**ResUtilGetResourceNameDependency**](/windows/previous-versions/ResApi/nc-resapi-presutil_get_resource_name_dependency?branch=master)             |
| Dependents                            | [**ClusterResourceEnum**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_resource_enum?branch=master)                                                                                                                                                                                                                                                                                                                                       |
| Disk information                      | [CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO](clusctl-resource-storage-get-disk-info.md)                                                                                                                                                                                                                                                                                                |
| Equality                              | [**ResUtilResourcesEqual**](/windows/previous-versions/ResApi/nc-resapi-presutil_resources_equal?branch=master)                                                                                                                                                                                                                                                                                                                                   |
| Flags                                 | [CLUSCTL\_RESOURCE\_GET\_FLAGS](clusctl-resource-get-flags.md)                                                                                                                                                                                                                                                                                                                          |
| Group that contains the resource      | [**GetClusterResourceState**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_resource_state?branch=master)                                                                                                                                                                                                                                                                                                                               |
| GUID                                  | [CLUSCTL\_RESOURCE\_GET\_ID](clusctl-resource-get-id.md)                                                                                                                                                                                                                                                                                                                                |
| Name                                  | [CLUSCTL\_RESOURCE\_GET\_NAME](clusctl-resource-get-name.md)                                                                                                                                                                                                                                                                                                                            |
| Network name dependency               | [CLUSCTL\_RESOURCE\_GET\_NETWORK\_NAME](clusctl-resource-get-network-name.md)                                                                                                                                                                                                                                                                                                           |
| Node that currently owns the resource | [**GetClusterResourceState**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_resource_state?branch=master)                                                                                                                                                                                                                                                                                                                               |
| Possible owner nodes                  | [**ClusterResourceEnum**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_resource_enum?branch=master)                                                                                                                                                                                                                                                                                                                                       |
| Properties                            | [CLUSCTL\_RESOURCE\_GET\_COMMON\_PROPERTIES](clusctl-resource-get-common-properties.md), [CLUSCTL\_RESOURCE\_GET\_RO\_COMMON\_PROPERTIES](clusctl-resource-get-ro-common-properties.md), [CLUSCTL\_RESOURCE\_GET\_RO\_PRIVATE\_PROPERTIES](clusctl-resource-get-ro-private-properties.md), [CLUSCTL\_RESOURCE\_GET\_PRIVATE\_PROPERTIES](clusctl-resource-get-private-properties.md) |
| Property names                        | [CLUSCTL\_RESOURCE\_ENUM\_COMMON\_PROPERTIES](clusctl-resource-enum-common-properties.md), [CLUSCTL\_RESOURCE\_ENUM\_PRIVATE\_PROPERTIES](clusctl-resource-enum-private-properties.md)                                                                                                                                                                                                 |
| Required dependencies                 | [CLUSCTL\_RESOURCE\_GET\_REQUIRED\_DEPENDENCIES](clusctl-resource-get-required-dependencies.md)                                                                                                                                                                                                                                                                                         |
| Resource class                        | [CLUSCTL\_RESOURCE\_GET\_CLASS\_INFO](clusctl-resource-get-class-info.md)                                                                                                                                                                                                                                                                                                               |
| Resource type                         | [CLUSCTL\_RESOURCE\_GET\_RESOURCE\_TYPE](clusctl-resource-get-resource-type.md)                                                                                                                                                                                                                                                                                                         |
| State                                 | [**GetClusterResourceState**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_resource_state?branch=master)                                                                                                                                                                                                                                                                                                                               |



 

For additional resource-related API elements, see [Resource Management Functions](resource-management-functions.md) and [Resource Control Codes](resource-control-codes.md).

 

 




