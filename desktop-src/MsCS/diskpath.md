---
title: DiskPath
description: If this is set to a disk (for example \ 0034;H \\ \ 0034;) then the Physical Disk resource will take control of that disk as part of the recovery process.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b5a9b876-76ce-425a-9130-1f5a8d7903aa
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DiskPath Failover Cluster , for Physical Disk private properties
- DiskPath Failover Cluster
topic_type:
- apiref
api_name:
- DiskPath
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DiskPath

Used in some recovery scenarios. If this is set to a disk (for example "H:\\") then the [*Physical Disk resource*](https://www.bing.com/search?q=*Physical Disk resource*) will take control of that disk as part of the recovery process. The following table summarizes the attributes of the **DiskPath** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Optional                                                         |
| Structure | [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | 0                                                                |



 

## Remarks

The [**CLUSPROP\_SZ\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_sz_declare) macro creates a [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **DiskPath** can be set with the following example code.


```C++
WCHAR                szDiskPathData[] = L"H:\\";
CLUSPROP_SZ_DECLARE( DiskPathValue, 
                     sizeof( szDiskPathData ) / sizeof( WCHAR ) );

DiskPathValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
DiskPathValue.cbLength  = sizeof( szDiskPathData );
StringCbCopy( DiskPathValue.sz, 
              DiskPathValue.cbLength, 
              szDiskPathData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Physical Disk Private Properties](physical-disk-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_sz_declare)
</dt> </dl>

 

 





