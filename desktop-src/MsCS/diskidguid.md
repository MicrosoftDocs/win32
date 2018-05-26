---
title: DiskIdGuid
description: Specifies the partition GUID for a Physical Disk resource formatted with a GUID Partition Table (GPT).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 276d0131-3c0e-4b38-a388-4780768550de
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DiskIdGuid Failover Cluster , for Physical Disk private properties
- DiskIdGuid Failover Cluster
topic_type:
- apiref
api_name:
- DiskIdGuid
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DiskIdGuid

Specifies the partition **GUID** for a [Physical Disk](physical-disk.md) resource formatted with a **GUID** Partition Table (GPT). The [**DiskIdType**](diskidtype.md) property of the [Physical Disk](physical-disk.md) resource has a value of **PARTITION\_STYLE\_GPT** (1) for GPT partitioned disks. The following table summarizes the attributes of the [**DiskIdGuid**](diskarbinterval.md) property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Required if [**DiskSignature**](disksignature.md) is missing    |
| Structure | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | 0                                                                |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for [**DiskIdGuid**](diskarbinterval.md) can be set with the following example code.


```C++
WCHAR                szDiskIdGuidData[] = L"d44e4b8d-ead2-4221-b709-ccbb4ef70fd1";
CLUSPROP_SZ_DECLARE( DiskIdGuidValue, sizeof(szDiskIdGuidData) / sizeof(WCHAR) );

DiskIdGuidValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
DiskIdGuidValue.cbLength  = sizeof( szDiskIdGuidData );
StringCbCopy( DiskIdGuidValue.sz, DiskIdGuidValue.cbLength, szDiskIdGuidData );
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

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**DiskSignature**](disksignature.md)
</dt> </dl>

 

 





