---
title: ResourceDllDeadlockPeriod
description: This property is not supported.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ab3b9d86-9bcf-4d80-a06a-4342ccb10841
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ResourceDllDeadlockPeriod Failover Cluster ,for clusters
- ResourceDllDeadlockPeriod Failover Cluster
topic_type:
- apiref
api_name:
- ResourceDllDeadlockPeriod
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ResourceDllDeadlockPeriod

\[This property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2008 R2, Windows Server 2008 and Windows Server 2003:  **

Specifies the overall time period (in seconds) used to determine if a resource access deadlock condition has occurred.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | 180                                       |
| Maximum   | 0xFFFFFFFF                                |
| Default   | 1800                                      |



 

## Remarks

The **ResourceDllDeadlockPeriod** property value is specified in seconds.

## Examples

The property value portion of a [property list](property-lists.md) entry for **ResourceDllDeadlockPeriod** can be set with the following example code:


```C++
DWORD ResourceDllDeadlockPeriodData = 4000;
CLUSPROP_DWORD ResourceDllDeadlockPeriodValue;

ResourceDllDeadlockPeriodValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
ResourceDllDeadlockPeriodValue.cbLength = sizeof(DWORD);
ResourceDllDeadlockPeriodValue.dw = ResourceDllDeadlockPeriodData;
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

[**ResourceDllDeadlockThreshold**](cluster-resourcedlldeadlockthreshold.md)
</dt> <dt>

[**ResourceDllDeadlockTimeout**](cluster-resourcedlldeadlocktimeout.md)
</dt> </dl>

 

 





