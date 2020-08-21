---
title: Local Group Functions
description: A local group can contain user accounts or global group accounts from one or more domains. (Global groups can contain users from only one domain.) A local group shares common privileges and rights only within its own domain.
ms.assetid: ed4c59d6-6532-4190-9807-95678053fc72
ms.topic: article
ms.date: 05/31/2018
---

# Local Group Functions

A *local group* can contain user accounts or global group accounts from one or more domains. (Global groups can contain users from only one domain.) A local group shares common privileges and rights only within its own domain.

The network management local group functions control members of local groups in a way that the functions can only be called locally on the system on which the local group is defined. On a workstation, or on a server that is not a domain controller, you can use only a local group defined on that system.

In Active Directory, domains that are in native mode, local groups are called *domain local groups*. Domain local groups are available on all domain controllers, member servers, and workstations joined to the domain. Active Directory mixed-mode domains are defined on the primary domain controller and replicated to all other domain controllers in the domain. Therefore, a local group is available on all domain controllers within the domain in which it was created..

The local group functions create or delete local groups, and review or adjust the memberships of local groups. These functions are listed following.



| Function                                                   | Description                                                             |
|------------------------------------------------------------|-------------------------------------------------------------------------|
| [**NetLocalGroupAdd**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupadd)               | Creates a local group.                                                  |
| [**NetLocalGroupAddMembers**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupaddmembers) | Adds one or more users or global groups to an existing local group.     |
| [**NetLocalGroupDel**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupdel)               | Deletes a local group, removing all existing members from the group.    |
| [**NetLocalGroupDelMembers**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupdelmembers) | Removes one or more members from an existing local group.               |
| [**NetLocalGroupEnum**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupenum)             | Returns information about each local group account on a server.         |
| [**NetLocalGroupGetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupgetinfo)       | Returns information about a particular local group account on a server. |
| [**NetLocalGroupGetMembers**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupgetmembers) | Lists all members of a specified local group.                           |
| [**NetLocalGroupSetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupsetinfo)       | Sets general information about a local group.                           |
| [**NetLocalGroupSetMembers**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupsetmembers) | Assigns members to a local group.                                       |



 

You can add a member to a local group by specifying the security identifier (SID) of the member. To translate a member account name to a SID, call the [**LookupAccountName**](/windows/desktop/api/winbase/nf-winbase-lookupaccountnamea) function.

When you create a local group by calling the [**NetLocalGroupAdd**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupadd) function, you must supply a local group name. Initially, the local group has no members.

Local group account information is available at the following levels:

-   [**LOCALGROUP\_INFO\_0**](/windows/desktop/api/Lmaccess/ns-lmaccess-localgroup_info_0)
-   [**LOCALGROUP\_INFO\_1**](/windows/desktop/api/Lmaccess/ns-lmaccess-localgroup_info_1)
-   [**LOCALGROUP\_INFO\_1002**](/windows/desktop/api/Lmaccess/ns-lmaccess-localgroup_info_1002)

Local group membership information is available at the following information levels:

-   [**LOCALGROUP\_MEMBERS\_INFO\_0**](/windows/desktop/api/Lmaccess/ns-lmaccess-localgroup_members_info_0)
-   [**LOCALGROUP\_MEMBERS\_INFO\_1**](/windows/desktop/api/Lmaccess/ns-lmaccess-localgroup_members_info_1)
-   [**LOCALGROUP\_MEMBERS\_INFO\_2**](/windows/desktop/api/Lmaccess/ns-lmaccess-localgroup_members_info_2)
-   [**LOCALGROUP\_MEMBERS\_INFO\_3**](/windows/desktop/api/Lmaccess/ns-lmaccess-localgroup_members_info_3)

You can retrieve the names of the local groups to which a user belongs by calling the [**NetUserGetLocalGroups**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusergetlocalgroups) function, specifying the following information level:

[**LOCALGROUP\_USERS\_INFO\_0**](/windows/desktop/api/Lmaccess/ns-lmaccess-localgroup_users_info_0)

For more information, see the network management [Group Functions](group-functions.md).

If you are programming for Active Directory, you may be able to call certain Active Directory Service Interface (ADSI) methods to achieve the same functionality you can achieve by calling the network management local group functions. For more information, see [**IADsGroup**](/windows/desktop/api/iads/nn-iads-iadsgroup).

 

 