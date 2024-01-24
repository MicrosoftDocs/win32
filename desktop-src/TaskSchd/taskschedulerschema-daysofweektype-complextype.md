---
title: daysOfWeekType Complex Type
description: Defines the child elements and sequencing information for the DaysOfWeek (weeklyScheduleType) and DaysOfWeek (monthlyDayOfWeekScheduleType) elements.
ms.assetid: b3315582-af7a-4d4c-8f6f-61de12a85f46
keywords:
- daysOfWeekType complex type Task Scheduler
topic_type:
- apiref
api_name:
- daysOfWeekType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# daysOfWeekType Complex Type

Defines the child elements and sequencing information for the [**DaysOfWeek (weeklyScheduleType)**](taskschedulerschema-daysofweek-weeklyscheduletype-element.md) and [**DaysOfWeek (monthlyDayOfWeekScheduleType)**](taskschedulerschema-daysofweek-monthlydayofweekscheduletype-element.md) elements.

``` syntax
<xs:complexType name="daysOfWeekType">
    <xs:all>
        <xs:element name="Monday"
            minOccurs="0"
        >
            <xs:complexType />
        </xs:element>
        <xs:element name="Tuesday"
            minOccurs="0"
        >
            <xs:complexType />
        </xs:element>
        <xs:element name="Wednesday"
            minOccurs="0"
        >
            <xs:complexType />
        </xs:element>
        <xs:element name="Thursday"
            minOccurs="0"
        >
            <xs:complexType />
        </xs:element>
        <xs:element name="Friday"
            minOccurs="0"
        >
            <xs:complexType />
        </xs:element>
        <xs:element name="Saturday"
            minOccurs="0"
        >
            <xs:complexType />
        </xs:element>
        <xs:element name="Sunday"
            minOccurs="0"
        >
            <xs:complexType />
        </xs:element>
    </xs:all>
</xs:complexType>
```

## Child elements



| Element                                                                   | Type | Description                         |
|---------------------------------------------------------------------------|------|-------------------------------------|
| [**Friday**](taskschedulerschema-friday-daysofweektype-element.md)       | N/A  | Task runs on Friday. <br/>    |
| [**Monday**](taskschedulerschema-monday-daysofweektype-element.md)       | N/A  | Task runs on Monday.<br/>     |
| [**Saturday**](taskschedulerschema-saturday-daysofweektype-element.md)   | N/A  | Task runs on Saturday. <br/>  |
| [**Sunday**](taskschedulerschema-sunday-daysofweektype-element.md)       | N/A  | Task runs on Sunday. <br/>    |
| [**Thursday**](taskschedulerschema-thursday-daysofweektype-element.md)   | N/A  | Task runs on Thursday <br/>   |
| [**Tuesday**](taskschedulerschema-tuesday-daysofweektype-element.md)     | N/A  | Task runs on Tuesday. <br/>   |
| [**Wednesday**](taskschedulerschema-wednesday-daysofweektype-element.md) | N/A  | Task runs on Wednesday. <br/> |



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

 

 





