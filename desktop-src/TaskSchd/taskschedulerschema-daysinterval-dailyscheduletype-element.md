---
title: DaysInterval (dailyScheduleType) Element
description: Specifies the interval between the days in the schedule.
ms.assetid: 495ea1c0-37eb-4b12-8241-bfc6489e33ed
keywords:
- DaysInterval element Task Scheduler
topic_type:
- apiref
api_name:
- DaysInterval
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# DaysInterval (dailyScheduleType) Element

Specifies the interval between the days in the schedule.

``` syntax
<xs:element name="DaysInterval"
    minOccurs="0"
>
    <xs:simpleType>
        <xs:restriction
            base="unsignedInt"
        >
            <xs:minInclusive
                value="1"
             />
            <xs:maxInclusive
                value="365"
             />
        </xs:restriction>
    </xs:simpleType>
</xs:element>
```

The element is defined by the [**dailyScheduleType**](taskschedulerschema-dailyscheduletype-complextype.md) complex type.

## Parent element



| Element                                                                                | Derived from                                                                   | Description                            |
|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|----------------------------------------|
| [**ScheduleByDay**](taskschedulerschema-schedulebyday-calendartriggertype-element.md) | [**dailyScheduleType**](taskschedulerschema-dailyscheduletype-complextype.md) | Specifies a daily schedule.<br/> |



## Remarks

For script development, the days interval for a daily trigger is specified by the [**DailyTrigger.DaysInterval**](dailytrigger-daysinterval.md) property.

For C++ development, the days interval for a daily trigger is specified by the [**IDailyTrigger::DaysInterval**](/windows/desktop/api/taskschd/nf-taskschd-idailytrigger-get_daysinterval) property.

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

 

 





