---
title: Sunday (daysOfWeekType) Element
description: Specifies that the task runs on Sunday.
ms.assetid: 856db869-2273-4bb8-88c8-c126bb16c87b
keywords:
- Sunday element Task Scheduler
topic_type:
- apiref
api_name:
- Sunday
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Sunday (daysOfWeekType) Element

Specifies that the task runs on Sunday.

``` syntax
<xs:element name="Sunday">
    <xs:complexType />
</xs:element>
```

The **Sunday** element is defined by the [**daysOfWeekType**](taskschedulerschema-daysofweektype-complextype.md) complex type.

## Parent element



| Element                                                                                                                  | Derived from                                                             | Description                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [**DaysOfWeek (monthlyDayOfWeekScheduleType)**](taskschedulerschema-daysofweek-monthlydayofweekscheduletype-element.md) | [**daysOfWeekType**](taskschedulerschema-daysofweektype-complextype.md) | Specifies the days of the week in which the task runs for a monthly day-of-week schedule.<br/> |
| [**DaysOfWeek (weeklyScheduleType)**](taskschedulerschema-daysofweek-weeklyscheduletype-element.md)                     | [**daysOfWeekType**](taskschedulerschema-daysofweektype-complextype.md) | Specifies the days of the week in which the task runs for a weekly schedule.<br/>              |



## Examples

The following XML defines a day of week calendar that starts a task on Sunday.


```XML
<DaysOfWeek>
    <Sunday/>
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

 

 





