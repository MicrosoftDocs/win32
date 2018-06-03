---
title: DiskGuid
description: Specifies the disk GUID for a Physical Disk resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: A8159E4B-865F-4B24-951C-D678E2CD955B
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DiskGuid Failover Cluster
topic_type:
- apiref
api_name:
- DiskGuid
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DiskGuid

Specifies the disk **GUID** for a [Physical Disk](physical-disk.md) resource.



| Attribute | Value                                                                    |
|-----------|--------------------------------------------------------------------------|
| Data type | Null-terminated Unicode string<br/>                                |
| Access    | [Read/write](read-write-properties.md)<br/>                       |
| Status    | Required if [**DiskSignature**](disksignature.md) is missing<br/> |
| Structure | [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)                                      |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).)         |
| Default   | 0<br/>                                                             |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_PHYSDISK\_DISKGUID**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Physical Disk Private Properties](physical-disk-private-properties.md)
</dt> </dl>

 

 





