---
title: DeadlockTimeout
description: Specifies the period (in milliseconds) of the deadlock detection heartbeat.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f08200c6-32a4-4b43-b41e-c8f976473321
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DeadlockTimeout Failover Cluster , for Resource common properties
- DeadlockTimeout Failover Cluster
topic_type:
- apiref
api_name:
- DeadlockTimeout
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DeadlockTimeout

Specifies the period (in milliseconds) of the deadlock detection heartbeat. The following table summarizes the attributes of the **DeadlockTimeout** property.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)<br/> |
| Minimum<br/>   | 1000 (1 second)<br/>                           |
| Maximum<br/>   | 0xFFFFFFFF<br/>                                |
| Default<br/>   | 300000 (5 minutes)<br/>                        |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for **DeadlockTimeout** can be set with the following example code:


```C++
DWORD          DeadlockTimeoutData = 60000; // 1 minute timeout
CLUSPROP_DWORD DeadlockTimeoutValue;

DeadlockTimeoutValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
DeadlockTimeoutValue.cbLength  = sizeof(DWORD);
DeadlockTimeoutValue.dw        = DeadlockTimeoutData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Resource Common Properties](resource-common-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> </dl>

 

 





