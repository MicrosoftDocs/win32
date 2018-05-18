---
title: Description
description: Provides comments about the group. The following table summarizes the attributes of the Description property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e9066553-e2ff-49bd-8e4d-c2b7ceb7fd7f'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Description Failover Cluster ,for groups", "Description Failover Cluster"]
topic_type:
- apiref
api_name:
- Description
api_type:
- NA
---

# Description

Provides comments about the [group](groups.md). The following table summarizes the attributes of the **Description** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Structure | [**CLUSPROP\_SZ**](clusprop-sz.md)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The [**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md) macro creates a [**CLUSPROP\_SZ**](clusprop-sz.md) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **Description** can be set with the following example code:


```C++
WCHAR szDescriptionData[] = L"Group description";
CLUSPROP_SZ_DECLARE( DescriptionValue, 
                     sizeof(szDescriptionData) / sizeof(WCHAR) );
DescriptionValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
DescriptionValue.cbLength = sizeof( szDescriptionData );
StringCbCopy( DescriptionValue.sz, 
              DescriptionValue.cbLength, 
              szDescriptionData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[**CLUSPROP\_SZ**](clusprop-sz.md)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md)
</dt> </dl>

 

 





