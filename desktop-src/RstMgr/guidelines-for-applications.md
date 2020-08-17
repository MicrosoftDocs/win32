---
title: Guidelines for Applications
description: Applications running on Windows Vista and Windows Server 2008 should adhere to these guidelines to ensure that the Restart Manager can shut down and restart applications if necessary to install updates.
ms.assetid: 97b1df63-65a9-47b4-891b-e4a754882b89
ms.topic: article
ms.date: 05/31/2018
---

# Guidelines for Applications

Applications running on Windows Vista and Windows Server 2008 should adhere to these guidelines to ensure that the Restart Manager can shut down and restart applications if necessary to install updates. Services can use the guidelines that are described in [Guidelines for Services](guidelines-for-services.md).

-   The Restart Manager queries GUI applications for shutdown by sending a [**WM\_QUERYENDSESSION**](/windows/desktop/Shutdown/wm-queryendsession) notification that has the *lParam* parameter set to **ENDSESSION\_CLOSEAPP** (0x1). Applications should not shut down when they receive a **WM\_QUERYENDSESSION** message because another application may not be ready to shut down. GUI applications should listen for the **WM\_QUERYENDSESSION** message and return a value of **TRUE** if the application is prepared to shut down and restart. If no application returns a value of **FALSE**, the Restart Manager sends a [**WM\_ENDSESSION**](/windows/desktop/Shutdown/wm-endsession) message with the *lParam* parameter set to **ENDSESSION\_CLOSEAPP** (0x1) and the *wparam* parameter set to **TRUE**. Applications should shut down only when they receive the **WM\_ENDSESSION** message. The Restart Manager also sends a [**WM\_CLOSE**](../winmsg/wm-close.md) message for GUI applications that do not shut down on receiving **WM\_ENDSESSION**. If any GUI application responds to a **WM\_QUERYENDSESSION** message by returning a value of **FALSE**, the shutdown is canceled. However, if the shutdown is forced, the application is terminated regardless.
-   When a GUI application receives a [**WM\_ENDSESSION**](/windows/desktop/Shutdown/wm-endsession) message, the application should prepare itself to shut down within the specified timeout period. At a minimum, applications should prepare by saving any user data and state information that is needed after a restart. It is recommended that applications periodically save the user data and state.
-   The Restart Manager sends a **CTRL\_C\_EVENT** notification to console applications that must be shut down and restarted. When a console application receives a **CTRL\_C\_EVENT** notification, the application should take actions necessary to prepare for a shutdown within the specified timeout period. At a minimum, console applications should define a [*HandlerRoutine*](/windows/console/handlerroutine) function to handle the **CTRL\_C\_EVENT** notification and should save any user data and state information that is going to be needed after a restart. It is recommended that applications periodically save the user data and state.
-   If any applications do not shut down in response to the shutdown messages, installers can use the **RmForceShutdown** option of the [**RmShutdown**](/windows/desktop/api/RestartManager/nf-restartmanager-rmshutdown) function to force the applications to shut down. When the installer specifies a forced shutdown, Restart Manager attempts to shut down the applications cleanly by sending the shutdown messages, but will force them shut if this fails. GUI applications and console applications can be forced to shut down to enable the installation of a critical security update. Because this can result in data loss, applications should handle the shutdown messages and shut down cleanly when required.
-   Applications should register for a restart by using the [**RegisterApplicationRestart**](/windows/desktop/api/winbase/nf-winbase-registerapplicationrestart) function. Restart Manager can only restart applications that have been registered for restart. This is the only way that the Restart Manager can determine the command-line command to use when restarting the application. If the application must reopen with some saved state or data, that information must be included in the command-line command that is registered for the application.
    > [!Note]  
    > If the restarted application must run in the same directory it ran in before being shut down, the application must save the directory information and then change to the directory after restarting.

     

    > [!Note]  
    > The [**RmRestart**](/windows/desktop/api/RestartManager/nf-restartmanager-rmrestart) function does not restart applications that do not run as the currently-logged on user. For example, the **RmRestart** function does not restart applications started with the **Run As** command that do not run as the currently-logged on user. These applications must be manually restarted.

     

-   When Restart Manager determines that a system restart is required to install an update, it does not shut down any applications and services. Instead, it leaves this to the installer to decide when to schedule a system restart and install the update. Installers can reduce the disruption to users caused by updates that require a system restart by using the [**ExitWindowsEx**](/windows/desktop/api/winuser/nf-winuser-exitwindowsex) function with the **EWX\_RESTARTAPPS** flag or the [**InitiateShutdown**](/windows/desktop/api/winreg/nf-winreg-initiateshutdowna) function with the **SHUTDOWN\_RESTARTAPPS** flag. Using these flags ensures that applications registered for restart are restarted after a system reboot, which minimizes the impact on the user.

 

 