---
title: WitnessDatabaseWriteTimeout
description: Specifies the maximum amount of time, in seconds, that a cluster database write to a witness can take before the write is abandoned.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: BD192200-755C-42F2-9181-74454B882EA3
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- WitnessDatabaseWriteTimeout Failover Cluster
topic_type:
- apiref
api_name:
- WitnessDatabaseWriteTimeout
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WitnessDatabaseWriteTimeout

Specifies the maximum amount of time, in seconds, that a cluster database write to a witness can take before the write is abandoned.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 1                                         |
| Maximum   | (24 \* 60 \* 60)                          |
| Default   | (5 \* 60)                                 |



 

## Remarks

The constant for this property is **CLUSTER\_WITNESS\_DATABASE\_WRITE\_TIMEOUT**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





