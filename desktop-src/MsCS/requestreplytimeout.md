---
title: RequestReplyTimeout
description: Describes the length of time a request from a node with a cluster state update will wait for replies from the other healthy nodes before the request times out.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 228c7803-7623-4019-9dc6-11f9db5f134f
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- RequestReplyTimeout Failover Cluster , for Cluster common properties
- RequestReplyTimeout Failover Cluster
topic_type:
- apiref
api_name:
- RequestReplyTimeout
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RequestReplyTimeout

Describes the length of time a request from a node with a cluster state update will wait for replies from the other healthy nodes before the request times out. Any nodes that do not reply within the request time out period will be removed from active membership in the cluster. The following table summarizes the attributes of the **RequestReplyTimeout** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 5 minutes                                 |
| Maximum   | 1440 minutes (24 hours)                   |
| Default   | 60 minutes                                |



 

## Remarks

The constant for this property is **CLUSTER\_REQUEST\_REPLY\_TIMEOUT**.

## Examples

The property value portion of a property list entry for **RequestReplyTimeout** can be set with the following example code.


```C++
DWORD          RequestReplyTimeoutData = 60;
CLUSPROP_DWORD RequestReplyTimeoutValue;

RequestReplyTimeoutValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
RequestReplyTimeoutValue.cbLength  = sizeof(DWORD);
RequestReplyTimeoutValue.dw        = RequestReplyTimeoutData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





