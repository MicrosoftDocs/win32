---
description: Install a Windows Installer package with elevated (system) privileges.
ms.assetid: 0bbec06a-0a2b-430a-a361-317a319da615
title: AlwaysInstallElevated
ms.topic: article
ms.date: 05/31/2018
---

# AlwaysInstallElevated

You can use the AlwaysInstallElevated policy to install a Windows Installer package with elevated (system) privileges.

**Warning:  **

This option is equivalent to granting full administrative rights, which can pose a massive security risk. Microsoft strongly discourages the use of this setting.

To install a package with elevated (system) privileges, set the AlwaysInstallElevated value to "1" under both of the following registry keys:

**HKEY\_CURRENT\_USER**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**

If the AlwaysInstallElevated value is not set to "1" under both of the preceding registry keys, the installer uses elevated privileges to install managed applications and uses the current user's privilege level for unmanaged applications.

Because this policy permits users to install applications that require access to directories and registry keys for which the user may not have permission to view or change, you should consider whether it provides your users with an appropriate level of security. Setting this policy directs Windows Installer to use system permissions when it installs the application on the system. If this policy is not set, applications not distributed by the administrator are installed using the user's privileges and only managed applications get elevated privileges.

Note that once the per-machine policy for AlwaysInstallElevated is enabled, any user can set their per-user setting.

## Remarks

For information about the interaction of this policy with installation sources, see [Managing Installation Sources](managing-installation-sources.md).

## Data Type

**REG\_DWORD**

 

 



