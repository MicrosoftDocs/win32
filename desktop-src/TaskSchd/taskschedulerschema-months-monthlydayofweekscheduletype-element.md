---
title: Months (monthlyDayOfWeekScheduleType) Element
description: Specifies the months of the year during which the task runs for a monthly day-of-week schedule.
ms.assetid: 420fa7f4-7106-483e-9b3b-d1ba51f25222
keywords:
- Months element Task Scheduler
topic_type:
- apiref
api_name:
- Months
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Months (monthlyDayOfWeekScheduleType) Element

Specifies the months of the year during which the task runs for a monthly day-of-week schedule.

``` syntax
<xs:element name="Months"
    type="monthsType"
 />
```

The **Months** element is defined by the [**monthlyDayOfWeekScheduleType**](taskschedulerschema-monthlydayofweekscheduletype-complextype.md) complex type.

## Parent element



| Element                                                                                                                            | Derived from                                                                                         | Description                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**ScheduleByMonthDayOfWeek (calendarTriggerType)**](taskschedulerschema-schedulebymonthdayofweek-calendartriggertype-element.md) | [**monthlyDayOfWeekScheduleType**](taskschedulerschema-monthlydayofweekscheduletype-complextype.md) | Specifies a trigger that starts a job for a monthly day-of-week schedule.<br/> |



## Child elements



| Element                                                               | Type | Description                                           |
|-----------------------------------------------------------------------|------|-------------------------------------------------------|
| [**April**](taskschedulerschema-april-monthstype-element.md)         |      | Specifies that the task runs in April.<br/>     |
| [**August**](taskschedulerschema-august-monthstype-element.md)       |      | Specifies that the task runs in August.<br/>    |
| [**December**](taskschedulerschema-december-monthstype-element.md)   |      | Specifies that the task runs in December.<br/>  |
| [**February**](taskschedulerschema-february-monthstype-element.md)   |      | Specifies that the task runs in February.<br/>  |
| [**January**](taskschedulerschema-january-monthstype-element.md)     |      | Specifies that the task runs in January.<br/>   |
| [**July**](taskschedulerschema-july-monthstype-element.md)           |      | Specifies that the task runs in July.<br/>      |
| [**June**](taskschedulerschema-june-monthstype-element.md)           |      | Specifies that the task runs in June.<br/>      |
| [**March**](taskschedulerschema-march-monthstype-element.md)         |      | Specifies that the task runs in March.<br/>     |
| [**May**](taskschedulerschema-may-monthstype-element.md)             |      | Specifies that the task runs in May.<br/>       |
| [**November**](taskschedulerschema-november-monthstype-element.md)   |      | Specifies that the task runs in November.<br/>  |
| [**October**](taskschedulerschema-october-monthstype-element.md)     |      | Specifies that the task runs in October.<br/>   |
| [**September**](taskschedulerschema-september-monthstype-element.md) |      | Specifies that the task runs in September.<br/> |



## Remarks

For scripting development, the months of a year for a monthly day-of-week schedule are specified using the [**MonthlyDOWTrigger.MonthsOfYear**](monthlydowtrigger-monthsofyear.md) property.

For C++ development, the months of a year for a monthly day-of-week schedule are specified using the [**IMonthlyDOWTrigger::MonthsOfYear**](/windows/desktop/api/taskschd/nf-taskschd-imonthlydowtrigger-get_monthsofyear) property.

The child elements above are defined by the [**monthsType**](taskschedulerschema-monthstype-complextype.md) complex type.

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

 

 





