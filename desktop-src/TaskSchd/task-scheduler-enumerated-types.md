---
title: Task Scheduler Enumerated Types
description: Lists the enumerations used by the Task Scheduler APIs.
ms.assetid: 9779d32b-0142-41bb-88e2-df79a3b0c1b2
keywords:
- Task Scheduler Task Scheduler , reference, enumerated types
ms.topic: article
ms.date: 05/31/2018
---

# Task Scheduler Enumerated Types

Describes the enumerated types that define the constants that are used by the Task Scheduler APIs.


The following enumerated types are introduced in Task Scheduler 2.0.



| Enumeration                                                                  | Description                                                                                                      |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [**TASK\_ACTION\_TYPE**](/windows/desktop/api/taskschd/ne-taskschd-task_action_type)                               | Defines the type of actions that a task can perform.                                                             |
| [**TASK\_COMPATIBILITY**](/windows/desktop/api/taskschd/ne-taskschd-task_compatibility)                            | Defines what versions of Task Scheduler or the AT command that the task is compatible with.                      |
| [**TASK\_CREATION**](/windows/desktop/api/taskschd/ne-taskschd-task_creation)                                       | Defines how the Task Scheduler service creates, updates, or disables the task.                                   |
| [**TASK\_ENUM\_FLAGS**](/windows/desktop/api/taskschd/ne-taskschd-task_enum_flags)                                 | Defines how the Task Scheduler enumerates through registered tasks.                                              |
| [**TASK\_INSTANCES\_POLICY**](/windows/desktop/api/taskschd/ne-taskschd-task_instances_policy)                     | Defines how the Task Scheduler handles existing instances of the task when it starts a new instance of the task. |
| [**TASK\_LOGON TYPE**](/windows/desktop/api/taskschd/ne-taskschd-task_logon_type)                                  | Defines what logon technique is required to run a task.                                                          |
| [**TASK\_PROCESSTOKENSID TYPE**](/windows/win32/api/taskschd/ne-taskschd-task_processtokensid_type)              | Defines the types of process SID that can used by tasks.                                                         |
| [**TASK\_RUN\_FLAGS**](/windows/desktop/api/taskschd/ne-taskschd-task_run_flags)                                   | Defines how a task is run.                                                                                       |
| [**TASK\_RUNLEVEL\_TYPE**](/windows/win32/api/taskschd/ne-taskschd-task_runlevel_type)                           | Defines LUA elevation flags that specify with what privilege level the task will be run.                         |
| [**TASK\_SESSION\_STATE\_CHANGE\_TYPE**](/windows/desktop/api/taskschd/ne-taskschd-task_session_state_change_type) | Defines what kinds of Terminal Server session state change you can use to trigger a task to start.               |
| [**TASK\_STATE**](/windows/desktop/api/taskschd/ne-taskschd-task_state)                                            | Defines the different states that a registered task can be in.                                                   |
| [**TASK\_TRIGGER\_TYPE2**](/windows/desktop/api/taskschd/ne-taskschd-task_trigger_type2)                                  | Defines the type of triggers that can be used by tasks.                                                          |



 


> [!WARNING]
> The Task Scheduler 1.0 enumerations are available only in Windows 2000, Windows XP, and Windows Server 2003 operating systems. They are deprecated as of Windows Vista and may be removed completely in the future. Please use the Task Scheduler 2.0 enumerations listed above instead.

 

## Related topics

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> <dt>

[Task Scheduler Reference](task-scheduler-reference.md)
</dt> </dl>

 

 




