---
title: TaskSettings.RestartInterval property
description: For scripting, gets or sets a value that specifies how long the Task Scheduler will attempt to restart the task.
ms.assetid: 'ad6f254d-55a8-478e-984e-a459f22043b5'
keywords:
- RestartInterval property Task Scheduler
- RestartInterval property Task Scheduler , TaskSettings object
- TaskSettings object Task Scheduler , RestartInterval property
topic_type:
- apiref
api_name:
- TaskSettings.RestartInterval
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskSettings.RestartInterval property

For scripting, gets or sets a value that specifies how long the Task Scheduler will attempt to restart the task.

This property is read/write.

## Syntax


```VB
TaskSettings.RestartInterval As String
```



## Property value

A value that specifies how long the Task Scheduler will attempt to restart the task. If this property is set, the [**RestartCount**](tasksettings-restartcount.md) property must also be set. The format for this string is `P<days>DT<hours>H<minutes>M<seconds>S` (for example, "PT5M" is 5 minutes, "PT1H" is 1 hour, and "PT20M" is 20 minutes). The maximum time allowed is 31 days, and the minimum time allowed is 1 minute.

## Remarks

When reading or writing XML for a task, this setting is specified in the [**Interval**](taskschedulerschema-interval-restarttype-element.md) element of the Task Scheduler schema.

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

 

 





