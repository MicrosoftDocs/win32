---
title: ClusSvcHeartbeatTimeout
description: This property is not supported.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7847386f-e631-4433-b0ee-2d672e82ef4e'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ClusSvcHeartbeatTimeout Failover Cluster ,for clusters", "ClusSvcHeartbeatTimeout Failover Cluster"]
topic_type:
- apiref
api_name:
- ClusSvcHeartbeatTimeout
api_type:
- NA
---

# ClusSvcHeartbeatTimeout

\[This property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2008 R2, Windows Server 2008 and Windows Server 2003:  **

Used by the cluster network driver to specify the maximum number of seconds allowed before a non-communicating [node](nodes.md) is considered to be offline and unavailable as a resource to the [*cluster*](c-gly.md#-wolf-cluster-gly).



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | 6                                         |
| Maximum   | None                                      |
| Default   | 60                                        |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for **ClusSvcHeartbeatTimeout** can be set with the following example code.


```C++
DWORD          ClusSvcHeartbeatTimeoutData = 720;
CLUSPROP_DWORD ClusSvcHeartbeatTimeoutValue;

ClusSvcHeartbeatTimeoutValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
ClusSvcHeartbeatTimeoutValue.cbLength  = sizeof(DWORD);
ClusSvcHeartbeatTimeoutValue.dw        = ClusSvcHeartbeatTimeoutData;
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

[Cluster Common Properties](cluster-common-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> </dl>

 

 





