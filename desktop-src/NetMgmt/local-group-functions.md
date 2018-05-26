---
title: Local Group Functions
description: A local group can contain user accounts or global group accounts from one or more domains. (Global groups can contain users from only one domain.) A local group shares common privileges and rights only within its own domain.
ms.assetid: ed4c59d6-6532-4190-9807-95678053fc72
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Local Group Functions

A *local group* can contain user accounts or global group accounts from one or more domains. (Global groups can contain users from only one domain.) A local group shares common privileges and rights only within its own domain.

The network management local group functions control members of local groups in a way that the functions can only be called locally on the system on which the local group is defined. On a workstation, or on a server that is not a domain controller, you can use only a local group defined on that system.

In Active Directory, domains that are in native mode, local groups are called *domain local groups*. Domain local groups are available on all domain controllers, member servers, and workstations joined to the domain. Active Directory mixed-mode domains are defined on the primary domain controller and replicated to all other domain controllers in the domain. Therefore, a local group is available on all domain controllers within the domain in which it was created..

The local group functions create or delete local groups, and review or adjust the memberships of local groups. These functions are listed following.



| Function                                                   | Description                                                             |
|------------------------------------------------------------|-------------------------------------------------------------------------|
| [**NetLocalGroupAdd**](/windows/win32/Lmaccess/nf-lmaccess-netlocalgroupadd?branch=master)               | Creates a local group.                                                  |
| [**NetLocalGroupAddMembers**](/windows/win32/Lmaccess/nf-lmaccess-netlocalgroupaddmembers?branch=master) | Adds one or more users or global groups to an existing local group.     |
| [**NetLocalGroupDel**](/windows/win32/Lmaccess/nf-lmaccess-netlocalgroupdel?branch=master)               | Deletes a local group, removing all existing members from the group.    |
| [**NetLocalGroupDelMembers**](/windows/win32/Lmaccess/nf-lmaccess-netlocalgroupdelmembers?branch=master) | Removes one or more members from an existing local group.               |
| [**NetLocalGroupEnum**](/windows/win32/Lmaccess/nf-lmaccess-netlocalgroupenum?branch=master)             | Returns information about each local group account on a server.         |
| [**NetLocalGroupGetInfo**](/windows/win32/Lmaccess/nf-lmaccess-netlocalgroupgetinfo?branch=master)       | Returns information about a particular local group account on a server. |
| [**NetLocalGroupGetMembers**](/windows/win32/Lmaccess/nf-lmaccess-netlocalgroupgetmembers?branch=master) | Lists all members of a specified local group.                           |
| [**NetLocalGroupSetInfo**](/windows/win32/Lmaccess/nf-lmaccess-netlocalgroupsetinfo?branch=master)       | Sets general information about a local group.                           |
| [**NetLocalGroupSetMembers**](/windows/win32/Lmaccess/nf-lmaccess-netlocalgroupsetmembers?branch=master) | Assigns members to a local group.                                       |



 

You can add a member to a local group by specifying the security identifier (SID) of the member. To translate a member account name to a SID, call the [**LookupAccountName**](https://msdn.microsoft.com/library/windows/desktop/aa379159) function.

When you create a local group by calling the [**NetLocalGroupAdd**](/windows/win32/Lmaccess/nf-lmaccess-netlocalgroupadd?branch=master) function, you must supply a local group name. Initially, the local group has no members.

Local group account information is available at the following levels:

-   [**LOCALGROUP\_INFO\_0**](/windows/win32/Lmaccess/ns-lmaccess-_localgroup_info_0?branch=master)
-   [**LOCALGROUP\_INFO\_1**](/windows/win32/Lmaccess/ns-lmaccess-_localgroup_info_1?branch=master)
-   [**LOCALGROUP\_INFO\_1002**](/windows/win32/Lmaccess/ns-lmaccess-_localgroup_info_1002?branch=master)

Local group membership information is available at the following information levels:

-   [**LOCALGROUP\_MEMBERS\_INFO\_0**](/windows/win32/Lmaccess/ns-lmaccess-_localgroup_members_info_0?branch=master)
-   [**LOCALGROUP\_MEMBERS\_INFO\_1**](/windows/win32/Lmaccess/ns-lmaccess-_localgroup_members_info_1?branch=master)
-   [**LOCALGROUP\_MEMBERS\_INFO\_2**](/windows/win32/Lmaccess/ns-lmaccess-_localgroup_members_info_2?branch=master)
-   [**LOCALGROUP\_MEMBERS\_INFO\_3**](/windows/win32/Lmaccess/ns-lmaccess-_localgroup_members_info_3?branch=master)

You can retrieve the names of the local groups to which a user belongs by calling the [**NetUserGetLocalGroups**](/windows/win32/Lmaccess/nf-lmaccess-netusergetlocalgroups?branch=master) function, specifying the following information level:

[**LOCALGROUP\_USERS\_INFO\_0**](/windows/win32/Lmaccess/ns-lmaccess-_localgroup_users_info_0?branch=master)

For more information, see the network management [Group Functions](group-functions.md).

If you are programming for Active Directory, you may be able to call certain Active Directory Service Interface (ADSI) methods to achieve the same functionality you can achieve by calling the network management local group functions. For more information, see [**IADsGroup**](https://msdn.microsoft.com/library/aa706021).

 

 




