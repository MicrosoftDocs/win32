---
description: On Windows 2000 and later operating systems, the installer sets the MsiNTSuiteWebServer property to 1 if the installer is running on a web edition of the Windows Server 2003.
ms.assetid: de462ba2-4654-4f47-9dd7-3bc9c6f0af0e
title: MsiNTSuiteWebServer property
ms.topic: reference
ms.date: 05/31/2018
---

# MsiNTSuiteWebServer property

On Windows 2000 and later operating systems, the installer sets the **MsiNTSuiteWebServer** property to 1 if the installer is running on a web edition of the Windows Server 2003. The installer sets this property to 1 only if the VER\_SUITE\_BLADE flag is set in the [**OSVERSIONINFOEX**](/windows/win32/api/winnt/ns-winnt-osversioninfoexa) structure. Otherwise the installer does not set this property.

## Remarks

This property is available only with the Windows Server 2003 release of the installer.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 
