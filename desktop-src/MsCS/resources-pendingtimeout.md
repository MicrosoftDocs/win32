---
title: PendingTimeout
description: Sets the number of milliseconds that a Resource Monitor will wait for a resource DLL to update the status of a resource in an OnlinePending or OfflinePending state before terminating the resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 12f5cb51-7c7c-49b1-8542-dbbff50d55b0
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- PendingTimeout Failover Cluster ,for resources
- PendingTimeout Failover Cluster
topic_type:
- apiref
api_name:
- PendingTimeout
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PendingTimeout

Sets the number of milliseconds that a [Resource Monitor](resource-monitor.md) will wait for a [resource DLL](resource-dlls.md) to update the status of a [resource](resources.md) in an OnlinePending or OfflinePending state before terminating the resource. The following table summarizes the attributes of the **PendingTimeout** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | 10                                        |
| Maximum   | 0xFFFFFFFF                                |
| Default   | 180000                                    |



 

## Remarks

The **PendingTimeout** property does not necessarily limit the time that a resource can spend in a ClusterOnlinePending or ClusterOfflinePending state. This property determines only how long a Resource Monitor will wait for resource DLLs to report status updates with the [**SetResourceStatus**](/windows/previous-versions/ResApi/nc-resapi-pset_resource_status_routine?branch=master) function. As long as a resource DLL never exceeds the **PendingTimeout** interval between calls to **SetResourceStatus**, the resource DLL can keep a resource in a pending state indefinitely.

If a resource DLL exceeds the **PendingTimeout** interval between calls to [**SetResourceStatus**](/windows/previous-versions/ResApi/nc-resapi-pset_resource_status_routine?branch=master), the Resource Monitor calls the resource DLL's [**Terminate**](/windows/previous-versions/ResApi/nc-resapi-pterminate_routine?branch=master) entry point function.

## Examples

The property value portion of a [property list](property-lists.md) entry for **PendingTimeout** can be set with the following example code:


```C++
DWORD PendingTimeoutData = 120000;
CLUSPROP_DWORD PendingTimeoutValue;
PendingTimeoutValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
PendingTimeoutValue.cbLength = sizeof(DWORD);
PendingTimeoutValue.dw = PendingTimeoutData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**Offline**](/windows/previous-versions/ResApi/nc-resapi-poffline_routine?branch=master)
</dt> <dt>

[**Online**](/windows/previous-versions/ResApi/nc-resapi-ponline_routine?branch=master)
</dt> <dt>

[**Terminate**](/windows/previous-versions/ResApi/nc-resapi-pterminate_routine?branch=master)
</dt> </dl>

 

 





