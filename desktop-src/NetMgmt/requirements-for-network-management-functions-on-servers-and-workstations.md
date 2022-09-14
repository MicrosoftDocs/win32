---
title: Requirements for Network Management Functions on Servers and Workstations
description: If you call one of the network management functions listed in this topic on a server or workstation, different access requirements apply to information queries and information updates.
ms.assetid: 05ff1771-8058-4c86-8f45-735bf41dc128
ms.topic: article
ms.date: 05/31/2018
---

# Requirements for Network Management Functions on Servers and Workstations

If you call one of the network management functions listed in this topic on a server or workstation, different access requirements apply to information queries and information updates.

## Queries

If you call one of the following functions to perform a query on a server or workstation, by default, all authenticated users can read and enumerate the information.

-   [**NetGroupEnum**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupenum), [**NetGroupGetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupgetinfo), [**NetGroupGetUsers**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupgetusers)
-   [**NetLocalGroupEnum**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupenum), [**NetLocalGroupGetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupgetinfo), [**NetLocalGroupGetMembers**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupgetmembers)
-   [**NetQueryDisplayInformation**](/windows/desktop/api/Lmaccess/nf-lmaccess-netquerydisplayinformation)
-   [**NetSessionGetInfo**](/windows/desktop/api/lmshare/nf-lmshare-netsessiongetinfo) (levels 1 and 2 only)
-   [**NetShareEnum**](/windows/desktop/api/lmshare/nf-lmshare-netshareenum) (levels 2 and 502 only)
-   [**NetUserEnum**](/windows/desktop/api/Lmaccess/nf-lmaccess-netuserenum), [**NetUserGetGroups**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusergetgroups), [**NetUserGetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusergetinfo), [**NetUserGetLocalGroups**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusergetlocalgroups), [**NetUserModalsGet**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusermodalsget)
-   [**NetWkstaGetInfo**](/windows/desktop/api/Lmwksta/nf-lmwksta-netwkstagetinfo), [**NetWkstaUserEnum**](/windows/desktop/api/Lmwksta/nf-lmwksta-netwkstauserenum)

Following is additional information about anonymous access when reading and enumerating information.

**Windows Server 2003 and Windows XP:** Anonymous access to information is possible if the EveryoneIncludesAnonymous policy setting allows anonymous access.

**Windows 2000:** Anonymous access to securable objects is possible if the RestrictAnonymous policy setting allows anonymous access. You can restrict anonymous access by setting the following key in the registry to the value 1.

**HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\Lsa**\\**RestrictAnonymous** = 1


## Updates

By default, only Administrators and Power Users can write information.

For more information about controlling access to securable objects, see [Access Control](/windows/desktop/SecAuthZ/access-control), [Privileges](/windows/desktop/SecAuthZ/privileges), and [Securable Objects](/windows/desktop/SecAuthZ/securable-objects). For more information about calling functions that require administrator privileges, see [Running with Special Privileges](/windows/desktop/SecBP/running-with-special-privileges).

 

 
