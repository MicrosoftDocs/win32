---
title: SystemMonitor.ScaleToFit method
description: Scale counter values to fit in the graph.
ms.assetid: 8e58e51a-4767-40da-836a-e49d34dec195
keywords:
- ScaleToFit method SysMon
- ScaleToFit method SysMon , SystemMonitor object
- SystemMonitor object SysMon , ScaleToFit method
topic_type:
- apiref
api_name:
- SystemMonitor.ScaleToFit
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.ScaleToFit method

Scale counter values to fit in the graph.

## Syntax


```VB
SystemMonitor.ScaleToFit( _
  ByVal selectedCountersOnly As Boolean _
)
```



## Parameters

<dl> <dt>

*selectedCountersOnly* \[in\]
</dt> <dd>

True to scale only the selected counters; otherwise, false to scale all counters.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method will clear the graph view. SYSMON then uses the scale factor specified for each counter to redraw the graph if the data source is a log file, or begin graphing new counter values if the data source is real time activity.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



## See also

<dl> <dt>

[**SystemMonitor**](systemmonitor.md)
</dt> <dt>

[**CounterItem.ScaleFactor**](counteritem-scalefactor.md)
</dt> <dt>

[**CounterItem.Selected**](counteritem-selected.md)
</dt> </dl>

 

 





