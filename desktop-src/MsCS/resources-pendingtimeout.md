---
title: PendingTimeout
description: Sets the number of milliseconds that a Resource Monitor will wait for a resource DLL to update the status of a resource in an OnlinePending or OfflinePending state before terminating the resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '12f5cb51-7c7c-49b1-8542-dbbff50d55b0'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["PendingTimeout Failover Cluster ,for resources", "PendingTimeout Failover Cluster"]
topic_type:
- apiref
api_name:
- PendingTimeout
api_type:
- NA
---

# PendingTimeout

Sets the number of milliseconds that a [Resource Monitor](resource-monitor.md) will wait for a [resource DLL](resource-dlls.md) to update the status of a [resource](resources.md) in an OnlinePending or OfflinePending state before terminating the resource. The following table summarizes the attributes of the **PendingTimeout** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | 10                                        |
| Maximum   | 0xFFFFFFFF                                |
| Default   | 180000                                    |



 

## Remarks

The **PendingTimeout** property does not necessarily limit the time that a resource can spend in a ClusterOnlinePending or ClusterOfflinePending state. This property determines only how long a Resource Monitor will wait for resource DLLs to report status updates with the [**SetResourceStatus**](setresourcestatus.md) function. As long as a resource DLL never exceeds the **PendingTimeout** interval between calls to **SetResourceStatus**, the resource DLL can keep a resource in a pending state indefinitely.

If a resource DLL exceeds the **PendingTimeout** interval between calls to [**SetResourceStatus**](setresourcestatus.md), the Resource Monitor calls the resource DLL's [**Terminate**](terminate.md) entry point function.

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
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> <dt>

[**Offline**](offline.md)
</dt> <dt>

[**Online**](online.md)
</dt> <dt>

[**Terminate**](terminate.md)
</dt> </dl>

 

 





