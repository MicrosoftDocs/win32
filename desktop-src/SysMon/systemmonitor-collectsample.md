---
title: SystemMonitor CollectSample method
description: Samples a value for each counter in the Counters object.
ms.assetid: 4c91c759-597f-4aa8-aa77-eb181616e8b0
keywords:
- CollectSample method SysMon
- CollectSample method SysMon , SystemMonitor interface
- SystemMonitor interface SysMon , CollectSample method
topic_type:
- apiref
api_name:
- SystemMonitor.CollectSample
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor::CollectSample method

Samples a value for each counter in the [**Counters**](counters.md) object.

## Syntax


```VB
Sub CollectSample()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Call **CollectSample** only if [**ManualUpdate**](systemmonitor-manualupdate.md) is True and you are sampling counter values from the current activity of the computer do not use this method when sampling from a log file. The graph or report is updated with the new value. Note that some types of graphs need two samples in order to graph the data, for example, the line graph.

To receive notification when the sample has been collected, implement the [**OnSampleCollected**](-systemmonitor-onsamplecollected.md) event.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



## See also

<dl> <dt>

[**Counters**](counters.md)
</dt> <dt>

[**SystemMonitor**](systemmonitor.md)
</dt> </dl>

 

 





