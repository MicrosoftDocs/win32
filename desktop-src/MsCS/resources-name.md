---
title: Name
description: Provides the name of the resource. The following table summarizes the attributes of the Name property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 61a4a2bc-e18f-4fac-82f0-8d5ef58e8d70
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Name Failover Cluster ,for resources
- Name Failover Cluster
topic_type:
- apiref
api_name:
- Name
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Name

Provides the name of the [resource](resources.md). The following table summarizes the attributes of the **Name** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read-only](read-only-properties.md)                            |
| Structure | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

Resource names are not case sensitive. A resource name must be unique within the cluster. The name is set when the resource is created and can be changed using the [**SetClusterResourceName**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_set_cluster_resource_name?branch=master) function.

Because the **Name** property is read-only, it cannot be changed using the [CLUSCTL\_RESOURCE\_SET\_COMMON\_PROPERTIES](clusctl-resource-set-common-properties.md) control code. Applications can change a resource's name only by calling [**SetClusterResourceName**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_set_cluster_resource_name?branch=master).

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[CLUSCTL\_RESOURCE\_SET\_COMMON\_PROPERTIES](clusctl-resource-set-common-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**SetClusterResourceName**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_set_cluster_resource_name?branch=master)
</dt> </dl>

 

 





