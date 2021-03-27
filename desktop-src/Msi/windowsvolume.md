---
description: The installer sets the WindowsVolume property to the volume of the windows folder.
ms.assetid: 56b78c88-ef58-4474-92ad-b42fe49a2f30
title: WindowsVolume property
ms.topic: reference
ms.date: 05/31/2018
---

# WindowsVolume property

The installer sets the **WindowsVolume** property to the volume of the windows folder. The property always ends with a backslash. This can be used to set the default location to the volume the Windows folder is on because the [**ROOTDRIVE**](rootdrive.md) property does not necessarily equal this drive.

## Remarks

Do not use the **WindowsVolume** property in the Directory column of the [Directory](directory-table.md) table. The [**WindowsFolder**](windowsfolder.md) property contains the path to the Windows folder.

## Requirements



| Requirement | Value |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




