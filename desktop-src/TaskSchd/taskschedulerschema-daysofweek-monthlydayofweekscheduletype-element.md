---
title: DaysOfWeek (monthlyDayOfWeekScheduleType) Element
description: Specifies the days of the week in which the task runs. | DaysOfWeek (monthlyDayOfWeekScheduleType) Element
ms.assetid: d84f0019-1369-465f-9054-0fb5a83cad6d
keywords:
- DaysOfWeek element Task Scheduler
topic_type:
- apiref
api_name:
- DaysOfWeek
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# DaysOfWeek (monthlyDayOfWeekScheduleType) Element

Specifies the days of the week in which the task runs.

``` syntax
<xs:element name="DaysOfWeek"
    type="daysOfWeekType"
 />
```

The **DaysOfWeek** element is defined by the [**monthlyDayOfWeekScheduleType**](taskschedulerschema-monthlydayofweekscheduletype-complextype.md) complex type.

## Parent element



| Element                                                                                                      | Derived from                                                                                         | Description                                                                          |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**ScheduleByMonthDayOfWeek**](taskschedulerschema-schedulebymonthdayofweek-calendartriggertype-element.md) | [**monthlyDayOfWeekScheduleType**](taskschedulerschema-monthlydayofweekscheduletype-complextype.md) | Specifies a trigger that starts a job for a monthly day-of-week schedule.<br/> |



## Child elements



| Element                                                                   | Type | Description                                           |
|---------------------------------------------------------------------------|------|-------------------------------------------------------|
| [**Friday**](taskschedulerschema-friday-daysofweektype-element.md)       |      | Specifies that the task runs on Friday.<br/>    |
| [**Monday**](taskschedulerschema-monday-daysofweektype-element.md)       |      | Specifies that the task runs on Monday.<br/>    |
| [**Saturday**](taskschedulerschema-saturday-daysofweektype-element.md)   |      | Specifies that the task runs on Saturday.<br/>  |
| [**Sunday**](taskschedulerschema-sunday-daysofweektype-element.md)       |      | Specifies that the task runs on Sunday.<br/>    |
| [**Thursday**](taskschedulerschema-thursday-daysofweektype-element.md)   |      | Specifies that the task runs on Thursday.<br/>  |
| [**Tuesday**](taskschedulerschema-tuesday-daysofweektype-element.md)     |      | Specifies that the task runs on Tuesday.<br/>   |
| [**Wednesday**](taskschedulerschema-wednesday-daysofweektype-element.md) |      | Specifies that the task runs on Wednesday.<br/> |



## Remarks

For scripting development, the days of the week for a monthly day-of-week calendar are specified using the [**MonthlyDOWTrigger.DaysOfWeek**](monthlydowtrigger-daysofweek.md) property.

For C++ development, the days of the week for a monthly day-of-week calendar are specified using the [**IMonthlyDOWTrigger::DaysOfWeek**](/windows/desktop/api/taskschd/nf-taskschd-imonthlydowtrigger-get_daysofweek) property.

The child elements above are defined by the [**daysOfWeekType**](taskschedulerschema-daysofweektype-complextype.md) complex type.

## Examples

The following XML defines a monthly day-of-week calendar that starts the task on Monday of the first week for each month of the year.


```XML
<ScheduleByMonthDayOfWeek>
    <Weeks>
        <Week>1</Week>
    </Weeks>
    <DaysOfWeek>
        <Monday/>
    </DaysOfWeek>
    <Months>
        <January/>
        <February/>
        <March/>
        <April/>
        <May/>
        <June/>
        <July/>
        <August/>
        <September/>
        <October/>
        <November/>
        <December/>
    <Months>
</ScheduleByMonthDayOfWeek>
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

 

 





