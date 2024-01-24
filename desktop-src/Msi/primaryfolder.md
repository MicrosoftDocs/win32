---
description: The PRIMARYFOLDER is a global property that allows the author to designate a primary folder for the installation.
ms.assetid: 7ba776de-53e5-491a-917b-37778fe0c438
title: PRIMARYFOLDER property
ms.topic: reference
ms.date: 05/31/2018
---

# PRIMARYFOLDER property

The **PRIMARYFOLDER** is a global property that allows the author to designate a primary folder for the installation. The value for this property must be the key name of a directory that exists in the [Directory table](directory-table.md).

The installer uses the resolved path of the primary folder to determine which volume to use when setting the values of the [**PrimaryVolumePath**](primaryvolumepath.md) property, [**PrimaryVolumeSpaceAvailable**](primaryvolumespaceavailable.md) property, [**PrimaryVolumeSpaceRequired**](primaryvolumespacerequired.md) property, and [**PrimaryVolumeSpaceRemaining**](primaryvolumespaceremaining.md) property. The installer provides the values of these latter properties to users in the user interface to help them manage disk space. Commonly package authors can select the largest folder as the primary folder.

The value for this property must be the key name of a directory record found in the [Directory table](directory-table.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




