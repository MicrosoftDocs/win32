---
title: SeparateMonitor
description: Indicates whether the resource requires its own Resource Monitor. The following table summarizes the attributes of the SeparateMonitor property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0ed3404e-f91a-4cac-aee7-f014ae329ac1
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- SeparateMonitor Failover Cluster ,for resources
- SeparateMonitor Failover Cluster
topic_type:
- apiref
api_name:
- SeparateMonitor
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SeparateMonitor

Indicates whether the [resource](resources.md) requires its own [Resource Monitor](resource-monitor.md). The following table summarizes the attributes of the **SeparateMonitor** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | **FALSE**                                 |
| Maximum   | **TRUE**                                  |
| Default   | **FALSE**                                 |



 

## Remarks

The data value for the **SeparateMonitor** property can be set to **TRUE** or **FALSE**. To use a debugger with a [resource](resources.md) DLL, the resource's **SeparateMonitor** property must be set to **TRUE**.

A change to the **SeparateMonitor** property does not take effect immediately unless the resource is offline at the time of the change. If the resource is online, the change takes effect after the resource is taken offline and brought back online.

## Examples

The property value portion of a [property list](property-lists.md) entry for **SeparateMonitor** can be set with the following example code:


```C++
DWORD SeparateMonitorData = TRUE;
CLUSPROP_DWORD SeparateMonitorValue;
SeparateMonitorValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
SeparateMonitorValue.cbLength = sizeof(DWORD);
SeparateMonitorValue.dw = SeparateMonitorData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> </dl>

 

 





