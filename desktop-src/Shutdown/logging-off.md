---
description: The ExitWindows function logs off the current user. You can also call the ExitWindowsEx function with the EXW\_LOGOFF flag.
ms.assetid: 906d92f1-7cbe-454e-9c71-34b4383aebab
title: Logging Off
ms.topic: article
ms.date: 05/31/2018
---

# Logging Off

The [**ExitWindows**](/windows/desktop/api/Winuser/nf-winuser-exitwindows) function logs off the current user. You can also call the [**ExitWindowsEx**](/windows/desktop/api/Winuser/nf-winuser-exitwindowsex) function with the EXW\_LOGOFF flag.

By default, when an application uses [**ExitWindows**](/windows/desktop/api/Winuser/nf-winuser-exitwindows) or [**ExitWindowsEx**](/windows/desktop/api/Winuser/nf-winuser-exitwindowsex) to log off, the system sends the [**WM\_QUERYENDSESSION**](wm-queryendsession.md) message to each window. Applications agree to terminate by returning **TRUE** when they receive this message. If any application returns **FALSE** when processing this message, the log-off operation is canceled. If your application handles the **WM\_QUERYENDSESSION** message, you can allow the user to cancel the log-off operation, even if another application or the system originated the end-session request. For an example, see [How to Log Off the Current User](how-to-log-off-the-current-user.md).

When an application returns **TRUE** for [**WM\_QUERYENDSESSION**](wm-queryendsession.md), it receives the [**WM\_ENDSESSION**](wm-endsession.md) message and it is terminated, regardless of how the other applications respond to the **WM\_QUERYENDSESSION** message.

To force all applications to terminate, use [**ExitWindowsEx**](/windows/desktop/api/Winuser/nf-winuser-exitwindowsex), and specify the EXW\_FORCE flag. This prevents the system from sending [**WM\_QUERYENDSESSION**](wm-queryendsession.md) messages.

The system also sends the CTRL\_LOGOFF\_EVENT control signal to every process during a log-off operation. A console application can register a [**HandlerRoutine**](/windows/console/handlerroutine) to process these messages.

If the process that called [**ExitWindowsEx**](/windows/desktop/api/Winuser/nf-winuser-exitwindowsex) is running in the logon session of the interactive user, all processes in the logon session are terminated. If the process calling **ExitWindowsEx** is in some other logon session, only the notifications are made; no processes are terminated.

## Related topics

<dl> <dt>

[How to Log Off the Current User](how-to-log-off-the-current-user.md)
</dt> </dl>

 

 
