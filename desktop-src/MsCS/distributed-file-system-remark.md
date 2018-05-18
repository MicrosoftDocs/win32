---
title: Remark
description: Provides a description of the Distributed File System resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'de99484e-5526-42f2-a1aa-1be29d7c4bb1'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Remark Failover Cluster ,for file system", "Remark Failover Cluster"]
topic_type:
- apiref
api_name:
- Remark
api_type:
- NA
---

# Remark

Provides a description of the Distributed File System [resource](resources.md). The following table summarizes the attributes of the **Remark** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Optional                                                         |
| Structure | [**CLUSPROP\_SZ**](clusprop-sz.md)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The [**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md) macro creates a [**CLUSPROP\_SZ**](clusprop-sz.md) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **Remark** can be set with the following example code.


```C++
WCHAR                szRemarkData[] = L"File Share Description";
CLUSPROP_SZ_DECLARE( RemarkValue, 
                     sizeof(szRemarkData) / sizeof(WCHAR) );

RemarkValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
RemarkValue.cbLength  =  sizeof( szRemarkData );
StringCbCopy( RemarkValue.sz, RemarkValue.cbLength, szRemarkData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Distributed File System Private Properties](distributed-file-system-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](clusprop-sz.md)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md)
</dt> </dl>

 

 





