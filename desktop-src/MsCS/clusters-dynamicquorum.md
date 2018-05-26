---
title: DynamicQuorum
description: Enables the cluster to change the required number of nodes that need to participate in quorum when nodes shut down or crash.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 73CD6CFB-7D0F-43ED-BE46-50C449C1EC45
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DynamicQuorum Failover Cluster
topic_type:
- apiref
api_name:
- DynamicQuorum
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DynamicQuorum

Enables the cluster to change the required number of nodes that need to participate in quorum when nodes shut down or crash.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | **FALSE** (0)                             |
| Maximum   | **TRUE** (1)                              |
| Default   | **TRUE** (1)                              |



 

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





