---
description: Typically, services are console applications that are designed to run unattended without a graphical user interface (GUI).
ms.assetid: 3d6e090a-00b1-47d8-a4fb-620f3db8ba9c
title: Interactive Services
ms.topic: article
ms.date: 05/31/2018
---

# Interactive Services

Typically, services are console applications that are designed to run unattended without a graphical user interface (GUI). However, some services may require occasional interaction with a user. This page discusses the best ways to interact with the user from a service.

> [!IMPORTANT]
> Services cannot directly interact with a user as of Windows Vista. Therefore, the techniques mentioned in the section titled Using an Interactive Service should not be used in new code.

 

## Interacting with a User from a Service Indirectly

You can use the following techniques to interact with the user from a service on all supported versions of Windows:

-   Display a dialog box in the user's session using the [**WTSSendMessage**](/windows/desktop/api/wtsapi32/nf-wtsapi32-wtssendmessagea) function.
-   Create a separate hidden GUI application and use the [**CreateProcessAsUser**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessasusera) function to run the application within the context of the interactive user. Design the GUI application to communicate with the service through some method of interprocess communication (IPC), for example, named pipes. The service communicates with the GUI application to tell it when to display the GUI. The application communicates the results of the user interaction back to the service so that the service can take the appropriate action. Note that IPC can expose your service interfaces over the network unless you use an appropriate access control list (ACL).

    If this service runs on a multiuser system, add the application to the following key so that it is run in each session: **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run**. If the application uses named pipes for IPC, the server can distinguish between multiple user processes by giving each pipe a unique name based on the session ID.

The following technique is also available for Windows Server 2003 and Windows XP:

-   Display a message box by calling the [**MessageBox**](/windows/win32/api/winuser/nf-winuser-messagebox) function with **MB\_SERVICE\_NOTIFICATION**. This is recommended for displaying simple status messages. Do not call **MessageBox** during service initialization or from the [**HandlerEx**](/windows/desktop/api/WinSvc/nc-winsvc-lphandler_function_ex) routine, unless you call it from a separate thread, so that you return to the SCM in a timely manner.

## Using an Interactive Service

By default, services use a noninteractive [window station](/windows/desktop/winstation/window-stations) and cannot interact with the user. However, an *interactive service* can display a user interface and receive user input.

> [!Caution]  
> Services running in an elevated security context, such as the LocalSystem account, should not create a window on the interactive desktop because any other application that is running on the interactive desktop can interact with this window. This exposes the service to any application that a logged-on user executes. Also, services that are running as LocalSystem should not access the interactive desktop by calling the [**OpenWindowStation**](/windows/desktop/api/winuser/nf-winuser-openwindowstationa) or [**GetThreadDesktop**](/windows/desktop/api/winuser/nf-winuser-getthreaddesktop) function.

 

To create an interactive service, do the following when calling the [**CreateService**](/windows/desktop/api/Winsvc/nf-winsvc-createservicea) function:

1.  Specify NULL for the *lpServiceStartName* parameter to run the service in the context of the [LocalSystem account](localsystem-account.md).
2.  Specify the **SERVICE\_INTERACTIVE\_PROCESS** flag.

To determine whether a service is running as an interactive service, call the [**GetProcessWindowStation**](/windows/desktop/api/winuser/nf-winuser-getprocesswindowstation) function to retrieve a handle to the window station, and the [**GetUserObjectInformation**](/windows/desktop/api/winuser/nf-winuser-getuserobjectinformationa) function to test whether the window station has the **WSF\_VISIBLE** attribute.

However, note that the following registry key contains a value, **NoInteractiveServices**, that controls the effect of SERVICE\_INTERACTIVE\_PROCESS:

**HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Windows**

The **NoInteractiveServices** value defaults to 1, which means that no service is allowed to run interactively, regardless of whether it has **SERVICE\_INTERACTIVE\_PROCESS**. When **NoInteractiveServices** is set to a 0, services with **SERVICE\_INTERACTIVE\_PROCESS** are allowed to run interactively.

**Windows 7, Windows Server 2008 R2, Windows XP and Windows Server 2003:** The **NoInteractiveServices** value defaults to 0, which means that services with **SERVICE\_INTERACTIVE\_PROCESS** are allowed to run interactively. When **NoInteractiveServices** is set to a nonzero value, no service started thereafter is allowed to run interactively, regardless of whether it has **SERVICE\_INTERACTIVE\_PROCESS**.

> [!IMPORTANT]
> All services run in Terminal Services session 0. Therefore, if an interactive service displays a user interface, it is visible only to the user who connected to session 0. Because there is no way to guarantee that the interactive user is connected to session 0, do not configure a service to run as an interactive service under Terminal Services or on a system that supports fast user switching (fast user switching is implemented using Terminal Services).

 

 

 
