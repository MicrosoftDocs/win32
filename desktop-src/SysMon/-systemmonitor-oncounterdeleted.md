---
title: SystemMonitor.OnCounterDeleted event
description: Notifies you before a counter is deleted from the Counters collection.
ms.assetid: ab6bc1ba-20cd-4774-853e-b6adb765fae3
keywords:
- OnCounterDeleted event SysMon
- OnCounterDeleted event SysMon , SystemMonitor class
- SystemMonitor class SysMon , OnCounterDeleted event
topic_type:
- apiref
api_name:
- SystemMonitor.OnCounterDeleted
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.OnCounterDeleted event

Notifies you before a counter is deleted from the [**Counters**](counters.md) collection.

## Syntax


```VB
SystemMonitor.OnCounterDeleted( _
  ByVal index As Long _
)
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

Index of the counter to be deleted from the [**Counters**](counters.md) collection object.

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

[**SystemMonitor.OnCounterAdded**](systemmonitor-oncounteradded.md)
</dt> <dt>

[**SystemMonitor.OnCounterSelected**](-systemmonitor-oncounterselected.md)
</dt> </dl>

 

 





