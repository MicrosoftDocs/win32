---
description: Windows Installer is integrated with Software Restriction Policy in Microsoft Windows XP.
ms.assetid: b1e58336-8908-45ee-86f0-81b2314fa77a
title: Windows Installer and Software Restriction Policy
ms.topic: article
ms.date: 05/31/2018
---

# Windows Installer and Software Restriction Policy

Windows Installer is integrated with Software Restriction Policy in Microsoft Windows XP. Software Restriction Policy is configurable through group policy. Software Restriction Policy allows an administrator to restrict both administrators and nonadministrators from running files based upon the path, URL zone, hash, or publisher criteria. Software Restriction Policy has two levels: unrestricted and disallowed. The Windows Installer only installs packages allowed to run at the unrestricted level.

Patches or transforms must also be allowed to run at the unrestricted level. If a package, patch, or transform is configured to run at a level different from unrestricted, the Windows Installer displays an error message and logs an entry in the application event log. Software restriction policy is evaluated the first time an application is installed, when a new patch is applied, and when the installation package is re-cached.

If a package, patch, or transform is restricted, the Windows Installer displays an error message and writes an [Event Logging](event-logging.md) entry in the application event log. Software restriction policy is evaluated the first time an application is installed, when a new patch is applied, and when the installation package is re-cached.

For more information on software restriction policy, consult the product documentation and [Microsoft Q&A](/answers/).

 

 



