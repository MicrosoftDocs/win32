---
title: ResourceDllDeadlockTimeout
description: This property is not supported.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e5f99621-7fcf-4c74-b4d7-9f10c71fb609
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ResourceDllDeadlockTimeout Failover Cluster ,for clusters
- ResourceDllDeadlockTimeout Failover Cluster
topic_type:
- apiref
api_name:
- ResourceDllDeadlockTimeout
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ResourceDllDeadlockTimeout

\[This property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2008 R2, Windows Server 2008 and Windows Server 2003:  **

Specifies the period (in seconds) of the deadlock detection heartbeat.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | 180                                       |
| Maximum   | 0xFFFFFFFF                                |
| Default   | 240                                       |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for **ResourceDllDeadlockTimeout** can be set with the following example code:


```C++
DWORD ResourceDllDeadlockTimeoutData = 600;
CLUSPROP_DWORD ResourceDllDeadlockTimeoutValue;

ResourceDllDeadlockTimeoutValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
ResourceDllDeadlockTimeoutValue.cbLength = sizeof(DWORD);
ResourceDllDeadlockTimeoutValue.dw = ResourceDllDeadlockTimeoutData;
```



## Requirements



|                                     |                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2003 Enterprise, Windows Server 2003 Datacenter<br/>       |
| End of client support<br/>    | None supported<br/>                                                       |
| End of server support<br/>    | Windows Server 2008 R2 Enterprise, Windows Server 2008 R2 Datacenter<br/> |



## See also

<dl> <dt>

[**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**EnableResourceDllDeadlockDetection**](cluster-enableresourcedlldeadlockdetection.md)
</dt> <dt>

[**ResourceDllDeadlockPeriod**](cluster-resourcedlldeadlockperiod.md)
</dt> <dt>

[**ResourceDllDeadlockThreshold**](cluster-resourcedlldeadlockthreshold.md)
</dt> </dl>

 

 





