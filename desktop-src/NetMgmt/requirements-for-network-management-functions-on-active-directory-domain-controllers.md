---
title: Requirements for Network Management Functions on Active Directory Domain Controllers
description: If you call one of the network management functions listed in this topic on a domain controller running Active Directory, access to a securable object is allowed or denied based on the access-control list (ACL) for the object.
ms.assetid: '4dfb3180-3ca5-4e22-b7a1-4e6b132431fb'
---

# Requirements for Network Management Functions on Active Directory Domain Controllers

If you call one of the network management functions listed in this topic on a domain controller running Active Directory, access to a [securable object](https://msdn.microsoft.com/library/windows/desktop/aa379557) is allowed or denied based on the [access-control list](https://msdn.microsoft.com/library/windows/desktop/aa374872) (ACL) for the object. (ACLs are specified in the directory.)

Different access requirements apply to information queries and information updates.

## Queries

For queries, the default ACL permits all authenticated users and members of the "[Pre-Windows 2000 compatible access](https://msdn.microsoft.com/library/windows/desktop/aa375347)" group to read and enumerate information. The functions listed following are affected:

-   [**NetGroupEnum**](netgroupenum.md), [**NetGroupGetInfo**](netgroupgetinfo.md), [**NetGroupGetUsers**](netgroupgetusers.md)
-   [**NetLocalGroupEnum**](netlocalgroupenum.md), [**NetLocalGroupGetInfo**](netlocalgroupgetinfo.md), [**NetLocalGroupGetMembers**](netlocalgroupgetmembers.md)
-   [**NetQueryDisplayInformation**](netquerydisplayinformation.md)
-   [**NetSessionGetInfo**](https://msdn.microsoft.com/library/windows/desktop/bb525383) (levels 1 and 2 only)
-   [**NetShareEnum**](https://msdn.microsoft.com/library/windows/desktop/bb525387) (levels 2 and 502 only)
-   [**NetUserEnum**](netuserenum.md), [**NetUserGetGroups**](netusergetgroups.md), [**NetUserGetInfo**](netusergetinfo.md), [**NetUserGetLocalGroups**](netusergetlocalgroups.md), [**NetUserModalsGet**](netusermodalsget.md)
-   [**NetWkstaGetInfo**](netwkstagetinfo.md), [**NetWkstaUserEnum**](netwkstauserenum.md)

Anonymous access to group information requires that the user Anonymous be explicitly added to the "Pre-Windows 2000 compatible access" group. This is because anonymous tokens do not include the Everyone Group SID.

**Windows 2000:** By default, the "Pre-Windows 2000 compatible access" group includes Everyone as a member. This enables anonymous access (Anonymous Logon) to information if the system allows anonymous access. Administrators can remove Everyone from the "Pre-Windows 2000 Compatible Access" group at any time. Removing Everyone from the group restricts information access to authenticated users only. For more information about anonymous access, see [Security Identifiers](https://msdn.microsoft.com/library/windows/desktop/aa379571) and [Well-Known SIDs](https://msdn.microsoft.com/library/windows/desktop/aa379649).

You can override the system default by setting the following key in the registry to the value 1:

**HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Lsa**\\**EveryoneIncludesAnonymous** = 1

See [**NetWkstaGetInfo**](netwkstagetinfo.md) and [**NetWkstaUserEnum**](netwkstauserenum.md) for additional information about anonymous access to group information when calling these two functions.

## Updates

For updates, the default ACL permits only Domain Administrators and Account Operators to write information. One exception is that users can change their own password and set the usri\*\_usr\_comment field. Another exception is that Account Operators cannot modify administration accounts. The functions listed following are affected:

-   [**NetGroupAdd**](netgroupadd.md), [**NetGroupAddUser**](netgroupadduser.md), [**NetGroupDel**](netgroupdel.md), [**NetGroupDelUser**](netgroupdeluser.md), [**NetGroupSetInfo**](netgroupsetinfo.md), [**NetGroupSetUsers**](netgroupsetusers.md)
-   [**NetLocalGroupAdd**](netlocalgroupadd.md), [**NetLocalGroupAddMembers**](netlocalgroupaddmembers.md), [**NetLocalGroupDel**](netlocalgroupdel.md), [**NetLocalGroupDelMembers**](netlocalgroupdelmembers.md), [**NetLocalGroupSetInfo**](netlocalgroupsetinfo.md), [**NetLocalGroupSetMembers**](netlocalgroupsetmembers.md)
-   [**NetMessageBufferSend**](netmessagebuffersend.md)
-   [**NetUserAdd**](netuseradd.md), [**NetUserChangePassword**](netuserchangepassword.md), [**NetUserDel**](netuserdel.md), [**NetUserModalsSet**](netusermodalsset.md), [**NetUserSetGroups**](netusersetgroups.md), [**NetUserSetInfo**](netusersetinfo.md)

Typically, callers must have write access to the entire object for calls to [**NetUserModalsSet**](netusermodalsset.md), [**NetUserSetInfo**](netusersetinfo.md), [**NetGroupSetInfo**](netgroupsetinfo.md) and [**NetLocalGroupSetInfo**](netlocalgroupsetinfo.md) to succeed. For finer access control, you should consider using ADSI. For more information about ADSI, see [Active Directory Service Interfaces](https://msdn.microsoft.com/library/aa772170).

For more information about controlling access to securable objects, see [Access Control](https://msdn.microsoft.com/library/windows/desktop/aa374860), [Privileges](https://msdn.microsoft.com/library/windows/desktop/aa379306), and [Securable Objects](https://msdn.microsoft.com/library/windows/desktop/aa379557). For more information about calling functions that require administrator privileges, see [Running with Special Privileges](https://msdn.microsoft.com/library/windows/desktop/ms717802).

 

 




