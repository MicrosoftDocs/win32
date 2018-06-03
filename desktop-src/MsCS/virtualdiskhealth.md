---
title: VirtualDiskHealth
description: Specifies the health of the virtual disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 79C0FD7B-C7F4-4EE1-8615-4D2058FB4FC3
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- VirtualDiskHealth Failover Cluster
topic_type:
- apiref
api_name:
- VirtualDiskHealth
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# VirtualDiskHealth

Specifies the health of the virtual disk.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 0                                         |
| Maximum   | 4                                         |
| Default   | 0                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_STORAGESPACE\_HEALTH**.

This property can be set to one of the following values:



| Value | Description                                |
|-------|--------------------------------------------|
| 0     | The health of the virtual disk is unknown. |
| 1     | The virtual disk is unhealthy.             |
| 2     | The virtual disk has a health warning..    |
| 3     | The virtual disk is healthy.               |
| 4     | This is the maximum value.                 |



 

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Physical Disk Private Properties](physical-disk-private-properties.md)
</dt> </dl>

 

 





