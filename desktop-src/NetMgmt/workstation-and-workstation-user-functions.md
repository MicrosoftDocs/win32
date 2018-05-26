---
title: Workstation and Workstation User Functions
description: The network management workstation functions perform administrative tasks on a local or remote workstation.
ms.assetid: cc400f43-297b-4ff4-8353-b268839c48b8
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Workstation and Workstation User Functions

The network management workstation functions perform administrative tasks on a local or remote workstation. Only a user or application with admin group membership, on a local or remote server, can perform administrative tasks on a workstation to control its operation, user access, and resource sharing. For more information about calling functions that require administrator privileges, see [Running with Special Privileges](https://msdn.microsoft.com/library/windows/desktop/ms717802).

The workstation functions are listed following.



| Function                                   | Description                                                             |
|--------------------------------------------|-------------------------------------------------------------------------|
| [**NetWkstaGetInfo**](/windows/win32/Lmwksta/nf-lmwksta-netwkstagetinfo?branch=master) | Returns information about the configuration elements for a workstation. |
| [**NetWkstaSetInfo**](/windows/win32/Lmwksta/nf-lmwksta-netwkstasetinfo?branch=master) | Configures a workstation.                                               |



 

The workstation functions allow access to two discrete types of workstation information:

-   System information
-   Platform-specific information

Within each type the data is categorized by security access. Data that is guest-accessible is a subset of the data that is user-accessible, which is in turn a subset of the admin-accessible data.

Workstation information is available at the following levels:

-   [**WKSTA\_INFO\_100**](/windows/win32/Lmwksta/ns-lmwksta-_wksta_info_100?branch=master)
-   [**WKSTA\_INFO\_101**](/windows/win32/Lmwksta/ns-lmwksta-_wksta_info_101?branch=master)
-   [**WKSTA\_INFO\_102**](/windows/win32/Lmwksta/ns-lmwksta-_wksta_info_102?branch=master)

The network management workstation user functions allow access to user-specific information. The user-specific information is separated from the workstation information because there can be more than one user on a workstation.

The workstation user functions are listed following.



| Function                                           | Description                                                                         |
|----------------------------------------------------|-------------------------------------------------------------------------------------|
| [**NetWkstaUserEnum**](/windows/win32/Lmwksta/nf-lmwksta-netwkstauserenum?branch=master)       | Lists information about all users currently logged on to the workstation.           |
| [**NetWkstaUserGetInfo**](/windows/win32/Lmwksta/nf-lmwksta-netwkstausergetinfo?branch=master) | Returns information about one currently logged-on user.                             |
| [**NetWkstaUserSetInfo**](/windows/win32/Lmwksta/nf-lmwksta-netwkstausersetinfo?branch=master) | Sets the user-specific information for the configuration elements of a workstation. |



 

Workstation user information is available at the following levels:

-   [**WKSTA\_USER\_INFO\_0**](/windows/win32/Lmwksta/ns-lmwksta-_wksta_user_info_0?branch=master)
-   [**WKSTA\_USER\_INFO\_1**](/windows/win32/Lmwksta/ns-lmwksta-_wksta_user_info_1?branch=master)
-   [**WKSTA\_USER\_INFO\_1101**](/windows/win32/Lmwksta/ns-lmwksta-_wksta_user_info_1101?branch=master)

 

 




