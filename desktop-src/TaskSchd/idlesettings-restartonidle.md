---
title: IdleSettings.RestartOnIdle property
description: For scripting, gets or sets a Boolean value that indicates whether the task is restarted when the computer cycles into an idle condition more than once.
ms.assetid: c77b6f5f-659c-4aa0-a5f7-39c01e5ca65e
keywords:
- RestartOnIdle property Task Scheduler
- RestartOnIdle property Task Scheduler , IdleSettings object
- IdleSettings object Task Scheduler , RestartOnIdle property
topic_type:
- apiref
api_name:
- IdleSettings.RestartOnIdle
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IdleSettings.RestartOnIdle property

For scripting, gets or sets a Boolean value that indicates whether the task is restarted when the computer cycles into an idle condition more than once.

## Syntax


```VB
IdleSettings.RestartOnIdle As Boolean
```



## Property value

A Boolean value that indicates whether the task must be restarted when the computer cycles into an idle condition more than once. The default is False.

## Remarks

This property is only used if the [**IdleSettings.StopOnIdleEnd**](idlesettings-stoponidleend.md) property is set to True.

When reading or writing XML for a task, this setting is specified in the [**RestartOnIdle**](taskschedulerschema-restartonidle-idlesettingstype-element.md) element of the Task Scheduler schema.

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

 

 





