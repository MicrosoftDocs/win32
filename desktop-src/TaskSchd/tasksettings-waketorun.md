---
title: TaskSettings.WakeToRun property
description: For scripting, gets or sets a Boolean value that indicates that the Task Scheduler will wake the computer when it is time to run the task.
ms.assetid: '51f83637-5bae-48c6-b750-b4467e651cec'
keywords:
- WakeToRun property Task Scheduler
- WakeToRun property Task Scheduler , TaskSettings object
- TaskSettings object Task Scheduler , WakeToRun property
topic_type:
- apiref
api_name:
- TaskSettings.WakeToRun
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskSettings.WakeToRun property

For scripting, gets or sets a Boolean value that indicates that the Task Scheduler will wake the computer when it is time to run the task.

This property is read/write.

## Syntax


```VB
TaskSettings.WakeToRun As Boolean
```



## Property value

If True, the property indicates that the Task Scheduler will wake the computer when it is time to run the task.

## Remarks

When the Task Scheduler service wakes the computer to run a task, the screen may remain off even though the computer is no longer in the sleep or hibernate mode. The screen will turn on when Windows Vista detects that a user has returned to use the computer.

When reading or writing XML for a task, this setting is specified in the [**WakeToRun**](taskschedulerschema-waketorun-settingstype-element.md) element of the Task Scheduler schema.

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

 

 





