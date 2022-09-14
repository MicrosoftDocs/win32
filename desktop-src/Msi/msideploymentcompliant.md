---
description: The MSIDEPLOYMENTCOMPLIANT property can be set to indicate to the installer that the package has been authored and tested to comply with User Account Control (UAC) in Windows Vista.
ms.assetid: 7ee0dc56-bb9d-4a6e-aa3e-ae4c83f583d7
title: MSIDEPLOYMENTCOMPLIANT property
ms.topic: reference
ms.date: 05/31/2018
---

# MSIDEPLOYMENTCOMPLIANT property

The **MSIDEPLOYMENTCOMPLIANT** property can be set to indicate to the installer that the package has been authored and tested to comply with [*User Account Control*](u-gly.md) (UAC) in Windows Vista. If this property is not set, the installer will determine whether the package complies with UAC on Windows Vista.

For more information about UAC and Windows Installer, see [Using Windows Installer with UAC](using-windows-installer-with-uac.md) and [Guidelines for Packages](guidelines-for-packages.md).

**Windows Installer 3.1, Windows Installer 3.0 and Windows Installer 2.0:** This property is ignored. This property is only used by Windows Installer 4.0 in Windows Vista.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum service pack required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[Not Supported in Windows Installer 3.1 and earlier versions](not-supported-in-windows-installer-version-3-1.md)
</dt> </dl>

 

 




