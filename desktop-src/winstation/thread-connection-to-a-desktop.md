---
title: Thread Connection to a Desktop
description: After a process connects to a window station, the system assigns a desktop to the thread making the connection.
ms.assetid: 45016619-ed11-4b0c-84e3-f8662553c64d
ms.topic: article
ms.date: 05/31/2018
---

# Thread Connection to a Desktop

After a process connects to a window station, the system assigns a desktop to the thread making the connection. The system determines the desktop to assign to the thread according to the following rules:

1.  If the thread has called the [**SetThreadDesktop**](/windows/win32/api/winuser/nf-winuser-setthreaddesktop) function, it connects to the specified desktop.
2.  If the thread did not call [**SetThreadDesktop**](/windows/win32/api/winuser/nf-winuser-setthreaddesktop), it connects to the desktop inherited from the parent process.
3.  If the thread did not call [**SetThreadDesktop**](/windows/win32/api/winuser/nf-winuser-setthreaddesktop) and did not inherit a desktop, the system attempts to open for MAXIMUM\_ALLOWED access and connect to a desktop as follows:
    -   If a desktop name was specified in the **lpDesktop** member of the [**STARTUPINFO**](/windows/desktop/api/processthreadsapi/ns-processthreadsapi-startupinfoa) structure that was used when the process was created, the thread connects to the specified desktop.
    -   Otherwise, the thread connects to the default desktop of the window station to which the process connected.

The desktop assigned during this connection process cannot be closed by calling the [**CloseDesktop**](/windows/win32/api/winuser/nf-winuser-closedesktop) function.

When a process is connecting to a desktop, the system searches the process's handle table for inherited handles. The system uses the first desktop handle it finds. If you want a child process to connect to a particular inherited desktop, you must ensure that the only the desired handle is marked inheritable. If a child process inherits multiple desktop handles, the results of the desktop connection are undefined.

Handles to a desktop that the system opens while connecting a process to a desktop are not inheritable.

## Related topics

<dl> <dt>

[Process Connection to a Window Station](process-connection-to-a-window-station.md)
</dt> </dl>

 

 