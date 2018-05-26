---
title: TaskSettings.Compatibility property
description: For scripting, gets or sets an integer value that indicates which version of Task Scheduler a task is compatible with.
ms.assetid: 04f77d3c-44fa-4091-b99e-af062f067ef9
keywords:
- Compatibility property Task Scheduler
- Compatibility property Task Scheduler , TaskSettings object
- TaskSettings object Task Scheduler , Compatibility property
topic_type:
- apiref
api_name:
- TaskSettings.Compatibility
api_location:
- taskschd.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TaskSettings.Compatibility property

For scripting, gets or sets an integer value that indicates which version of Task Scheduler a task is compatible with.

This property is read/write.

## Syntax


```VB
TaskSettings.Compatibility As Integer
```



## Property value



| Value                                                                                                                                                                                                                                         | Meaning                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <span id="TASK_COMPATIBILITY_AT"></span><span id="task_compatibility_at"></span><dl> <dt>**TASK\_COMPATIBILITY\_AT**</dt> <dt>0</dt> </dl> | The task is compatible with the AT command.<br/>     |
| <span id="TASK_COMPATIBILITY_V1"></span><span id="task_compatibility_v1"></span><dl> <dt>**TASK\_COMPATIBILITY\_V1**</dt> <dt>1</dt> </dl> | The task is compatible with Task Scheduler 1.0.<br/> |
| <span id="TASK_COMPATIBILITY_V2"></span><span id="task_compatibility_v2"></span><dl> <dt>**TASK\_COMPATIBILITY\_V2**</dt> <dt>2</dt> </dl> | The task is compatible with Task Scheduler 2.0.<br/> |



 

## Remarks

Task compatibility, which is set through the [**Compatibility**](/windows/win32/taskschd/nf-taskschd-itasksettings-get_compatibility?branch=master) property, should only be set to TASK\_COMPATIBILITY\_V1 if a task needs to be accessed or modified from a Windows XP, Windows Server 2003, or Windows 2000 computer. Otherwise, it is recommended that Task Scheduler 2.0 compatibility be used because the task will have more features.

Tasks compatible with the AT command can only have one time trigger.

Tasks compatible with Task Scheduler 1.0 can only have a time trigger, a logon trigger, or a boot trigger, and the task can only have an executable action.

For more information about task compatibility, see [What's New in Task Scheduler](what-s-new-in-task-scheduler.md) and [Tasks](tasks.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**TASK\_COMPATIBILITY**](/windows/win32/taskschd/ne-taskschd-_task_compatibility?branch=master)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





