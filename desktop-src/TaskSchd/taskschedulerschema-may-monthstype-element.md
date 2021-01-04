---
title: May (monthsType) Element
description: Specifies that the task runs in May.
ms.assetid: 1fcc3eb7-6500-4ba3-b146-14d169d9b445
keywords:
- May element Task Scheduler
topic_type:
- apiref
api_name:
- May
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# May (monthsType) Element

Specifies that the task runs in May.

``` syntax
<xs:element name="May">
    <xs:complexType />
</xs:element>
```

The **May** element is defined by the [**monthsType**](taskschedulerschema-monthstype-complextype.md) complex type.

## Parent element



| Element                                                                                                          | Derived from                                                     | Description                                                                                                |
|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [**Months (monthlyDayOfWeekScheduleType)**](taskschedulerschema-months-monthlydayofweekscheduletype-element.md) | [**monthsType**](taskschedulerschema-monthstype-complextype.md) | Specifies the months of the year during which the task runs for a monthly day-of-week schedule.<br/> |
| [**Months (monthlyScheduleType)**](taskschedulerschema-months-monthlyscheduletype-element.md)                   | [**monthsType**](taskschedulerschema-monthstype-complextype.md) | Specifies the months of the year during which the task runs for a monthly schedule.<br/>             |



## Examples

The following XML defines a months calendar that runs the task in May.


```XML
<Months>
    <May/>
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

 

 





