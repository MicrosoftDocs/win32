---
title: RouteHistoryLength
description: The number of heartbeats to log after a cluster network failure.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: E99D03A9-EB6D-4C37-B478-4330062B2701
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- RouteHistoryLength Failover Cluster
topic_type:
- apiref
api_name:
- RouteHistoryLength
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RouteHistoryLength

The number of heartbeats to log after a cluster network failure.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | 0                                         |
| Maximum   | 40                                        |
| Default   | 10                                        |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_ROUTE\_HISTORY\_LENGTH**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





