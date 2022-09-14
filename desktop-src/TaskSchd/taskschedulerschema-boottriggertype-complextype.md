---
title: bootTriggerType Complex Type
description: Defines the child element and sequencing information for the BootTrigger element.
ms.assetid: 36ade928-7640-4f91-ab76-18398b0cd65f
keywords:
- bootTriggerType complex type Task Scheduler
topic_type:
- apiref
api_name:
- bootTriggerType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# bootTriggerType Complex Type

Defines the child element and sequencing information for the [**BootTrigger**](taskschedulerschema-boottrigger-triggergroup-element.md) element.

``` syntax
<xs:complexType name="bootTriggerType">
    <xs:complexContent>
        <xs:extension
            base="triggerBaseType"
        >
            <xs:sequence>
                <xs:element name="Delay"
                    type="duration"
                    default="PT0M"
                    minOccurs="0"
                 />
            </xs:sequence>
        </xs:extension>
    </xs:complexContent>
</xs:complexType>
```

## Child elements



| Element                                                            | Type     | Description                                                                                 |
|--------------------------------------------------------------------|----------|---------------------------------------------------------------------------------------------|
| [**Delay**](taskschedulerschema-delay-boottriggertype-element.md) | duration | Amount of time between when the system is booted and when the trigger is fired. <br/> |



## Remarks

In addition to the child element defined here, the [**BootTrigger**](taskschedulerschema-boottrigger-triggergroup-element.md) element also uses child elements defined by the [**triggerBaseType**](taskschedulerschema-triggerbasetype-complextype.md) complex type.

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

 

 





