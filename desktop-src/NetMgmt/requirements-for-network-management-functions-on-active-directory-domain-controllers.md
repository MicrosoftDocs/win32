---
title: Requirements for Network Management Functions on Active Directory Domain Controllers
description: If you call one of the network management functions listed in this topic on a domain controller running Active Directory, access to a securable object is allowed or denied based on the access-control list (ACL) for the object.
ms.assetid: 4dfb3180-3ca5-4e22-b7a1-4e6b132431fb
ms.topic: article
ms.date: 05/31/2018
---

# Requirements for Network Management Functions on Active Directory Domain Controllers

If you call one of the network management functions listed in this topic on a domain controller running Active Directory, access to a [securable object](/windows/desktop/SecAuthZ/securable-objects) is allowed or denied based on the [access-control list](/windows/desktop/SecAuthZ/access-control-lists) (ACL) for the object. (ACLs are specified in the directory.)

Different access requirements apply to information queries and information updates.

## Queries

For queries, the default ACL permits all authenticated users and members of the "[Pre-Windows 2000 compatible access](/windows/desktop/SecAuthZ/allowing-anonymous-access)" group to read and enumerate information. The functions listed following are affected:

-   [**NetGroupEnum**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupenum), [**NetGroupGetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupgetinfo), [**NetGroupGetUsers**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupgetusers)
-   [**NetLocalGroupEnum**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupenum), [**NetLocalGroupGetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupgetinfo), [**NetLocalGroupGetMembers**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupgetmembers)
-   [**NetQueryDisplayInformation**](/windows/desktop/api/Lmaccess/nf-lmaccess-netquerydisplayinformation)
-   [**NetSessionGetInfo**](/windows/desktop/api/lmshare/nf-lmshare-netsessiongetinfo) (levels 1 and 2 only)
-   [**NetShareEnum**](/windows/desktop/api/lmshare/nf-lmshare-netshareenum) (levels 2 and 502 only)
-   [**NetUserEnum**](/windows/desktop/api/Lmaccess/nf-lmaccess-netuserenum), [**NetUserGetGroups**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusergetgroups), [**NetUserGetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusergetinfo), [**NetUserGetLocalGroups**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusergetlocalgroups), [**NetUserModalsGet**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusermodalsget)
-   [**NetWkstaGetInfo**](/windows/desktop/api/Lmwksta/nf-lmwksta-netwkstagetinfo), [**NetWkstaUserEnum**](/windows/desktop/api/Lmwksta/nf-lmwksta-netwkstauserenum)

Anonymous access to group information requires that the user Anonymous be explicitly added to the "Pre-Windows 2000 compatible access" group. This is because anonymous tokens do not include the Everyone Group SID.

**Windows 2000:** By default, the "Pre-Windows 2000 compatible access" group includes Everyone as a member. This enables anonymous access (Anonymous Logon) to information if the system allows anonymous access. Administrators can remove Everyone from the "Pre-Windows 2000 Compatible Access" group at any time. Removing Everyone from the group restricts information access to authenticated users only. For more information about anonymous access, see [Security Identifiers](/windows/desktop/SecAuthZ/security-identifiers) and [Well-Known SIDs](/windows/desktop/SecAuthZ/well-known-sids).

You can override the system default by setting the following key in the registry to the value 1:

**HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Lsa**\\**EveryoneIncludesAnonymous** = 1

See [**NetWkstaGetInfo**](/windows/desktop/api/Lmwksta/nf-lmwksta-netwkstagetinfo) and [**NetWkstaUserEnum**](/windows/desktop/api/Lmwksta/nf-lmwksta-netwkstauserenum) for additional information about anonymous access to group information when calling these two functions.

## Updates

For updates, the default ACL permits only Domain Administrators and Account Operators to write information. One exception is that users can change their own password and set the usri\*\_usr\_comment field. Another exception is that Account Operators cannot modify administration accounts. The functions listed following are affected:

-   [**NetGroupAdd**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupadd), [**NetGroupAddUser**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupadduser), [**NetGroupDel**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupdel), [**NetGroupDelUser**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupdeluser), [**NetGroupSetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupsetinfo), [**NetGroupSetUsers**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupsetusers)
-   [**NetLocalGroupAdd**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupadd), [**NetLocalGroupAddMembers**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupaddmembers), [**NetLocalGroupDel**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupdel), [**NetLocalGroupDelMembers**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupdelmembers), [**NetLocalGroupSetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupsetinfo), [**NetLocalGroupSetMembers**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupsetmembers)
-   [**NetMessageBufferSend**](/windows/desktop/api/Lmmsg/nf-lmmsg-netmessagebuffersend)
-   [**NetUserAdd**](/windows/desktop/api/Lmaccess/nf-lmaccess-netuseradd), [**NetUserChangePassword**](/windows/desktop/api/Lmaccess/nf-lmaccess-netuserchangepassword), [**NetUserDel**](/windows/desktop/api/Lmaccess/nf-lmaccess-netuserdel), [**NetUserModalsSet**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusermodalsset), [**NetUserSetGroups**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusersetgroups), [**NetUserSetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusersetinfo)

Typically, callers must have write access to the entire object for calls to [**NetUserModalsSet**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusermodalsset), [**NetUserSetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusersetinfo), [**NetGroupSetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupsetinfo) and [**NetLocalGroupSetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupsetinfo) to succeed. For finer access control, you should consider using ADSI. For more information about ADSI, see [Active Directory Service Interfaces](/windows/desktop/ADSI/active-directory-service-interfaces-adsi).

For more information about controlling access to securable objects, see [Access Control](/windows/desktop/SecAuthZ/access-control), [Privileges](/windows/desktop/SecAuthZ/privileges), and [Securable Objects](/windows/desktop/SecAuthZ/securable-objects). For more information about calling functions that require administrator privileges, see [Running with Special Privileges](/windows/desktop/SecBP/running-with-special-privileges).

 

 