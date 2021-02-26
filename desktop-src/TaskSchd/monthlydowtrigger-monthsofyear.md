---
title: MonthlyDOWTrigger.MonthsOfYear property
description: For scripting, gets or sets the months of the year during which the task runs. | MonthlyDOWTrigger.MonthsOfYear property
ms.assetid: '4ab7ab43-9c9b-4cd3-be8f-1989b83e8cf3'
keywords:
- MonthsOfYear property Task Scheduler
- MonthsOfYear property Task Scheduler , MonthlyDOWTrigger object
- MonthlyDOWTrigger object Task Scheduler , MonthsOfYear property
topic_type:
- apiref
api_name:
- MonthlyDOWTrigger.MonthsOfYear
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# MonthlyDOWTrigger.MonthsOfYear property

For scripting, gets or sets the months of the year during which the task runs.

## Syntax


```VB
MonthlyDOWTrigger.MonthsOfYear As short
```



## Property value

A bitwise mask that indicates the months of the year during which the task runs.

## Remarks

The following table shows the mapping of the bitwise mask used by this property.



| Month     | Hex value | Decimal value |
|-----------|-----------|---------------|
| January   | 0X01      | 1             |
| February  | 0x02      | 2             |
| March     | 0X04      | 4             |
| April     | 0X08      | 8             |
| May       | 0X10      | 16            |
| June      | 0X20      | 32            |
| July      | 0x40      | 64            |
| August    | 0X80      | 128           |
| September | 0X100     | 256           |
| October   | 0X200     | 512           |
| November  | 0X400     | 1024          |
| December  | 0X800     | 2048          |



 

When reading or writing XML for a task, the months of the year of a monthly day-of-week calendar are specified by the [**Months**](taskschedulerschema-months-monthlydayofweekscheduletype-element.md) element of the Task Scheduler schema.

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

 

 





