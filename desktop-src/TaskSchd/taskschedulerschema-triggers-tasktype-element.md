---
title: Triggers (taskType) Element
description: Specifies the triggers that start the task.
ms.assetid: 4bf8e85e-3742-433d-821f-736fb2ff7139
keywords:
- Triggers element Task Scheduler
topic_type:
- apiref
api_name:
- Triggers
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Triggers (taskType) Element

Specifies the triggers that start the task.

``` syntax
<xs:element name="Triggers"
    type="triggersType"
 />
```

The **Triggers** element is defined by the [**triggersType**](taskschedulerschema-triggerstype-complextype.md) complex type.

## Parent element



| Element                                          | Derived from                                                 | Description                                                                  |
|--------------------------------------------------|--------------------------------------------------------------|------------------------------------------------------------------------------|
| [**Task**](taskschedulerschema-task-element.md) | [**taskType**](taskschedulerschema-tasktype-complextype.md) | Defines the task that is performed by the Task Scheduler service.<br/> |



## Child elements



| Element                                                                                     | Type                                                                                       | Description                                                                                  |
|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [**BootTrigger**](taskschedulerschema-boottrigger-triggergroup-element.md)                 | [**bootTriggerType**](taskschedulerschema-boottriggertype-complextype.md)                 | Specifies a trigger that starts a task when the system is booted.<br/>                 |
| [**CalendarTrigger**](taskschedulerschema-calendartrigger-triggergroup-element.md)         | [**calendarTriggerType**](taskschedulerschema-calendartriggertype-complextype.md)         | Specifies a daily, weekly, monthly, or a monthly day-of-the-week (DOW) trigger.<br/>   |
| [**EventTrigger**](taskschedulerschema-eventtrigger-triggergroup-element.md)               | [**eventTriggerType**](taskschedulerschema-eventtriggertype-complextype.md)               | Specifies a trigger that starts a task when a system event occurs.<br/>                |
| [**IdleTrigger**](taskschedulerschema-idletrigger-triggergroup-element.md)                 | [**idleTriggerType**](taskschedulerschema-idletriggertype-complextype.md)                 | Specifies a trigger that starts a task when the computer goes into an idle state.<br/> |
| [**LogonTrigger**](taskschedulerschema-logontrigger-triggergroup-element.md)               | [**logonTriggerType**](taskschedulerschema-logontriggertype-complextype.md)               | Specifies a trigger that starts a task when a user logs on.<br/>                       |
| [**RegistrationTrigger**](taskschedulerschema-registrationtrigger-triggergroup-element.md) | [**registrationTriggerType**](taskschedulerschema-registrationtriggertype-complextype.md) | Specifies a trigger that starts a task when the task is registered.<br/>               |
| [**TimeTrigger**](taskschedulerschema-timetrigger-triggergroup-element.md)                 | [**timeTriggerType**](taskschedulerschema-timetriggertype-complextype.md)                 | Specifies a trigger that starts a task when the trigger is activated.<br/>             |



## Remarks

The child elements listed above can be added in any order.

For C++ development, the triggers of a task are specified using the [**Triggers property of ITaskDefinition**](/windows/desktop/api/taskschd/nf-taskschd-itaskdefinition-get_triggers).

For scripting development, the triggers of a task are specified using the [**TaskDefinition.Triggers**](taskdefinition-triggers.md) property.

## Examples

For a complete example of the XML for a task that specifies a trigger, see [Time Trigger Example (XML)](time-trigger-example--xml-.md).

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

 

 





