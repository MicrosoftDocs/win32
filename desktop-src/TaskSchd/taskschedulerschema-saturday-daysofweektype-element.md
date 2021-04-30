---
title: Saturday (daysOfWeekType) Element
description: Specifies that the task runs on Saturday.
ms.assetid: def26a72-c143-466a-b5b0-6105078afffa
keywords:
- Saturday element Task Scheduler
topic_type:
- apiref
api_name:
- Saturday
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Saturday (daysOfWeekType) Element

Specifies that the task runs on Saturday.

``` syntax
<xs:element name="Saturday">
    <xs:complexType />
</xs:element>
```

The **Saturday** element is defined by the [**daysOfWeekType**](taskschedulerschema-daysofweektype-complextype.md) complex type.

## Parent element



| Element                                                                                                                  | Derived from                                                             | Description                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [**DaysOfWeek (monthlyDayOfWeekScheduleType)**](taskschedulerschema-daysofweek-monthlydayofweekscheduletype-element.md) | [**daysOfWeekType**](taskschedulerschema-daysofweektype-complextype.md) | Specifies the days of the week in which the task runs for a monthly day-of-week schedule.<br/> |
| [**DaysOfWeek (weeklyScheduleType)**](taskschedulerschema-daysofweek-weeklyscheduletype-element.md)                     | [**daysOfWeekType**](taskschedulerschema-daysofweektype-complextype.md) | Specifies the days of the week in which the task runs for a weekly schedule.<br/>              |



## Examples

The following XML defines a day of week calendar that starts a task on Saturday.


```XML
<DaysOfWeek>
    <Saturday/>
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

 

 





