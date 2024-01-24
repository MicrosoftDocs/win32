---
title: SystemMonitor.OnDblClick event
description: Notifies you when a user double-clicks the graph line, histogram bar, or report item with the left mouse button.
ms.assetid: 06ad86ff-fcc0-4be5-a54c-7a6aa1147cf9
keywords:
- OnDblClick event SysMon
- OnDblClick event SysMon , SystemMonitor class
- SystemMonitor class SysMon , OnDblClick event
topic_type:
- apiref
api_name:
- SystemMonitor.OnDblClick
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.OnDblClick event

Notifies you when a user double-clicks the graph line, histogram bar, or report item with the left mouse button.

## Syntax


```VB
SystemMonitor.OnDblClick( _
  ByRef index As Long _
)
```



## Parameters

<dl> <dt>

*index* \[in, out\]
</dt> <dd>

Index of the selected counter in the [**Counters**](counters.md) collection object. An index value of 0 is returned if no counter was selected; otherwise, the index of the selected counter is returned.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

When this event is triggered, the counter that the user selected in the line graph and histogram is also selected in the Legend pane. This makes it easier for the user of the System Monitor to see which counter is selected when several counter values are displayed.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



 

 





