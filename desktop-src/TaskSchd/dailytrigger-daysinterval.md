---
title: DailyTrigger.DaysInterval property
description: For scripting, gets or sets the interval between the days in the schedule.
ms.assetid: 13e9f6fd-62ee-4b19-8b3d-a6808e146340
keywords:
- DaysInterval property Task Scheduler
- DaysInterval property Task Scheduler , DailyTrigger object
- DailyTrigger object Task Scheduler , DaysInterval property
topic_type:
- apiref
api_name:
- DailyTrigger.DaysInterval
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# DailyTrigger.DaysInterval property

For scripting, gets or sets the interval between the days in the schedule.

## Syntax


```VB
DailyTrigger.DaysInterval As short
```



## Property value

The interval between the days in the schedule.

## Remarks

An interval of 1 produces a daily schedule. An interval of 2 produces an every-other day schedule.

When reading or writing your own XML for a task, the interval for a daily schedule is specified using the [**DaysInterval**](taskschedulerschema-daysinterval-dailyscheduletype-element.md) element of the Task Scheduler schema.

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

[**DailyTrigger**](dailytrigger.md)
</dt> </dl>

 

 





