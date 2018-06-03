---
title: ResourceDllDeadlockThreshold
description: This property is not supported.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0e893410-f5b7-4957-a2cd-5ad95bdc5c48
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ResourceDllDeadlockThreshold Failover Cluster ,for clusters
- ResourceDllDeadlockThreshold Failover Cluster
topic_type:
- apiref
api_name:
- ResourceDllDeadlockThreshold
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ResourceDllDeadlockThreshold

\[This property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2008 R2, Windows Server 2008 and Windows Server 2003:  **

Specifies the number of deadlock timeouts which must occur within the deadlock timeout period before a deadlocked condition is considered to have occurred.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 0                                         |
| Maximum   | 0xFFFFFFFF                                |
| Default   | 3                                         |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for **ResourceDllDeadlockThreshold** can be set with the following example code:


```C++
DWORD ResourceDllDeadlockThresholdData = 5;
CLUSPROP_DWORD ResourceDllDeadlockThresholdValue;

ResourceDllDeadlockThresholdValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
ResourceDllDeadlockThresholdValue.cbLength = sizeof(DWORD);
ResourceDllDeadlockThresholdValue.dw = ResourceDllDeadlockThresholdData;
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

[**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dt>

[**EnableResourceDllDeadlockDetection**](cluster-enableresourcedlldeadlockdetection.md)
</dt> <dt>

[**ResourceDllDeadlockPeriod**](cluster-resourcedlldeadlockperiod.md)
</dt> <dt>

[**ResourceDllDeadlockTimeout**](cluster-resourcedlldeadlocktimeout.md)
</dt> </dl>

 

 





