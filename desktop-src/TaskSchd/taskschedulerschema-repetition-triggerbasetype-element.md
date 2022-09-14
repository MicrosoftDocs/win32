---
title: Repetition (triggerBaseType) Element
description: Specifies how often the task is run and how long the repetition pattern is repeated after the task is started.
ms.assetid: d43c7f9a-3a7b-44a9-901b-9ad18c027b1b
keywords:
- Repetition element Task Scheduler
topic_type:
- apiref
api_name:
- Repetition
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Repetition (triggerBaseType) Element

Specifies how often the task is run and how long the repetition pattern is repeated after the task is started.

``` syntax
<xs:element name="Repetition"
    type="repetitionType"
 />
```

The **Repetition** element is defined by the [**triggerBaseType**](taskschedulerschema-triggerbasetype-complextype.md) complex type.

## Parent element



| Element                                                                                     | Derived from                                                                               | Description                                                                                  |
|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [**BootTrigger**](taskschedulerschema-boottrigger-triggergroup-element.md)                 | [**bootTriggerType**](taskschedulerschema-boottriggertype-complextype.md)                 | Specifies a trigger that starts a task when the system is booted.<br/>                 |
| [**CalendarTrigger**](taskschedulerschema-calendartrigger-triggergroup-element.md)         | [**calendarTriggerType**](taskschedulerschema-calendartriggertype-complextype.md)         | Specifies a daily, weekly, monthly, or a monthly day-of-the-week (DOW) trigger.<br/>   |
| [**EventTrigger**](taskschedulerschema-eventtrigger-triggergroup-element.md)               | [**eventTriggerType**](taskschedulerschema-eventtriggertype-complextype.md)               | Specifies a trigger that starts a task when a system event occurs.<br/>                |
| [**IdleTrigger**](taskschedulerschema-idletrigger-triggergroup-element.md)                 | [**idleTriggerType**](taskschedulerschema-idletriggertype-complextype.md)                 | Specifies a trigger that starts a task when the computer goes into an idle state.<br/> |
| [**LogonTrigger**](taskschedulerschema-logontrigger-triggergroup-element.md)               | [**logonTriggerType**](taskschedulerschema-logontriggertype-complextype.md)               | Specifies a trigger that starts a task when a user logs on.<br/>                       |
| [**RegistrationTrigger**](taskschedulerschema-registrationtrigger-triggergroup-element.md) | [**registrationTriggerType**](taskschedulerschema-registrationtriggertype-complextype.md) | Specifies a trigger that starts a task when the task is registered.<br/>               |
| [**TimeTrigger**](taskschedulerschema-timetrigger-triggergroup-element.md)                 | [**timeTriggerType**](taskschedulerschema-timetriggertype-complextype.md)                 | Specifies a trigger that starts a task when the trigger is activated.<br/>             |



## Child elements



| Element                                                                                   | Type     | Description                                                                                                         |
|-------------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------|
| [**Duration**](taskschedulerschema-duration-repetitiontype-element.md)                   | duration | Specifies how long the pattern is repeated.<br/>                                                              |
| [**Interval**](taskschedulerschema-interval-repetitiontype-element.md)                   | duration | Specifies the amount of time between each restart of the task.<br/>                                           |
| [**StopAtDurationEnd**](taskschedulerschema-stopatdurationend-repetitiontype-element.md) | boolean  | Specifies that a running instances of the task is stopped at the end of the repetition pattern duration.<br/> |



## Remarks

If you specify a repetition duration for a task, you must also specify the repetition interval.

If you register a task that contains a trigger with a repetition interval equal to one minute and a repetition duration equal to four minutes, the task will be launched five times. The five repetitions can be defined by the following pattern.

1.  A task starts at the beginning of the first minute.
2.  The next task starts at the end of the first minute.
3.  The next task starts at the end of the second minute.
4.  The next task starts at the end of the third minute.
5.  The next task starts at the end of the fourth minute.

**Windows Server 2003, Windows XP and Windows 2000:** If you register a task that contains a trigger with a repetition interval equal to one minute and a repetition duration equal to four minutes, the task will be launched four times.

**Windows Vista, Windows 7, Windows Server 2008, Windows 8 and Windows Server 2012:** Usually, setting the repetition duration to an exact multiple of the interval yields the numbers described above. However, under certain heavy load conditions, it is possible for the duration to timeout before TaskScheduler can launch the final task interval.

For scripting development, the repetition pattern is specified using the [**Trigger.Repetition**](trigger-repetition.md) property that is inherited by all the trigger objects.

For C++ development, the repetition pattern is specified using the [**ITRigger::Repetition**](/windows/desktop/api/taskschd/nf-taskschd-itrigger-get_repetition) property that is inherited by all the trigger interfaces.

## Examples

The following XML defines a boot trigger element that specifies a repetition pattern for a trigger.


```XML
<BootTrigger>
    <StartBoundary>2005-01-01T08:00:00</StartBoundary>
    <EndBounadry>2007-01-01T08:00:00</EndBoundary>
    <Enabled>true</Enabled>
    <Repetition>
        <Interval></Interval>
        <Duration></Duration>
        <StopAtDurationEnd>true</StopAtDirationEnd>
    </Repetition>
    <ExecutionTimeLimit></ExecutionTimeLimit>
    <Delay><Delay>
 </BootTrigger>
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





