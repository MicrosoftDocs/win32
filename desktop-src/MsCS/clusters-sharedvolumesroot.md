---
title: SharedVolumesRoot
description: Specifies the root directory from which the cluster shared volumes (CSVs) are linked.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 28D26F55-9276-47B3-B4DB-59477ADE89F9
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- SharedVolumesRoot Failover Cluster
topic_type:
- apiref
api_name:
- SharedVolumesRoot
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SharedVolumesRoot

Specifies the root directory from which the cluster shared volumes (CSVs) are linked.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | **NULL**-terminated Unicode string                               |
| Access    | [Read-only](read-only-properties.md)                            |
| Structure | [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The constant for this property is **CLUSTER\_SHARED\_VOLUMES\_ROOT**.

The entire path of a CSV share is stored if the share is part of a [scale out file server](scale-out-file-server.md), so the system root drive must be identical for all cluster nodes within that type of file server.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





