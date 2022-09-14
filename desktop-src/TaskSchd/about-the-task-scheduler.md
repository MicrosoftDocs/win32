---
title: About the Task Scheduler
description: The Task Scheduler service allows you to perform automated tasks on a chosen computer.
ms.assetid: 13816b8b-3090-4d17-86bb-8e632ca0cd37
keywords:
- Task Scheduler Task Scheduler , about
ms.topic: article
ms.date: 05/31/2018
---

# About the Task Scheduler

The Task Scheduler service allows you to perform automated tasks on a chosen computer. With this service, you can schedule any program to run at a convenient time for you or when a specific event occurs. The Task Scheduler monitors the time or event criteria that you choose and then executes the task when those criteria are met.

## Where Task Scheduler is Installed

The Task Scheduler is automatically installed with several Microsoft operating systems.

Task Scheduler 1.0 is installed with the Windows Server 2003, Windows XP, and Windows 2000 operating systems.

Task Scheduler 2.0 is installed with Windows Vista and Windows Server 2008.

The Task Scheduler 2.0 API should be used in developing applications that use the Task Scheduler service on Windows Vista. For more information, see [Task Scheduler Reference](task-scheduler-reference.md).

Task Scheduler is started each time the operating system is started. It can be run either through the Task Scheduler graphical user interface (GUI) or through the Task Scheduler API described in this SDK.

## Information about Tasks

Tasks are the main component of the Task Scheduler. For information on what tasks are and what their components are, see the following topics:

-   [Tasks](tasks.md)
-   [Task Actions](task-actions.md)
-   [Task Triggers](task-triggers.md)
-   [Task Registration Information](task-registration-information.md)
-   [Task Idle Conditions](task-idle-conditions.md)
-   [Security Contexts for Tasks](security-contexts-for-running-tasks.md)
-   [Repeating A Task](repeating-a-task.md)
-   [Automatic Maintenance](task-maintenence.md)

For more information and examples about how to use the Task Scheduler interfaces, scripting objects, and XML, see [Using the Task Scheduler](using-the-task-scheduler.md).

## Related topics

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 




