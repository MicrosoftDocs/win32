---
title: SystemMonitor.OnCounterAdded event
description: Notifies you when a counter is added to the Counters collection.
ms.assetid: f798443f-e2f1-4d25-b142-d88d6e4fe12c
keywords:
- OnCounterAdded event SysMon
- OnCounterAdded event SysMon , SystemMonitor class
- SystemMonitor class SysMon , OnCounterAdded event
topic_type:
- apiref
api_name:
- SystemMonitor.OnCounterAdded
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.OnCounterAdded event

Notifies you when a counter is added to the [**Counters**](counters.md) collection.

## Syntax


```VB
SystemMonitor.OnCounterAdded( _
  ByVal index As Long _
)
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

Index of the counter added to the [**Counters**](counters.md) collection object.

</dd> </dl>

## Return value

This event does not return a value.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



## See also

<dl> <dt>

[**SystemMonitor.OnCounterDeleted**](-systemmonitor-oncounterdeleted.md)
</dt> <dt>

[**SystemMonitor.OnCounterSelected**](-systemmonitor-oncounterselected.md)
</dt> </dl>

 

 





