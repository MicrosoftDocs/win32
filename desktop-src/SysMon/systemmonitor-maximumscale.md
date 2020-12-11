---
title: SystemMonitor.MaximumScale property
description: Retrieves or sets the maximum value of the vertical (Y) axis of the graph.
ms.assetid: 305886e3-2586-47c7-a888-6e393580c456
keywords:
- MaximumScale property SysMon
- MaximumScale property SysMon , SystemMonitor class
- SystemMonitor class SysMon , MaximumScale property
topic_type:
- apiref
api_name:
- SystemMonitor.MaximumScale
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.MaximumScale property

Retrieves or sets the maximum value of the vertical (Y) axis of the graph.

This property is read-only.

## Syntax


```VB
Property MaximumScale As Long
```



## Property value

Positive maximum value of the vertical axis of the graph. The default maximum value of the vertical scale is 100. The lowest value that you can set the maximum value to is one more than the [**MinimumScale**](systemmonitor-minimumscale.md) value. The highest value that you can set the maximum value to is 999,999,999.

## Remarks

The control automatically adjusts the position of the scale numbers displayed on the vertical scale according to the size of the displayed control.

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

[**SystemMonitor.MinimumScale**](systemmonitor-minimumscale.md)
</dt> <dt>

[**SystemMonitor.ShowScaleLabels**](systemmonitor-showscalelabels.md)
</dt> </dl>

 

 





