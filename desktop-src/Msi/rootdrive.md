---
description: The ROOTDRIVE property specifies the default drive for the destination directory of the installation.
ms.assetid: 9f36dc2a-2fb5-4787-a630-c7cc93ef51ec
title: ROOTDRIVE property
ms.topic: reference
ms.date: 05/31/2018
---

# ROOTDRIVE property

The **ROOTDRIVE** property specifies the default drive for the destination directory of the installation. If the Directory column of the [Directory table](directory-table.md) indicates the root destination directory by a property name that is undefined, the installer uses the value of the **ROOTDRIVE** property to resolve the path to the destination directory.

If **ROOTDRIVE** is not set at a command line or authored into the [Property table](property-table.md), the installer sets this property. During an [administrative installation](administrative-installation.md) the installer sets **ROOTDRIVE** to the first connected network drive it finds that can be written to. If it is not an administrative installation, or if the installer can find no network drives, the installer sets **ROOTDRIVE** to the local drive that can be written to having the most free space.

The value for this property must end with '\\'.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




