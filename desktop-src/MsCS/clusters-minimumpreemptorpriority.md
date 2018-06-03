---
title: MinimumPreemptorPriority
description: Specifies the lowest priority group that can preempt other groups.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: E7CBD922-D70C-43C0-9CB1-EB60ACFE8A4B
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- MinimumPreemptorPriority Failover Cluster
topic_type:
- apiref
api_name:
- MinimumPreemptorPriority
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MinimumPreemptorPriority

Specifies the lowest priority group that can preempt other groups.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 0                                         |
| Maximum   | 4999                                      |
| Default   | 1                                         |



 

## Remarks

The constant for this property is **MINIMUM\_PREEMPTOR\_PRIORITY**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





