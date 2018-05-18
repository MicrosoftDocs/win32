---
title: Workstation and Workstation User Functions
description: The network management workstation functions perform administrative tasks on a local or remote workstation.
ms.assetid: 'cc400f43-297b-4ff4-8353-b268839c48b8'
---

# Workstation and Workstation User Functions

The network management workstation functions perform administrative tasks on a local or remote workstation. Only a user or application with admin group membership, on a local or remote server, can perform administrative tasks on a workstation to control its operation, user access, and resource sharing. For more information about calling functions that require administrator privileges, see [Running with Special Privileges](https://msdn.microsoft.com/library/windows/desktop/ms717802).

The workstation functions are listed following.



| Function                                   | Description                                                             |
|--------------------------------------------|-------------------------------------------------------------------------|
| [**NetWkstaGetInfo**](netwkstagetinfo.md) | Returns information about the configuration elements for a workstation. |
| [**NetWkstaSetInfo**](netwkstasetinfo.md) | Configures a workstation.                                               |



 

The workstation functions allow access to two discrete types of workstation information:

-   System information
-   Platform-specific information

Within each type the data is categorized by security access. Data that is guest-accessible is a subset of the data that is user-accessible, which is in turn a subset of the admin-accessible data.

Workstation information is available at the following levels:

-   [**WKSTA\_INFO\_100**](wksta-info-100-str.md)
-   [**WKSTA\_INFO\_101**](wksta-info-101-str.md)
-   [**WKSTA\_INFO\_102**](wksta-info-102-str.md)

The network management workstation user functions allow access to user-specific information. The user-specific information is separated from the workstation information because there can be more than one user on a workstation.

The workstation user functions are listed following.



| Function                                           | Description                                                                         |
|----------------------------------------------------|-------------------------------------------------------------------------------------|
| [**NetWkstaUserEnum**](netwkstauserenum.md)       | Lists information about all users currently logged on to the workstation.           |
| [**NetWkstaUserGetInfo**](netwkstausergetinfo.md) | Returns information about one currently logged-on user.                             |
| [**NetWkstaUserSetInfo**](netwkstausersetinfo.md) | Sets the user-specific information for the configuration elements of a workstation. |



 

Workstation user information is available at the following levels:

-   [**WKSTA\_USER\_INFO\_0**](wksta-user-info-0-str.md)
-   [**WKSTA\_USER\_INFO\_1**](wksta-user-info-1-str.md)
-   [**WKSTA\_USER\_INFO\_1101**](wksta-user-info-1101-str.md)

 

 




