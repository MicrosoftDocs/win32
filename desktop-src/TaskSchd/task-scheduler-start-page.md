---
title: Task Scheduler for developers
description: The Task Scheduler enables you to automatically perform routine tasks on a chosen computer. The Task Scheduler does so by monitoring whatever criteria you choose and then executing the tasks when those criteria are met.
ms.assetid: 15970a51-c139-48b8-b82b-605728d0f386
keywords:
- Task Scheduler for developers
- Task Scheduler for development
- Developing with Task Scheduler
- Task Scheduler, portal page
ms.topic: article
ms.date: 02/07/2023
---

# Task Scheduler for developers

> [!IMPORTANT]
> This topic and the other topics in this section are for a developer audience. For info about using the Task Scheduler component in your capacity as an administrator, or an IT Professional, see [Task Scheduler](/dynamics365/business-central/dev-itpro/developer/devenv-task-scheduler) in the Microsoft Dynamics 365 documentation.

The Task Scheduler enables you to automatically perform routine tasks on a chosen computer. The Task Scheduler does so by monitoring whatever criteria you choose (referred to as triggers) and then executing the tasks when those criteria are met.

Some examples of tasks that you can use the Task Scheduler to execute are: starting an application; sending an email message; or displaying a message box. You can schedule a task to execute in response to these triggers:

- When a specific system event occurs.
- At a specific time.
- At a specific time on a daily schedule.
- At a specific time on a weekly schedule.
- At a specific time on a monthly schedule.
- At a specific time on a monthly day-of-week schedule.
- When the computer enters an idle state.
- When the task is registered.
- When the system is booted.
- When a user logs on.
- When a Terminal Server session changes state.

## API information

The Task Scheduler provides APIs in these forms:

- Task Scheduler 2.0: Interfaces and objects are provided for C++, and for scripting development, respectively.
- Task Scheduler 1.0: Interfaces are provided for C++ development only.

## Run-time requirements

The Task Scheduler requires the following operating systems:

- Task Scheduler 2.0: Client requires Windows Vista or later. Server requires Windows Server 2008 or later.
- Task Scheduler 1.0: Client requires Windows Vista or Windows XP. Server requires Windows Server 2008 or Windows Server 2003.

## In this section

| Topic | Description |
|-|-|
| [What's new in Task Scheduler](what-s-new-in-task-scheduler.md) | Summary of new functionality introduced by the Task Scheduler. |
| [About the Task Scheduler](about-the-task-scheduler.md) | General conceptual information about the Task Scheduler API. |
| [Using the Task Scheduler](using-the-task-scheduler.md) | Code examples that show how to use the Task Scheduler APIs. |
| [Task Scheduler reference](task-scheduler-reference.md) | Detailed reference information for Task Scheduler APIs and the Task Scheduler schema. |
