---
description: The MsiWin32AssemblySupport property indicates whether the computer supports Win32 assemblies.
ms.assetid: 037202b6-41e4-4631-abbe-11291a5e5000
title: MsiWin32AssemblySupport property
ms.topic: reference
ms.date: 05/31/2018
---

# MsiWin32AssemblySupport property

The **MsiWin32AssemblySupport** property indicates whether the computer supports Win32 assemblies. On systems that support Win32 assemblies, the installer sets the value of **MsiWin32AssemblySupport** to the file version of sxs.dll. The installer does not set this property if the operating system does not support Win32 assemblies. For more information, see [Assemblies](assemblies.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




