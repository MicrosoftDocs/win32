---
title: Arbitrate
description: Specifies whether to arbitrate on pool disks before applying a persistent reservation (PR).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: DF3BB346-7442-4A58-BF86-DACF3514C1C0
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Arbitrate Failover Cluster
topic_type:
- apiref
api_name:
- Arbitrate
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Arbitrate

Specifies whether to arbitrate on pool disks before applying a persistent reservation (PR).

The following table summarizes the attributes of the **Arbitrate** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | **FALSE** (0)                             |
| Maximum   | **TRUE** (1)                              |
| Default   | 0                                         |



 

## Remarks

If arbitration is applied, 7 seconds are added to the failover time. Quorum pools are always arbitrated, while for non-quorum pools, the default value is 0.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Storage Pool Private Properties](storage-pool-private-properties.md)
</dt> </dl>

 

 





