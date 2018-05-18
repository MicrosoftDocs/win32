---
title: QuorumArbitrationTimeMin
description: This property is not supported.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '95561177-6fee-43cd-ac24-f91388e61135'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["QuorumArbitrationTimeMin Failover Cluster ,for clusters", "QuorumArbitrationTimeMin Failover Cluster"]
topic_type:
- apiref
api_name:
- QuorumArbitrationTimeMin
api_type:
- NA
---

# QuorumArbitrationTimeMin

\[This property is available for use only in Windows Server 2003.\]

This property is not supported.

**Windows Server 2003:  **

The **QuorumArbitrationTimeMin** property specifies the minimum number of seconds a [node](nodes.md) is allowed to spend arbitrating for the quorum resource in a [*cluster*](c-gly.md#-wolf-cluster-gly).



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | 1                                         |
| Maximum   | 3600                                      |
| Default   | 7                                         |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for **QuorumArbitrationTimeMin** can be set with the following example code:


```C++
DWORD          QuorumArbitrationTimeMinData = 20;
CLUSPROP_DWORD QuorumArbitrationTimeMinValue;

QuorumArbitrationTimeMinValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
QuorumArbitrationTimeMinValue.cbLength  = sizeof(DWORD);
QuorumArbitrationTimeMinValue.dw        = QuorumArbitrationTimeMinData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 Enterprise, Windows Server 2003 Datacenter<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



## See also

<dl> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> </dl>

 

 





