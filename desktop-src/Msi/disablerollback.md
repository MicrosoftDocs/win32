---
description: If this system policy is set to 1, the installer does not store rollback files during installation and disables installation rollback.
ms.assetid: 01747de6-7478-4403-ba36-8ff1abc2b70f
title: DisableRollback
ms.topic: article
ms.date: 05/31/2018
---

# DisableRollback

If this [system policy](system-policy.md) is set to 1, the installer does not store rollback files during installation and disables installation rollback. By default, rollback is enabled. Administrators are advised to not use this policy unless it is absolutely essential. For more information, see [Rollback Installation](rollback-installation.md).

## Registry Key

To disable rollback for per-user installations, set **DisableRollback** to 1 under the following registry key:

**HKEY\_CURRENT\_USER**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**

To disable rollback for per-computer installations, set **DisableRollback** to 1 under the following registry key.

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**

## Data Type

**REG\_DWORD**

 

 



