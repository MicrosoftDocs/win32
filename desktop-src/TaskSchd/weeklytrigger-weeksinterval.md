---
title: WeeklyTrigger.WeeksInterval property
description: For scripting, gets or sets the interval between the weeks in the schedule.
ms.assetid: 11f2c708-a95b-4b9c-a3a6-9b37b01d2d0b
keywords:
- WeeksInterval property Task Scheduler
- WeeksInterval property Task Scheduler , WeeklyTrigger object
- WeeklyTrigger object Task Scheduler , WeeksInterval property
topic_type:
- apiref
api_name:
- WeeklyTrigger.WeeksInterval
api_location:
- taskschd.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WeeklyTrigger.WeeksInterval property

For scripting, gets or sets the interval between the weeks in the schedule.

## Syntax


```VB
WeeklyTrigger.WeeksInterval As short
```



## Property value

The interval between the weeks in the schedule.

## Remarks

An interval of 1 produces a weekly schedule. An interval of 2 produces an every-other week schedule.

When reading or writing your own XML for a task, the interval for a weekly schedule is specified using the [**WeeksInterval**](taskschedulerschema-weeksinterval-weeklyscheduletype-element.md) element of the Task Scheduler schema.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





