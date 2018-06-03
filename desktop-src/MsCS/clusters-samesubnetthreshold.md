---
title: SameSubnetThreshold
description: Controls how many heartbeats can be missed on the same subnet before the route is declared as unreachable.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 149B942D-4782-4911-B669-A5B9BF7EDEA0
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- SameSubnetThreshold Failover Cluster
topic_type:
- apiref
api_name:
- SameSubnetThreshold
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SameSubnetThreshold

Controls how many heartbeats can be missed on the same subnet before the route is declared as unreachable. This property applies to routes on the same network subnet.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 3                                         |
| Maximum   | 120                                       |
| Default   | 5                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_SAME\_SUBNET\_THRESHOLD**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





