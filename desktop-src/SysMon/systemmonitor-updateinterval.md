---
title: SystemMonitor.UpdateInterval property
description: Retrieves or sets the length of time that SYSMON waits before the next time it collects counter data and updates the graph or report.
ms.assetid: 297931e4-23ae-4384-a04a-9c1fa8aa1239
keywords:
- UpdateInterval property SysMon
- UpdateInterval property SysMon , SystemMonitor class
- SystemMonitor class SysMon , UpdateInterval property
topic_type:
- apiref
api_name:
- SystemMonitor.UpdateInterval
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.UpdateInterval property

Retrieves or sets the length of time that SYSMON waits before the next time it collects counter data and updates the graph or report.

This property is read-only.

## Syntax


```VB
Property UpdateInterval As Single
```



## Property value

Length of time, in seconds, that SYSMON waits before the next time it collects counter data and updates the graph or report. The minimum interval is 1 second (this is also the default value). The maximum value is 1,000,000.

## Remarks

This property is relevant only when [**SystemMonitor.ManualUpdate**](systemmonitor-manualupdate.md) is set to False.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



## See also

<dl> <dt>

[**SystemMonitor**](systemmonitor.md)
</dt> </dl>

 

 





