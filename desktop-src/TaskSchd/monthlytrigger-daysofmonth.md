---
title: MonthlyTrigger.DaysOfMonth property
description: For scripting, gets or sets the days of the month during which the task runs.
ms.assetid: '4da80d0f-ae0c-4e56-b51b-6ee6ab309d7c'
keywords:
- DaysOfMonth property Task Scheduler
- DaysOfMonth property Task Scheduler , MonthlyTrigger object
- MonthlyTrigger object Task Scheduler , DaysOfMonth property
topic_type:
- apiref
api_name:
- MonthlyTrigger.DaysOfMonth
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# MonthlyTrigger.DaysOfMonth property

For scripting, gets or sets the days of the month during which the task runs.

## Syntax


```VB
MonthlyTrigger.DaysOfMonth As long
```



## Property value

A bitwise mask that indicates the days of the month during which the task runs.

## Remarks



| Day of month | Hex value  | Decimal value |
|--------------|------------|---------------|
| 1            | 0x01       | 1             |
| 2            | 0x02       | 2             |
| 3            | 0x04       | 4             |
| 4            | 0x08       | 8             |
| 5            | 0x10       | 16            |
| 6            | 0x20       | 32            |
| 7            | 0x40       | 64            |
| 8            | 0x80       | 128           |
| 9            | 0x100      | 256           |
| 10           | 0x200      | 512           |
| 11           | 0x400      | 1024          |
| 12           | 0x800      | 2048          |
| 13           | 0x1000     | 4096          |
| 14           | 0x2000     | 8192          |
| 15           | 0x4000     | 16384         |
| 16           | 0x8000     | 32768         |
| 17           | 0x10000    | 65536         |
| 18           | 0x20000    | 131072        |
| 19           | 0x40000    | 262144        |
| 20           | 0x80000    | 524288        |
| 21           | 0x100000   | 1048576       |
| 22           | 0x200000   | 2097152       |
| 23           | 0x400000   | 4194304       |
| 24           | 0x800000   | 8388608       |
| 25           | 0x1000000  | 16777216      |
| 26           | 0x2000000  | 33554432      |
| 27           | 0x4000000  | 67108864      |
| 28           | 0x8000000  | 134217728     |
| 29           | 0x10000000 | 268435456     |
| 30           | 0x20000000 | 536870912     |
| 31           | 0x40000000 | 1073741824    |
| Last         | 0x80000000 | 2147483648    |



 

When reading or writing your own XML for a task, the days of the month are specified using the [**DaysOfMonth**](taskschedulerschema-daysofmonth-monthlyscheduletype-element.md) element of the Task Scheduler schema.

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
</dt> <dt>

[**MonthlyTrigger**](monthlytrigger.md)
</dt> </dl>

 

 





