---
title: CrossSubnetThreshold
description: Controls how many Cluster Service heartbeats can be missed across subnets before it determines that Cluster Service has stopped responding.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8E290237-63FE-4BDE-8F81-E3275A2FEEFD
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CrossSubnetThreshold Failover Cluster
topic_type:
- apiref
api_name:
- CrossSubnetThreshold
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CrossSubnetThreshold

Controls how many Cluster Service heartbeats can be missed across subnets before it determines that Cluster Service has stopped responding.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 3                                         |
| Maximum   | 120                                       |
| Default   | 5                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_CROSS\_SUBNET\_THRESHOLD**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





