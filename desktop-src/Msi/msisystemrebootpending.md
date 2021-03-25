---
description: The installer sets the value of the MsiSystemRebootPending property to 1 if there is an operation pending to rename a file.
ms.assetid: 8bbbf42e-fb55-4e5d-a574-2c3aaa87a73a
title: MsiSystemRebootPending property
ms.topic: reference
ms.date: 05/31/2018
---

# MsiSystemRebootPending property

The installer sets the value of the **MsiSystemRebootPending** property to 1 if there is an operation pending to rename a file.

Package authors can base a condition in the [LaunchCondition table](launchcondition-table.md) on this property to prevent the installation of their package in cases where there is an operation pending to rename a file. This may be done to prevent a restart of the operating system caused by the renaming of the file. The installer does not set the **MsiSystemRebootPending** property in all cases that require a restart of the system.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer 4.5 on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[System Reboots](system-reboots.md)
</dt> <dt>

[Not Supported in Windows Installer 3.1 and earlier versions](not-supported-in-windows-installer-version-3-1.md)
</dt> </dl>

 

 




