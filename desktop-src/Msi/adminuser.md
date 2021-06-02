---
description: The installer sets this property if the user has administrator privileges.
ms.assetid: 2e7fd269-bd5f-40b7-b123-36b9c783a917
title: AdminUser property
ms.topic: reference
ms.date: 05/31/2018
---

# AdminUser property

The installer sets this property if the user has administrator privileges.

**Windows Server 2008 and Windows Vista:** The **AdminUser** property is the same as the [**Privileged**](privileged.md) property. Authors should used the **Privileged** property. The installer sets these properties if the user has administrator privileges, if the application has been assigned by a system administrator, or if both the user and machine policies AlwaysInstallElevated are set to true.

## Remarks

The differences between these properties may have been used in some legacy packages. For example, **AdminUser** may have been used instead of [**Privileged**](privileged.md) in conditional statements, because the installer only sets the **AdminUser** property if the user is an administrator. The installer sets the **Privileged** property if the user is an administrator, or if policy enables the user to install with elevated privileges.

**Windows Server 2008 and Windows Vista:** Not supported. The [**Privileged**](privileged.md) and **AdminUser** are the same. Packages that require distinct **Privileged** and **AdminUser** properties can restore the difference by setting the [**MSIUSEREALADMINDETECTION**](msiuserealadmindetection.md) property.

For more information, see [Installing a Package with Elevated Privileges for a Non-Admin](installing-a-package-with-elevated-privileges-for-a-non-admin.md), and [**Privileged**](privileged.md) property.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Vista or Windows Server 2008. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




