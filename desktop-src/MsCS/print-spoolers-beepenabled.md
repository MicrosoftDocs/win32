---
title: BeepEnabled
description: TBD.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ce6682b2-d4d9-44ee-83a5-20e0e5cd7472
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- BeepEnabled Failover Cluster ,for print spoolers
- BeepEnabled Failover Cluster
topic_type:
- apiref
api_name:
- BeepEnabled
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# BeepEnabled

TBD. The following table summarizes the attributes of the **BeepEnabled** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | **FALSE** (0)                             |
| Maximum   | **TRUE** (1)                              |
| Default   | 0                                         |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for **BeepEnabled** can be set with the following example code.


```C++
DWORD          dwBeepEnabledData = 1;
CLUSPROP_DWORD BeepEnabledValue;

BeepEnabledValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
BeepEnabledValue.cbLength  = sizeof(DWORD);
BeepEnabledValue.dw        = dwBeepEnabledData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Print Spooler Private Properties](print-spooler-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> </dl>

 

 





