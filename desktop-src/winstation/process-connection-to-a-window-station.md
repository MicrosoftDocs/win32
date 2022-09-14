---
title: Process Connection to a Window Station
description: A process automatically establishes a connection to a window station and desktop when it first calls a USER32 or GDI32 function (other than the window station and desktop functions).
ms.assetid: 280f69e7-5c99-41a7-94e3-da13deaac9f5
ms.topic: article
ms.date: 05/31/2018
---

# Process Connection to a Window Station

A process automatically establishes a connection to a window station and desktop when it first calls a USER32 or GDI32 function (other than the window station and desktop functions). The system determines the window station to which a process connects according to the following rules:

1.  If the process has called the [**SetProcessWindowStation**](/windows/win32/api/winuser/nf-winuser-setprocesswindowstation) function, it connects to the window station specified in that call.
2.  If the process did not call [**SetProcessWindowStation**](/windows/win32/api/winuser/nf-winuser-setprocesswindowstation), it connects to the window station inherited from the parent process.
3.  If the process did not call [**SetProcessWindowStation**](/windows/win32/api/winuser/nf-winuser-setprocesswindowstation) and did not inherit a window station, the system attempts to open for MAXIMUM\_ALLOWED access and connect to a window station as follows:
    -   If a window station name was specified in the **lpDesktop** member of the [**STARTUPINFO**](/windows/desktop/api/processthreadsapi/ns-processthreadsapi-startupinfoa) structure that was used when the process was created, the process connects to the specified window station.
    -   Otherwise, if the process is running in the logon session of the interactive user, the process connects to the interactive window station.
    -   If the process is running in a noninteractive logon session, the window station name is formed based on the logon session identifier and an attempt is made to open that window station. If the open operation fails because this window station does not exist, the system tries to create the window station and a default desktop.

The window station assigned during this connection process cannot be closed by calling the [**CloseWindowStation**](/windows/win32/api/winuser/nf-winuser-closewindowstation) function.

When a process is connecting to a window station, the system searches the process's handle table for inherited handles. The system uses the first window station handle it finds. If you want a child process to connect to a particular inherited window station, you must ensure that only the desired handle is marked inheritable. If a child process inherits multiple window station handles, the results of the window station connection are undefined.

Handles to a window station that the system opens while connecting a process to a window station are not inheritable.

## Related topics

<dl> <dt>

[Thread Connection to a Desktop](thread-connection-to-a-desktop.md)
</dt> </dl>

 

 