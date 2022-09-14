---
title: Starting an Executable When a Task is Registered
description: Writing a task that starts an executable when a task is registered is done by defining a registration trigger and an executable action.
ms.assetid: 426fa79d-7f0d-42fb-a8c4-15981d13be71
keywords:
- Task Scheduler examples Task Scheduler , registration trigger
ms.topic: article
ms.date: 05/31/2018
---

# Starting an Executable When a Task is Registered

Writing a task that starts an executable when a task is registered is done by defining a registration trigger and an executable action.

## Registration Trigger

Registration triggers start a task as soon as it is registered. You can also specify a delay for the registration trigger, which starts a task after a specific amount of time (the delay) after the task is registered. The delay is specified in the [**Delay**](/windows/desktop/api/taskschd/nf-taskschd-iregistrationtrigger-get_delay) property of the [**IRegistrationTrigger**](/windows/desktop/api/taskschd/nn-taskschd-iregistrationtrigger) interface ([**RegistrationTrigger**](registrationtrigger.md) for scripting).

> [!Note]  
> When a task with a registration trigger is updated, the task will execute after the update occurs.

 

## Registration Trigger Examples

The following examples start Notepad when a task is registered:

-   [Registration Trigger Example (Scripting)](registration-trigger-example--scripting-.md)
-   [Registration Trigger Example (C++)](registration-trigger-example--c---.md)
-   [Registration Trigger Example (XML)](registration-trigger-example--xml-.md)

## Related topics

<dl> <dt>

[Using the Task Scheduler](using-the-task-scheduler.md)
</dt> </dl>

 

 




