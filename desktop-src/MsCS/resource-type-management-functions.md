---
title: Resource Type Management Functions
description: The resource type management functions manage cluster resource types.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5bcb0411-d9c1-47e7-b799-5b1fcf2a9274
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- cluster object management functions Failover Cluster ,resource type management functions
- resource type management functions Failover Cluster
- resource types Failover Cluster ,management functions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resource Type Management Functions

The resource type management functions manage [cluster resource types](resource-types.md).

## In this section

<dl> <dt>

[*ClusterResourceTypeCloseEnum*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_resource_type_close_enum)
</dt> <dd>

Closes a [resource type](resource-types.md) enumeration handle.

</dd> <dt>

[*ClusterResourceTypeEnum*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_resource_type_enum)
</dt> <dd>

Enumerates a [resource type's](resource-types.md) possible owner [nodes](nodes.md) or resources

</dd> <dt>

[*ClusterResourceTypeGetEnumCount*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_resource_type_get_enum_count)
</dt> <dd>

Returns the number of [cluster objects](cluster-objects.md) associated with a [resource\_type](resource-types.md) enumeration handle.

</dd> <dt>

[*ClusterResourceTypeOpenEnum*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_resource_type_open_enum)
</dt> <dd>

Opens an enumerator for iterating through a [resource type's](resource-types.md) possible owner [nodes](nodes.md) or resources.

</dd> <dt>

[*CreateClusterResourceType*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_create_cluster_resource_type)
</dt> <dd>

Creates a [resource type](resource-types.md) in a [cluster](https://www.bing.com/search?q=cluster).

</dd> <dt>

[*DeleteClusterResourceType*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_delete_cluster_resource_type)
</dt> <dd>

Removes a [resource type](resource-types.md) from a [cluster](https://www.bing.com/search?q=cluster).

</dd> <dt>

[**RegisterClusterResourceTypeNotifyV2**](/previous-versions/windows/desktop/api/ClusApi/nf-clusapi-registerclusterresourcetypenotifyv2)
</dt> <dd>

Adds a notification type to a cluster notification port.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Object Management Functions](cluster-object-management-functions.md)
</dt> </dl>

 

 




