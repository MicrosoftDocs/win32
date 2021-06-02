---
title: SystemMonitor BrowseCounters method
description: Displays the Add Counters dialog box.
ms.assetid: 7edc4a80-4a04-49fd-b383-b892e1e16215
keywords:
- BrowseCounters method SysMon
- BrowseCounters method SysMon , SystemMonitor interface
- SystemMonitor interface SysMon , BrowseCounters method
topic_type:
- apiref
api_name:
- SystemMonitor.BrowseCounters
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor::BrowseCounters method

Displays the **Add Counters** dialog box.

## Syntax


```VB
Sub BrowseCounters()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This dialog box lets the user select local or remote performance counters from a list of performance objects. The selected counters are added to the [**Counters**](counters.md) collection and displayed in the graph or report.

To receive notification when a counter is added, implement the [**OnCounterAdded**](systemmonitor-oncounteradded.md) event.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



## See also

<dl> <dt>

[**SystemMonitor**](systemmonitor.md)
</dt> <dt>

[**Counters.Add**](counters-add.md)
</dt> </dl>

 

 





