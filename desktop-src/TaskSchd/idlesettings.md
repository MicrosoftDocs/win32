---
title: IdleSettings object
description: Scripting object that specifies how the Task Scheduler performs tasks when the computer is in an idle condition.
ms.assetid: d303596a-0a84-4056-9f7a-5a9512852002
keywords:
- IdleSettings object Task Scheduler
- IdleSettings object Task Scheduler , described
topic_type:
- apiref
api_name:
- IdleSettings
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IdleSettings object

A scripting object that specifies how the Task Scheduler performs tasks when the computer is in an idle condition. For information about idle conditions, see [Task Idle Conditions](task-idle-conditions.md).

## Members

The **IdleSettings** object has these types of members:

- [Properties](#properties)

### Properties

The **IdleSettings** object has these properties.

> [!NOTE]
> The *IdleDuration* and *WaitTimeout* settings are deprecated. They're still present in the Task Scheduler user interface, and their interface methods may still return valid values, but they're no longer used.

| Property                                                       | Access type           | Description                                                                                                                                                     |
|:---------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**RestartOnIdle**](idlesettings-restartonidle.md)<br/> | Read/write<br/> | Gets or sets a Boolean value that indicates whether the task is restarted when the computer cycles into an idle condition more than once.<br/>            |
| [**StopOnIdleEnd**](idlesettings-stoponidleend.md)<br/> | Read/write<br/> | Gets or sets a Boolean value that indicates that the Task Scheduler will terminate the task if the idle condition ends before the task is completed.<br/> |
| **Deprecated**: [**IdleDuration**](idlesettings-idleduration.md)<br/>   | Read/write<br/> | Gets or sets a value that indicates the amount of time that the computer must be in an idle state before the task is run.<br/>                            |
| **Deprecated**: [**WaitTimeout**](idlesettings-waittimeout.md)<br/>     | Read/write<br/> | Gets or sets a value that indicates the amount of time that the Task Scheduler will wait for an idle condition to occur.<br/>                             |

## Remarks

When reading or writing XML for a task, this setting is specified in the [**IdleSettings**](taskschedulerschema-idlesettings-settingstype-element.md) element of the Task Scheduler schema.

If a task is triggered by an idle trigger, then the [**IdleSettings.WaitTimeout**](idlesettings-waittimeout.md) property is ignored.

> [!NOTE]
> *IdleSettings.IdleDuration* and *IdleSettings.WaitTimeout* are deprecated.

## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |

## See also

[Task Scheduler Objects](task-scheduler-objects.md)

[Task Scheduler](task-scheduler-start-page.md)
