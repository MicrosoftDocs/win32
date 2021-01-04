---
title: Delay (eventTriggerType) Element
description: Specifies the amount of time between when the event occurs and when the task is started.
ms.assetid: b38bebc7-9818-41f0-a277-cb0e63c28d86
keywords:
- Delay element Task Scheduler
topic_type:
- apiref
api_name:
- Delay
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Delay (eventTriggerType) Element

Specifies the amount of time between when the event occurs and when the task is started. The format for this string is PnYnMnDTnHnMnS, where nY is the number of years, nM is the number of months, nD is the number of days, 'T' is the date/time separator, nH is the number of hours, nM is the number of minutes, and nS is the number of seconds (for example, PT5M specifies 5 minutes and P1M4DT2H5M specifies one month, four days, two hours, and five minutes). For more information about the duration type, see <https://go.microsoft.com/fwlink/p/?linkid=106886>.

``` syntax
<xs:element name="Delay"
    type="duration"
 />
```

The **Delay** element is defined by the [**eventTriggerType**](taskschedulerschema-eventtriggertype-complextype.md) complex type.

## Parent element



| Element                                                                       | Derived from                                                                 | Description                                                                   |
|-------------------------------------------------------------------------------|------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [**EventTrigger**](taskschedulerschema-eventtrigger-triggergroup-element.md) | [**eventTriggerType**](taskschedulerschema-eventtriggertype-complextype.md) | Specifies a trigger that starts a task when a system event occurs.<br/> |



## Remarks

For script development, the event trigger delay is specified by the [**EventTrigger.Delay**](eventtrigger-delay.md) property.

For C++ development, the event trigger delay is specified by the [**IEventTrigger::Delay**](/windows/desktop/api/taskschd/nf-taskschd-ieventtrigger-get_delay) property.

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

 

 





