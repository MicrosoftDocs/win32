---
description: This is a per-machine system policy that can be used when the administrator only wants per-machine applications installed.
ms.assetid: 3afa1d89-b76b-4184-b0d7-25cbf6749c7f
title: DisableUserInstalls
ms.topic: article
ms.date: 05/31/2018
---

# DisableUserInstalls

This is a per-machine [system policy](system-policy.md) that can be used when the administrator only wants per-machine applications installed.

If this policy is not set, the installer searches the registry for applications in the following order: managed applications registered as per-user, unmanaged applications registered as per-user, and finally applications registered as per-machine.

If this policy is set to 1, the installer ignores all applications registered as per-user and only searches for applications registered as per-machine. Calls to the Windows Installer application programming interface or system ignore per-user applications. An attempt to perform an installation in the per-user [installation context](installation-context.md) causes the installer to display an error message and stops the installation. In this case, the Windows Installer also prevents per-user installations from a terminal server.

## Registry Key

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**

## Data Type

**REG\_DWORD**

 

 



