---
title: EndBoundary (triggerBaseType) Element
description: Specifies the date and time when the trigger is deactivated. The trigger cannot start the task after it is deactivated.
ms.assetid: 84731c0b-3fb8-44dd-be1a-67547add1f9e
keywords:
- EndBoundary element Task Scheduler
topic_type:
- apiref
api_name:
- EndBoundary
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# EndBoundary (triggerBaseType) Element

Specifies the date and time when the trigger is deactivated. The trigger cannot start the task after it is deactivated.

``` syntax
<xs:element name="EndBoundary"
    type="dateTime"
 />
```

The **EndBoundary** element is defined by the [**triggerBaseType**](taskschedulerschema-triggerbasetype-complextype.md) complex type.

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



## Remarks

For scripting development, the end boundary is specified using the [**Trigger.EndBoundary**](trigger-endboundary.md) property that is inherited by the all trigger objects.

For C++ development, the end boundary is specified using the [**ITrigger::EndBoundary**](/windows/desktop/api/taskschd/nf-taskschd-itrigger-get_endboundary) property that is inherited by the all trigger interfaces.

## Examples

The following XML defines a boot trigger element that defines an end boundary of January 1, 2007: 8:00 AM.


```XML
<BootTrigger>
    <StartBoundary>2005-01-01T08:00:00</StartBoundary>
    <EndBounadry>2007-01-01T08:00:00</EndBoundary>
    <Enabled>true</Enabled>
    <Repetition></Repetition>
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

 

 





