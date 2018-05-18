---
title: TaskSettings.Enabled property
description: For scripting, gets or sets a Boolean value that indicates that the task is enabled. The task can be performed only when this setting is True.
ms.assetid: '6c6e7f51-9591-4b84-b06b-124cd88a0345'
keywords: ["Enabled property Task Scheduler", "Enabled property Task Scheduler , TaskSettings object", "TaskSettings object Task Scheduler , Enabled property"]
topic_type:
- apiref
api_name:
- TaskSettings.Enabled
api_location:
- taskschd.dll
api_type:
- COM
---

# TaskSettings.Enabled property

For scripting, gets or sets a Boolean value that indicates that the task is enabled. The task can be performed only when this setting is True.

This property is read/write.

## Syntax


```VB
TaskSettings.Enabled As Boolean
```



## Property value

If True, the task is enabled. If False, the task is not enabled.

## Remarks

When reading or writing XML for a task, this setting is specified in the [**Enabled (settingsType)**](taskschedulerschema-enabled-settingstype-element.md) element of the Task Scheduler schema.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





