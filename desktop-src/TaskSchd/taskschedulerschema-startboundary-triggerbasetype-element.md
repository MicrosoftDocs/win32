---
title: StartBoundary (triggerBaseType) Element
description: Specifies the date and time when the trigger is activated.
ms.assetid: 95a62ae5-4eba-49df-a25f-0d1181772833
keywords:
- StartBoundary element Task Scheduler
topic_type:
- apiref
api_name:
- StartBoundary
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# StartBoundary (triggerBaseType) Element

Specifies the date and time when the trigger is activated.

``` syntax
<xs:element name="StartBoundary"
    type="dateTime"
 />
```

The **StartBoundary** element is defined by the [**triggerBaseType**](taskschedulerschema-triggerbasetype-complextype.md) complex type.

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

The **&lt;StartBoundary&gt;** element is a required element for time and calendar triggers ([**&lt;TimeTrigger&gt;**](taskschedulerschema-timetrigger-triggergroup-element.md) and [**&lt;CalendarTrigger&gt;**](taskschedulerschema-calendartrigger-triggergroup-element.md)).

For scripting development, the end boundary is specified using the [**Trigger.StartBoundary**](trigger-startboundary.md) property that is inherited by the all trigger objects.

For C++ development, the end boundary is specified using the [**ITrigger::StartBoundary**](/windows/desktop/api/taskschd/nf-taskschd-itrigger-get_startboundary) property that is inherited by the all trigger interfaces.

## Examples

The following XML defines a boot trigger element that defines a start boundary of January 1, 2005: 8:00 AM.


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

 

 





