---
title: February (monthsType) Element
description: Specifies that the task runs in February.
ms.assetid: 871449f8-fa3a-4e1f-be36-bc5c98125721
keywords:
- February element Task Scheduler
topic_type:
- apiref
api_name:
- February
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# February (monthsType) Element

Specifies that the task runs in February.

``` syntax
<xs:element name="February">
    <xs:complexType />
</xs:element>
```

The **February** element is defined by the [**monthsType**](taskschedulerschema-monthstype-complextype.md) complex type.

## Parent element



| Element                                                                                                          | Derived from                                                     | Description                                                                                                |
|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [**Months (monthlyDayOfWeekScheduleType)**](taskschedulerschema-months-monthlydayofweekscheduletype-element.md) | [**monthsType**](taskschedulerschema-monthstype-complextype.md) | Specifies the months of the year during which the task runs for a monthly day-of-week schedule.<br/> |
| [**Months (monthlyScheduleType)**](taskschedulerschema-months-monthlyscheduletype-element.md)                   | [**monthsType**](taskschedulerschema-monthstype-complextype.md) | Specifies the months of the year during which the task runs for a monthly schedule.<br/>             |



## Examples

The following XML defines a months calendar that runs the task in February.


```XML
<Months>
    <February/>
</Months>
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

 

 





