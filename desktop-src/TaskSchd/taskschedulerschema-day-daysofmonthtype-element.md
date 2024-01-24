---
title: Day (daysOfMonthType) Element
description: Specifies a day of the month during which the task runs.
ms.assetid: b213df09-9301-4a51-b000-edfdafbe861e
keywords:
- Day element Task Scheduler
topic_type:
- apiref
api_name:
- Day
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Day (daysOfMonthType) Element

Specifies a day of the month during which the task runs.

``` syntax
<xs:element name="Day"
    type="dayOfMonthType"
 />
```

The **Day** element is defined by the [**daysOfMonthType**](taskschedulerschema-daysofmonthtype-complextype.md) complex type.

## Parent element



| Element                                                                            | Derived from                                                               | Description                                                            |
|------------------------------------------------------------------------------------|----------------------------------------------------------------------------|------------------------------------------------------------------------|
| [**DaysOfMonth**](taskschedulerschema-daysofmonth-monthlyscheduletype-element.md) | [**daysOfMonthType**](taskschedulerschema-daysofmonthtype-complextype.md) | Specifies the days of the month during which the task runs.<br/> |



## Examples

The following XML defines the days portion of a monthly calendar that runs the task on the 1st and 15th day of the month.


```XML
<DaysOfMonth>
    <Day>1</Day>
    <Day>15</Day>
</DaysOfMonth>
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> </dl>

 

 





