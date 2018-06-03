---
title: SameSubnetDelay
description: Controls the delay, in milliseconds, between netft heartbeats.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 81D86242-AB66-45C6-B894-563F4E5F61D6
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- SameSubnetDelay Failover Cluster
topic_type:
- apiref
api_name:
- SameSubnetDelay
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SameSubnetDelay

Controls the delay, in milliseconds, between netft heartbeats. This property applies to routes on the same network subnet.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 250                                       |
| Maximum   | 2000                                      |
| Default   | 1000                                      |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_SAME\_SUBNET\_DELAY**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





