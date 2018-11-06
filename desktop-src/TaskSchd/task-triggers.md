---
title: Task Triggers
description: A trigger is a set of criteria that, when met, starts the execution of a task.
ms.assetid: 8b4dff8b-9dc3-4856-aed6-648588a089be
keywords:
- creating triggers Task Scheduler
- triggers Task Scheduler
- triggers Task Scheduler , described
- triggers Task Scheduler , time-based
- triggers Task Scheduler , event-based
- event-based triggers Task Scheduler
- time-based triggers Task Scheduler
ms.topic: article
ms.date: 05/31/2018
---

# Task Triggers

A trigger is a set of criteria that, when met, starts the execution of a task. Task Scheduler provides both time-based and event-based triggers that can start a task in several different ways. A given task can be started by one or more triggers. A task can have a maximum of 48 triggers.

## Time-based Triggers

Time-based triggers start tasks at specified times. This includes starting the task once at a specific time or starting the task multiple times on a daily, weekly, monthly, or monthly day-of-week schedule.

## Event-based Triggers

Event-based triggers start a task in response to certain system events. For example, event-based triggers can be set to start a task when the system starts up, when a user logs on to the local computer, or when the system becomes idle.

## Multiple Triggers

Each task can be started by one or more triggers, allowing the task to be started in any number of ways. However, multiple triggers are implemented differently in Task Scheduler 1.0 and Task Scheduler 2.0.

In Task Scheduler 2.0, each trigger is defined by a separate trigger API that is associated with the task through the trigger collection.

In Task Scheduler 1.0, multiple triggers can be thought of as a schedule, a set of times at which the task starts. In this case, the schedule is the set of times (specified by the union of all of the triggers associated with the work item) at which a work item will execute.

## Related topics

<dl> <dt>

[Repeating A Task](repeating-a-task.md)
</dt> <dt>

[Trigger Types](trigger-types.md)
</dt> <dt>

[Trigger Interfaces](trigger-interfaces.md)
</dt> <dt>

[About The Task Scheduler](about-the-task-scheduler.md)
</dt> </dl>

 

 




