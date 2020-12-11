---
title: TaskSettings.IdleSettings property
description: For scripting, gets or sets the information that specifies how the Task Scheduler performs tasks when the computer is in an idle condition.
ms.assetid: '5205db6d-668e-498a-bbd5-edfcf66eec7f'
keywords:
- IdleSettings property Task Scheduler
- IdleSettings property Task Scheduler , TaskSettings object
- TaskSettings object Task Scheduler , IdleSettings property
topic_type:
- apiref
api_name:
- TaskSettings.IdleSettings
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskSettings.IdleSettings property

For scripting, gets or sets the information that specifies how the Task Scheduler performs tasks when the computer is in an idle condition. For information about idle conditions, see [Task Idle Conditions](task-idle-conditions.md).

This property is read/write.

## Syntax


```VB
TaskSettings.IdleSettings As IdleSettings
```



## Property value

An [**IdleSettings**](idlesettings.md) object that specifies how the Task Scheduler handles the task when the computer goes into an idle condition.

## Remarks

When reading or writing XML for a task, this setting is specified in the [**IdleSettings**](taskschedulerschema-idlesettings-settingstype-element.md) element of the Task Scheduler schema.

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

 

 





