---
title: ConsumedCapacity
description: Contains the consumed capacity, in bytes, of the storage pool.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'B8BEE9B9-890E-4C6A-BA3F-4D748A21E455'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ConsumedCapacity Failover Cluster"]
topic_type:
- apiref
api_name:
- ConsumedCapacity
api_type:
- NA
---

# ConsumedCapacity

Contains the consumed capacity, in bytes, of the storage pool.

The following table summarizes the attributes of the **ConsumedCapacity** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Status    | Required                                  |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | 0                                         |
| Maximum   | 0                                         |
| Default   | 0                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_STORAGESPACE\_POOLCONSUMEDCAPACITY**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Storage Pool Private Properties](storage-pool-private-properties.md)
</dt> </dl>

 

 





