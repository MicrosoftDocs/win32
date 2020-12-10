---
title: WeeklyTrigger.DaysOfWeek property
description: For scripting, gets or sets the days of the week on which the task runs.
ms.assetid: '79f279d4-d6d2-428b-bbed-226e4eaaefb6'
keywords:
- DaysOfWeek property Task Scheduler
- DaysOfWeek property Task Scheduler , WeeklyTrigger object
- WeeklyTrigger object Task Scheduler , DaysOfWeek property
topic_type:
- apiref
api_name:
- WeeklyTrigger.DaysOfWeek
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# WeeklyTrigger.DaysOfWeek property

For scripting, gets or sets the days of the week on which the task runs.

## Syntax


```VB
WeeklyTrigger.DaysOfWeek As short
```



## Property value

A bitwise mask that indicates the days of the week on which the task runs.

## Remarks

The following table shows the mapping of the bitwise mask used by this property.



| Month     | Hex value | Decimal value |
|-----------|-----------|---------------|
| Sunday    | 0X01      | 1             |
| Monday    | 0x02      | 2             |
| Tuesday   | 0X04      | 4             |
| Wednesday | 0X08      | 8             |
| Thursday  | 0X10      | 16            |
| Friday    | 0x20      | 32            |
| Saturday  | 0X40      | 64            |



 

When reading or writing your own XML for a task, the days of the week are specified using the [**DaysOfWeek**](taskschedulerschema-daysofweek-weeklyscheduletype-element.md) element of the Task Scheduler schema.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





