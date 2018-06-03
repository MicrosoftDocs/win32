---
title: ClusterUpgradeVersion
description: .
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: CC9FD449-AC63-4D2F-9327-C9419622D9FC
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusterUpgradeVersion Failover Cluster
topic_type:
- apiref
api_name:
- ClusterUpgradeVersion
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusterUpgradeVersion



| Attribute | Value                                            |
|-----------|--------------------------------------------------|
| Data type | **DWORD**                                        |
| Access    | [Read/write](read-write-properties.md)          |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)        |
| Minimum   | 0                                                |
| Maximum   | 0xFFFFFFFF                                       |
| Default   | **CLUSTER\_INTERNAL\_CURRENT\_UPGRADE\_VERSION** |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_UPGRADE\_VERSION**.

The value of **CLUSTER\_INTERNAL\_CURRENT\_UPGRADE\_VERSION** is the current build number.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





