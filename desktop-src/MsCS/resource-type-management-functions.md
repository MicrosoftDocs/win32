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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Resource Type Management Functions

The resource type management functions manage [cluster resource types](resource-types.md).

## In this section

<dl> <dt>

[*ClusterResourceTypeCloseEnum*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_resource_type_close_enum?branch=master)
</dt> <dd>

Closes a [resource type](resource-types.md) enumeration handle.

</dd> <dt>

[*ClusterResourceTypeEnum*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_resource_type_enum?branch=master)
</dt> <dd>

Enumerates a [resource type's](resource-types.md) possible owner [nodes](nodes.md) or resources

</dd> <dt>

[*ClusterResourceTypeGetEnumCount*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_resource_type_get_enum_count?branch=master)
</dt> <dd>

Returns the number of [cluster objects](cluster-objects.md) associated with a [resource\_type](resource-types.md) enumeration handle.

</dd> <dt>

[*ClusterResourceTypeOpenEnum*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_resource_type_open_enum?branch=master)
</dt> <dd>

Opens an enumerator for iterating through a [resource type's](resource-types.md) possible owner [nodes](nodes.md) or resources.

</dd> <dt>

[*CreateClusterResourceType*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_create_cluster_resource_type?branch=master)
</dt> <dd>

Creates a [resource type](resource-types.md) in a [cluster](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

[*DeleteClusterResourceType*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_delete_cluster_resource_type?branch=master)
</dt> <dd>

Removes a [resource type](resource-types.md) from a [cluster](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

[**RegisterClusterResourceTypeNotifyV2**](/windows/previous-versions/ClusApi/nf-clusapi-registerclusterresourcetypenotifyv2?branch=master)
</dt> <dd>

Adds a notification type to a cluster notification port.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Object Management Functions](cluster-object-management-functions.md)
</dt> </dl>

 

 




