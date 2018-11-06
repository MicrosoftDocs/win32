---
title: Starting an Executable on System Boot
description: Writing a task that starts an executable when a system is booted is done by defining a boot trigger and an executable action.
ms.assetid: 9e2359df-a223-4a0c-9051-01b73a83c1f7
keywords:
- Task Scheduler examples Task Scheduler , boot trigger
ms.topic: article
ms.date: 05/31/2018
---

# Starting an Executable on System Boot

Writing a task that starts an executable when a system is booted is done by defining a boot trigger and an executable action.

## Boot Trigger

Boot triggers are activated by their start boundary but they do not start the executable until the system is booted. You can also specify a delay time in the boot trigger that specifies the amount of time between when the system is booted and when the task is started. This is defined by the [**Delay**](/windows/desktop/api/taskschd/nf-taskschd-iboottrigger-get_delay) property in the [**IBootTrigger**](/windows/desktop/api/taskschd/nn-taskschd-iboottrigger) interface ([**BootTrigger**](boottrigger.md) object for scripting).

## Boot Trigger Examples

The following examples start Notepad after the system is booted:

-   [Boot Trigger Example (Scripting)](boot-trigger-example--scripting-.md)
-   [Boot Trigger Example (C++)](boot-trigger-example--c---.md)
-   [Boot Trigger Example (XML)](boot-trigger-example--xml-.md)

## Related topics

<dl> <dt>

[Using the Task Scheduler](using-the-task-scheduler.md)
</dt> </dl>

 

 




