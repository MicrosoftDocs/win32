---
title: Local Group Functions
description: A local group can contain user accounts or global group accounts from one or more domains. (Global groups can contain users from only one domain.) A local group shares common privileges and rights only within its own domain.
ms.assetid: 'ed4c59d6-6532-4190-9807-95678053fc72'
---

# Local Group Functions

A *local group* can contain user accounts or global group accounts from one or more domains. (Global groups can contain users from only one domain.) A local group shares common privileges and rights only within its own domain.

The network management local group functions control members of local groups in a way that the functions can only be called locally on the system on which the local group is defined. On a workstation, or on a server that is not a domain controller, you can use only a local group defined on that system.

In Active Directory, domains that are in native mode, local groups are called *domain local groups*. Domain local groups are available on all domain controllers, member servers, and workstations joined to the domain. Active Directory mixed-mode domains are defined on the primary domain controller and replicated to all other domain controllers in the domain. Therefore, a local group is available on all domain controllers within the domain in which it was created..

The local group functions create or delete local groups, and review or adjust the memberships of local groups. These functions are listed following.



| Function                                                   | Description                                                             |
|------------------------------------------------------------|-------------------------------------------------------------------------|
| [**NetLocalGroupAdd**](netlocalgroupadd.md)               | Creates a local group.                                                  |
| [**NetLocalGroupAddMembers**](netlocalgroupaddmembers.md) | Adds one or more users or global groups to an existing local group.     |
| [**NetLocalGroupDel**](netlocalgroupdel.md)               | Deletes a local group, removing all existing members from the group.    |
| [**NetLocalGroupDelMembers**](netlocalgroupdelmembers.md) | Removes one or more members from an existing local group.               |
| [**NetLocalGroupEnum**](netlocalgroupenum.md)             | Returns information about each local group account on a server.         |
| [**NetLocalGroupGetInfo**](netlocalgroupgetinfo.md)       | Returns information about a particular local group account on a server. |
| [**NetLocalGroupGetMembers**](netlocalgroupgetmembers.md) | Lists all members of a specified local group.                           |
| [**NetLocalGroupSetInfo**](netlocalgroupsetinfo.md)       | Sets general information about a local group.                           |
| [**NetLocalGroupSetMembers**](netlocalgroupsetmembers.md) | Assigns members to a local group.                                       |



 

You can add a member to a local group by specifying the security identifier (SID) of the member. To translate a member account name to a SID, call the [**LookupAccountName**](https://msdn.microsoft.com/library/windows/desktop/aa379159) function.

When you create a local group by calling the [**NetLocalGroupAdd**](netlocalgroupadd.md) function, you must supply a local group name. Initially, the local group has no members.

Local group account information is available at the following levels:

-   [**LOCALGROUP\_INFO\_0**](localgroup-info-0-str.md)
-   [**LOCALGROUP\_INFO\_1**](localgroup-info-1-str.md)
-   [**LOCALGROUP\_INFO\_1002**](localgroup-info-1002-str.md)

Local group membership information is available at the following information levels:

-   [**LOCALGROUP\_MEMBERS\_INFO\_0**](localgroup-members-info-0-str.md)
-   [**LOCALGROUP\_MEMBERS\_INFO\_1**](localgroup-members-info-1-str.md)
-   [**LOCALGROUP\_MEMBERS\_INFO\_2**](localgroup-members-info-2-str.md)
-   [**LOCALGROUP\_MEMBERS\_INFO\_3**](localgroup-members-info-3-str.md)

You can retrieve the names of the local groups to which a user belongs by calling the [**NetUserGetLocalGroups**](netusergetlocalgroups.md) function, specifying the following information level:

[**LOCALGROUP\_USERS\_INFO\_0**](localgroup-users-info-0-str.md)

For more information, see the network management [Group Functions](group-functions.md).

If you are programming for Active Directory, you may be able to call certain Active Directory Service Interface (ADSI) methods to achieve the same functionality you can achieve by calling the network management local group functions. For more information, see [**IADsGroup**](https://msdn.microsoft.com/library/aa706021).

 

 




