---
title: EnabledEventLogs
description: Specifies the enabled event logs for a resource type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1DC22D46-E138-4513-BC95-B7045B52A90E'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["EnabledEventLogs Failover Cluster"]
topic_type:
- apiref
api_name:
- EnabledEventLogs
api_type:
- NA
---

# EnabledEventLogs

Specifies the enabled event logs for a resource type.



| Attribute            | Value                                                            |
|----------------------|------------------------------------------------------------------|
| Data type<br/> | An array of null-terminated Unicode strings.<br/>          |
| Access<br/>    | [Read/write](read-write-properties.md)                          |
| Structure<br/> | [**CLUSPROP\_MULTI\_SZ**](clusprop-multi-sz.md)                 |
| Minimum<br/>   | 0                                                                |
| Maximum<br/>   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default<br/>   | 0                                                                |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_RESTYPE\_ENABLED\_EVENT\_LOGS**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Resource Type Common Properties](resource-type-common-properties.md)
</dt> </dl>

 

 





