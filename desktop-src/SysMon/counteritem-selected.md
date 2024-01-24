---
title: CounterItem.Selected property
description: Retrieves or sets a value that indicates if the counter is selected.
ms.assetid: 293cc2ea-728c-4364-be2b-080bd188fe1c
keywords:
- Selected property SysMon
- Selected property SysMon , CounterItem object
- CounterItem object SysMon , Selected property
topic_type:
- apiref
api_name:
- CounterItem.Selected
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# CounterItem.Selected property

Retrieves or sets a value that indicates if the counter is selected.

This property is read/write.

## Syntax


```VB
Property Selected As Boolean
```



## Property value

True if the counter is selected; otherwise, false.

## Remarks

You can select one or more counters from the collection of counters. Selecting a counter, selects the counter in the Legend, makes the counter visible in the Legend, and generates an [**OnCounterSelected**](-systemmonitor-oncounterselected.md) event.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



## See also

<dl> <dt>

[**CounterItem**](counteritem.md)
</dt> </dl>

 

 





