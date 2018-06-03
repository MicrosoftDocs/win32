---
title: PreventQuorum
description: Specifies whether to prevent a cluster node from achieving a quorum.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1218585C-C290-40CE-A707-A9809C432681
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- PreventQuorum Failover Cluster
topic_type:
- apiref
api_name:
- PreventQuorum
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PreventQuorum

Specifies whether to prevent a cluster node from achieving a quorum.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | **FALSE** (0)                             |
| Maximum   | **TRUE** (1)                              |
| Default   | **FALSE** (0)                             |



 

"1" prevents the node from achieving a quorum, "0" does not.

## Remarks

The constant for this property is **CLUSREG\_NAME\_PREVENTQUORUM**.

This property is used to prevent two instances of the same cluster from running at the same time.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





