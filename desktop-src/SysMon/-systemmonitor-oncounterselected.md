---
title: SystemMonitor.OnCounterSelected event
description: Notifies you when a counter is selected.
ms.assetid: 788a95a7-47ec-41f9-bf46-324ad3cc8a4e
keywords:
- OnCounterSelected event SysMon
- OnCounterSelected event SysMon , SystemMonitor class
- SystemMonitor class SysMon , OnCounterSelected event
topic_type:
- apiref
api_name:
- SystemMonitor.OnCounterSelected
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.OnCounterSelected event

Notifies you when a counter is selected.

## Syntax


```VB
SystemMonitor.OnCounterSelected( _
  ByVal index As Long _
)
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

Index of the selected counter in the [**Counters**](counters.md) collection object.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

You can receive this event when

-   You set [**CounterItem.Selected**](counteritem-selected.md) to True
-   The user selects a counter in the Legend
-   The user double-clicks on a counter in the Legend

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



## See also

<dl> <dt>

[**SystemMonitor.OnCounterAdded**](systemmonitor-oncounteradded.md)
</dt> <dt>

[**SystemMonitor.OnCounterDeleted**](-systemmonitor-oncounterdeleted.md)
</dt> </dl>

 

 





