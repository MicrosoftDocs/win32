---
Description: Microsoft Corporation
ms.assetid: '42aaf4ab-2727-42a9-ad37-ed898b03415d'
title: 'Fast User Switching: Issues for Assistive Technology Vendors'
---

# Fast User Switching: Issues for Assistive Technology Vendors

Microsoft Corporation

November 2001

**Summary:** This article discusses how Fast User Switching, a feature supported by Windows XP, affects various Assistive Technology issues. (4 printed pages)

-   [Introduction](#introduction)
-   [Impact on Assistive Technology Vendors](#impact-on-assistive-technology-vendors)
    -   [ATV Scenario](#atv-scenario)
-   [Solutions](#solutions)
    -   [Run Assistive Technology Main Module as a Windows Service](#run-assistive-technology-main-module-as-a-windows-service)
    -   [Do Not Run Windows Services](#do-not-run-windows-services)
    -   [Do Not Use Fast User Switching](#do-not-use-fast-user-switching)
-   [Known Issues](#known-issues)
-   [Additional Reading](#additional-reading)

## Introduction

Microsoft Windows XP supports Fast User Switching, an innovative feature that enables multiple users to log on to one system at the same time and switch quickly between their open accounts. Each session is a separate user environment, complete with its own profile and settings. Fast User Switching is implemented using Terminal Services. Applications that rely on custom services or drivers will require additional code to support this feature.

Assistive technology vendors (ATVs) should note the following key elements of Fast User Switching:

-   Windows services do not run in any session other than Session 0.
-   The friendly logon screen used to switch out of Session 0 still runs inside Session 0. Windows services can still run in this friendly logon screen; however, as soon as the switch occurs, the user is running in another session. Unless the service has been written with the explicit knowledge of sessions, any application depending on the service will fail.
-   The user who runs Session 0 is non-deterministic. The first user to log on after a computer is restarted runs Session 0. The next user runs Session 1, and so on. When the first user logs off, the next user to log on will pick up Session 0.
-   Hardware resources such as ports and sound cards need to be managed carefully. Because all sessions are open simultaneously, hardware resource contention can result. Audio is redirected on every session switch; therefore a reinitialization delay may occur.
-   If assistive technology software is running in a session that is not active, the software can still perform different processing tasks. Optimization can be made to suspend processing when a session is not active.

## Impact on Assistive Technology Vendors

Applications that rely on user mode drivers can take advantage of Fast User Switching without requiring special device management.

If you want an application that requires custom services or drivers to support Fast User Switching, be sure that the system notifies the application of session switching. This will allow the application to manage these drivers and services when it is not running under the current session. The application programming interface (API) [**WTSRegisterSessionNotification**](https://msdn.microsoft.com/library/aa383841) allows applications to register and notifies the hWnd when a session switch occurs. When a session is either connected or disconnected from a computer, the windows message WM\_WTSESSION\_CHANGE is sent to the hWnd that is registered to be notified.

The *wParam* value is used to inform applications whether the connection is remote or on the console. Console sessions indicate that a session switch is occurring on the current machine. The *wParam* value can have one of the following values.



| Value                    | Meaning                                              |
|--------------------------|------------------------------------------------------|
| WTS\_CONSOLE\_CONNECT    | A session was connected to the console session.      |
| WTS\_CONSOLE\_DISCONNECT | A session was disconnected from the console session. |
| WTS\_REMOTE\_CONNECT     | A session was connected to the remote session.       |
| WTS\_REMOTE\_DISCONNECT  | A session was disconnected from the remote session.  |
| WTS\_SESSION\_LOGON      | A user has logged on to the session.                 |
| WTS\_SESSION\_LOGOFF     | A user has logged off of the session.                |
| WTS\_SESSION\_LOCK       | A session has been locked.                           |
| WTS\_SESSION\_UNLOCK     | A session has been unlocked.                         |



 

The *lParam* value will indicate the identifier of the session that is being given the console; applications will also need to verify that the session they are running under is the session that is being asked to connect to the console before establishing a link to drivers or services.

### ATV Scenario

The following scenario describes an example of a problem that ATVs may encounter with Fast User Switching. Assume that the SerialKey module is running as a Windows service.

1.  User 1 logs on. Session 0 is active. SerialKey, running as a Windows service, gets data from the COM port and calls [**SendInput**](https://msdn.microsoft.com/library/windows/desktop/ms646310) to simulate key input into the active application in Session 0.
2.  User 2 uses the friendly logon screen to try to switch the session. The SerialKey Windows service continues to run properly.
3.  After User 2 switches the session to Session 1, the SerialKey Windows service is still running in Session 0. The SerialKey service is not in Session 1, and User 2 is unable to use SerialKey.

## Solutions

The following three solutions are available for ATVs.

-   [Run Assistive Technology Main Module as a Windows Service](#run-assistive-technology-main-module-as-a-windows-service)
-   [Do Not Run Windows Services](#do-not-run-windows-services)
-   [Do Not Use Fast User Switching](#do-not-use-fast-user-switching)

### Run Assistive Technology Main Module as a Windows Service

The assistive technology main module runs as a Windows service in Session 0. Services run in Session 0. They can create processes in other sessions to execute other code and they can communicate with those processes such as named pipes. SerialKey, for example, could be updated to work in any session.

### Do Not Run Windows Services

If the assistive technology does not require access to the friendly logon screen, the assistive technology can provide a solution without running services. The assistive technology application must be launched when a session is started. The application in a given session will need to be notified that its session is being switched in or switched away so that it knows when to release or regain control of resources such as ports and other hardware.

### Do Not Use Fast User Switching

An ATV can instruct the user to turn off Fast User Switching.

## Known Issues

The following section lists issues that some ATVs have experienced with Fast User Switching.

**Issue**: A screen reader that is running on Session 1 closes when the user switches to Session 2. When the user switches back to Session 1, the screen reader turns on but the user sees a blank screen.

**Solution**: Check internal flag settings in the assistive technology software. The following two scenarios depict an assistive technology application functioning correctly:

-   Scenario 1: User 1 logs on and starts an assistive technology application in Session 1. User 2 logs on and begins Session 2. As soon as the assistive technology detects the session switch event, it turns off for Session 1. User 2 finishes Session 2, and User 1 switches back to Session 1. As soon as the assistive technology detects the session switch event, it turns on for Session 1.
-   Scenario 2: User 1 logs on and starts an assistive technology application in Session 1. User 2 logs on. As soon as the assistive technology detects the session switch event, it turns off in Session 1. User 2 starts the assistive technology in Session 2. When User 1 switches back to Session 1, the assistive technology turns off in Session 2 and switches on in Session 1.

**Issue**: After installing a screen reader and logging on as User 1, the session switches to User 2, the screen becomes blank, and the keyboard is unresponsive. Users must restart the computer at this point.

**Solution**: Fast User Switching is a new technology that will require new programming considerations. For more information, please see [Microsoft Windows XP Fast User Switching: Design Guide for Building Business Applications](http://go.microsoft.com/fwlink/p/?linkid=209213).

**Issue:** How can you be aware of sessions so that you can release resources when a session has become inactive?

**Solution**: Fast User Switching is a new technology that will require new programming considerations. For more information, please see [Microsoft Windows XP Fast User Switching: Design Guide for Building Business Applications](http://go.microsoft.com/fwlink/p/?linkid=209213).

## Additional Reading

For more information about Fast User Switching and related technologies, see [Microsoft Windows XP Fast User Switching: Design Guide for Building Business Applications](http://go.microsoft.com/fwlink/p/?linkid=209213). Also try searching [MSDN](http://go.microsoft.com/fwlink/p/?linkid=147527) for other articles about Fast User Switching.

 

 



