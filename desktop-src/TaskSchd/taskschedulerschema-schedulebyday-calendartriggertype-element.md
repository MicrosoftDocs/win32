---
title: ScheduleByDay (calendarTriggerType) Element
description: Specifies a daily schedule.
ms.assetid: 5a6097ce-a855-4b08-84c5-71f06343805e
keywords:
- daily trigger Task Scheduler , XML element
- ScheduleByDay element Task Scheduler
topic_type:
- apiref
api_name:
- ScheduleByDay
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ScheduleByDay (calendarTriggerType) Element

Specifies a daily schedule. For example, the task starts at 8:00 AM every day, every-other day, every third day, and so on.

``` syntax
<xs:element name="ScheduleByDay"
    type="dailyScheduleType"
 />
```

The **ScheduleByDay** element is defined by the [**calendarTriggerType**](taskschedulerschema-calendartriggertype-complextype.md) complex type.

## Parent element



| Element                                                                             | Derived from                                                                       | Description                                                                                |
|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [**CalendarTrigger**](taskschedulerschema-calendartrigger-triggergroup-element.md) | [**calendarTriggerType**](taskschedulerschema-calendartriggertype-complextype.md) | Specifies a daily, weekly, monthly, or a monthly day-of-the-week (DOW) trigger.<br/> |



## Child elements



| Element                                                                            | Type             | Description                                                         |
|------------------------------------------------------------------------------------|------------------|---------------------------------------------------------------------|
| [**DaysInterval**](taskschedulerschema-daysinterval-dailyscheduletype-element.md) | **unsignedByte** | Specifies the interval between the days in the schedule.<br/> |



## Remarks

The child element listed previously is defined by the [**dailyScheduleType**](taskschedulerschema-dailyscheduletype-complextype.md) complex element types.

The time of day that the task is started is set by the [**StartBoundary**](taskschedulerschema-startboundary-triggerbasetype-element.md) element.

For scripting development, a daily trigger is specified using the [**DailyTrigger**](weeklytrigger.md) object.

For C++ development, a daily trigger is specified using the [**IDailyTrigger**](/windows/desktop/api/taskschd/nn-taskschd-idailytrigger) interface.

## Examples

The following XML defines a daily calendar trigger that starts the task every day.


```XML
<CalendarTrigger>
    <StartBoundary>2005-01-01T00:00:00</StartBoundary>
    <EndBounadry>2007-01-01T00:00:00</EndBoundary>
    <ScheduleByDay>
        <DaysInterval>1</DaysInterval>
    </ScheduleByDay>
</CalendarTrigger>
```



For a complete example of the XML for a task that specifies a daily schedule, see [Daily Trigger Example (XML)](daily-trigger-example--xml-.md).

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

 

 





