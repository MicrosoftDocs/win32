---
title: TotalCapacity
description: Contains the total capacity, in bytes, of the storage pool.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 462BFFE2-565B-4A58-96F6-A7BF4D137923
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- TotalCapacity Failover Cluster
topic_type:
- apiref
api_name:
- TotalCapacity
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TotalCapacity

Contains the total capacity, in bytes, of the storage pool.

The following table summarizes the attributes of the **TotalCapacity** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Status    | Required                                  |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 0                                         |
| Maximum   | 0                                         |
| Default   | 0                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_STORAGESPACE\_POOLTOTALCAPACITY**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Storage Pool Private Properties](storage-pool-private-properties.md)
</dt> </dl>

 

 





