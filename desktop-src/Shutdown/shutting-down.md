---
description: There are three ways for an application to shut down local or remote computers:shut down the systemshut down the system and restart itshut down the application, shut down and restart the system, and restart any applications that have been registered for restart
ms.assetid: acadf58f-3f68-4fa1-bdcf-8f85c8479263
title: Shutting Down
ms.topic: article
ms.date: 05/31/2018
---

# Shutting Down

There are three ways for an application to shut down local or remote computers:

-   shut down the system
-   shut down the system and restart it
-   shut down the application, shut down and restart the system, and restart any applications that have been registered for restart

To shut down the system, use the [**ExitWindowsEx**](/windows/desktop/api/Winuser/nf-winuser-exitwindowsex) function with the EWX\_SHUTDOWN flag. For an example, see [How to Shut Down the System](how-to-shut-down-the-system.md). To shut down and restart the system, use the EWX\_REBOOT flag. To restart any applications that have been registered for restart using the [**RegisterApplicationRestart**](/windows/win32/api/winbase/nf-winbase-registerapplicationrestart) function, use the EXW\_RESTARTAPPS flag.

The [**InitiateShutdown**](/windows/desktop/api/Winreg/nf-winreg-initiateshutdowna), [**InitiateSystemShutdown**](/windows/desktop/api/Winreg/nf-winreg-initiatesystemshutdowna), and [**InitiateSystemShutdownEx**](/windows/desktop/api/Winreg/nf-winreg-initiatesystemshutdownexa) functions start a timer and display a dialog box that prompts the user to log off. While this dialog box is displayed, the [**AbortSystemShutdown**](/windows/desktop/api/Winreg/nf-winreg-abortsystemshutdowna) function can stop the timer and prevent the computer from shutting down. However, if the timer expires, the computer is shut down. These functions can also restart the computer following a shutdown operation. For more information, see [Displaying the Shutdown Dialog Box](displaying-the-shutdown-dialog-box.md).

## Shutdown Notifications

Applications with a window and message queue receive shutdown notifications through the [**WM\_QUERYENDSESSION**](wm-queryendsession.md) and [**WM\_ENDSESSION**](wm-endsession.md) messages. These applications should return **TRUE** to indicate that they can be terminated. Applications should not block system shutdown unless it is absolutely necessary. Applications should perform any required cleanup while processing **WM\_ENDSESSION**. Applications that have unsaved data could save the data to a temporary location and restore it the next time the application starts. It is recommended that applications save their data and state frequently; for example, automatically save data between save operations initiated by the user to reduce the amount of data to be saved at shutdown.

Console applications receive shutdown notifications in their handler routines. To register a console handler, use the [**SetConsoleCtrlHandler**](/windows/console/setconsolectrlhandler) function.

Service applications receive shutdown notifications in their handler routines. To register a service control handler, use the [**RegisterServiceCtrlHandlerEx**](/windows/win32/api/winsvc/nf-winsvc-registerservicectrlhandlerexa) function.

## Blocking Shutdown

If an application must block a potential system shutdown, it can call the [**ShutdownBlockReasonCreate**](/windows/desktop/api/Winuser/nf-winuser-shutdownblockreasoncreate) function. The caller provides a reason string that will be displayed to the user. The reason string should be short and clear, providing the user with the information necessary to decide whether to continue shutting down the system.

## Related topics

<dl> <dt>

[How to Shut Down the System](how-to-shut-down-the-system.md)
</dt> </dl>

 

 
