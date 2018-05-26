---
title: VirtualDiskName
description: Contains the name of the virtual disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: FEBE53C0-22B1-4B3F-93C2-F9CF15A210FA
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- VirtualDiskName Failover Cluster
topic_type:
- apiref
api_name:
- VirtualDiskName
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# VirtualDiskName

Contains the name of the virtual disk.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read-only](read-only-properties.md)                            |
| Status    | Optional                                                         |
| Structure | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_STORAGESPACE\_NAME**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Physical Disk Private Properties](physical-disk-private-properties.md)
</dt> </dl>

 

 





