---
title: IdleSettings.StopOnIdleEnd property
description: For scripting, gets or sets a Boolean value that indicates that the Task Scheduler will terminate the task if the idle condition ends before the task is completed.
ms.assetid: 5908bf6b-227a-4234-a741-82cf38163171
keywords:
- StopOnIdleEnd property Task Scheduler
- StopOnIdleEnd property Task Scheduler , IdleSettings object
- IdleSettings object Task Scheduler , StopOnIdleEnd property
topic_type:
- apiref
api_name:
- IdleSettings.StopOnIdleEnd
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IdleSettings.StopOnIdleEnd property

For scripting, gets or sets a Boolean value that indicates that the Task Scheduler will terminate the task if the idle condition ends before the task is completed.

## Syntax


```VB
IdleSettings.StopOnIdleEnd As Boolean
```



## Property value

A Boolean value that indicates that the Task Scheduler will terminate the task if the idle condition ends before the task is completed.

## Remarks

When reading or writing XML for a task, this setting is specified in the [**StopOnIdleEnd**](taskschedulerschema-terminateonidleend-idlesettingstype-element.md) element of the Task Scheduler schema.

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
</dt> <dt>

[**IdleSettings**](idlesettings.md)
</dt> </dl>

 

 





