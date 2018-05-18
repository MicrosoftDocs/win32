---
title: DiskArbInterval
description: Controls the arbitration interval (in seconds) used by the persistent reservation (PR) protocol.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e1e5df7f-2ffa-4935-a5c0-acefc083c5fb'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["DiskArbInterval Failover Cluster , for Physical Disk private properties", "DiskArbInterval Failover Cluster"]
topic_type:
- apiref
api_name:
- DiskArbInterval
api_type:
- NA
---

# DiskArbInterval

Controls the arbitration interval (in seconds) used by the persistent reservation (PR) protocol. The following table summarizes the attributes of the **DiskArbInterval** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | 1                                         |
| Maximum   | 0xFFFFFFFF                                |
| Default   | 3                                         |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for **DiskArbInterval** can be set with the following example code.


```C++
DWORD          DiskArbIntervalData = 3;
CLUSPROP_DWORD DiskArbIntervalValue;

DiskArbIntervalValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
DiskArbIntervalValue.cbLength  = sizeof(DWORD);
DiskArbIntervalValue.dw        = DiskArbIntervalData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Physical Disk Private Properties](physical-disk-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> </dl>

 

 





