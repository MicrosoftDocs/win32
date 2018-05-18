---
title: DllName
description: Provides the name of the dynamic-link library (DLL) for the resource type. The following table summarizes the attributes of the DllName property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '87bacea4-e031-46dd-afd2-55205f2c60a3'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["DllName Failover Cluster ,for resource types", "DllName Failover Cluster"]
topic_type:
- apiref
api_name:
- DllName
api_type:
- NA
---

# DllName

Provides the name of the dynamic-link library (DLL) for the [resource type](resource-types.md). The following table summarizes the attributes of the **DllName** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read-only](read-only-properties.md)                            |
| Structure | [**CLUSPROP\_SZ**](clusprop-sz.md)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

Because the **DllName** property is read-only, it cannot be changed using the [CLUSCTL\_RESOURCE\_TYPE\_SET\_COMMON\_PROPERTIES](clusctl-resource-type-set-common-properties.md) control code. The **DllName** property is set when the resource type is created with the [**CreateClusterResourceType**](createclusterresourcetype.md) function.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[**CLUSPROP\_SZ**](clusprop-sz.md)
</dt> <dt>

[**CreateClusterResourceType**](createclusterresourcetype.md)
</dt> </dl>

 

 





