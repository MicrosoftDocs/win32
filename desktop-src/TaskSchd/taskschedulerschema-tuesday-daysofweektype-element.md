---
title: Tuesday (daysOfWeekType) Element
description: Specifies that the task runs on Tuesday.
ms.assetid: 588608e9-33f9-405d-8b4b-35f11ab403db
keywords:
- Tuesday element Task Scheduler
topic_type:
- apiref
api_name:
- Tuesday
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Tuesday (daysOfWeekType) Element

Specifies that the task runs on Tuesday.

``` syntax
<xs:element name="Tuesday">
    <xs:complexType />
</xs:element>
```

The **Tuesday** element is defined by the [**daysOfWeekType**](taskschedulerschema-daysofweektype-complextype.md) complex type.

## Parent element



| Element                                                                                                                  | Derived from                                                             | Description                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [**DaysOfWeek (monthlyDayOfWeekScheduleType)**](taskschedulerschema-daysofweek-monthlydayofweekscheduletype-element.md) | [**daysOfWeekType**](taskschedulerschema-daysofweektype-complextype.md) | Specifies the days of the week in which the task runs for a monthly day-of-week schedule.<br/> |
| [**DaysOfWeek (weeklyScheduleType)**](taskschedulerschema-daysofweek-weeklyscheduletype-element.md)                     | [**daysOfWeekType**](taskschedulerschema-daysofweektype-complextype.md) | Specifies the days of the week in which the task runs for a weekly schedule.<br/>              |



## Examples

The following XML defines a day of week calendar that starts a task on Tuesday.


```XML
<DaysOfWeek>
    <Tuesday/>
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

 

 





