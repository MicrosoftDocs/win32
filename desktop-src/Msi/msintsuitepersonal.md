---
description: On Windows XP and later operating systems, the installer sets the MsiNTSuitePersonal property to 1 if the operating system is Windows XP Home Edition.
ms.assetid: 324a4c45-bd64-4361-90ba-6a0554a9c5ef
title: MsiNTSuitePersonal property
ms.topic: reference
ms.date: 05/31/2018
---

# MsiNTSuitePersonal property

On Windows XP and later operating systems, the installer sets the **MsiNTSuitePersonal** property to 1 if the operating system is Windows XP Home Edition. The installer sets this property to 1 only if the VER\_SUITE\_PERSONAL flag is set in the [**OSVERSIONINFOEX**](/windows/win32/api/winnt/ns-winnt-osversioninfoexa) structure. Otherwise the installer does not set this property.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 
