---
title: Window Station and Desktop Functions
description: Applications can use the following functions with window station objects.
ms.assetid: 6214c28f-1035-446c-8c79-5d1dd638af2a
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Window Station and Desktop Functions

Applications can use the following functions with [window station](window-stations.md) objects.



| Function                                                     | Description                                                                                                     |
|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [**CloseWindowStation**](https://msdn.microsoft.com/en-us/library/ms682047(v=VS.85).aspx)             | Closes an open window station handle.                                                                           |
| [**CreateWindowStation**](https://msdn.microsoft.com/en-us/library/ms682496(v=VS.85).aspx)           | Creates a window station object, associates it with the current process, and assigns it to the current session. |
| [**EnumWindowStations**](https://msdn.microsoft.com/en-us/library/ms682644(v=VS.85).aspx)             | Enumerates all window stations in the current session.                                                          |
| [**GetProcessWindowStation**](https://msdn.microsoft.com/en-us/library/ms683225(v=VS.85).aspx)   | Retrieves a handle to the current window station for the calling process.                                       |
| [**GetUserObjectInformation**](https://msdn.microsoft.com/en-us/library/ms683238(v=VS.85).aspx) | Retrieves information about the specified window station or desktop object.                                     |
| [**GetUserObjectSecurity**](https://msdn.microsoft.com/library/windows/desktop/aa446675)  | Retrieves security information for the specified window station or desktop object.                              |
| [**OpenWindowStation**](https://msdn.microsoft.com/en-us/library/ms684339(v=VS.85).aspx)               | Opens the specified window station.                                                                             |
| [**SetProcessWindowStation**](https://msdn.microsoft.com/en-us/library/ms686232(v=VS.85).aspx)   | Assigns the specified window station to the calling process.                                                    |
| [**SetUserObjectInformation**](https://msdn.microsoft.com/en-us/library/ms686287(v=VS.85).aspx) | Sets information about the specified window station or desktop object.                                          |
| [**SetUserObjectSecurity**](https://msdn.microsoft.com/library/windows/desktop/aa379592)  | Sets security information for the specified window station or desktop object.                                   |



 

Applications can use the following functions with [desktop](desktops.md) objects.



| Function                                                     | Description                                                                                                                        |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [**CloseDesktop**](https://msdn.microsoft.com/en-us/library/ms682024(v=VS.85).aspx)                         | Closes an open handle to a desktop object.                                                                                         |
| [**CreateDesktop**](https://msdn.microsoft.com/en-us/library/ms682124(v=VS.85).aspx)                       | Creates a new desktop, associates it with the current window station of the calling process, and assigns it to the calling thread. |
| [**CreateDesktopEx**](https://msdn.microsoft.com/en-us/library/ms682127(v=VS.85).aspx)                   | Creates a new desktop, associates it with the current window station of the calling process, and assigns it to the calling thread. |
| [**EnumDesktops**](https://msdn.microsoft.com/en-us/library/ms682614(v=VS.85).aspx)                         | Enumerates all desktops associated with the current window station of the calling process.                                         |
| [**EnumDesktopWindows**](https://msdn.microsoft.com/en-us/library/ms682615(v=VS.85).aspx)             | Enumerates all top-level windows associated with the specified desktop.                                                            |
| [**GetThreadDesktop**](https://msdn.microsoft.com/en-us/library/ms683232(v=VS.85).aspx)                 | Retrieves a handle to the desktop assigned to the specified thread.                                                                |
| [**GetUserObjectInformation**](https://msdn.microsoft.com/en-us/library/ms683238(v=VS.85).aspx) | Gets information about a window station or desktop object.                                                                         |
| [**GetUserObjectSecurity**](https://msdn.microsoft.com/library/windows/desktop/aa446675)  | Gets security information for a window station or desktop object.                                                                  |
| [**OpenDesktop**](https://msdn.microsoft.com/en-us/library/ms684303(v=VS.85).aspx)                           | Opens the specified desktop object.                                                                                                |
| [**OpenInputDesktop**](https://msdn.microsoft.com/en-us/library/ms684309(v=VS.85).aspx)                 | Opens the desktop that receives user input.                                                                                        |
| [**SetThreadDesktop**](https://msdn.microsoft.com/en-us/library/ms686250(v=VS.85).aspx)                 | Assigns the specified desktop to the calling thread.                                                                               |
| [**SetUserObjectInformation**](https://msdn.microsoft.com/en-us/library/ms686287(v=VS.85).aspx) | Sets information about a window station or desktop object.                                                                         |
| [**SetUserObjectSecurity**](https://msdn.microsoft.com/library/windows/desktop/aa379592)  | Sets security information for a window station or desktop object.                                                                  |
| [**SwitchDesktop**](https://msdn.microsoft.com/en-us/library/ms686347(v=VS.85).aspx)                       | Makes a desktop visible and activates it. This enables the desktop to receive input from the user.                                 |



 

 

 




