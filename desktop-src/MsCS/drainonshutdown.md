---
title: DrainOnShutdown
description: Specifies whether to enable Node Drain for a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6DDD569C-0EF9-4818-90AB-BA8396E13DDB'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["DrainOnShutdown Failover Cluster"]
topic_type:
- apiref
api_name:
- DrainOnShutdown
api_type:
- NA
---

# DrainOnShutdown

Specifies whether to enable Node Drain for a cluster.



| Attribute            | Value                                     |
|----------------------|-------------------------------------------|
| Data type<br/> | **DWORD**                                 |
| Access<br/>    | [Read/write](read-write-properties.md)   |
| Structure<br/> | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum<br/>   | 0<br/>                              |
| Maximum<br/>   | 1<br/>                              |
| Default<br/>   | 1<br/>                              |



 

" 0" disables Node Drain, "1" enables it.

## Remarks

The constant for this property is **CLUSREG\_NAME\_DRAIN\_ON\_SHUTDOWN**.

When a cluster node is about to shut down for maintenance, Node Drain first pauses the node, and then distributes the roles to active nodes in the cluster.

## Requirements



|                                     |                                   |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | None supported<br/>         |
| Minimum supported server<br/> | Windows Server 2012 R2<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





