---
title: Week (weeksType) Element
description: Specifies a specific week of the month.
ms.assetid: 0cec07da-e9e7-43ef-9f54-48d00114ba1f
keywords:
- Week element Task Scheduler
topic_type:
- apiref
api_name:
- Week
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Week (weeksType) Element

Specifies a specific week of the month.

``` syntax
<xs:element name="Week"
    type="weekType"
 />
```

The **Week** element is defined by the [**weeksType**](taskschedulerschema-weekstype-complextype.md) complex type.

## Parent element



| Element                                                                                                        | Derived from                                                   | Description                                                           |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|-----------------------------------------------------------------------|
| [**Weeks (monthlyDayOfWeekScheduleType)**](taskschedulerschema-weeks-monthlydayofweekscheduletype-element.md) | [**weeksType**](taskschedulerschema-weekstype-complextype.md) | Specifies the weeks of the month in which the task is run.<br/> |



## Remarks

When specifying the weeks of the month, use the numbers 1-4 for the first four weeks of the month or use the string "Last" to indicate that last week of the month.

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

 

 





