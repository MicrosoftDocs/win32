---
title: SnapshotAgeLimit
description: The maximum age, in UTC, to keep a snapshot of a physical disk resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '09BC97FB-511C-47D3-8AB5-EB8B11AB5930'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["SnapshotAgeLimit Failover Cluster"]
topic_type:
- apiref
api_name:
- SnapshotAgeLimit
api_type:
- NA
---

# SnapshotAgeLimit

The maximum age, in UTC, to keep a snapshot of a physical disk resource.



| Attribute            | Value                                                            |
|----------------------|------------------------------------------------------------------|
| Data type<br/> | A null-terminated Unicode string<br/>                      |
| Access<br/>    | [Read-only](read-only-properties.md)                            |
| Structure<br/> | [**CLUSPROP\_SZ**](clusprop-sz.md)                              |
| Maximum<br/>   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default<br/>   | **NULL**                                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_PHYSDISK\_CSVSNAPSHOTAGELIMIT**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Physical Disk Private Properties](physical-disk-private-properties.md)
</dt> </dl>

 

 





