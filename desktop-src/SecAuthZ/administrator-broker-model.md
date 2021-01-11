---
description: The application is divided into two programs. One of the programs runs as a standard user, and the other runs with administrator privilege.
ms.assetid: 1e661915-5797-421d-b96f-72949f441aba
title: Administrator Broker Model
ms.topic: article
ms.date: 05/31/2018
---

# Administrator Broker Model

In the administrator broker model, the application is divided into two programs. One of the programs runs as a standard user, and the other runs with administrator privilege.

Using an application manifest, mark the standard user program with a **requestedExecutionLevel** of **asInvoker** and mark the administrative program with a **requestedExecutionLevel** of **requireAdministrator**. A user launches the standard user program first. When the user attempts to perform an operation that requires a full administrator access token, the standard user program calls the [**ShellExecute**](/windows/desktop/api/shellapi/nf-shellapi-shellexecutea) function to launch the administrative program. The **ShellExecute** function prompts the user for approval before running the application with the user's full administrator access token. The administrative program can then perform tasks that require administrator privilege.

The administrative program is not completely isolated from the standard user program. The administrative program can enable interprocess communication with the standard user program. However, such communication is limited by the default mandatory integrity policy. For information about mandatory integrity considerations, see [Designing Applications to Run at a Low Integrity Level](/previous-versions/dotnet/articles/bb625960(v=msdn.10)).

The following are possible uses for the administrator broker model:

-   Developing wizards. When a hardware wizard determines that a required driver is not installed on the computer or located in the enterprise's approved location, it calls an elevated application with the ability to move a driver into the computer store.
-   Autorun.exe calling Setup.exe. When a user runs software from a CD, Autorun.exe, which runs as a standard user, starts Setup.exe, which runs as an administrator, to install the software onto the computer.

The following are drawbacks to using the administrator broker model:

-   The transitions from application to application can be confusing to the user. It can be difficult to inform the user why a new application appears on the monitor.
-   It can be difficult to pass state information between the two applications. For example, you would not use this model to pass state information between a standard user control panel (CPL) and its administrator counterpart simply to allow the same CPL to have administrative and standard user functionality. The standard user CPL would have to store its state somewhere.
-   There can be a lot of replicated code when splitting the functionality between two programs.

## Related topics

<dl> <dt>

[Developing Applications that Require Administrator Privilege](developing-applications-that-require-administrator-privilege.md)
</dt> <dt>

[Administrator COM Object Model](administrator-com-object-model.md)
</dt> <dt>

[Operating System Service Model](operating-system-service-model.md)
</dt> <dt>

[Elevated Task Model](elevated-task-model.md)
</dt> </dl>

 

 
