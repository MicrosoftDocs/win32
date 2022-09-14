---
title: Enabled (triggerBaseType) Element
description: Specifies that the trigger is enabled.
ms.assetid: 14c98f40-0ec5-4dc1-978e-b02c08ee2384
keywords:
- Enabled element Task Scheduler
topic_type:
- apiref
api_name:
- Enabled
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Enabled (triggerBaseType) Element

Specifies that the trigger is enabled.

``` syntax
<xs:element name="Enabled"
    type="boolean"
 />
```

The **Enabled** element is defined by the [**triggerBaseType**](taskschedulerschema-triggerbasetype-complextype.md) complex type.

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

For scripting development, this information is accessed through the [**Trigger.Enabled**](trigger-enabled.md) property that is inherited by the all trigger objects.

For C++ development, this information is accessed through the [**ITrigger::Enabled**](/windows/desktop/api/taskschd/nf-taskschd-itrigger-get_enabled) property that is inherited by the all trigger interfaces.

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

 

 





