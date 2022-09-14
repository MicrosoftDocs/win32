---
title: monthlyScheduleType Complex Type
description: Defines the child elements and sequencing information for the ScheduleByMonth (calendarTriggerType) element.
ms.assetid: 3ade775c-ca44-403e-9602-80095c7dba1a
keywords:
- monthlyScheduleType complex type Task Scheduler
topic_type:
- apiref
api_name:
- monthlyScheduleType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# monthlyScheduleType Complex Type

Defines the child elements and sequencing information for the [**ScheduleByMonth (calendarTriggerType)**](taskschedulerschema-schedulebymonth-calendartriggertype-element.md) element.

``` syntax
<xs:complexType name="monthlyScheduleType">
    <xs:all>
        <xs:element name="DaysOfMonth"
            type="daysOfMonthType"
            minOccurs="0"
         />
        <xs:element name="Months"
            type="monthsType"
            minOccurs="0"
         />
    </xs:all>
</xs:complexType>
```

## Child elements



| Element                                                                            | Type                                                                       | Description                                                                                    |
|------------------------------------------------------------------------------------|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [**DaysOfMonth**](taskschedulerschema-daysofmonth-monthlyscheduletype-element.md) | [**daysOfMonthType**](taskschedulerschema-daysofmonthtype-complextype.md) | Specifies the days of the month during which the task runs.<br/>                         |
| [**Months**](taskschedulerschema-months-monthlyscheduletype-element.md)           | [**monthsType**](taskschedulerschema-monthstype-complextype.md)           | Specifies the months of the year during which the task runs for a monthly schedule.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Complex Types](task-scheduler-schema-complex-types.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





