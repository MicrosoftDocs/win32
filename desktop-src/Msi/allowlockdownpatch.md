---
description: If this per-machine system policy is not set, only administrators can patch existing products that were installed using elevated privileges.
ms.assetid: cd07dcb0-b9b5-4186-a916-604c40f88b5f
title: AllowLockdownPatch
ms.topic: article
ms.date: 05/31/2018
---

# AllowLockdownPatch

If this per-machine [system policy](system-policy.md) is not set, only administrators can patch existing products that were installed using elevated privileges. If AllowLockdownPatch is set to "1", nonadministrative users can, in some cases, apply patches to products while running an installation using elevated privileges. With the policy set, the patch can install [minor upgrades](minor-upgrades.md) while running an installation using elevated privileges, the patch cannot install [major upgrades](major-upgrades.md). Setting this policy also enables nonadministrative users to run programs at LocalSystem privileges during an elevated installation.

The default setting is recommended to ensure a secure environment.

## Registry Key

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**

## Data Type

**REG\_DWORD**

## Remarks

Any user can apply a patch during a nonelevated installation. Setting this per-machine [system policy](system-policy.md) to "1" gives nonadministrative users the additional flexibility of applying patches to any product during an elevated installation. If this policy is not set, nonadministrative users cannot apply a patch to assigned or published applications.

Setting this policy also enables nonadministrative users to run arbitrary programs at LocalSystem privileges if they have a Windows Installer patch package that installs or launches those programs.

 

 



