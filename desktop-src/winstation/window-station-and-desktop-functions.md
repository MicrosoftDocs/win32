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
| [**CloseWindowStation**](closewindowstation.md)             | Closes an open window station handle.                                                                           |
| [**CreateWindowStation**](createwindowstation.md)           | Creates a window station object, associates it with the current process, and assigns it to the current session. |
| [**EnumWindowStations**](enumwindowstations.md)             | Enumerates all window stations in the current session.                                                          |
| [**GetProcessWindowStation**](getprocesswindowstation.md)   | Retrieves a handle to the current window station for the calling process.                                       |
| [**GetUserObjectInformation**](getuserobjectinformation.md) | Retrieves information about the specified window station or desktop object.                                     |
| [**GetUserObjectSecurity**](https://msdn.microsoft.com/library/windows/desktop/aa446675)  | Retrieves security information for the specified window station or desktop object.                              |
| [**OpenWindowStation**](openwindowstation.md)               | Opens the specified window station.                                                                             |
| [**SetProcessWindowStation**](setprocesswindowstation.md)   | Assigns the specified window station to the calling process.                                                    |
| [**SetUserObjectInformation**](setuserobjectinformation.md) | Sets information about the specified window station or desktop object.                                          |
| [**SetUserObjectSecurity**](https://msdn.microsoft.com/library/windows/desktop/aa379592)  | Sets security information for the specified window station or desktop object.                                   |



 

Applications can use the following functions with [desktop](desktops.md) objects.



| Function                                                     | Description                                                                                                                        |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [**CloseDesktop**](closedesktop.md)                         | Closes an open handle to a desktop object.                                                                                         |
| [**CreateDesktop**](createdesktop.md)                       | Creates a new desktop, associates it with the current window station of the calling process, and assigns it to the calling thread. |
| [**CreateDesktopEx**](createdesktopex.md)                   | Creates a new desktop, associates it with the current window station of the calling process, and assigns it to the calling thread. |
| [**EnumDesktops**](enumdesktops.md)                         | Enumerates all desktops associated with the current window station of the calling process.                                         |
| [**EnumDesktopWindows**](enumdesktopwindows.md)             | Enumerates all top-level windows associated with the specified desktop.                                                            |
| [**GetThreadDesktop**](getthreaddesktop.md)                 | Retrieves a handle to the desktop assigned to the specified thread.                                                                |
| [**GetUserObjectInformation**](getuserobjectinformation.md) | Gets information about a window station or desktop object.                                                                         |
| [**GetUserObjectSecurity**](https://msdn.microsoft.com/library/windows/desktop/aa446675)  | Gets security information for a window station or desktop object.                                                                  |
| [**OpenDesktop**](opendesktop.md)                           | Opens the specified desktop object.                                                                                                |
| [**OpenInputDesktop**](openinputdesktop.md)                 | Opens the desktop that receives user input.                                                                                        |
| [**SetThreadDesktop**](setthreaddesktop.md)                 | Assigns the specified desktop to the calling thread.                                                                               |
| [**SetUserObjectInformation**](setuserobjectinformation.md) | Sets information about a window station or desktop object.                                                                         |
| [**SetUserObjectSecurity**](https://msdn.microsoft.com/library/windows/desktop/aa379592)  | Sets security information for a window station or desktop object.                                                                  |
| [**SwitchDesktop**](switchdesktop.md)                       | Makes a desktop visible and activates it. This enables the desktop to receive input from the user.                                 |



 

 

 




