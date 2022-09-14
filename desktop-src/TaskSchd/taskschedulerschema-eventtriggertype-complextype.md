---
title: eventTriggerType Complex Type
description: Defines the child elements and sequencing information for the EventTrigger element.
ms.assetid: c678af6f-bdfb-4c4d-85d7-2d93abfc2a7d
keywords:
- eventTriggerType complex type Task Scheduler
topic_type:
- apiref
api_name:
- eventTriggerType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# eventTriggerType Complex Type

Defines the child elements and sequencing information for the [**EventTrigger**](taskschedulerschema-eventtrigger-triggergroup-element.md) element.

``` syntax
<xs:complexType name="eventTriggerType">
    <xs:complexContent>
        <xs:extension
            base="triggerBaseType"
        >
            <xs:sequence>
                <xs:element name="Subscription"
                    type="nonEmptyString"
                 />
                <xs:element name="Delay"
                    type="duration"
                    default="PT0M"
                    minOccurs="0"
                 />
                <xs:element name="ValueQueries"
                    type="namedValues"
                    minOccurs="0"
                 />
            </xs:sequence>
        </xs:extension>
    </xs:complexContent>
</xs:complexType>
```

## Child elements



| Element                                                                           | Type                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Delay**](taskschedulerschema-delay-eventtriggertype-element.md)               | duration                                                                | Specifies the amount of time between when the event occurs and when the task is started.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**Subscription**](taskschedulerschema-subscription-eventtriggertype-element.md) | [**nonEmptyString**](taskschedulerschema-nonemptystring-simpletype.md) | Specifies the XPath query that identifies the event that fires the trigger.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [**ValueQueries**](taskschedulerschema-valuequeries-eventtriggertype-element.md) | [**namedValues**](taskschedulerschema-namedvalues-complextype.md)      | Specifies a sequence of elements that each contain a name and an XPath query value. The queries are applied to an event returned from the event subscription specified in the [**Subscription**](taskschedulerschema-subscription-eventtriggertype-element.md) element. The name for the XPath query value can be used as a variable in the [**Body**](taskschedulerschema-body-showmessagetype-element.md) element in the [**ShowMessage**](taskschedulerschema-showmessage-actiongroup-element.md) action section of a task. <br/> |



## Remarks

In addition to the child element defined here, the [**EventTrigger**](taskschedulerschema-eventtrigger-triggergroup-element.md) element also uses child elements defined by the [**triggerBaseType**](taskschedulerschema-triggerbasetype-complextype.md) complex type.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Complex Types](task-scheduler-schema-complex-types.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





