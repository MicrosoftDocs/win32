---
title: Requirements for Network Management Functions on Servers and Workstations
description: If you call one of the network management functions listed in this topic on a server or workstation, different access requirements apply to information queries and information updates.
ms.assetid: 05ff1771-8058-4c86-8f45-735bf41dc128
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Requirements for Network Management Functions on Servers and Workstations

If you call one of the network management functions listed in this topic on a server or workstation, different access requirements apply to information queries and information updates.

## Queries

If you call one of the following functions to perform a query on a server or workstation, by default, all authenticated users can read and enumerate the information.

-   [**NetGroupEnum**](/windows/win32/Lmaccess/nf-lmaccess-netgroupenum?branch=master), [**NetGroupGetInfo**](/windows/win32/Lmaccess/nf-lmaccess-netgroupgetinfo?branch=master), [**NetGroupGetUsers**](/windows/win32/Lmaccess/nf-lmaccess-netgroupgetusers?branch=master)
-   [**NetLocalGroupEnum**](/windows/win32/Lmaccess/nf-lmaccess-netlocalgroupenum?branch=master), [**NetLocalGroupGetInfo**](/windows/win32/Lmaccess/nf-lmaccess-netlocalgroupgetinfo?branch=master), [**NetLocalGroupGetMembers**](/windows/win32/Lmaccess/nf-lmaccess-netlocalgroupgetmembers?branch=master)
-   [**NetQueryDisplayInformation**](/windows/win32/Lmaccess/nf-lmaccess-netquerydisplayinformation?branch=master)
-   [**NetSessionGetInfo**](https://msdn.microsoft.com/library/windows/desktop/bb525383) (levels 1 and 2 only)
-   [**NetShareEnum**](https://msdn.microsoft.com/library/windows/desktop/bb525387) (levels 2 and 502 only)
-   [**NetUserEnum**](/windows/win32/Lmaccess/nf-lmaccess-netuserenum?branch=master), [**NetUserGetGroups**](/windows/win32/Lmaccess/nf-lmaccess-netusergetgroups?branch=master), [**NetUserGetInfo**](/windows/win32/Lmaccess/nf-lmaccess-netusergetinfo?branch=master), [**NetUserGetLocalGroups**](/windows/win32/Lmaccess/nf-lmaccess-netusergetlocalgroups?branch=master), [**NetUserModalsGet**](/windows/win32/Lmaccess/nf-lmaccess-netusermodalsget?branch=master)
-   [**NetWkstaGetInfo**](/windows/win32/Lmwksta/nf-lmwksta-netwkstagetinfo?branch=master), [**NetWkstaUserEnum**](/windows/win32/Lmwksta/nf-lmwksta-netwkstauserenum?branch=master)

Following is additional information about anonymous access when reading and enumerating information.

**Windows Server 2003 and Windows XP:** Anonymous access to information is possible if the EveryoneIncludesAnonymous policy setting allows anonymous access.

**Windows 2000:** Anonymous access to securable objects is possible if the RestrictAnonymous policy setting allows anonymous access. You can restrict anonymous access by setting the following key in the registry to the value 1.

**HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\Lsa**\\**RestrictAnonymous** = 1

For more information, see the following article in the Microsoft Knowledge Base:

ARTICLE ID: [Q246261](Http://go.microsoft.com/fwlink/p/?linkid=83997)

TITLE: How to use the RestrictAnonymous registry Value.

## Updates

By default, only Administrators and Power Users can write information.

For more information about controlling access to securable objects, see [Access Control](https://msdn.microsoft.com/library/windows/desktop/aa374860), [Privileges](https://msdn.microsoft.com/library/windows/desktop/aa379306), and [Securable Objects](https://msdn.microsoft.com/library/windows/desktop/aa379557). For more information about calling functions that require administrator privileges, see [Running with Special Privileges](https://msdn.microsoft.com/library/windows/desktop/ms717802).

 

 




