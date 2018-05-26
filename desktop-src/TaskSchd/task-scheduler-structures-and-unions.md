---
title: Task Scheduler Structures and Unions
description: Lists the structures and unions used by the Task Scheduler 1.0 APIs.
ms.assetid: 37dc7818-7719-4975-b7bd-f8c2d5cc008b
keywords:
- Task Scheduler Task Scheduler , reference, structures and unions
- triggers Task Scheduler , structures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Task Scheduler Structures and Unions

This section describes the structures and unions used by the Task Scheduler APIs.

All the structures and unions below are used by Task Scheduler 1.0.



| Name                                               | Description                                                                                                                     |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [**DAILY**](/windows/win32/Mstask/ns-mstask-_daily?branch=master)                             | Defines the interval, in days, at which a task is run.                                                                          |
| [**MONTHLYDATE**](/windows/win32/Mstask/ns-mstask-_monthlydate?branch=master)                 | Defines the day of the month the task will run.                                                                                 |
| [**MONTHLYDOW**](/windows/win32/Mstask/ns-mstask-_monthlydow?branch=master)                   | Defines the date(s) that the task runs by month, week, and day of the week.                                                     |
| [**TASK\_TRIGGER**](/windows/win32/Mstask/ns-mstask-_task_trigger?branch=master)              | Defines the times to run a scheduled [*work item*](w.md#-msb-work-items-gly).                                                  |
| [**TRIGGER\_TYPE\_UNION**](/windows/win32/Mstask/ns-mstask-_trigger_type_union?branch=master) | Defines the invocation schedule of the trigger within the **Type** member of a [**TASK\_TRIGGER**](/windows/win32/Mstask/ns-mstask-_task_trigger?branch=master) structure. |
| [**WEEKLY**](/windows/win32/Mstask/ns-mstask-_weekly?branch=master)                           | Defines the interval, in weeks, between invocations of a task.                                                                  |



 

 

 




