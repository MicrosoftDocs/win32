---
title: Window Station and Desktop Functions
description: Applications can use the following functions with window station objects.
ms.assetid: 6214c28f-1035-446c-8c79-5d1dd638af2a
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Window Station and Desktop Functions

Applications can use the following functions with [window station](window-stations.md) objects.



| Function                                                     | Description                                                                                                     |
|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [**CloseWindowStation**](/windows/desktop/api/Winuser/nf-winuser-closewindowstation)             | Closes an open window station handle.                                                                           |
| [**CreateWindowStation**](/windows/desktop/api/Winuser/nf-winuser-createwindowstationa)           | Creates a window station object, associates it with the current process, and assigns it to the current session. |
| [**EnumWindowStations**](/windows/desktop/api/Winuser/nf-winuser-enumwindowstationsa)             | Enumerates all window stations in the current session.                                                          |
| [**GetProcessWindowStation**](/windows/desktop/api/Winuser/nf-winuser-getprocesswindowstation)   | Retrieves a handle to the current window station for the calling process.                                       |
| [**GetUserObjectInformation**](/windows/desktop/api/Winuser/nf-winuser-getuserobjectinformationa) | Retrieves information about the specified window station or desktop object.                                     |
| [**GetUserObjectSecurity**](https://msdn.microsoft.com/library/windows/desktop/aa446675)  | Retrieves security information for the specified window station or desktop object.                              |
| [**OpenWindowStation**](/windows/desktop/api/Winuser/nf-winuser-openwindowstationa)               | Opens the specified window station.                                                                             |
| [**SetProcessWindowStation**](/windows/desktop/api/Winuser/nf-winuser-setprocesswindowstation)   | Assigns the specified window station to the calling process.                                                    |
| [**SetUserObjectInformation**](/windows/desktop/api/Winuser/nf-winuser-setuserobjectinformationa) | Sets information about the specified window station or desktop object.                                          |
| [**SetUserObjectSecurity**](https://msdn.microsoft.com/library/windows/desktop/aa379592)  | Sets security information for the specified window station or desktop object.                                   |



 

Applications can use the following functions with [desktop](desktops.md) objects.



| Function                                                     | Description                                                                                                                        |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [**CloseDesktop**](/windows/desktop/api/Winuser/nf-winuser-closedesktop)                         | Closes an open handle to a desktop object.                                                                                         |
| [**CreateDesktop**](/windows/desktop/api/Winuser/nf-winuser-createdesktopa)                       | Creates a new desktop, associates it with the current window station of the calling process, and assigns it to the calling thread. |
| [**CreateDesktopEx**](/windows/desktop/api/Winuser/nf-winuser-createdesktopexa)                   | Creates a new desktop, associates it with the current window station of the calling process, and assigns it to the calling thread. |
| [**EnumDesktops**](/windows/desktop/api/Winuser/nf-winuser-enumdesktopsa)                         | Enumerates all desktops associated with the current window station of the calling process.                                         |
| [**EnumDesktopWindows**](/windows/desktop/api/Winuser/nf-winuser-enumdesktopwindows)             | Enumerates all top-level windows associated with the specified desktop.                                                            |
| [**GetThreadDesktop**](/windows/desktop/api/Winuser/nf-winuser-getthreaddesktop)                 | Retrieves a handle to the desktop assigned to the specified thread.                                                                |
| [**GetUserObjectInformation**](/windows/desktop/api/Winuser/nf-winuser-getuserobjectinformationa) | Gets information about a window station or desktop object.                                                                         |
| [**GetUserObjectSecurity**](https://msdn.microsoft.com/library/windows/desktop/aa446675)  | Gets security information for a window station or desktop object.                                                                  |
| [**OpenDesktop**](/windows/desktop/api/Winuser/nf-winuser-opendesktopa)                           | Opens the specified desktop object.                                                                                                |
| [**OpenInputDesktop**](/windows/desktop/api/Winuser/nf-winuser-openinputdesktop)                 | Opens the desktop that receives user input.                                                                                        |
| [**SetThreadDesktop**](/windows/desktop/api/Winuser/nf-winuser-setthreaddesktop)                 | Assigns the specified desktop to the calling thread.                                                                               |
| [**SetUserObjectInformation**](/windows/desktop/api/Winuser/nf-winuser-setuserobjectinformationa) | Sets information about a window station or desktop object.                                                                         |
| [**SetUserObjectSecurity**](https://msdn.microsoft.com/library/windows/desktop/aa379592)  | Sets security information for a window station or desktop object.                                                                  |
| [**SwitchDesktop**](/windows/desktop/api/Winuser/nf-winuser-switchdesktop)                       | Makes a desktop visible and activates it. This enables the desktop to receive input from the user.                                 |



 

 

 




