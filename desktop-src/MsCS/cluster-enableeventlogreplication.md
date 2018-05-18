---
title: EnableEventLogReplication
description: Controls whether the system, application, and security event log entries of all the node's are replicated across the entire cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b7704d8a-9415-4f35-b4c8-28ab8a103595'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["EnableEventLogReplication Failover Cluster ,for clusters", "EnableEventLogReplication Failover Cluster"]
topic_type:
- apiref
api_name:
- EnableEventLogReplication
api_type:
- NA
---

# EnableEventLogReplication

\[This property is available for use only in Windows Server 2003.\]

Controls whether the system, application, and security event log entries of all the [node's](nodes.md) are replicated across the entire [*cluster*](c-gly.md#-wolf-cluster-gly).



| Attribute            | Value                                                                                                |
|----------------------|------------------------------------------------------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                                                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>                                                   |
| Structure<br/> | [**CLUSPROP\_DWORD**](clusprop-dword.md)<br/>                                                 |
| Minimum<br/>   | **FALSE** (0). The node's event log entries are not replicated across the entire cluster.<br/> |
| Maximum<br/>   | **TRUE** (1). The node's event log entries are replicated across the entire cluster.<br/>      |
| Default<br/>   | **TRUE**<br/>                                                                                  |



 

## Remarks

The **EnableEventLogReplication** property only affects events logged to a node's system, application, and security logs.

## Examples

The property value portion of a [property list](property-lists.md) entry for **EnableEventLogReplication** can be set with the following example code.


```C++
CLUSPROP_DWORD PropertyValue;

PropertyValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
PropertyValue.cbLength  = sizeof(DWORD);
PropertyValue.dw        = FALSE;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 Enterprise, Windows Server 2003 Datacenter<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> </dl>

 

 





