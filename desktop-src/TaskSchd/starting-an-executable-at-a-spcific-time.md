---
title: Starting an Executable at a Specific Time
description: Writing a task that starts an executable at a specific time is done by defining a time trigger and an executable action.
ms.assetid: a45a403d-5a54-4648-b517-41e01a0745c9
keywords:
- Task Scheduler examples Task Scheduler , time trigger
- Task Scheduler examples Task Scheduler , starting an executable
ms.topic: article
ms.date: 05/31/2018
---

# Starting an Executable at a Specific Time

Writing a task that starts an executable at a specific time is done by defining a time trigger and an executable action.

## Start Boundary

It is important to note that a time trigger is different from other time-based triggers in that it is fired when the trigger is activated by its start boundary. Other time-based triggers are activated by their start boundary, but they do not start performing their actions (in this case starting an executable) until a scheduled date is reached.

## Time Trigger Examples

The following examples start Notepad 30 seconds after the task is activated:

-   [Time Trigger Example (C++)](time-trigger-example--c---.md)
-   [Time Trigger Example (Scripting)](time-trigger-example--scripting-.md)
-   [Time Trigger Example (XML)](time-trigger-example--xml-.md)

## Related topics

<dl> <dt>

[Using the Task Scheduler](using-the-task-scheduler.md)
</dt> </dl>

 

 




