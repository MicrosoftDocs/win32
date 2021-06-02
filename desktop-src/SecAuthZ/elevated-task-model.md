---
description: An application running as a standard user performs operations that require administrator privilege by starting a scheduled task.
ms.assetid: cd7485b3-6be5-4163-9a86-7892dbc59181
title: Elevated Task Model
ms.topic: article
ms.date: 05/31/2018
---

# Elevated Task Model

In the elevated task model, an application running as a standard user performs operations that require administrator privilege by starting a scheduled task.

**Windows Server 2003 and Windows XP:** The elevated task model is not supported.

Tasks do not consume as many system resources as services, and tasks automatically close when finished. Consider using this model instead of the [Operating System Service Model](operating-system-service-model.md) unless backward compatibility with earlier operating systems is necessary.

To use a task to perform privileged operations for a standard user application, the following conditions must be met:

-   The task must be set to run as **SYSTEM**.
-   The [*security descriptor*](/windows/desktop/SecGloss/s-gly) associated with the task must be configured to allow standard users to start the task.
-   The task scheduler service must be running.

For information about how to create and start tasks, see [Task Scheduler](/windows/desktop/TaskSchd/task-scheduler-start-page).

## Related topics

<dl> <dt>

[Developing Applications that Require Administrator Privilege](developing-applications-that-require-administrator-privilege.md)
</dt> <dt>

[Administrator Broker Model](administrator-broker-model.md)
</dt> <dt>

[Administrator COM Object Model](administrator-com-object-model.md)
</dt> <dt>

[Operating System Service Model](operating-system-service-model.md)
</dt> </dl>

 

 
