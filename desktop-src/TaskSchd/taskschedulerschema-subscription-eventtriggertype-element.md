---
title: Subscription (eventTriggerType) Element
description: Specifies the XPath query that identifies the event that fires the trigger.
ms.assetid: ea351a55-c6f9-4e39-b15e-c2a1027a1360
keywords:
- Subscription element Task Scheduler
topic_type:
- apiref
api_name:
- Subscription
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Subscription (eventTriggerType) Element

Specifies the XPath query that identifies the event that fires the trigger.

``` syntax
<xs:element name="Subscription"
    type="nonEmptyString"
 />
```

The **Subscription** element is defined by the [**eventTriggerType**](taskschedulerschema-eventtriggertype-complextype.md) complex type.

## Parent element



| Element                                                                       | Derived from                                                                 | Description                                                                   |
|-------------------------------------------------------------------------------|------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [**EventTrigger**](taskschedulerschema-eventtrigger-triggergroup-element.md) | [**eventTriggerType**](taskschedulerschema-eventtriggertype-complextype.md) | Specifies a trigger that starts a task when a system event occurs.<br/> |



## Remarks

For script development, the event subscription is specified by the [**EventTrigger.Subscription**](eventtrigger-subscription.md) property.

For C++ development, the event subscription is specified by the [**IEventTrigger::Subscription**](/windows/desktop/api/taskschd/nf-taskschd-ieventtrigger-get_subscription) property.

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

 

 





