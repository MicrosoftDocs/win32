---
title: DailyTrigger object
description: Scripting object that represents a trigger that starts a task based on a daily schedule.
ms.assetid: f03f53a0-0060-4793-96c1-b47a96852579
keywords:
- daily trigger Task Scheduler , object
- DailyTrigger object Task Scheduler
- DailyTrigger object Task Scheduler , described
topic_type:
- apiref
api_name:
- DailyTrigger
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# DailyTrigger object

Scripting object that represents a trigger that starts a task based on a daily schedule.

## Members

The **DailyTrigger** object has these types of members:

-   [Properties](#properties)

### Properties

The **DailyTrigger** object has these properties.



| Property                                                            | Access type           | Description                                                                                                                                                                                 |
|:--------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DaysInterval**](dailytrigger-daysinterval.md)<br/>        | Read/write<br/> | Gets or sets the interval between the days in the schedule.<br/>                                                                                                                      |
| [**Enabled**](trigger-enabled.md)<br/>                       | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets a Boolean value that indicates whether the trigger is enabled.<br/>                                                |
| [**EndBoundary**](trigger-endboundary.md)<br/>               | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the date and time when the trigger is deactivated. The trigger cannot start the task after it is deactivated.<br/> |
| [**ExecutionTimeLimit**](trigger-executiontimelimit.md)<br/> | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the maximum amount of time that the task launched by the trigger is allowed to run.<br/>                           |
| [**Id**](/windows/desktop/api/taskschd/nf-taskschd-itrigger-get_id)<br/>                                | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the identifier for the trigger.<br/>                                                                               |
| [**RandomDelay**](dailytrigger-randomdelay.md)<br/>          | Read/write<br/> | Gets or sets a delay time that is randomly added to the start time of the trigger.<br/>                                                                                               |
| [**Repetition**](trigger-repetition.md)<br/>                 | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets how often the task is run and how long the repetition pattern is repeated after the task is started.<br/>          |
| [**StartBoundary**](trigger-startboundary.md)<br/>           | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the date and time when the trigger is activated.<br/>                                                              |
| [**Type**](/windows/desktop/api/taskschd/nf-taskschd-itrigger-get_type)<br/>                            | Read-only<br/>  | Inherited from the [**Trigger**](trigger.md) object. Gets the type of the trigger.<br/>                                                                                              |



 

## Remarks

The time of day that the task is started is set by the [**StartBoundary**](trigger-startboundary.md) property.

An interval of 1 produces a daily schedule. An interval of 2 produces an every other day schedule and so on.

When reading or writing your own XML for a task, a daily trigger is specified using the [**ScheduleByDay**](taskschedulerschema-schedulebyday-calendartriggertype-element.md) element of the Task Scheduler schema.

## Examples

For more information and a code example for this scripting object, see [Daily Trigger Example (Scripting)](daily-trigger-example--scripting-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**Trigger**](trigger.md)
</dt> <dt>

[**TriggerCollection**](triggercollection.md)
</dt> <dt>

[**TriggerCollection.Create**](triggercollection-create.md)
</dt> </dl>

 

 





