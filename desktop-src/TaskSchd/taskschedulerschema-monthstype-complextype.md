---
title: monthsType Complex Type
description: Defines the child elements and sequencing information for the Months (monthlyDayOfWeekScheduleType) and Months (monthlyScheduleType) elements.
ms.assetid: f1faa67a-2f5f-4a00-a1df-2d44e218278b
keywords:
- monthsType complex type Task Scheduler
topic_type:
- apiref
api_name:
- monthsType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# monthsType Complex Type

Defines the child elements and sequencing information for the [**Months (monthlyDayOfWeekScheduleType)**](taskschedulerschema-months-monthlydayofweekscheduletype-element.md) and [**Months (monthlyScheduleType)**](taskschedulerschema-months-monthlyscheduletype-element.md) elements.

``` syntax
<xs:complexType name="monthsType">
    <xs:all>
        <xs:element name="January"
            minOccurs="0"
        >
            <xs:complexType />
        </xs:element>
        <xs:element name="February"
            minOccurs="0"
        >
            <xs:complexType />
        </xs:element>
        <xs:element name="March"
            minOccurs="0"
        >
            <xs:complexType />
        </xs:element>
        <xs:element name="April"
            minOccurs="0"
        >
            <xs:complexType />
        </xs:element>
        <xs:element name="May"
            minOccurs="0"
        >
            <xs:complexType />
        </xs:element>
        <xs:element name="June"
            minOccurs="0"
        >
            <xs:complexType />
        </xs:element>
        <xs:element name="July"
            minOccurs="0"
        >
            <xs:complexType />
        </xs:element>
        <xs:element name="August"
            minOccurs="0"
        >
            <xs:complexType />
        </xs:element>
        <xs:element name="September"
            minOccurs="0"
        >
            <xs:complexType />
        </xs:element>
        <xs:element name="October"
            minOccurs="0"
        >
            <xs:complexType />
        </xs:element>
        <xs:element name="November"
            minOccurs="0"
        >
            <xs:complexType />
        </xs:element>
        <xs:element name="December"
            minOccurs="0"
        >
            <xs:complexType />
        </xs:element>
    </xs:all>
</xs:complexType>
```

## Child elements



| Element                                                               | Type | Description                                            |
|-----------------------------------------------------------------------|------|--------------------------------------------------------|
| [**April**](taskschedulerschema-april-monthstype-element.md)         | N/A  | Specifies that the task runs in April. <br/>     |
| [**August**](taskschedulerschema-august-monthstype-element.md)       | N/A  | Specifies that the task runs in August. <br/>    |
| [**December**](taskschedulerschema-december-monthstype-element.md)   | N/A  | Specifies that the task runs in December. <br/>  |
| [**February**](taskschedulerschema-february-monthstype-element.md)   | N/A  | Specifies that the task runs in February. <br/>  |
| [**January**](taskschedulerschema-january-monthstype-element.md)     | N/A  | Specifies that the task runs in January. <br/>   |
| [**July**](taskschedulerschema-july-monthstype-element.md)           | N/A  | Specifies that the task runs in July. <br/>      |
| [**June**](taskschedulerschema-june-monthstype-element.md)           | N/A  | Specifies that the task runs in June. <br/>      |
| [**March**](taskschedulerschema-march-monthstype-element.md)         | N/A  | Specifies that the task runs in March. <br/>     |
| [**May**](taskschedulerschema-may-monthstype-element.md)             | N/A  | Specifies that the task runs in May. <br/>       |
| [**November**](taskschedulerschema-november-monthstype-element.md)   | N/A  | Specifies that the task runs in November. <br/>  |
| [**October**](taskschedulerschema-october-monthstype-element.md)     | N/A  | Specifies that the task runs in October. <br/>   |
| [**September**](taskschedulerschema-september-monthstype-element.md) | N/A  | Specifies that the task runs in September. <br/> |



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

 

 





