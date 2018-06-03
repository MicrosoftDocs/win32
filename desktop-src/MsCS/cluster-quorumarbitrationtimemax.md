---
title: QuorumArbitrationTimeMax
description: Specifies the maximum number of seconds a node is allowed to spend arbitrating for the quorum resource in a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6618195c-9d2b-435f-92c9-4cd4e9fd77bc
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- QuorumArbitrationTimeMax Failover Cluster ,for clusters
- QuorumArbitrationTimeMax Failover Cluster
topic_type:
- apiref
api_name:
- QuorumArbitrationTimeMax
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# QuorumArbitrationTimeMax

Specifies the maximum number of seconds a [node](nodes.md) is allowed to spend arbitrating for the quorum resource in a [*cluster*](https://www.bing.com/search?q=*cluster*).



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 1                                         |
| Maximum   | 3600                                      |
| Default   | 20                                        |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_QUORUM\_ARBITRATION\_TIMEOUT**.

**Windows Server 2008:** The default is 60 seconds.

## Examples

The property value portion of a [property list](property-lists.md) entry for **QuorumArbitrationTimeMax** can be set with the following example code:


```C++
DWORD QuorumArbitrationTimeMaxData = 20;
CLUSPROP_DWORD QuorumArbitrationTimeMaxValue;

QuorumArbitrationTimeMaxValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
QuorumArbitrationTimeMaxValue.cbLength = sizeof(DWORD);
QuorumArbitrationTimeMaxValue.dw = QuorumArbitrationTimeMaxData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> </dl>

 

 





