---
title: Task Scheduler Enumerated Types
description: Lists the enumerations used by the Task Scheduler APIs.
ms.assetid: 9779d32b-0142-41bb-88e2-df79a3b0c1b2
keywords:
- Task Scheduler Task Scheduler , reference, enumerated types
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Task Scheduler Enumerated Types

Describes the enumerated types that define the constants that are used by the Task Scheduler APIs.

## 

The following enumerated types are introduced in Task Scheduler 2.0.



| Enumeration                                                                  | Description                                                                                                      |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [**TASK\_ACTION\_TYPE**](/windows/win32/taskschd/ne-taskschd-_task_action_type?branch=master)                               | Defines the type of actions that a task can perform.                                                             |
| [**TASK\_COMPATIBILITY**](/windows/win32/taskschd/ne-taskschd-_task_compatibility?branch=master)                            | Defines what versions of Task Scheduler or the AT command that the task is compatible with.                      |
| [**TASK\_CREATION**](/windows/win32/taskschd/ne-taskschd-_task_creation?branch=master)                                       | Defines how the Task Scheduler service creates, updates, or disables the task.                                   |
| [**TASK\_ENUM\_FLAGS**](/windows/win32/taskschd/ne-taskschd-_task_enum_flags?branch=master)                                 | Defines how the Task Scheduler enumerates through registered tasks.                                              |
| [**TASK\_INSTANCES\_POLICY**](/windows/win32/taskschd/ne-taskschd-_task_instances_policy?branch=master)                     | Defines how the Task Scheduler handles existing instances of the task when it starts a new instance of the task. |
| [**TASK\_LOGON TYPE**](/windows/win32/taskschd/ne-taskschd-_task_logon_type?branch=master)                                  | Defines what logon technique is required to run a task.                                                          |
| [**TASK\_PROCESSTOKENSID TYPE**](/windows/win32/taskschd/ne-taskschd-_task_processtokensid?branch=master)              | Defines the types of process SID that can used by tasks.                                                         |
| [**TASK\_RUN\_FLAGS**](/windows/win32/taskschd/ne-taskschd-_task_run_flags?branch=master)                                   | Defines how a task is run.                                                                                       |
| [**TASK\_RUNLEVEL\_TYPE**](/windows/win32/taskschd/ne-taskschd-_task_runlevel?branch=master)                           | Defines LUA elevation flags that specify with what privilege level the task will be run.                         |
| [**TASK\_SESSION\_STATE\_CHANGE\_TYPE**](/windows/win32/taskschd/ne-taskschd-_task_session_state_change_type?branch=master) | Defines what kinds of Terminal Server session state change you can use to trigger a task to start.               |
| [**TASK\_STATE**](/windows/win32/taskschd/ne-taskschd-_task_state?branch=master)                                            | Defines the different states that a registered task can be in.                                                   |
| [**TASK\_TRIGGER\_TYPE2**](/windows/win32/taskschd/ne-taskschd-_task_trigger_type2?branch=master)                                  | Defines the type of triggers that can be used by tasks.                                                          |



 

## 

> \[!Warning\]  
> The Task Scheduler 1.0 enumerations are available only in Windows 2000, Windows XP, and Windows Server 2003 operating systems. They are deprecated as of Windows Vista and may be removed completely in the future. Please use the Task Scheduler 2.0 enumerations listed above instead.

 

## Related topics

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> <dt>

[Task Scheduler Reference](task-scheduler-reference.md)
</dt> </dl>

 

 




