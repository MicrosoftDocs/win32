---
title: ClusSvcRegroupStageTimeout
description: Controls the amount of time, in seconds, that a node waits on other nodes in a membership stage before deciding that they have failed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'F622C705-C953-41B4-80F1-1809724764C8'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ClusSvcRegroupStageTimeout Failover Cluster"]
topic_type:
- apiref
api_name:
- ClusSvcRegroupStageTimeout
api_type:
- NA
---

# ClusSvcRegroupStageTimeout

Controls the amount of time, in seconds, that a node waits on other nodes in a membership stage before deciding that they have failed.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | 2                                         |
| Maximum   | 30                                        |
| Default   | 5                                         |



 

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





