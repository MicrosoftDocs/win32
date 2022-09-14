---
title: Task Scheduler Structures and Unions
description: Lists the structures and unions used by the Task Scheduler 1.0 APIs.
ms.assetid: 37dc7818-7719-4975-b7bd-f8c2d5cc008b
keywords:
- Task Scheduler Task Scheduler , reference, structures and unions
- triggers Task Scheduler , structures
ms.topic: article
ms.date: 05/31/2018
---

# Task Scheduler Structures and Unions

This section describes the structures and unions used by the Task Scheduler APIs.

All the structures and unions below are used by Task Scheduler 1.0.



| Name                                               | Description                                                                                                                     |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [**DAILY**](/windows/desktop/api/Mstask/ns-mstask-daily)                             | Defines the interval, in days, at which a task is run.                                                                          |
| [**MONTHLYDATE**](/windows/desktop/api/Mstask/ns-mstask-monthlydate)                 | Defines the day of the month the task will run.                                                                                 |
| [**MONTHLYDOW**](/windows/desktop/api/Mstask/ns-mstask-monthlydow)                   | Defines the date(s) that the task runs by month, week, and day of the week.                                                     |
| [**TASK\_TRIGGER**](/windows/desktop/api/Mstask/ns-mstask-task_trigger)              | Defines the times to run a scheduled [*work item*](w.md).                                                  |
| [**TRIGGER\_TYPE\_UNION**](/windows/desktop/api/Mstask/ns-mstask-trigger_type_union) | Defines the invocation schedule of the trigger within the **Type** member of a [**TASK\_TRIGGER**](/windows/desktop/api/Mstask/ns-mstask-task_trigger) structure. |
| [**WEEKLY**](/windows/desktop/api/Mstask/ns-mstask-weekly)                           | Defines the interval, in weeks, between invocations of a task.                                                                  |



 

 

 




