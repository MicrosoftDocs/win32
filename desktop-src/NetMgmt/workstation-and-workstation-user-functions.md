---
title: Workstation and Workstation User Functions
description: The network management workstation functions perform administrative tasks on a local or remote workstation.
ms.assetid: cc400f43-297b-4ff4-8353-b268839c48b8
ms.topic: article
ms.date: 05/31/2018
---

# Workstation and Workstation User Functions

The network management workstation functions perform administrative tasks on a local or remote workstation. Only a user or application with admin group membership, on a local or remote server, can perform administrative tasks on a workstation to control its operation, user access, and resource sharing. For more information about calling functions that require administrator privileges, see [Running with Special Privileges](/windows/desktop/SecBP/running-with-special-privileges).

The workstation functions are listed following.



| Function                                   | Description                                                             |
|--------------------------------------------|-------------------------------------------------------------------------|
| [**NetWkstaGetInfo**](/windows/desktop/api/Lmwksta/nf-lmwksta-netwkstagetinfo) | Returns information about the configuration elements for a workstation. |
| [**NetWkstaSetInfo**](/windows/desktop/api/Lmwksta/nf-lmwksta-netwkstasetinfo) | Configures a workstation.                                               |



 

The workstation functions allow access to two discrete types of workstation information:

-   System information
-   Platform-specific information

Within each type the data is categorized by security access. Data that is guest-accessible is a subset of the data that is user-accessible, which is in turn a subset of the admin-accessible data.

Workstation information is available at the following levels:

-   [**WKSTA\_INFO\_100**](/windows/desktop/api/Lmwksta/ns-lmwksta-wksta_info_100)
-   [**WKSTA\_INFO\_101**](/windows/desktop/api/Lmwksta/ns-lmwksta-wksta_info_101)
-   [**WKSTA\_INFO\_102**](/windows/desktop/api/Lmwksta/ns-lmwksta-wksta_info_102)

The network management workstation user functions allow access to user-specific information. The user-specific information is separated from the workstation information because there can be more than one user on a workstation.

The workstation user functions are listed following.



| Function                                           | Description                                                                         |
|----------------------------------------------------|-------------------------------------------------------------------------------------|
| [**NetWkstaUserEnum**](/windows/desktop/api/Lmwksta/nf-lmwksta-netwkstauserenum)       | Lists information about all users currently logged on to the workstation.           |
| [**NetWkstaUserGetInfo**](/windows/desktop/api/Lmwksta/nf-lmwksta-netwkstausergetinfo) | Returns information about one currently logged-on user.                             |
| [**NetWkstaUserSetInfo**](/windows/desktop/api/Lmwksta/nf-lmwksta-netwkstausersetinfo) | Sets the user-specific information for the configuration elements of a workstation. |



 

Workstation user information is available at the following levels:

-   [**WKSTA\_USER\_INFO\_0**](/windows/desktop/api/Lmwksta/ns-lmwksta-wksta_user_info_0)
-   [**WKSTA\_USER\_INFO\_1**](/windows/desktop/api/Lmwksta/ns-lmwksta-wksta_user_info_1)
-   [**WKSTA\_USER\_INFO\_1101**](/windows/desktop/api/Lmwksta/ns-lmwksta-wksta_user_info_1101)

 

 