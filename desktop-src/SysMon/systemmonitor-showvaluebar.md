---
title: SystemMonitor.ShowValueBar property
description: Retrieves or sets a value that determines whether the value bar (the set of statistical values below the graph) is displayed on the control.
ms.assetid: 320fbbbb-c4ea-4772-9b10-1e123849c255
keywords:
- ShowValueBar property SysMon
- ShowValueBar property SysMon , SystemMonitor class
- SystemMonitor class SysMon , ShowValueBar property
topic_type:
- apiref
api_name:
- SystemMonitor.ShowValueBar
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.ShowValueBar property

Retrieves or sets a value that determines whether the value bar (the set of statistical values below the graph) is displayed on the control.

This property is read-only.

## Syntax


```VB
Property ShowValueBar As Boolean
```



## Property value

True indicates that the value bar is displayed on the control; otherwise false. The default value for this property is true.

## Remarks

The displayed statistics include the last value, the average value, and the minimum and maximum values of the currently selected counter over the displayed time interval. To select the counter values to display, the user must select the counter in the Legend pane of the control.

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

 

 





