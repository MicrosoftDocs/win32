---
description: The TARGETDIR property specifies the root destination directory for the installation.
ms.assetid: 279bb9ad-afb6-406e-b74a-8424da177e6f
title: TARGETDIR property
ms.topic: reference
ms.date: 05/31/2018
---

# TARGETDIR property

The **TARGETDIR** property specifies the root destination directory for the installation. **TARGETDIR** must be the name of one root in the [Directory](directory-table.md) table. There may be only a single root destination directory. During an [administrative installation](administrative-installation.md) this property specifies the location to copy the installation package. During a non-administrative installation this property specifies the root destination directory.

To specify the root destination directory, set the Directory column of the Directory table to the **TARGETDIR** property and the DefaultDir column to the [**SourceDir**](sourcedir.md) property. If the **TARGETDIR** property is defined, the destination directory is resolved to the property's value. If the **TARGETDIR** property is undefined, the [**ROOTDRIVE**](rootdrive.md) property is used to resolve the path. For more information about using the **TARGETDIR** property, see [Using the Directory Table](using-the-directory-table.md).

Note that the value of the **TARGETDIR** property is typically set at the command line or through a user interface. Setting **TARGETDIR** by authoring a path into the [Property table](property-table.md) is not recommended because computers differ in the set up of the local drive.

For more information on how to change TARGETDIR during an installation see [Changing the Target Location for a Directory](changing-the-target-location-for-a-directory.md)

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




