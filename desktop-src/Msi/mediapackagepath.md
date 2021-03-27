---
description: If the installation package shipping with an application is not at the root of the CD-ROM that customers receive, the MEDIAPACKAGEPATH property must be set on the command line to the relative path of the application on the CD-ROM.For example, if the path to the package on the media is E:\\MyPath\\My.msi, then use MEDIAPACKAGEPATH=&\#0034;\\MyPath\\&\#0034;.Administrators may create CD-ROMs from an administrative installation point. If the location of the root of the installation is changed on the new CD-ROMs, the MEDIAPACKAGEPATH property must be set to the new path to install from this media. A source with a location on the CD-ROM different than what is specified in the package is unusable. It is not necessary, however, to use this property when creating an administrative installation point from shipping media.
ms.assetid: 18b3b19d-28e9-4311-9cc9-3e4224b4ddfe
title: MEDIAPACKAGEPATH property
ms.topic: reference
ms.date: 05/31/2018
---

# MEDIAPACKAGEPATH property

If the installation package shipping with an application is not at the root of the CD-ROM that customers receive, the **MEDIAPACKAGEPATH** property must be set on the command line to the relative path of the application on the CD-ROM.

For example, if the path to the package on the media is E:\\MyPath\\My.msi, then use MEDIAPACKAGEPATH="\\MyPath\\".

Administrators may create CD-ROMs from an administrative installation point. If the location of the root of the installation is changed on the new CD-ROMs, the **MEDIAPACKAGEPATH** property must be set to the new path to install from this media. A source with a location on the CD-ROM different than what is specified in the package is unusable. It is not necessary, however, to use this property when creating an administrative installation point from shipping media.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




