---
title: CrossSubnetDelay
description: Controls the time interval, in milliseconds, that the cluster network driver waits between sending Cluster Service heartbeats across subnets.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 41A86CB2-08C8-4122-A4BC-2586E4DD15E9
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CrossSubnetDelay Failover Cluster
topic_type:
- apiref
api_name:
- CrossSubnetDelay
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CrossSubnetDelay

Controls the time interval, in milliseconds, that the cluster network driver waits between sending Cluster Service heartbeats across subnets.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 250                                       |
| Maximum   | 4000                                      |
| Default   | 1000                                      |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_CROSS\_SUBNET\_DELAY**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





