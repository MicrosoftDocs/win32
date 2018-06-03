---
title: EnableEventDeltaGeneration
description: Controls whether a time delta event is logged when a set of event log entries are replicated to nodes across the entire cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7062af46-cade-4069-a8c3-401d8e73d1ff
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- EnableEventDeltaGeneration Failover Cluster ,for clusters
- EnableEventDeltaGeneration Failover Cluster
topic_type:
- apiref
api_name:
- EnableEventDeltaGeneration
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EnableEventDeltaGeneration

\[This property is available for use only in Windows Server 2003.\]

Controls whether a time delta event is logged when a set of event log entries are replicated to [nodes](nodes.md) across the entire [*cluster*](https://www.bing.com/search?q=*cluster*).



| Attribute            | Value                                                                                             |
|----------------------|---------------------------------------------------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                                                              |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>                                                |
| Structure<br/> | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)<br/>                                              |
| Minimum<br/>   | **FALSE** (0). Do not generate a time delta log when event log entries are replicated.<br/> |
| Maximum<br/>   | **TRUE** (1). Generate a time delta log when event log entries are replicated.<br/>         |
| Default<br/>   | **TRUE**<br/>                                                                               |



 

## Remarks

When a set of events in the event log are replicated across nodes in the cluster, the **EnableEventDeltaGeneration** property controls whether a time delta event is added to the event log during replication to indicate the time difference between the nodes in the cluster.

## Examples

The property value portion of a [property list](property-lists.md) entry for **EnableEventDeltaGeneration** can be set with the following example code.


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
| Minimum supported server<br/> | Windows Server 2003 Enterprise, Windows Server 2003 Datacenter<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> </dl>

 

 





