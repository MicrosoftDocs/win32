---
description: The Privileged property indicates whether the installation is performed in the context of elevated privileges.
ms.assetid: 483ab73a-3ff7-4111-a6b5-eac990d85bd7
title: Privileged property
ms.topic: reference
ms.date: 05/31/2018
---

# Privileged property

The **Privileged** property indicates whether the installation is performed in the context of elevated privileges. The installer sets this property if the user has administrator privileges, if the application has been assigned by a system administrator, or if both the user and machine policies AlwaysInstallElevated are set to true.

## Default Value

The installer does not set this property if the user is not allowed to install with elevated privileges.

## Remarks

Developers of installer packages can use the **Privileged** property to make the installation conditional upon system policy, the user being an administrator, or assignment by an administrator.

When running on Windows Vista, the **Privileged** and [**AdminUser**](adminuser.md) are the same.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




