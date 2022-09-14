---
description: Windows XP user accounts enable multiple users to be logged on simultaneously, each with his or her own settings and each running his or her own applications.
ms.assetid: bc404afc-f73e-404d-854d-faab5cf205a5
title: User Accounts with Fast User Switching and Remote Desktop
ms.topic: article
ms.date: 05/31/2018
---

# User Accounts with Fast User Switching and Remote Desktop

Windows XP user accounts enable multiple users to be logged on simultaneously, each with his or her own settings and each running his or her own applications. Because one user does not have to log off to allow access to another user, each user's desktop is easily accessed using the fast user switching feature. User accounts also include the Personal Terminal Server feature, or Remote Desktop, which enables users to access their desktop account from remote systems.

The following topics are discussed.

-   [Infrastructure Usage Requirements](#infrastructure-usage-requirements)
-   [Compatibility with Existing Applications](#compatibility-with-existing-applications)
-   [Registering for Session Switching Notification](#registering-for-session-switching-notification)
-   [Ensuring Only One Instance of Your Application Is Running](#ensuring-only-one-instance-of-your-application-is-running)
-   [Shutting Down Your Application Across All Sessions](#shutting-down-your-application-across-all-sessions)
-   [Interaction with System Services](#interaction-with-system-services)
-   [Remote Desktop and Bandwidth](#remote-desktop-and-bandwidth)

## Infrastructure Usage Requirements

Underlying infrastructure inherited from Windows 2000 supports state separation of user data, user settings, and computer settings. Taking advantage of this infrastructure, the following are required to successfully run your application under Windows XP.

-   Default to the **My Documents** folder for storage of user-created data.
-   Classify and store application data correctly.
-   Degrade gracefully on "Access Denied" messages.

Temporary files, memory-mapped files, and documents should all be stored in the appropriate subdirectory of the user's profile directory. Use [**SHGetFolderLocation**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetfolderlocation) or [**SHGetFolderPath**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetfolderpatha) to determine the appropriate storage location for these files. Passing the [**CSIDL\_APPDATA**](csidl.md) flag to these functions returns the path of a file system directory that serves as a common repository for application-specific data. Use the flag [**CSIDL\_LOCAL\_APPDATA**](csidl.md) in place of **CSIDL\_APPDATA** for data that should change when the user changes, such as temporary files.

The requirements listed above are a subset of those in the Microsoft Certification program. For more information, see the **Certified for Windows Program** page at https://www.microsoft.com/windowsserver2003/partners/isvs/cfw.mspx.

## Compatibility with Existing Applications

Both fast user switching and Personal Terminal Server use Terminal Services technology and therefore are compatible with most earlier Microsoft Win32 applications. If an application is Windows 2000 Logo compliant, implementing basic profile separation and power management features, that application should run properly under individual Windows XP user accounts.

## Registering for Session Switching Notification

Typically, an application does not need to be notified when a desktop switch occurs. However, applications that must be notified when the account under which they are running is the current desktop, such as applications that access the serial port or other shared resources, can register for desktop switch notification. To register for a notification, use the [**WTSRegisterSessionNotification**](/windows/win32/api/wtsapi32/nf-wtsapi32-wtsregistersessionnotification) function.

Once that function has been called, the window with handle *hWnd* is registered to receive a [**WM\_WTSSESSION\_CHANGE**](../termserv/wm-wtssession-change.md) message through its **WndProc** function. The session ID is sent in the **lParam** parameter, and a code that indicates the event that generated the message is sent in **wParam** as one of the following flags.

-   WTS\_CONSOLE\_CONNECT
-   WTS\_CONSOLE\_DISCONNECT
-   WTS\_REMOTE\_CONNECT
-   WTS\_REMOTE\_DISCONNECT
-   WTS\_SESSION\_LOGOFF
-   WTS\_SESSION\_LOGON

Applications can use this message to track their state, as well as to release and acquire console-specific resources. User desktops can be dynamically switched between remote and console control. Applications should use the [**WM\_WTSSESSION\_CHANGE**](../termserv/wm-wtssession-change.md) message to synchronize with the remote or local connection state.

When your process no longer requires these notifications or is terminating, it should call [**WTSUnRegisterSessionNotification**](/windows/win32/api/wtsapi32/nf-wtsapi32-wtsunregistersessionnotification) to unregister its notification.

> [!IMPORTANT]
> The **hWnd** values passed to [**WTSRegisterSessionNotification**](/windows/win32/api/wtsapi32/nf-wtsapi32-wtsregistersessionnotification) are reference counted, so you must make an equal number of calls to [**WTSUnRegisterSessionNotification**](/windows/win32/api/wtsapi32/nf-wtsapi32-wtsunregistersessionnotification) to ensure the release of all allocated resources.

 

## Ensuring Only One Instance of Your Application Is Running

Many applications must ensure that they have only one instance running. There are several ways to do this in Windows XP. Among them are the following:

-   Use [**FindWindow**](/windows/win32/api/winuser/nf-winuser-findwindowa) or [**FindWindowEx**](/windows/win32/api/winuser/nf-winuser-findwindowexa) to search for a known window that your application opens. If that window is already open, you can use that as an indication that the application is already running.
-   Create a mutex or semaphore object when your application is opened, and close that object when the application terminates. The global object namespace is separated for each desktop, allowing a unique list of mutex and semaphore objects for each.

## Shutting Down Your Application Across All Sessions

An application might need to shut itself down across all sessions. For example, an application running in two or more sessions simultaneously might download a new file from the web. Then it might need to close itself and restart with the updated bits. This, of course, would need to be done in all running sessions. Your application should be written so that it exits cleanly when a notification is received.

## Interaction with System Services

From a programmatic standpoint, the following cases need to be addressed.

-   The server process receives a direct request from a client process.

    In this case, the message is probably transmitted using a local procedure call (LPC) or a remote procedure call (RPC). There are APIs for either LPC or RPC that enable retrieval of the client token. Once the client token is obtained, the server can use it in a call to [**CreateProcessAsUser**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessasusera). This brings up the process on the correct window station, assuming that the client user token has a session tag, which it should.

    > [!Note]  
    > [**CreateProcessAsUser**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessasusera) does not support handle inheritance across sessions at this time.

     

-   The server process receives a notification and needs to display the UI, but the display does not have to be in the current user's context.

    In this case, the server process can duplicate its primary process token and change the session identifier in question to match the current session identifier. The current session identifier can be obtained by using the [**WTSGetActiveConsoleSessionId**](/windows/win32/api/winbase/nf-winbase-wtsgetactiveconsolesessionid) function.

    > [!Note]  
    > To set the token session ID, you need the **SE\_TCB\_PRIVILEGE**. You will have this only as a service running in NT AUTHORITY\\SYSTEM.

     

## Remote Desktop and Bandwidth

With the addition of the Remote Desktop feature to Windows XP, applications should make an effort not to use more bandwidth than needed, avoiding extensive screen drawings and animation effects if the desktop is connected remotely. To determine whether the current session is remote, you can call [**GetSystemMetrics**](/windows/win32/api/winuser/nf-winuser-getsystemmetrics) with **SM\_REMOTESESSION**. Be aware, however, that this call does not distinguish between remote and disconnected.

 

 
