---
title: TaskSettings.StartWhenAvailable property
description: For scripting, gets or sets a Boolean value that indicates that the Task Scheduler can start the task at any time after its scheduled time has passed.
ms.assetid: '911de67c-baf8-4346-9b4c-e39e5f96c0fe'
keywords:
- StartWhenAvailable property Task Scheduler
- StartWhenAvailable property Task Scheduler , TaskSettings object
- TaskSettings object Task Scheduler , StartWhenAvailable property
topic_type:
- apiref
api_name:
- TaskSettings.StartWhenAvailable
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskSettings.StartWhenAvailable property

For scripting, gets or sets a Boolean value that indicates that the Task Scheduler can start the task at any time after its scheduled time has passed.

This property is read/write.

## Syntax


```VB
TaskSettings.StartWhenAvailable As Boolean
```



## Property value

If True, the property indicates that the Task Scheduler can start the task at any time after its scheduled time has passed. The default is False.

## Remarks

This property applies only to time-based tasks with an end boundary or time-based tasks that are set to repeat infinitely.

Tasks that are started after the scheduled time has passed (because of the [**StartWhenAvailable**](/windows/desktop/api/taskschd/nf-taskschd-itasksettings-get_startwhenavailable) property being set to True) are queued in the Task Scheduler service's queue of tasks and they are started after a delay. The default delay is 10 minutes.

When reading or writing XML for a task, this setting is specified in the [**StartWhenAvailable**](taskschedulerschema-startwhenavailable-settingstype-element.md) element of the Task Scheduler schema.

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

 

 





