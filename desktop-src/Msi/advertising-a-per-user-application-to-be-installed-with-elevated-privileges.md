---
description: 'To advertise an application on a per-user installation basis when the application requires elevated (that is, system) privileges for installation, use the guidelines in the following list:'
ms.assetid: 0d2bd2d9-0eac-4519-862c-15f0ee5cbc40
title: Advertising a Per-User Application To Be Installed with Elevated Privileges
ms.topic: article
ms.date: 05/31/2018
---

# Advertising a Per-User Application To Be Installed with Elevated Privileges

To advertise an application on a per-user installation basis when the application requires elevated (that is, system) privileges for installation, use the guidelines in the following list:

-   Your process must be a service that runs under the LocalSystem system account on Windows XP or later.
-   Generate an advertise script by calling [**MsiAdvertiseProduct**](/windows/desktop/api/Msi/nf-msi-msiadvertiseproducta) or [**MsiAdvertiseProductEx**](/windows/desktop/api/Msi/nf-msi-msiadvertiseproductexa).
-   Your process must impersonate the user that is the target for the advertisement.
-   Call [**MsiAdvertiseScript**](/windows/desktop/api/Msi/nf-msi-msiadvertisescripta), and use the flags SCRIPTFLAGS\_CACHEINFO \| SCRIPTFLAGS\_REGDATA\_APPINFO \| SCRIPTFLAGS\_REGDATA\_CNFGINFO \| SCRIPTFLAGS\_SHORTCUTS.

When you follow the guidelines, you advertise an application to a specified user, and when the user chooses to install, the application is installed with elevated privileges.

## Related topics

<dl> <dt>

[Patching Per-User Managed Applications](patching-per-user-managed-applications.md)
</dt> </dl>

 

 



