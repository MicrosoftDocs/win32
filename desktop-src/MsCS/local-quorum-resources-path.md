---
title: Path
description: Indicates the default location for the quorum files on the local quorum device.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'be7014d3-e065-4183-8b8f-369ac437b29a'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Path Failover Cluster , for local quorums", "Path Failover Cluster"]
topic_type:
- apiref
api_name:
- Path
api_type:
- NA
---

# Path

\[The **Path** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Indicates the default location for the quorum files on the local quorum device. The following table summarizes the attributes of the **Path** property.



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

The property value portion of a [property list](property-lists.md) entry for **Path** can be set with the following example code.


```C++
WCHAR szPathData[] = L"G:\\ShareDirectory";
CLUSPROP_SZ_DECLARE( PathValue, 
                     sizeof( szPathData ) / sizeof( WCHAR ) );

PathValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
PathValue.cbLength  = sizeof( szPathData );
StringCbCopy( PathValue.sz, 
              PathValue.cbLength, 
              szPathData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



 

 





