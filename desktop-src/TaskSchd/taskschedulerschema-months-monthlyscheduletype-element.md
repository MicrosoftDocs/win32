---
title: Months (monthlyScheduleType) Element
description: Specifies the months of the year during which the task runs for a monthly schedule.
ms.assetid: 71c9f7ac-01fc-4837-bccf-1869df2bc24e
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

# Months (monthlyScheduleType) Element

Specifies the months of the year during which the task runs for a monthly schedule.

``` syntax
<xs:element name="Months"
    type="monthsType"
 />
```

The **Months** element is defined by the [**monthlyScheduleType**](taskschedulerschema-monthlyscheduletype-complextype.md) complex type.

## Parent element



| Element                                                                                    | Derived from                                                                       | Description                               |
|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|-------------------------------------------|
| [**ScheduleByMonth**](taskschedulerschema-schedulebymonth-calendartriggertype-element.md) | [**monthlyScheduleType**](taskschedulerschema-monthlyscheduletype-complextype.md) | Specifies a monthly schedule. <br/> |



## Child elements



| Element                                                                            | Type | Description                                           |
|------------------------------------------------------------------------------------|------|-------------------------------------------------------|
| [**April (monthsType)**](taskschedulerschema-april-monthstype-element.md)         |      | Specifies that the task runs in April.<br/>     |
| [**August (monthsType)**](taskschedulerschema-august-monthstype-element.md)       |      | Specifies that the task runs in August.<br/>    |
| [**December (monthsType)**](taskschedulerschema-december-monthstype-element.md)   |      | Specifies that the task runs in December.<br/>  |
| [**February (monthsType)**](taskschedulerschema-february-monthstype-element.md)   |      | Specifies that the task runs in February.<br/>  |
| [**January (monthsType)**](taskschedulerschema-january-monthstype-element.md)     |      | Specifies that the task runs in January.<br/>   |
| [**July (monthsType)**](taskschedulerschema-july-monthstype-element.md)           |      | Specifies that the task runs in July.<br/>      |
| [**June (monthsType)**](taskschedulerschema-june-monthstype-element.md)           |      | Specifies that the task runs in June.<br/>      |
| [**March (monthsType)**](taskschedulerschema-march-monthstype-element.md)         |      | Specifies that the task runs in March.<br/>     |
| [**May (monthsType)**](taskschedulerschema-may-monthstype-element.md)             |      | Specifies that the task runs in May.<br/>       |
| [**November (monthsType)**](taskschedulerschema-november-monthstype-element.md)   |      | Specifies that the task runs in November.<br/>  |
| [**October (monthsType)**](taskschedulerschema-october-monthstype-element.md)     |      | Specifies that the task runs in October.<br/>   |
| [**September (monthsType)**](taskschedulerschema-september-monthstype-element.md) |      | Specifies that the task runs in September.<br/> |



## Remarks

For script development, the months of the schedule are specified using the [**MonthlyTrigger.MonthsOfYear**](monthlytrigger-monthsofyear.md) property.

For C++ development, the months of the schedule are specified using the [**IMonthlyTrigger::MonthsOfYear**](/windows/desktop/api/taskschd/nf-taskschd-imonthlytrigger-get_monthsofyear) property.

## Examples

The following XML defines a monthly calendar that starts the task on the 1st and 15th day of every month of the year.


```XML
</ScheduleByMonth>
    <DaysOfMonth>
        <Day>1</Day>
        <Day>15</Day>
    </DaysOfMonth
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
</ScheduleByMonth>
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

 

 





