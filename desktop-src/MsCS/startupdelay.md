---
title: StartupDelay
description: The group set delay in seconds.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0F4D1147-5DCA-42BB-81EF-4D79B19C56C0'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["StartupDelay Failover Cluster"]
topic_type:
- apiref
api_name:
- StartupDelay
api_type:
- NA
---

# StartupDelay

The group set delay in seconds.



| Attribute | Value                                                         |
|-----------|---------------------------------------------------------------|
| Data type | **DWORD**                                                     |
| Access    | [Read/write](read-write-properties.md)                       |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md)                     |
| Minimum   | 0                                                             |
| Maximum   | 0xFFFFFFFF                                                    |
| Default   | **CLUSTER\_GROUP\_SET\_STARTUP\_DELAY\_IN\_SECONDS\_DEFAULT** |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_GROUPSET\_STARTUP\_DELAY**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Groupset Common Properties](collection-common-properties.md)
</dt> </dl>

 

 





