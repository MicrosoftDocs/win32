---
title: TaskSettings.AllowHardTerminate property
description: For scripting, gets or sets a Boolean value that indicates that the task may be terminated by the Task Scheduler service using TerminateProcess.
ms.assetid: '1dfd692e-efbe-41a2-8dbd-b14cf26bbcb7'
keywords:
- AllowHardTerminate property Task Scheduler
- AllowHardTerminate property Task Scheduler , TaskSettings object
- TaskSettings object Task Scheduler , AllowHardTerminate property
topic_type:
- apiref
api_name:
- TaskSettings.AllowHardTerminate
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskSettings.AllowHardTerminate property

For scripting, gets or sets a Boolean value that indicates that the task may be terminated by the Task Scheduler service using [**TerminateProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-terminateprocess). The service will try to close the running task by sending the [**WM\_CLOSE**](../winmsg/wm-close.md) notification, and if the task does not respond, the task will be terminated only if this property is set to true.

This property is read/write.

## Syntax


```VB
TaskSettings.AllowHardTerminate As Boolean
```



## Property value

If True, the task can be terminated by using [**TerminateProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-terminateprocess). If False, the task cannot be terminated by using **TerminateProcess**.

## Remarks

When reading or writing XML for a task, this setting is specified in the [AllowHardTerminate](taskschedulerschema-allowhardterminate-settingstype-element.md) element of the Task Scheduler schema.

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

 

