---
title: ScheduleByWeek (calendarTriggerType) Element
description: Specifies a weekly schedule.
ms.assetid: d2c33e76-0564-4b3c-ab86-e7bca667fa4f
keywords:
- weekly trigger Task Scheduler , XML element
- ScheduleByWeek element Task Scheduler
topic_type:
- apiref
api_name:
- ScheduleByWeek
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ScheduleByWeek (calendarTriggerType) Element

Specifies a weekly schedule. For example, the task starts at 8:00 AM on a specific day of the week every week or on a specific day of the week every other week.

``` syntax
<xs:element name="ScheduleByWeek"
    type="weeklyScheduleType"
 />
```

The **ScheduleByWeek** element is defined by the [**calendarTriggerType**](taskschedulerschema-calendartriggertype-complextype.md) complex type.

## Parent element



| Element                                                                             | Derived from                                                                       | Description                                                                                |
|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [**CalendarTrigger**](taskschedulerschema-calendartrigger-triggergroup-element.md) | [**calendarTriggerType**](taskschedulerschema-calendartriggertype-complextype.md) | Specifies a daily, weekly, monthly, or a monthly day-of-the-week (DOW) trigger.<br/> |



## Child elements



| Element                                                                               | Type                                                                     | Description                                                          |
|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------|
| [**DaysOfWeek**](taskschedulerschema-daysofweek-weeklyscheduletype-element.md)       | [**daysOfWeekType**](taskschedulerschema-daysofweektype-complextype.md) | Specifies the days of the week in which the task runs.<br/>    |
| [**WeeksInterval**](taskschedulerschema-weeksinterval-weeklyscheduletype-element.md) | unsignedByte                                                             | Specifies the interval between the weeks in the schedule.<br/> |



## Remarks

The child elements listed above are defined by the [**weeklyScheduleType**](taskschedulerschema-weeklyscheduletype-complextype.md) complex element types.

The time of day that the task is started is set by the [**StartBoundary**](taskschedulerschema-startboundary-triggerbasetype-element.md) element.

For scripting development, a weekly trigger is specified using the [**WeeklyTrigger**](weeklytrigger.md) object.

For C++ development, a weekly trigger is specified using the [**IWeeklyTrigger**](/windows/desktop/api/taskschd/nn-taskschd-iweeklytrigger) interface.

## Examples

The following XML defines a weekly calendar trigger that starts a task Monday through Friday (at 8:00 AM) every week.


```XML
<CalendarTrigger>
    <StartBoundary>2005-01-01T08:00:00</StartBoundary>
    <EndBounadry>2007-01-01T00:00:00</EndBoundary>
    <ScheduleByWeek>
        <WeeksInterval>1</WeeksInterval>
        <DaysOfWeek>
            <Monday/>
            <Tuesday/>
            <Wednesday/>
            <Thurday/>
            <Friday/>
        </DaysOfWeek>
    </ScheduleByWeek>
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

 

 





