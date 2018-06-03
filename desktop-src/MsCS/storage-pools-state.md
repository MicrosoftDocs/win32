---
title: State
description: Specifies the state of the storage pool.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: F2579FEB-013A-4198-BCD5-6CA2D48CB266
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- State Failover Cluster
topic_type:
- apiref
api_name:
- State
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# State

Specifies the state of the storage pool.

The following table summarizes the attributes of the **State** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Status    | Required                                  |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 0                                         |
| Maximum   | 4                                         |
| Default   | 0                                         |



 

## Remarks

This property can be set to one of the following values:



| Value | Description                                                                                                |
|-------|------------------------------------------------------------------------------------------------------------|
| 0     | The state of the storage pool is unknown.                                                                  |
| 1     | A minority of the disks in the storage pool are available.                                                 |
| 2     | A majority of the disks in the storage pool are available, and the pool is functioning in a degraded mode. |
| 3     | The storage pool is fully functioning.                                                                     |
| 4     | The maximum value.                                                                                         |



 

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Storage Pool Private Properties](storage-pool-private-properties.md)
</dt> </dl>

 

 





