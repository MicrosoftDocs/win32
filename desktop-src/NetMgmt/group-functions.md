---
title: Group Functions
description: A global group contains user accounts from one domain that are grouped together under one group account name.
ms.assetid: 2199258d-bde9-4fdb-b9c1-147616420fbe
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Group Functions

A *global group* contains user accounts from one domain that are grouped together under one group account name. A global group can contain only members (users) from the domain where the global group is created; it cannot contain local groups. A global group is available within its own domain and within any trusting domain.

The network management group functions control global groups. The group functions are listed following.



| Function                                     | Description                                                                       |
|----------------------------------------------|-----------------------------------------------------------------------------------|
| [**NetGroupAdd**](/windows/win32/Lmaccess/nf-lmaccess-netgroupadd?branch=master)           | Creates a global group.                                                           |
| [**NetGroupAddUser**](/windows/win32/Lmaccess/nf-lmaccess-netgroupadduser?branch=master)   | Adds one user to an existing global group.                                        |
| [**NetGroupDel**](/windows/win32/Lmaccess/nf-lmaccess-netgroupdel?branch=master)           | Removes a global group whether or not the group has any members.                  |
| [**NetGroupDelUser**](/windows/win32/Lmaccess/nf-lmaccess-netgroupdeluser?branch=master)   | Removes one user name from a global group.                                        |
| [**NetGroupEnum**](/windows/win32/Lmaccess/nf-lmaccess-netgroupenum?branch=master)         | Lists all global groups on a server.                                              |
| [**NetGroupGetInfo**](/windows/win32/Lmaccess/nf-lmaccess-netgroupgetinfo?branch=master)   | Returns information about a particular global group.                              |
| [**NetGroupGetUsers**](/windows/win32/Lmaccess/nf-lmaccess-netgroupgetusers?branch=master) | Lists all members of a particular global group.                                   |
| [**NetGroupSetInfo**](/windows/win32/Lmaccess/nf-lmaccess-netgroupsetinfo?branch=master)   | Sets general information about a global group.                                    |
| [**NetGroupSetUsers**](/windows/win32/Lmaccess/nf-lmaccess-netgroupsetusers?branch=master) | Assigns members to a new global group; replaces the members of an existing group. |



 

When you call the [**NetGroupAdd**](/windows/win32/Lmaccess/nf-lmaccess-netgroupadd?branch=master) function to create a global group, you must supply a group name. Initially, a new group has no members.

User accounts automatically belong to the special global group Domain Users. Membership in this group is indirectly controlled by the [**NetUserAdd**](/windows/win32/Lmaccess/nf-lmaccess-netuseradd?branch=master), [**NetUserDel**](/windows/win32/Lmaccess/nf-lmaccess-netuserdel?branch=master), and [**NetUserSetInfo**](/windows/win32/Lmaccess/nf-lmaccess-netusersetinfo?branch=master) functions.

Global group account information is available at the following levels:

-   [**GROUP\_INFO\_0**](/windows/win32/Lmaccess/ns-lmaccess-_group_info_0?branch=master)
-   [**GROUP\_INFO\_1**](/windows/win32/Lmaccess/ns-lmaccess-_group_info_1?branch=master)
-   [**GROUP\_INFO\_2**](/windows/win32/Lmaccess/ns-lmaccess-_group_info_2?branch=master)
-   [**GROUP\_INFO\_3**](/windows/win32/Lmaccess/ns-lmaccess-_group_info_3?branch=master)
-   [**GROUP\_INFO\_1002**](/windows/win32/Lmaccess/ns-lmaccess-_group_info_1002?branch=master)
-   [**GROUP\_INFO\_1005**](/windows/win32/Lmaccess/ns-lmaccess-_group_info_1005?branch=master)

The 1002 and 1005 levels are valid only for the [**NetGroupSetInfo**](/windows/win32/Lmaccess/nf-lmaccess-netgroupsetinfo?branch=master) function.

Global group member information is available at the following information level:

-   [**GROUP\_USERS\_INFO\_0**](/windows/win32/Lmaccess/ns-lmaccess-_group_users_info_0?branch=master)

For more information, see the network management [Local Group Functions](local-group-functions.md).

If you are programming for Active Directory, you may be able to call certain Active Directory Service Interface (ADSI) methods to achieve the same functionality you can achieve by calling the network management group functions. For more information, see [**IADsGroup**](https://msdn.microsoft.com/library/aa706021).

 

 




