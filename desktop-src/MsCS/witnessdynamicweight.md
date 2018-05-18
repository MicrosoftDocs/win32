---
title: WitnessDynamicWeight
description: Specifies the weight of a file share quorum witness for dynamic quorum.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'B2CC5C8B-A098-422D-9F64-6135F2620AEE'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["WitnessDynamicWeight Failover Cluster"]
topic_type:
- apiref
api_name:
- WitnessDynamicWeight
api_type:
- NA
---

# WitnessDynamicWeight

Specifies the weight of a file share quorum witness for dynamic quorum.



| Attribute            | Value                                     |
|----------------------|-------------------------------------------|
| Data type<br/> | **DWORD**                                 |
| Access<br/>    | [Read/write](read-write-properties.md)   |
| Structure<br/> | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum<br/>   | 0<br/>                              |
| Maximum<br/>   | 1<br/>                              |
| Default<br/>   | 0<br/>                              |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_WITNESS\_DYNAMIC\_WEIGHT**.

## Requirements



|                                     |                                   |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | None supported<br/>         |
| Minimum supported server<br/> | Windows Server 2012 R2<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





