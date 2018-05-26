---
title: MinimumNeverPreemptPriority
description: Specifies the lowest priority group that cannot be preempted.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 71E28A29-0CE1-4DA3-B58B-231C422A880E
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- MinimumNeverPreemptPriority Failover Cluster
topic_type:
- apiref
api_name:
- MinimumNeverPreemptPriority
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MinimumNeverPreemptPriority

Specifies the lowest priority group that cannot be preempted.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | 0                                         |
| Maximum   | 4999                                      |
| Default   | 3000                                      |



 

## Remarks

The constant for this property is **MINIMUM\_NEVER\_PREEMPT\_PRIORITY**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





