---
title: TaskSettings.StopIfGoingOnBatteries property
description: For scripting, gets or sets a Boolean value that indicates that the task will be stopped if the computer is going onto batteries.
ms.assetid: 'a133cba0-c93e-4963-83a3-7587e323fc6e'
keywords:
- StopIfGoingOnBatteries property Task Scheduler
- StopIfGoingOnBatteries property Task Scheduler , TaskSettings object
- TaskSettings object Task Scheduler , StopIfGoingOnBatteries property
topic_type:
- apiref
api_name:
- TaskSettings.StopIfGoingOnBatteries
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskSettings.StopIfGoingOnBatteries property

For scripting, gets or sets a Boolean value that indicates that the task will be stopped if the computer is going onto batteries.

This property is read/write.

## Syntax


```VB
TaskSettings.StopIfGoingOnBatteries As Boolean
```



## Property value

A Boolean value that indicates that the task will be stopped if the computer is going onto batteries. If True, the property indicates that the task will be stopped if the computer is going onto batteries. If False, the property indicates that the task will not be stopped if the computer is going onto batteries. The default is True. See Remarks for more details.

## Remarks

When reading or writing XML for a task, this setting is specified in the [**StopIfGoingOnBatteries**](taskschedulerschema-stopifgoingonbatteries-settingstype-element.md) element of the Task Scheduler schema.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





