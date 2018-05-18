---
title: Task Scheduler 1.0 Interfaces
description: The interfaces that are described in the following topics provide programmatic access to the functionality that is available within the Task Scheduler that is used in the Windows 2000, Windows XP, and Windows Server 2003 operating systems.
ms.assetid: '25f9c1ad-1859-4788-a876-6f4faa6e556e'
---

# Task Scheduler 1.0 Interfaces

\[\[This API may be altered or unavailable in subsequent versions of the operating system or product. Please use the [Task Scheduler 2.0 Interfaces](task-scheduler-2-0-interfaces.md) or [Task Scheduler 2.0 Enumerated Types](task-scheduler-2-0-enumerated-types.md) instead.\] \]

The interfaces that are described in the following topics provide programmatic access to the functionality that is available within the Task Scheduler that is used in the Windows 2000, Windows XP, and Windows Server 2003 operating systems.

These topics contain a description of the interface, a list of the properties and methods defined by the interface, and remarks about any special circumstances that should be noted when using the interface.

## 

The following interfaces are introduced by Task Scheduler 1.0.



| Interface                                        | Description                                                                                                                                                                                                                           |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IEnumWorkItems**](ienumworkitems.md)         | Provides the methods for enumerating the tasks in the [*Scheduled Tasks folder*](s.md#-msb-scheduled-tasks-folder-gly).                                                                                                              |
| [**IProvideTaskPage**](iprovidetaskpage.md)     | Provides the methods to access the property sheet settings of a task.                                                                                                                                                                 |
| [**IScheduledWorkItem**](ischeduledworkitem.md) | Provides the methods for managing specific [*work items*](w.md#-msb-work-items-gly).                                                                                                                                                 |
| [**ITask**](itask.md)                           | Provides the methods for running tasks, getting or setting task information, and terminating tasks. It is derived from the [**IScheduledWorkItem**](ischeduledworkitem.md) interface and inherits all the methods of that interface. |
| [**ITaskScheduler**](itaskscheduler.md)         | Provides the methods for scheduling tasks.                                                                                                                                                                                            |
| [**ITaskTrigger**](itasktrigger.md)             | Provides the methods for accessing and setting triggers for a task. Triggers specify task start times, repetition criteria, and other parameters that control when a task is run.                                                     |



 

 

 




