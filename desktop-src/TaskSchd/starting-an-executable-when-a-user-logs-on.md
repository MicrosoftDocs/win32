---
title: Starting an Executable When a User Logs On
description: Writing a task that starts an executable when a user logs on is done by defining a logon trigger and an executable action.
ms.assetid: 0c5912aa-913d-42ce-a01b-b1359b49bb2f
keywords:
- Task Scheduler examples Task Scheduler , logon trigger
ms.topic: article
ms.date: 05/31/2018
---

# Starting an Executable When a User Logs On

Writing a task that starts an executable when a user logs on is done by defining a logon trigger and an executable action.

## Logon Trigger

Logon triggers are activated by their start boundary but they do not start the executable until a specified user logs on. You can specify the logon trigger to start when a certain user logs on by specifying the user in the [**UserId**](/windows/desktop/api/taskschd/nf-taskschd-ilogontrigger-get_userid) property of the [**ILogonTrigger**](/windows/desktop/api/taskschd/nn-taskschd-ilogontrigger) interface ([**LogonTrigger**](logontrigger.md) for scripting).

## LogonTrigger Examples

The following examples start Notepad after a user logs on.

-   [Logon Trigger Example (Scripting)](logon-trigger-example--scripting-.md)
-   [Logon Trigger Example (C++)](logon-trigger-example--c---.md)
-   [Logon Trigger Example (XML)](logon-trigger-example--xml-.md)

## Related topics

<dl> <dt>

[Using the Task Scheduler](using-the-task-scheduler.md)
</dt> </dl>

 

 




