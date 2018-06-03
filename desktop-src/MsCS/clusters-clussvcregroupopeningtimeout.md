---
title: ClusSvcRegroupOpeningTimeout
description: Controls the amount of time, in seconds, that a node waits on other nodes in the opening stage before deciding that they have failed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: F4DBFF05-19D2-4B19-8220-5A695901F874
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusSvcRegroupOpeningTimeout Failover Cluster
topic_type:
- apiref
api_name:
- ClusSvcRegroupOpeningTimeout
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusSvcRegroupOpeningTimeout

Controls the amount of time, in seconds, that a node waits on other nodes in the opening stage before deciding that they have failed.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 1                                         |
| Maximum   | 20                                        |
| Default   | 5                                         |



 

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





