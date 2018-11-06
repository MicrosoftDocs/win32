---
title: Enumerating Tasks and Displaying Task Information
description: Displaying information about a task, such as the task name, state, or the last time the task was run, is done by enumerating through running tasks or the tasks in a task folder and displaying the desired information.
ms.assetid: a0305089-89ff-42b7-b3f1-99a6484d2e5e
keywords:
- enumerating tasks Task Scheduler
- Task Scheduler examples Task Scheduler , enumerating tasks
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Tasks and Displaying Task Information

Displaying information about a task, such as the task name, state, or the last time the task was run, is done by enumerating through running tasks or the tasks in a task folder and displaying the desired information.

## Accessing Properties of Registered Tasks

To display a registered task's property value, you must connect to the Task Scheduler service, and then get an instance of the task folder that contains the tasks you want information about. You then get a collection of all the registered tasks in the task folder. Then you enumerate through each registered task and get and display a property value for each task.

## Accessing Properties of Running Tasks

To display a running task's property value, you must connect to the Task Scheduler service, and then get a collection of all the running tasks (including or excluding hidden tasks). Then you enumerate through each running task and get and display a property value for each task.

## Example

The following examples enumerate tasks and display the name and state of the tasks:

-   [Displaying Task Names and States (Scripting)](displaying-task-names-and-state--scripting-.md)
-   [Displaying Task Names and State (C++)](displaying-task-names-and-state--c---.md)

## Related topics

<dl> <dt>

[Using the Task Scheduler](using-the-task-scheduler.md)
</dt> </dl>

 

 




