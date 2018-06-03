---
title: Name
description: Specifies the display name of the resource type. The display name is the name that appears to administrators in the Cluster Administrator user interface. The following table summarizes the attributes of the Name property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ea20f675-9be9-4317-ad0c-03e905c87b81
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Name Failover Cluster ,for resource types
- Name Failover Cluster
topic_type:
- apiref
api_name:
- Name
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Name

Specifies the [display name](display-names.md) of the [resource type](resource-types.md). The display name is the name that appears to administrators in the [Cluster Administrator](cluster-administrator.md) user interface. The following table summarizes the attributes of the **Name** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Structure | [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

It is important to distinguish between the display name of the resource type and the registered name of the resource type. For more information, see [Display Names](display-names.md).

The [**Type**](resources-type.md) property for resources also specifies a resource type display name.

The [**CLUSPROP\_SZ\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_sz_declare) macro creates a [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **Name** can be set with the following example code:


```C++
WCHAR szNameData[] = L"Spreadsheet App";
CLUSPROP_SZ_DECLARE( NameValue, sizeof( szNameData ) / sizeof( WCHAR ) );
NameValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
NameValue.cbLength = sizeof( szNameData );
StringCbCopy( NameValue.sz, NameValue.cbLength, szNameData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_sz_declare)
</dt> <dt>

[**Type**](resources-type.md)
</dt> </dl>

 

 





