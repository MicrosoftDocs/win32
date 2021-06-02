---
title: MonthlyDOWTrigger.WeeksOfMonth property
description: For scripting, gets or sets the weeks of the month during which the task runs.
ms.assetid: '62c3b654-622e-4a71-b77e-1b3fd5fb46b8'
keywords:
- WeeksOfMonth property Task Scheduler
- WeeksOfMonth property Task Scheduler , MonthlyDOWTrigger object
- MonthlyDOWTrigger object Task Scheduler , WeeksOfMonth property
topic_type:
- apiref
api_name:
- MonthlyDOWTrigger.WeeksOfMonth
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# MonthlyDOWTrigger.WeeksOfMonth property

For scripting, gets or sets the weeks of the month during which the task runs.

## Syntax


```VB
MonthlyDOWTrigger.WeeksOfMonth As short
```



## Property value

A bitwise mask that indicates the days of the week during which the task runs.

## Remarks

The following table shows the mapping of the bitwise mask used by this property.



| Week                     | Hex Value | Decimal Value |
|--------------------------|-----------|---------------|
| First week of the month  | 0X01      | 1             |
| Second week of the month | 0x02      | 2             |
| Third week of the month  | 0X04      | 4             |
| Fourth week of the month | 0X08      | 8             |



 

When reading or writing XML for a task, the days of the week of a monthly day-of-week calendar are specified by the [**Weeks**](taskschedulerschema-weeks-monthlydayofweekscheduletype-element.md) element.

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

 

 





