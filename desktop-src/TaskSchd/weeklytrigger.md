---
title: WeeklyTrigger object
description: Scripting object that represents a trigger that starts a task based on a weekly schedule.
ms.assetid: 'a000d7a8-0239-440f-b49b-7f0c55b01e8e'
keywords:
- weekly trigger Task Scheduler , object
- WeeklyTrigger object Task Scheduler
- WeeklyTrigger object Task Scheduler , described
topic_type:
- apiref
api_name:
- WeeklyTrigger
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# WeeklyTrigger object

Scripting object that represents a trigger that starts a task based on a weekly schedule. For example, the task starts at 8:00 A.M. on a specific day of the week every week or every other week.

## Members

The **WeeklyTrigger** object has these types of members:

-   [Properties](#properties)

### Properties

The **WeeklyTrigger** object has these properties.



| Property                                                            | Access type           | Description                                                                                                                                                                                 |
|:--------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DaysOfWeek**](weeklytrigger-daysofweek.md)<br/>           | Read/write<br/> | Gets or sets the days of the week on which the task runs.<br/>                                                                                                                        |
| [**Enabled**](trigger-enabled.md)<br/>                       | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets a Boolean value that indicates whether the trigger is enabled.<br/>                                                |
| [**EndBoundary**](trigger-endboundary.md)<br/>               | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the date and time when the trigger is deactivated. The trigger cannot start the task after it is deactivated.<br/> |
| [**ExecutionTimeLimit**](trigger-executiontimelimit.md)<br/> | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the maximum amount of time that the task launched by the trigger is allowed to run.<br/>                           |
| [**Id**](/windows/desktop/api/taskschd/nf-taskschd-itrigger-get_id)<br/>                                | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the identifier for the trigger.<br/>                                                                               |
| [**RandomDelay**](weeklytrigger-randomdelay.md)<br/>         | Read/write<br/> | Gets or sets a delay time that is randomly added to the start time of the trigger.<br/>                                                                                               |
| [**Repetition**](trigger-repetition.md)<br/>                 | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets how often the task is run and how long the repetition pattern is repeated after the task is started.<br/>          |
| [**StartBoundary**](trigger-startboundary.md)<br/>           | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the date and time when the trigger is activated.<br/>                                                              |
| [**Type**](/windows/desktop/api/taskschd/nf-taskschd-itrigger-get_type)<br/>                            | Read-only<br/>  | Inherited from the [**Trigger**](trigger.md) object. Gets the type of the trigger.<br/>                                                                                              |
| [**WeeksInterval**](weeklytrigger-weeksinterval.md)<br/>     | Read/write<br/> | Gets or sets the interval between the weeks in the schedule.<br/>                                                                                                                     |



 

## Remarks

The time of day that the task is started is set by the [**StartBoundary**](trigger-startboundary.md) property.

When reading or writing your own XML for a task, a weekly trigger is specified using the [**ScheduleByWeek**](taskschedulerschema-schedulebyweek-calendartriggertype-element.md) element of the Task Scheduler schema.

## Examples

For more information and a code example for this scripting object, see [Weekly Trigger Example (Scripting)](weekly-trigger-example--scripting-.md).

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

 

 





