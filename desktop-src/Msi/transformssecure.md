---
description: Setting the TRANSFORMSSECURE property to 1 informs the installer that transforms are to be cached locally on the user's computer in a location where the user does not have write access.
ms.assetid: 414025c3-7b83-42c7-9954-7393fba06061
title: TRANSFORMSSECURE property
ms.topic: reference
ms.date: 05/31/2018
---

# TRANSFORMSSECURE property

Setting the **TRANSFORMSSECURE** property to 1 informs the installer that transforms are to be cached locally on the user's computer in a location where the user does not have write access. Setting this property is like setting the [TransformsSecure policy](transformssecure-policy.md) except that the scope is different. Setting TransformsSecure policy applies to all packages installed by a given user. Setting the **TRANSFORMSSECURE** property applies to the package regardless of the user.

The purpose of this property is to provide for secure transform storage with traveling users of Windows 2000. When this property is set, a [maintenance installation](maintenance-installation.md) can only use the transform from the specified path. If the path is not available the maintenance installation fails. A source for each secure transform must therefore reside at the location of the source of the installation package. Then if the installer finds that the transform is missing on the local computer, it can restore the transform from this source.

## Remarks

Windows Installer interprets the [**TRANSFORMSATSOURCE**](transformsatsource.md) property to be the same as the **TRANSFORMSSECURE** property.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[Database Transforms](database-transforms.md)
</dt> </dl>

 

 




