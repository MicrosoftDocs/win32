---
title: Task Scheduler 1.0 Interfaces
description: The interfaces that are described in the following topics provide programmatic access to the functionality that is available within the Task Scheduler that is used in the Windows 2000, Windows XP, and Windows Server 2003 operating systems.
ms.assetid: 25f9c1ad-1859-4788-a876-6f4faa6e556e
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Task Scheduler 1.0 Interfaces

\[\[This API may be altered or unavailable in subsequent versions of the operating system or product. Please use the [Task Scheduler 2.0 Interfaces](task-scheduler-2-0-interfaces.md) or [Task Scheduler 2.0 Enumerated Types](task-scheduler-2-0-enumerated-types.md) instead.\] \]

The interfaces that are described in the following topics provide programmatic access to the functionality that is available within the Task Scheduler that is used in the Windows 2000, Windows XP, and Windows Server 2003 operating systems.

These topics contain a description of the interface, a list of the properties and methods defined by the interface, and remarks about any special circumstances that should be noted when using the interface.

## 

The following interfaces are introduced by Task Scheduler 1.0.



| Interface                                        | Description                                                                                                                                                                                                                           |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IEnumWorkItems**](/windows/win32/Mstask/nn-mstask-ienumworkitems?branch=master)         | Provides the methods for enumerating the tasks in the [*Scheduled Tasks folder*](s.md#-msb-scheduled-tasks-folder-gly).                                                                                                              |
| [**IProvideTaskPage**](/windows/win32/Mstask/nn-mstask-iprovidetaskpage?branch=master)     | Provides the methods to access the property sheet settings of a task.                                                                                                                                                                 |
| [**IScheduledWorkItem**](/windows/win32/Mstask/nn-mstask-ischeduledworkitem?branch=master) | Provides the methods for managing specific [*work items*](w.md#-msb-work-items-gly).                                                                                                                                                 |
| [**ITask**](/windows/win32/Mstask/nn-mstask-itask?branch=master)                           | Provides the methods for running tasks, getting or setting task information, and terminating tasks. It is derived from the [**IScheduledWorkItem**](/windows/win32/Mstask/nn-mstask-ischeduledworkitem?branch=master) interface and inherits all the methods of that interface. |
| [**ITaskScheduler**](/windows/win32/Mstask/nn-mstask-itaskscheduler?branch=master)         | Provides the methods for scheduling tasks.                                                                                                                                                                                            |
| [**ITaskTrigger**](/windows/win32/Mstask/nn-mstask-itasktrigger?branch=master)             | Provides the methods for accessing and setting triggers for a task. Triggers specify task start times, repetition criteria, and other parameters that control when a task is run.                                                     |



 

 

 




