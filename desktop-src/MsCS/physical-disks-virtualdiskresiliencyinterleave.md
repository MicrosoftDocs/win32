---
title: VirtualDiskResiliencyInterleave
description: Specifies the interleave stripe size, in bytes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: DDCE49BE-88B0-43C3-A27C-BE3BD8DB5A27
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- VirtualDiskResiliencyInterleave Failover Cluster
topic_type:
- apiref
api_name:
- VirtualDiskResiliencyInterleave
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# VirtualDiskResiliencyInterleave

Specifies the interleave stripe size, in bytes.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 0                                         |
| Maximum   | 0                                         |
| Default   | 0                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_STORAGESPACE\_RESILIENCYINTERLEAVE**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Physical Disk Private Properties](physical-disk-private-properties.md)
</dt> </dl>

 

 





