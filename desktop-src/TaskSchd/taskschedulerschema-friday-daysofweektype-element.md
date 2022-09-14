---
title: Friday (daysOfWeekType) Element
description: Specifies that the task runs on Friday.
ms.assetid: bff85911-d354-4954-8c69-7b6f2ca312d3
keywords:
- Friday element Task Scheduler
topic_type:
- apiref
api_name:
- Friday
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Friday (daysOfWeekType) Element

Specifies that the task runs on Friday.

``` syntax
<xs:element name="Friday">
    <xs:complexType />
</xs:element>
```

The **Friday** element is defined by the [**daysOfWeekType**](taskschedulerschema-daysofweektype-complextype.md) complex type.

## Parent element



| Element                                                                                                                  | Derived from                                                             | Description                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [**DaysOfWeek (monthlyDayOfWeekScheduleType)**](taskschedulerschema-daysofweek-monthlydayofweekscheduletype-element.md) | [**daysOfWeekType**](taskschedulerschema-daysofweektype-complextype.md) | Specifies the days of the week in which the task runs for a monthly day-of-week schedule.<br/> |
| [**DaysOfWeek (weeklyScheduleType)**](taskschedulerschema-daysofweek-weeklyscheduletype-element.md)                     | [**daysOfWeekType**](taskschedulerschema-daysofweektype-complextype.md) | Specifies the days of the week in which the task runs for a weekly schedule.<br/>              |



## Examples

The following XML defines a day of week calendar that starts a task on Friday.


```XML
<DaysOfWeek>
    <Friday/>
</DaysOfWeek>
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

 

 





