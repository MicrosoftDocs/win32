---
title: CsvEnforceWriteThrough
description: Controls the write-through caching policy of a physical disk resource on a cluster shared volume.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '60474A33-67C3-496F-A272-DAD6C3CA44FB'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CsvEnforceWriteThrough Failover Cluster"]
topic_type:
- apiref
api_name:
- CsvEnforceWriteThrough
api_type:
- NA
---

# CsvEnforceWriteThrough

Controls the write-through caching policy of a physical disk resource on a cluster shared volume.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | 0                                         |
| Maximum   | 3                                         |
| Default   | 0                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_PHYSDISK\_CSVWRITETHROUGH**.

The **CsvEnforceWriteThrough** property can be set to one of the following values.



| Value        | Description                                                                                                                                                                                                                 |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0<br/> | Do not add write-through.<br/>                                                                                                                                                                                        |
| 1<br/> | Add write-through to all down-level I/O sent by direct I/O.<br/>                                                                                                                                                      |
| 2<br/> | Add write-through to all down-level I/O sent by direct I/O and harden the virtual desktop infrastructure (VDl) on a write-through file object.<br/>                                                                   |
| 3<br/> | Add write-through to all down-level I/O sent by direct I/O, harden the virtual desktop infrastructure (VDl) on a write-through file object, and ensure that top-level files are always opened for write-through.<br/> |



 

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Physical Disk Private Properties](physical-disk-private-properties.md)
</dt> </dl>

 

 





