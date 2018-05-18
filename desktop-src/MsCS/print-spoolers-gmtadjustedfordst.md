---
title: GMTAdjustedForDST
description: TBD.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '39bceace-92a7-4223-bfad-36901256d0dc'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["GMTAdjustedForDST Failover Cluster ,for print spoolers", "GMTAdjustedForDST Failover Cluster"]
topic_type:
- apiref
api_name:
- GMTAdjustedForDST
api_type:
- NA
---

# GMTAdjustedForDST

TBD. The following table summarizes the attributes of the **GMTAdjustedForDST** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | **FALSE** (0)                             |
| Maximum   | **TRUE** (1)                              |
| Default   | 1                                         |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for **GMTAdjustedForDST** can be set with the following example code.


```C++
DWORD          dwGMTAdjustedForDSTData = 1;
CLUSPROP_DWORD GMTAdjustedForDSTValue;

GMTAdjustedForDSTValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
GMTAdjustedForDSTValue.cbLength  = sizeof(DWORD);
GMTAdjustedForDSTValue.dw        = dwGMTAdjustedForDSTData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Print Spooler Private Properties](print-spooler-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> </dl>

 

 





