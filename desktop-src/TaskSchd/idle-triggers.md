---
title: Idle Triggers for Task Scheduler 1.0
description: An idle trigger is an event-based trigger that is fired a specific number of times after the computer becomes idle. There are multiple conditions that define when a computer becomes idle, such as when no keyboard or mouse input occurs.
ms.assetid: f2e0b120-dadc-470f-8349-42843149bb60
ms.topic: article
ms.date: 05/31/2018
---

# Idle Triggers for Task Scheduler 1.0

An idle trigger is an event-based trigger that is fired a specific number of times after the computer becomes idle. There are multiple conditions that define when a computer becomes idle, such as when no keyboard or mouse input occurs.

Idle triggers are created by specifying TASK\_EVENT\_TRIGGER\_ON\_IDLE in the [**TASK\_TRIGGER\_TYPE**](/windows/desktop/api/Mstask/ne-mstask-task_trigger_type) member of the [**TASK\_TRIGGER**](/windows/desktop/api/Mstask/ns-mstask-task_trigger) structure. The idle trigger is fired when the system becomes idle for the amount of time that is specified by the idle wait time of the work item.

> [!Note]  
> When TASK\_EVENT\_TRIGGER\_ON\_IDLE is specified, the **wStartHour**, **wStartMinute**, and **Type** members of the [**TASK\_TRIGGER**](/windows/desktop/api/Mstask/ns-mstask-task_trigger) structure are ignored.

 

You can set the idle wait time of a work item by calling the [**IScheduledWorkItem::SetIdleWait**](/windows/desktop/api/Mstask/nf-mstask-ischeduledworkitem-setidlewait) method. This method sets the amount of time (in minutes) that the system must remain idle before the trigger is fired and the work item is executed.

To retrieve the idle time of a task, call the [**IScheduledWorkItem::GetIdleWait**](/windows/desktop/api/Mstask/nf-mstask-ischeduledworkitem-getidlewait) method.

## Related topics

<dl> <dt>

[Task Triggers](task-triggers.md)
</dt> </dl>

 

 




