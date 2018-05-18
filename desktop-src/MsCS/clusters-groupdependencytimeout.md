---
title: GroupDependencyTimeout
description: The group dependency timeout, in seconds.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'F525AF9F-62BB-43AA-8013-A18DEE48DE70'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSREG_NAME_GROUP_DEPENDENCY_TIMEOUT", "CLUSREG_NAME_GROUP_DEPENDENCY_TIMEOUT", "GroupDependencyTimeout Failover Cluster"]
topic_type:
- apiref
api_name:
- GroupDependencyTimeout
api_type:
- NA
---

# GroupDependencyTimeout

The group dependency timeout, in seconds.



| Attribute            | Value                                     |
|----------------------|-------------------------------------------|
| Data type<br/> | **DWORD**                                 |
| Access<br/>    | [Read/write](read-write-properties.md)   |
| Structure<br/> | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum<br/>   | 0<br/>                              |
| Maximum<br/>   | 0xFFFFFFFF<br/>                     |
| Default<br/>   | 600 (10 minutes)<br/>               |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_GROUP\_DEPENDENCY\_TIMEOUT**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





