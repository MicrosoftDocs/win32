---
title: Group Functions
description: A global group contains user accounts from one domain that are grouped together under one group account name.
ms.assetid: '2199258d-bde9-4fdb-b9c1-147616420fbe'
---

# Group Functions

A *global group* contains user accounts from one domain that are grouped together under one group account name. A global group can contain only members (users) from the domain where the global group is created; it cannot contain local groups. A global group is available within its own domain and within any trusting domain.

The network management group functions control global groups. The group functions are listed following.



| Function                                     | Description                                                                       |
|----------------------------------------------|-----------------------------------------------------------------------------------|
| [**NetGroupAdd**](netgroupadd.md)           | Creates a global group.                                                           |
| [**NetGroupAddUser**](netgroupadduser.md)   | Adds one user to an existing global group.                                        |
| [**NetGroupDel**](netgroupdel.md)           | Removes a global group whether or not the group has any members.                  |
| [**NetGroupDelUser**](netgroupdeluser.md)   | Removes one user name from a global group.                                        |
| [**NetGroupEnum**](netgroupenum.md)         | Lists all global groups on a server.                                              |
| [**NetGroupGetInfo**](netgroupgetinfo.md)   | Returns information about a particular global group.                              |
| [**NetGroupGetUsers**](netgroupgetusers.md) | Lists all members of a particular global group.                                   |
| [**NetGroupSetInfo**](netgroupsetinfo.md)   | Sets general information about a global group.                                    |
| [**NetGroupSetUsers**](netgroupsetusers.md) | Assigns members to a new global group; replaces the members of an existing group. |



 

When you call the [**NetGroupAdd**](netgroupadd.md) function to create a global group, you must supply a group name. Initially, a new group has no members.

User accounts automatically belong to the special global group Domain Users. Membership in this group is indirectly controlled by the [**NetUserAdd**](netuseradd.md), [**NetUserDel**](netuserdel.md), and [**NetUserSetInfo**](netusersetinfo.md) functions.

Global group account information is available at the following levels:

-   [**GROUP\_INFO\_0**](group-info-0-str.md)
-   [**GROUP\_INFO\_1**](group-info-1-str.md)
-   [**GROUP\_INFO\_2**](group-info-2-str.md)
-   [**GROUP\_INFO\_3**](group-info-3-str.md)
-   [**GROUP\_INFO\_1002**](group-info-1002-str.md)
-   [**GROUP\_INFO\_1005**](group-info-1005-str.md)

The 1002 and 1005 levels are valid only for the [**NetGroupSetInfo**](netgroupsetinfo.md) function.

Global group member information is available at the following information level:

-   [**GROUP\_USERS\_INFO\_0**](group-users-info-0-str.md)

For more information, see the network management [Local Group Functions](local-group-functions.md).

If you are programming for Active Directory, you may be able to call certain Active Directory Service Interface (ADSI) methods to achieve the same functionality you can achieve by calling the network management group functions. For more information, see [**IADsGroup**](https://msdn.microsoft.com/library/aa706021).

 

 




