---
title: PoolId
description: Specifies the global identifier (GUID) of the storage pool.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: EB769D69-906F-4672-A5DE-3DA38100A892
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- PoolId Failover Cluster
topic_type:
- apiref
api_name:
- PoolId
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PoolId

Specifies the global identifier (GUID) of the storage pool.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read-only](read-only-properties.md)                            |
| Status    | Optional                                                         |
| Structure | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_STORAGESPACE\_POOLIDGUID**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Physical Disk Private Properties](physical-disk-private-properties.md)
</dt> </dl>

 

 





