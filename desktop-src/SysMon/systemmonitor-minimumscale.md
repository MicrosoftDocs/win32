---
title: SystemMonitor.MinimumScale property
description: Retrieves or sets the minimum value of the vertical (Y) axis of the graph.
ms.assetid: 22dacfbf-27bb-48fe-b646-4cf17645a131
keywords:
- MinimumScale property SysMon
- MinimumScale property SysMon , SystemMonitor class
- SystemMonitor class SysMon , MinimumScale property
topic_type:
- apiref
api_name:
- SystemMonitor.MinimumScale
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.MinimumScale property

Retrieves or sets the minimum value of the vertical (Y) axis of the graph.

This property is read-only.

## Syntax


```VB
Property MinimumScale As Long
```



## Property value

Positive minimum value of the vertical axis of the graph. The default minimum value of the vertical scale is 0. The highest value that you can set the minimum value to is one less than [**MaximumScale**](systemmonitor-maximumscale.md) value.

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

[**SystemMonitor.MaximumScale**](systemmonitor-maximumscale.md)
</dt> <dt>

[**SystemMonitor.ShowScaleLabels**](systemmonitor-showscalelabels.md)
</dt> </dl>

 

 





