---
title: Type
description: Specifies the display name of the resource. The following table summarizes the attributes of the Type property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e4f76b6a-f445-41f6-8c37-45f925af9dd5
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Type Failover Cluster ,for resources
- Type Failover Cluster
topic_type:
- apiref
api_name:
- Type
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Type

Specifies the display name of the resource. The following table summarizes the attributes of the **Type** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Structure | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

It is important to distinguish between the display name of the resource's type and the registered name of the resource's type. For more information, see [Display Names](display-names.md).

To access the type name of a resource type, call [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) and pass [CLUSCTL\_RESOURCE\_GET\_RESOURCE\_TYPE](clusctl-resource-get-resource-type.md) for the *dwControlCode* parameter.

The [**Name**](resource-types-name.md) property for resource types also specifies a resource type display name.

The [**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master) macro creates a [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **Type** can be set with the following example code:


```C++
WCHAR szTypeData[] = L"Generic Application";
CLUSPROP_SZ_DECLARE( TypeValue, sizeof( szTypeData ) / sizeof( WCHAR ) );
TypeValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
TypeValue.cbLength = sizeof( szTypeData );
StringCbCopy( TypeValue.sz, TypeValue.cbLength, szTypeData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[CLUSCTL\_RESOURCE\_GET\_RESOURCE\_TYPE](clusctl-resource-get-resource-type.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master)
</dt> <dt>

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master)
</dt> <dt>

[**Name**](resource-types-name.md)
</dt> </dl>

 

 





