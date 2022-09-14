---
title: Group Functions
description: A global group contains user accounts from one domain that are grouped together under one group account name.
ms.assetid: 2199258d-bde9-4fdb-b9c1-147616420fbe
ms.topic: article
ms.date: 05/31/2018
---

# Group Functions

A *global group* contains user accounts from one domain that are grouped together under one group account name. A global group can contain only members (users) from the domain where the global group is created; it cannot contain local groups. A global group is available within its own domain and within any trusting domain.

The network management group functions control global groups. The group functions are listed following.



| Function                                     | Description                                                                       |
|----------------------------------------------|-----------------------------------------------------------------------------------|
| [**NetGroupAdd**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupadd)           | Creates a global group.                                                           |
| [**NetGroupAddUser**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupadduser)   | Adds one user to an existing global group.                                        |
| [**NetGroupDel**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupdel)           | Removes a global group whether or not the group has any members.                  |
| [**NetGroupDelUser**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupdeluser)   | Removes one user name from a global group.                                        |
| [**NetGroupEnum**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupenum)         | Lists all global groups on a server.                                              |
| [**NetGroupGetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupgetinfo)   | Returns information about a particular global group.                              |
| [**NetGroupGetUsers**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupgetusers) | Lists all members of a particular global group.                                   |
| [**NetGroupSetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupsetinfo)   | Sets general information about a global group.                                    |
| [**NetGroupSetUsers**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupsetusers) | Assigns members to a new global group; replaces the members of an existing group. |



 

When you call the [**NetGroupAdd**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupadd) function to create a global group, you must supply a group name. Initially, a new group has no members.

User accounts automatically belong to the special global group Domain Users. Membership in this group is indirectly controlled by the [**NetUserAdd**](/windows/desktop/api/Lmaccess/nf-lmaccess-netuseradd), [**NetUserDel**](/windows/desktop/api/Lmaccess/nf-lmaccess-netuserdel), and [**NetUserSetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusersetinfo) functions.

Global group account information is available at the following levels:

-   [**GROUP\_INFO\_0**](/windows/desktop/api/Lmaccess/ns-lmaccess-group_info_0)
-   [**GROUP\_INFO\_1**](/windows/desktop/api/Lmaccess/ns-lmaccess-group_info_1)
-   [**GROUP\_INFO\_2**](/windows/desktop/api/Lmaccess/ns-lmaccess-group_info_2)
-   [**GROUP\_INFO\_3**](/windows/desktop/api/Lmaccess/ns-lmaccess-group_info_3)
-   [**GROUP\_INFO\_1002**](/windows/desktop/api/Lmaccess/ns-lmaccess-group_info_1002)
-   [**GROUP\_INFO\_1005**](/windows/desktop/api/Lmaccess/ns-lmaccess-group_info_1005)

The 1002 and 1005 levels are valid only for the [**NetGroupSetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupsetinfo) function.

Global group member information is available at the following information level:

-   [**GROUP\_USERS\_INFO\_0**](/windows/desktop/api/Lmaccess/ns-lmaccess-group_users_info_0)

For more information, see the network management [Local Group Functions](local-group-functions.md).

If you are programming for Active Directory, you may be able to call certain Active Directory Service Interface (ADSI) methods to achieve the same functionality you can achieve by calling the network management group functions. For more information, see [**IADsGroup**](/windows/desktop/api/iads/nn-iads-iadsgroup).

 

 