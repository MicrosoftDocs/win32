---
title: September (monthsType) Element
description: Specifies that the task runs in September.
ms.assetid: b1ad2221-ca22-4808-bf20-ecf3cbb930f2
keywords:
- September element Task Scheduler
topic_type:
- apiref
api_name:
- September
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# September (monthsType) Element

Specifies that the task runs in September.

``` syntax
<xs:element name="September">
    <xs:complexType />
</xs:element>
```

The **September** element is defined by the [**monthsType**](taskschedulerschema-monthstype-complextype.md) complex type.

## Parent element



| Element                                                                                                          | Derived from                                                     | Description                                                                                                |
|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [**Months (monthlyDayOfWeekScheduleType)**](taskschedulerschema-months-monthlydayofweekscheduletype-element.md) | [**monthsType**](taskschedulerschema-monthstype-complextype.md) | Specifies the months of the year during which the task runs for a monthly day-of-week schedule.<br/> |
| [**Months (monthlyScheduleType)**](taskschedulerschema-months-monthlyscheduletype-element.md)                   | [**monthsType**](taskschedulerschema-monthstype-complextype.md) | Specifies the months of the year during which the task runs for a monthly schedule.<br/>             |



## Examples

The following XML defines a months calendar that runs the task in September.


```XML
<Months>
    <September/>
</Months>
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

 

 





