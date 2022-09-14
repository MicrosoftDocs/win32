---
title: DaysOfWeek (weeklyScheduleType) Element
description: Specifies the days of the week in which the task runs. | DaysOfWeek (weeklyScheduleType) Element
ms.assetid: 86555681-2324-4095-9eab-fdef40e0acba
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

# DaysOfWeek (weeklyScheduleType) Element

Specifies the days of the week in which the task runs.

``` syntax
<xs:element name="DaysOfWeek"
    type="daysOfWeekType"
 />
```

The **DaysOfWeek** element is defined by the [**weeklyScheduleType**](taskschedulerschema-weeklyscheduletype-complextype.md) complex type.

## Parent element



| Element                                                                                  | Derived from                                                                     | Description                             |
|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|-----------------------------------------|
| [**ScheduleByWeek**](taskschedulerschema-schedulebyweek-calendartriggertype-element.md) | [**weeklyScheduleType**](taskschedulerschema-weeklyscheduletype-complextype.md) | Specifies a weekly schedule.<br/> |



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

The previous child elements are defined by the [**daysOfWeekType**](taskschedulerschema-daysofweektype-complextype.md) complex type.

For scripting development, the weekly interval is specified using the [**WeeklyTrigger.WeeksInterval**](weeklytrigger-weeksinterval.md) property.

For C++ development, the weekly interval is specified using the [**IWeeklyTrigger::WeeksInterval**](/windows/desktop/api/taskschd/nf-taskschd-iweeklytrigger-get_weeksinterval) property.

## Examples

The following XML defines a daily calendar trigger that starts a task Monday through Friday ( at 8:00 AM) every week.


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



For a complete example of the XML for a task that uses a weekly trigger, see [Weekly Trigger Example (XML)](weekly-trigger-example--xml-.md).

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

 

 





