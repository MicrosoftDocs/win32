---
title: ScheduleByMonth (calendarTriggerType) Element
description: Specifies a monthly schedule.
ms.assetid: 3a23f4d0-bdaf-4f2a-81c6-8652a0849fc8
keywords:
- ScheduleByMonth element Task Scheduler
topic_type:
- apiref
api_name:
- ScheduleByMonth
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ScheduleByMonth (calendarTriggerType) Element

Specifies a monthly schedule. For example, the task starts at 8:00 AM on specific days of the month on specific months.

``` syntax
<xs:element name="ScheduleByMonth"
    type="monthlyScheduleType"
 />
```

The **ScheduleByMonth** element is defined by the [**calendarTriggerType**](taskschedulerschema-calendartriggertype-complextype.md) complex type.

## Parent element



| Element                                                                             | Derived from                                                                       | Description                                                                                |
|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [**CalendarTrigger**](taskschedulerschema-calendartrigger-triggergroup-element.md) | [**calendarTriggerType**](taskschedulerschema-calendartriggertype-complextype.md) | Specifies a daily, weekly, monthly, or a monthly day-of-the-week (DOW) trigger.<br/> |



## Child elements



| Element                                                                                                  | Type                                                                       | Description                                                             |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|-------------------------------------------------------------------------|
| [**DaysOfMonth (monthlyScheduleType)**](taskschedulerschema-daysofmonth-monthlyscheduletype-element.md) | [**daysOfMonthType**](taskschedulerschema-daysofmonthtype-complextype.md) | Specifies the days of the month during which the task runs.<br/>  |
| [**Months (monthlyScheduleType)**](taskschedulerschema-months-monthlyscheduletype-element.md)           | [**monthsType**](taskschedulerschema-monthstype-complextype.md)           | Specifies the months of the year during which the task runs.<br/> |



## Remarks

The time of day that the task is started is set by the [**StartBoundary**](taskschedulerschema-startboundary-triggerbasetype-element.md) element.

For script development, a monthly trigger is specified using the [**MonthlyTrigger**](monthlytrigger.md) object.

For C++ development, a monthly trigger is specified using the [**IMonthlyTrigger**](/windows/desktop/api/taskschd/nn-taskschd-imonthlytrigger) interface.

The child elements listed below are defined by the [**monthlyScheduleType**](taskschedulerschema-monthlyscheduletype-complextype.md) complex element types.

## Examples

The following XML defines a monthly calendar trigger that starts a task ( at 8:00 AM) on the 1st and 15th day of every month of the year.


```XML
<CalendarTrigger>
    <StartBoundary>2005-01-01T08:00:00</StartBoundary>
    <EndBounadry>2007-01-01T00:00:00</EndBoundary>
    <ScheduleByMonth>
        <DaysOfMonth>
            <Day>1</Day>
            <Day>15</Day>
        </DaysOfMonth>
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
        </Months>
    </ScheduleByMonth>
</CalendarTrigger>
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

 

 





