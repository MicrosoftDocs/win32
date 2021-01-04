---
title: ValueQueries (eventTriggerType) Element
description: Contains a sequence of elements that each contain a name and an XPath query value.
ms.assetid: 4b57568c-81b6-43fd-9194-9817c4817197
keywords:
- ValueQueries element Task Scheduler
topic_type:
- apiref
api_name:
- ValueQueries
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ValueQueries (eventTriggerType) Element

Contains a sequence of elements that each contain a name and an XPath query value. The queries are applied to an event returned from the event subscription specified in the [**Subscription**](taskschedulerschema-subscription-eventtriggertype-element.md) element. The name for the XPath query value can be used as a variable in the action section of a task.

``` syntax
<xs:element name="ValueQueries"
    type="namedValues"
    minOccurs="0"
 />
```

The **ValueQueries** element is defined by the [**eventTriggerType**](taskschedulerschema-eventtriggertype-complextype.md) complex type.

## Parent element



| Element                                                                                      | Derived from                                                                 | Description                                                                   |
|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [**EventTrigger (triggerGroup)**](taskschedulerschema-eventtrigger-triggergroup-element.md) | [**eventTriggerType**](taskschedulerschema-eventtriggertype-complextype.md) | Specifies a trigger that starts a task when a system event occurs.<br/> |



## Remarks

For C++ development, see [**ValueQueries Property of IEventTrigger**](/windows/desktop/api/taskschd/nf-taskschd-ieventtrigger-get_valuequeries).

For script development, see [**EventTrigger.ValueQueries**](eventtrigger-valuequeries.md).

## Examples

For a complete example of the XML for a task that specifies a an event trigger using this element, see [Event Trigger Example (XML)](/previous-versions//aa446889(v=vs.85)).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

