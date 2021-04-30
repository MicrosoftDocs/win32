---
title: TaskSettings.AllowDemandStart property
description: For scripting, gets or sets a Boolean value that indicates that the task can be started by using either the Run command or the Context menu.
ms.assetid: '1eae19ae-3b4d-4eb2-82d0-685ef2729f36'
keywords:
- AllowDemandStart property Task Scheduler
- AllowDemandStart property Task Scheduler , TaskSettings object
- TaskSettings object Task Scheduler , AllowDemandStart property
topic_type:
- apiref
api_name:
- TaskSettings.AllowDemandStart
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskSettings.AllowDemandStart property

For scripting, gets or sets a Boolean value that indicates that the task can be started by using either the Run command or the Context menu.

This property is read/write.

## Syntax


```VB
TaskSettings.AllowDemandStart As Boolean
```



## Property value

If True, the task can be run by using the Run command or the Context menu. If False, the task cannot be run using the Run command or the Context menu. The default is True.

## Remarks

When this property is set to True, the task can be started independent of when any triggers start the task.

When reading or writing XML for a task, this setting is specified in the [AllowStartOnDemand](taskschedulerschema-allowstartondemand-settingstype-element.md) element of the Task Scheduler schema.

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

 

 





