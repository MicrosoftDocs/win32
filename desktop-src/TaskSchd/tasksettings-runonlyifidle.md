---
title: TaskSettings.RunOnlyIfIdle property
description: For scripting, gets or sets a Boolean value that indicates that the Task Scheduler will run the task only if the computer is in an idle condition.
ms.assetid: 2ea0b2bd-793b-427f-9177-c8d124e5ae25
keywords:
- RunOnlyIfIdle property Task Scheduler
- RunOnlyIfIdle property Task Scheduler , TaskSettings object
- TaskSettings object Task Scheduler , RunOnlyIfIdle property
topic_type:
- apiref
api_name:
- TaskSettings.RunOnlyIfIdle
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

# TaskSettings.RunOnlyIfIdle property

For scripting, gets or sets a Boolean value that indicates that the Task Scheduler will run the task only if the computer is in an idle condition.

This property is read/write.

## Syntax


```VB
TaskSettings.RunOnlyIfIdle As Boolean
```



## Property value

If True, the property indicates that the Task Scheduler will run the task only if the computer is in an idle condition. The default is False.

## Remarks

When reading or writing XML for a task, this setting is specified in the [**RunOnlyIfIdle**](taskschedulerschema-runonlyifidle-settingstype-element.md) element of the Task Scheduler schema.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





