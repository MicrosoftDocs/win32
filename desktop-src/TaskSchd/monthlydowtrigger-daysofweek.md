---
title: MonthlyDOWTrigger.DaysOfWeek property
description: For scripting, gets or sets the days of the week during which the task runs.
ms.assetid: 'dd9b2463-69a1-4e77-a8f7-26b186d3d02d'
keywords:
- DaysOfWeek property Task Scheduler
- DaysOfWeek property Task Scheduler , MonthlyDOWTrigger object
- MonthlyDOWTrigger object Task Scheduler , DaysOfWeek property
topic_type:
- apiref
api_name:
- MonthlyDOWTrigger.DaysOfWeek
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# MonthlyDOWTrigger.DaysOfWeek property

For scripting, gets or sets the days of the week during which the task runs.

## Syntax


```VB
MonthlyDOWTrigger.DaysOfWeek As short
```



## Property value

A bitwise mask that indicates the days of the week during which the task runs.

## Remarks

The following table shows the mapping of the bitwise mask used by this property.



| Day of Week | Hex Value | Decimal Value |
|-------------|-----------|---------------|
| Sunday      | 0x01      | 1             |
| Monday      | 0x02      | 2             |
| Tuesday     | 0x04      | 4             |
| Wednesday   | 0x08      | 8             |
| Thursday    | 0x10      | 16            |
| Friday      | 0x20      | 32            |
| Saturday    | 0x40      | 64            |



 

When reading or writing XML for a task, the days of the week of a monthly day-of-week calendar are specified by the [**DaysOfWeek**](taskschedulerschema-daysofweek-monthlydayofweekscheduletype-element.md) element.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**MonthlyDOWTrigger**](monthlydowtrigger.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





