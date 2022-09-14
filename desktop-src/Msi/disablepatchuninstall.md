---
description: If this per-machine system policy is set to 1, patches cannot be removed from the computer by a user or an administrator.
ms.assetid: e964cb2b-ceaa-4122-bf54-cf1eeab4bc25
title: DisablePatchUninstall
ms.topic: article
ms.date: 05/31/2018
---

# DisablePatchUninstall

If this per-machine [system policy](system-policy.md) is set to 1, patches cannot be removed from the computer by a user or an administrator. The Windows Installer can still remove a patch that is no longer applicable to a product. If this policy is not set, a user can remove a patch from the computer only if the user has been granted privileges to remove the patch. This can depend on whether the user is an administrator, whether [DisableMsi](disablemsi.md) and [AlwaysInstallElevated](alwaysinstallelevated.md) policy settings are set, and whether the patch was installed in a per-user managed, per-user unmanaged, or per-machine context.

## Registry Key

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**

## Data Type

**REG\_DWORD**

## Related topics

<dl> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 



