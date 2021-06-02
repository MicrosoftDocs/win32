---
title: SystemMonitor.Highlight property
description: Retrieves or sets a value indicating whether the values of the selected counters are highlighted in the graph.
ms.assetid: 5342b81f-71bb-4564-b520-1e91d3002c5b
keywords:
- Highlight property SysMon
- Highlight property SysMon , SystemMonitor class
- SystemMonitor class SysMon , Highlight property
topic_type:
- apiref
api_name:
- SystemMonitor.Highlight
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.Highlight property

Retrieves or sets a value indicating whether the values of the selected counters are highlighted in the graph.

This property is read-only.

## Syntax


```VB
Property Highlight As Boolean
```



## Property value

True indicates that the values of the selected counters are highlighted in the graph; otherwise, False. The default value is False.

## Remarks

To select one or more counters, you can set [**CounterItem.Selected**](counteritem-selected.md) to True, or the user can select the counters from the list of counters shown in the Legend.

**Prior to Windows Vista:** You cannot programmatically select counters and the user can select only one counter from the list of counters shown in the Legend.

Highlighting can be black or white, depending on the value of the [**BackColor**](systemmonitor-backcolor.md) property. The highlighting is automatically set to the color that will provide sufficient contrast between highlight color and the background color.

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

[**CounterItem.Selected**](counteritem-selected.md)
</dt> </dl>

 

 





