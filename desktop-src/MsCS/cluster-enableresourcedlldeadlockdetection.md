---
title: EnableResourceDllDeadlockDetection
description: This property is not supported.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 97dfaf8c-0ccb-4c19-bf48-3d4806347e41
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- EnableResourceDllDeadlockDetection Failover Cluster ,for clusters
- EnableResourceDllDeadlockDetection Failover Cluster
topic_type:
- apiref
api_name:
- EnableResourceDllDeadlockDetection
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# EnableResourceDllDeadlockDetection

\[This property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2008 R2, Windows Server 2008 and Windows Server 2003:  **

Controls whether the cluster service monitors the entry points to Resource DLLs for access deadlock (a condition that occurs when two processes are each waiting for the other to complete before proceeding).



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | FALSE (0).                                |
| Maximum   | TRUE (1).                                 |
| Default   | **FALSE**                                 |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for **EnableResourceDllDeadlockDetection** can be set with the following example code:


```C++
CLUSPROP_DWORD PropertyValue;
PropertyValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
PropertyValue.cbLength = sizeof(DWORD);
PropertyValue.dw = FALSE;
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

[**ResourceDllDeadlockPeriod**](cluster-resourcedlldeadlockperiod.md)
</dt> <dt>

[**ResourceDllDeadlockThreshold**](cluster-resourcedlldeadlockthreshold.md)
</dt> <dt>

[**ResourceDllDeadlockTimeout**](cluster-resourcedlldeadlocktimeout.md)
</dt> </dl>

 

 





