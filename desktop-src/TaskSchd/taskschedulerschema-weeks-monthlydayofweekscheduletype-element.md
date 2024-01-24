---
title: Weeks (monthlyDayOfWeekScheduleType) Element
description: Specifies the weeks of the month in which the task is run.
ms.assetid: c126d1e2-6e60-4067-9fc2-86c9522cce5d
keywords:
- Weeks element Task Scheduler
topic_type:
- apiref
api_name:
- Weeks
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Weeks (monthlyDayOfWeekScheduleType) Element

Specifies the weeks of the month in which the task is run.

``` syntax
<xs:element name="Weeks"
    type="weeksType"
 />
```

The **Weeks** element is defined by the [**monthlyDayOfWeekScheduleType**](taskschedulerschema-monthlydayofweekscheduletype-complextype.md) complex type.

## Parent element



| Element                                                                                                      | Derived from                                                                                         | Description                                                                         |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [**ScheduleByMonthDayOfWeek**](taskschedulerschema-schedulebymonthdayofweek-calendartriggertype-element.md) | [**monthlyDayOfWeekScheduleType**](taskschedulerschema-monthlydayofweekscheduletype-complextype.md) | Specifies a trigger that starts a job on a monthly day-of-week schedule.<br/> |



## Child elements



| Element                                                    | Type                                                        | Description                                        |
|------------------------------------------------------------|-------------------------------------------------------------|----------------------------------------------------|
| [**Week**](taskschedulerschema-week-weekstype-element.md) | [**weekType**](taskschedulerschema-weektype-simpletype.md) | Specifies a specific week of the month.<br/> |



## Remarks

For scripting development, the weeks of the month are specified using the [**MonthlyDOWTrigger.WeeksOfMonth**](monthlydowtrigger-weeksofmonth.md) property.

For C++ development, the weeks of the month are specified using the [**IMonthlyDOWTrigger::WeeksOfMonth**](/windows/desktop/api/taskschd/nf-taskschd-imonthlydowtrigger-get_weeksofmonth) property.

When specifying the weeks of the month, use 1-4 to specify the first four weeks of the month or use the string "Last" to indicate the last week regardless of which week it is.

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

 

 





