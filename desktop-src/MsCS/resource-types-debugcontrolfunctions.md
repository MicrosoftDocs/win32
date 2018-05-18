---
title: DebugControlFunctions
description: This property is not supported.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'bb524537-9262-466f-b56e-c6fb7e8ff746'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["DebugControlFunctions Failover Cluster ,for resource types", "DebugControlFunctions Failover Cluster"]
topic_type:
- apiref
api_name:
- DebugControlFunctions
api_type:
- NA
---

# DebugControlFunctions

\[This property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2008 R2, Windows Server 2008 and Windows Server 2003:  **

Indicates whether the [Cluster service](cluster-service.md) should create a separate [Resource Monitor](resource-monitor.md) to use for debugging the control functions of a resource type. The following table summarizes the attributes of the **DebugControlFunctions** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | **FALSE**                                 |
| Maximum   | **TRUE**                                  |
| Default   | **FALSE**                                 |



 

## Remarks

The data value for the **DebugControlFunctions** property can be **TRUE** or **FALSE**. When set to **TRUE**, the Cluster service starts a new Resource Monitor that can be used for control function debugging.

## Examples

The property value portion of a [property list](property-lists.md) entry for **DebugControlFunctions** can be set with the following example code:


```C++
DWORD DebugControlFunctionsData = TRUE;
CLUSPROP_DWORD DebugControlFunctionsValue;
DebugControlFunctionsValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
DebugControlFunctionsValue.cbLength = sizeof(DWORD);
DebugControlFunctionsValue.dw = DebugControlFunctionsData;
```



## Requirements



|                                     |                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2003 Enterprise, Windows Server 2003 Datacenter<br/>       |
| End of client support<br/>    | None supported<br/>                                                       |
| End of server support<br/>    | Windows Server 2008 R2 Enterprise, Windows Server 2008 R2 Datacenter<br/> |



## See also

<dl> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> </dl>

 

 





