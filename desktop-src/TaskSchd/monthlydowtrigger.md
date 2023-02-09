---
title: MonthlyDOWTrigger object
description: Scripting object that represents a trigger that starts a task on a monthly day-of-week schedule.
ms.assetid: '18607189-295f-4f7d-bf72-f0ac8d5067cf'
keywords:
- monthly DOW trigger Task Scheduler , object
- MonthlyDOWTrigger object Task Scheduler
- MonthlyDOWTrigger object Task Scheduler , described
topic_type:
- apiref
api_name:
- MonthlyDOWTrigger
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# MonthlyDOWTrigger object

Scripting object that represents a trigger that starts a task on a monthly day-of-week schedule. For example, the task starts on every first Thursday, May through October.

## Members

The **MonthlyDOWTrigger** object has these types of members:

-   [Properties](#properties)

### Properties

The **MonthlyDOWTrigger** object has these properties.



| Property                                                                          | Access type           | Description                                                                                                                                                                                 |
|:----------------------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DaysOfWeek**](monthlydowtrigger-daysofweek.md)<br/>                     | Read/write<br/> | Gets or sets the days of the week during which the task runs.<br/>                                                                                                                    |
| [**Enabled**](trigger-enabled.md)<br/>                                     | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets a Boolean value that indicates whether the trigger is enabled.<br/>                                                |
| [EndBoundary](trigger-endboundary.md)<br/>                                 | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the date and time when the trigger is deactivated. The trigger cannot start the task after it is deactivated.<br/> |
| [**ExecutionTimeLimit**](trigger-executiontimelimit.md)<br/>               | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the maximum amount of time that the task launched by this trigger is allowed to run.<br/>                          |
| [**Id**](/windows/desktop/api/taskschd/nf-taskschd-itrigger-get_id)<br/>                                              | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the identifier for the trigger.<br/>                                                                               |
| [**MonthsOfYear**](monthlydowtrigger-monthsofyear.md)<br/>                 | Read/write<br/> | Gets or sets the months of the year during which the task runs.<br/>                                                                                                                  |
| [**RandomDelay**](monthlydowtrigger-randomdelay.md)<br/>                   | Read/write<br/> | Gets or sets a delay time that is randomly added to the start time of the trigger.<br/>                                                                                               |
| [**Repetition**](trigger-repetition.md)<br/>                               | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets how often the task is run and how long the repetition pattern is repeated after the task is started.<br/>          |
| [**RunOnLastWeekOfMonth**](monthlydowtrigger-runonlastweekofmonth.md)<br/> | Read/write<br/> | Gets or sets a Boolean value that indicates that the task runs on the last week of the month.<br/>                                                                                    |
| [**StartBoundary**](trigger-startboundary.md)<br/>                         | Read/write<br/> | Inherited from the [**Trigger**](trigger.md) object. Gets or sets the date and time when the trigger is activated.<br/>                                                              |
| [**Type**](/windows/desktop/api/taskschd/nf-taskschd-itrigger-get_type)<br/>                                          | Read-only<br/>  | Inherited from the [**Trigger**](trigger.md) object. Gets the type of the trigger.<br/>                                                                                              |
| [**WeeksOfMonth**](monthlydowtrigger-weeksofmonth.md)<br/>                 | Read/write<br/> | Gets or sets the weeks of the month during which the task runs.<br/>                                                                                                                  |



 

## Remarks

The time of day that the task is started is set by the [**StartBoundary**](trigger-startboundary.md) property.

When reading or writing XML for a task, a monthly day-of-week trigger is specified using the [**ScheduleByMonthDayOfWeek**](taskschedulerschema-schedulebymonthdayofweek-calendartriggertype-element.md) element of the Task Scheduler schema.

On the day that daylight savings time (DST) starts in a year, for a Pacific time zone (time shifted from 02:00 AM to 03:00 AM in 2022), any task that's scheduled to run between 02:00 AM and 02:59:59:999 AM will run at the earliest possible time that exists in that given day&mdash;that is, at 03:00 AM. This applies to all DST time zones based on the various times at which they observe DST.

Consider a weekly task that's set to run every Sunday of 2022 at 02:30 AM in the Pacific time zone such that the next run time is Mar 13, 2022 02:30 AM. As 02:30 AM is a time that doesn't exist on Mar 13, 2022, the task runs at 03:00 AM instead. On other Sundays of the year, the task runs as usual at 02:30 AM.

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

[Task Scheduler Objects](task-scheduler-objects.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> <dt>

[**TriggerCollection**](triggercollection.md)
</dt> <dt>

[**TriggerCollection.Create**](triggercollection-create.md)
</dt> </dl>

 

 





