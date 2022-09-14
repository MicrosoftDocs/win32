---
title: July (monthsType) Element
description: Specifies that the task runs in July.
ms.assetid: 6fcb06f1-0806-469c-a283-ba8f2ba2c256
keywords:
- July element Task Scheduler
topic_type:
- apiref
api_name:
- July
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# July (monthsType) Element

Specifies that the task runs in July.

``` syntax
<xs:element name="July">
    <xs:complexType />
</xs:element>
```

The **July** element is defined by the [**monthsType**](taskschedulerschema-monthstype-complextype.md) complex type.

## Parent element



| Element                                                                                                          | Derived from                                                     | Description                                                                                                |
|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [**Months (monthlyDayOfWeekScheduleType)**](taskschedulerschema-months-monthlydayofweekscheduletype-element.md) | [**monthsType**](taskschedulerschema-monthstype-complextype.md) | Specifies the months of the year during which the task runs for a monthly day-of-week schedule.<br/> |
| [**Months (monthlyScheduleType)**](taskschedulerschema-months-monthlyscheduletype-element.md)                   | [**monthsType**](taskschedulerschema-monthstype-complextype.md) | Specifies the months of the year during which the task runs for a monthly schedule.<br/>             |



## Examples

The following XML defines a months calendar that runs the task in July.


```XML
<Months>
    <July/>
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

 

 





