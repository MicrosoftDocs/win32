---
title: Window Station and Desktop Functions
description: Applications can use the following functions with window station objects.
ms.assetid: 6214c28f-1035-446c-8c79-5d1dd638af2a
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Window Station and Desktop Functions

Applications can use the following functions with [window station](window-stations.md) objects.



| Function                                                     | Description                                                                                                     |
|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [**CloseWindowStation**](/windows/win32/Winuser/nf-winuser-closewindowstation?branch=master)             | Closes an open window station handle.                                                                           |
| [**CreateWindowStation**](/windows/win32/Winuser/nf-winuser-createwindowstationa?branch=master)           | Creates a window station object, associates it with the current process, and assigns it to the current session. |
| [**EnumWindowStations**](/windows/win32/Winuser/nf-winuser-enumwindowstationsa?branch=master)             | Enumerates all window stations in the current session.                                                          |
| [**GetProcessWindowStation**](/windows/win32/Winuser/nf-winuser-getprocesswindowstation?branch=master)   | Retrieves a handle to the current window station for the calling process.                                       |
| [**GetUserObjectInformation**](/windows/win32/Winuser/nf-winuser-getuserobjectinformationa?branch=master) | Retrieves information about the specified window station or desktop object.                                     |
| [**GetUserObjectSecurity**](https://msdn.microsoft.com/library/windows/desktop/aa446675)  | Retrieves security information for the specified window station or desktop object.                              |
| [**OpenWindowStation**](/windows/win32/Winuser/nf-winuser-openwindowstationa?branch=master)               | Opens the specified window station.                                                                             |
| [**SetProcessWindowStation**](/windows/win32/Winuser/nf-winuser-setprocesswindowstation?branch=master)   | Assigns the specified window station to the calling process.                                                    |
| [**SetUserObjectInformation**](/windows/win32/Winuser/nf-winuser-setuserobjectinformationa?branch=master) | Sets information about the specified window station or desktop object.                                          |
| [**SetUserObjectSecurity**](https://msdn.microsoft.com/library/windows/desktop/aa379592)  | Sets security information for the specified window station or desktop object.                                   |



 

Applications can use the following functions with [desktop](desktops.md) objects.



| Function                                                     | Description                                                                                                                        |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [**CloseDesktop**](/windows/win32/Winuser/nf-winuser-closedesktop?branch=master)                         | Closes an open handle to a desktop object.                                                                                         |
| [**CreateDesktop**](/windows/win32/Winuser/nf-winuser-createdesktopa?branch=master)                       | Creates a new desktop, associates it with the current window station of the calling process, and assigns it to the calling thread. |
| [**CreateDesktopEx**](/windows/win32/Winuser/nf-winuser-createdesktopexa?branch=master)                   | Creates a new desktop, associates it with the current window station of the calling process, and assigns it to the calling thread. |
| [**EnumDesktops**](/windows/win32/Winuser/nf-winuser-enumdesktopsa?branch=master)                         | Enumerates all desktops associated with the current window station of the calling process.                                         |
| [**EnumDesktopWindows**](/windows/win32/Winuser/nf-winuser-enumdesktopwindows?branch=master)             | Enumerates all top-level windows associated with the specified desktop.                                                            |
| [**GetThreadDesktop**](/windows/win32/Winuser/nf-winuser-getthreaddesktop?branch=master)                 | Retrieves a handle to the desktop assigned to the specified thread.                                                                |
| [**GetUserObjectInformation**](/windows/win32/Winuser/nf-winuser-getuserobjectinformationa?branch=master) | Gets information about a window station or desktop object.                                                                         |
| [**GetUserObjectSecurity**](https://msdn.microsoft.com/library/windows/desktop/aa446675)  | Gets security information for a window station or desktop object.                                                                  |
| [**OpenDesktop**](/windows/win32/Winuser/nf-winuser-opendesktopa?branch=master)                           | Opens the specified desktop object.                                                                                                |
| [**OpenInputDesktop**](/windows/win32/Winuser/nf-winuser-openinputdesktop?branch=master)                 | Opens the desktop that receives user input.                                                                                        |
| [**SetThreadDesktop**](/windows/win32/Winuser/nf-winuser-setthreaddesktop?branch=master)                 | Assigns the specified desktop to the calling thread.                                                                               |
| [**SetUserObjectInformation**](/windows/win32/Winuser/nf-winuser-setuserobjectinformationa?branch=master) | Sets information about a window station or desktop object.                                                                         |
| [**SetUserObjectSecurity**](https://msdn.microsoft.com/library/windows/desktop/aa379592)  | Sets security information for a window station or desktop object.                                                                  |
| [**SwitchDesktop**](/windows/win32/Winuser/nf-winuser-switchdesktop?branch=master)                       | Makes a desktop visible and activates it. This enables the desktop to receive input from the user.                                 |



 

 

 




