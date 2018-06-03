---
title: ClusterGroupWaitDelay
description: Specifies the maximum time, in seconds, that a group waits for its preferred node to come online during cluster startup before coming online on a different node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 65DFA485-F72F-421D-84F8-551CC3E2CE38
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusterGroupWaitDelay Failover Cluster
topic_type:
- apiref
api_name:
- ClusterGroupWaitDelay
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusterGroupWaitDelay

Specifies the maximum time, in seconds, that a group waits for its preferred node to come online during cluster startup before coming online on a different node.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 0                                         |
| Maximum   | 3600                                      |
| Default   | 120                                       |



 

## Remarks

The constant for this property is **CLUSTER\_GROUP\_WAIT\_DELAY**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





