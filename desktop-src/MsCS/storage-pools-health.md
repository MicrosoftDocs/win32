---
title: Health
description: Specifies the health of the storage pool.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'CE3DA0D9-FAFE-46CB-B749-9AC6272D979E'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Health Failover Cluster"]
topic_type:
- apiref
api_name:
- Health
api_type:
- NA
---

# Health

Specifies the health of the storage pool.

The following table summarizes the attributes of the **Health** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Status    | Required                                  |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | 0                                         |
| Maximum   | 4                                         |
| Default   | 0                                         |



 

## Remarks

This property can be set to one of the following values:



| Value | Description                                |
|-------|--------------------------------------------|
| 0     | The health of the storage pool is unknown. |
| 1     | The storage pool is unhealthy.             |
| 2     | The storage pool has a health warning.     |
| 3     | The storage pool is healthy.               |
| 4     | The maximum value.                         |



 

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Storage Pool Private Properties](storage-pool-private-properties.md)
</dt> </dl>

 

 





