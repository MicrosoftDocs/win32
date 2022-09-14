---
title: TaskSettings.Priority property
description: For scripting, gets or sets the priority level of the task.
ms.assetid: '2548fcb6-c649-4822-a2ea-77546aac2ec5'
keywords:
- Priority property Task Scheduler
- Priority property Task Scheduler , TaskSettings object
- TaskSettings object Task Scheduler , Priority property
topic_type:
- apiref
api_name:
- TaskSettings.Priority
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskSettings.Priority property

For scripting, gets or sets the priority level of the task.

This property is read/write.

## Syntax


```VB
TaskSettings.Priority As Integer
```



## Property value

The priority level (0-10) of the task. The default is 7.

## Remarks

Priority level 0 is the highest priority, and priority level 10 is the lowest priority. The default value is 7. Priority levels 7 and 8 are used for background tasks, and priority levels 4, 5, and 6 are used for interactive tasks.

The task's action is started in a process with a priority that is based on a Priority Class value. A Priority Level value (thread priority) is used for COM handler, message box, and email task actions. For more information about the Priority Class and Priority Level values, see [Scheduling Priorities](/windows/desktop/ProcThread/scheduling-priorities). The following table lists the possible values for the *priority* parameter, and the corresponding Priority Class and Priority Level values.



| Task *priority* | Priority Class                 | Priority Level                   |
|-----------------|--------------------------------|----------------------------------|
| 0               | REALTIME\_PRIORITY\_CLASS      | THREAD\_PRIORITY\_TIME\_CRITICAL |
| 1               | HIGH\_PRIORITY\_CLASS          | THREAD\_PRIORITY\_HIGHEST        |
| 2               | ABOVE\_NORMAL\_PRIORITY\_CLASS | THREAD\_PRIORITY\_ABOVE\_NORMAL  |
| 3               | ABOVE\_NORMAL\_PRIORITY\_CLASS | THREAD\_PRIORITY\_ABOVE\_NORMAL  |
| 4               | NORMAL\_PRIORITY\_CLASS        | THREAD\_PRIORITY\_NORMAL         |
| 5               | NORMAL\_PRIORITY\_CLASS        | THREAD\_PRIORITY\_NORMAL         |
| 6               | NORMAL\_PRIORITY\_CLASS        | THREAD\_PRIORITY\_NORMAL         |
| 7               | BELOW\_NORMAL\_PRIORITY\_CLASS | THREAD\_PRIORITY\_BELOW\_NORMAL  |
| 8               | BELOW\_NORMAL\_PRIORITY\_CLASS | THREAD\_PRIORITY\_BELOW\_NORMAL  |
| 9               | IDLE\_PRIORITY\_CLASS          | THREAD\_PRIORITY\_LOWEST         |
| 10              | IDLE\_PRIORITY\_CLASS          | THREAD\_PRIORITY\_IDLE           |



 

When reading or writing XML for a task, this setting is specified in the [**Priority (settingsType)**](taskschedulerschema-priority-settingstype-element.md) element of the Task Scheduler schema.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**TaskSettings**](tasksettings.md)
</dt> </dl>

 

