---
title: RepetitionPattern object
description: Scripting object that defines how often the task is run and how long the repetition pattern is repeated after the task is started.
ms.assetid: 'a4e63da7-78ab-46a9-9b55-8460355753cf'
keywords:
- triggers Task Scheduler , repetition pattern object
- repetition pattern Task Scheduler , object
- RepetitionPattern object Task Scheduler
- RepetitionPattern object Task Scheduler , described
topic_type:
- apiref
api_name:
- RepetitionPattern
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RepetitionPattern object

Scripting object that defines how often the task is run and how long the repetition pattern is repeated after the task is started.

## Members

The **RepetitionPattern** object has these types of members:

-   [Properties](#properties)

### Properties

The **RepetitionPattern** object has these properties.



| Property                                                                    | Access type           | Description                                                                                                                                        |
|:----------------------------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Duration**](repetitionpattern-duration.md)<br/>                   | Read/write<br/> | Gets or sets how long the pattern is repeated.<br/>                                                                                          |
| [**Interval**](repetitionpattern-interval.md)<br/>                   | Read/write<br/> | Gets or sets the amount of time between each restart of the task.<br/>                                                                       |
| [**StopAtDurationEnd**](repetitionpattern-stopatdurationend.md)<br/> | Read/write<br/> | Gets or sets a Boolean value that indicates if a running instance of the task is stopped at the end of the repetition pattern duration.<br/> |



 

## Remarks

If you specify a repetition duration for a task, you must also specify the repetition interval.

If you register a task that contains a trigger with a repetition interval equal to one minute and a repetition duration equal to four minutes, the task will be launched five times. The five repetitions can be defined by the following pattern.

1.  A task starts at the beginning of the first minute.
2.  The next task starts at the end of the first minute.
3.  The next task starts at the end of the second minute.
4.  The next task starts at the end of the third minute.
5.  The next task starts at the end of the fourth minute.

**Windows Server 2003, Windows XP and Windows 2000:** If you register a task that contains a trigger with a repetition interval equal to one minute and a repetition duration equal to four minutes, the task will be launched four times.

When reading or writing XML for a task, the repetition pattern is specified using the [**Repetition**](taskschedulerschema-repetition-triggerbasetype-element.md) element of the Task Scheduler schema.

## Examples

For more information and example code for this property, see [Daily Trigger Example (Scripting)](daily-trigger-example--scripting-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[Task Scheduler Objects](task-scheduler-objects.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





