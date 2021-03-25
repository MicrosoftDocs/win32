---
description: The installer sets the ProgramFiles64Folder property to the full path of the predefined 64-bit Program Files folder. The existing ProgramFilesFolder property is set to the corresponding 32-bit folder.
ms.assetid: 9301628a-3d56-4d0a-aab5-88663742daa1
title: ProgramFiles64Folder property
ms.topic: reference
ms.date: 05/31/2018
---

# ProgramFiles64Folder property

The installer sets the **ProgramFiles64Folder** property to the full path of the predefined 64-bit Program Files folder. The existing [**ProgramFilesFolder**](programfilesfolder.md) property is set to the corresponding 32-bit folder.

## Remarks

The installer sets this property. For example, on 64-bit Windows, the value may be C:\\Program Files. This property is not used on 32-bit Windows.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




