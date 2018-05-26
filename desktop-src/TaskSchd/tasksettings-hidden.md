---
title: TaskSettings.Hidden property
description: For scripting, gets or sets a Boolean value that indicates that the task will not be visible in the UI.
ms.assetid: 05d466e4-26f8-4fde-8c7e-9e16daadc220
keywords:
- Hidden property Task Scheduler
- Hidden property Task Scheduler , TaskSettings object
- TaskSettings object Task Scheduler , Hidden property
topic_type:
- apiref
api_name:
- TaskSettings.Hidden
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

# TaskSettings.Hidden property

For scripting, gets or sets a Boolean value that indicates that the task will not be visible in the UI. However, administrators can override this setting through the use of a "master switch" that makes all tasks visible in the UI.

This property is read/write.

## Syntax


```VB
TaskSettings.Hidden As Boolean
```



## Property value

If **True**, the value indicates that the task will not be visible in the UI. If **False**, the task will be visible in the UI. The default is **False**.

## Remarks

When reading or writing XML for a task, this setting is specified in the [**Hidden (settingsType)**](taskschedulerschema-hidden-settingstype-element.md) element of the Task Scheduler schema.

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

 

 





