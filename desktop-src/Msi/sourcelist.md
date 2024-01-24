---
description: The SOURCELIST property is a semicolon-delimited list of network or URL source paths to the application's installation package.
ms.assetid: '9dc1e195-a108-4f8f-b008-e08fc7658fc0'
title: SOURCELIST property
ms.topic: article
ms.date: 05/31/2018
---

# SOURCELIST property

The **SOURCELIST** property is a semicolon-delimited list of network or URL source paths to the application's installation package. This list is appended to the end of each user's existing source list for the application. The installer locates a source by enumerating the list of source paths and uses the first accessible location it finds. Only this source can be used for the remainder of the installation. Each path specified in the source list must therefore be to a location having a complete source for the application. The entire directory tree at each source location must be the same and must include all of the required source files, including any cabinets. Each location must have an .msi file with the same file name and product code.

## Default Value

The installer only checks the **SOURCELIST** property if the product has not already been advertised or installed. In all other cases the installer uses the existing source list that is in the registry.

## Remarks

Sources added using the **SOURCELIST** property are added directly to the end of the list for each type of source and always come after the default source specified by the [**SourceDir**](sourcedir.md) property.

For Windows Installer the number of sources in the **SOURCELIST** property is unlimited. [**MsiSourceListAddSource**](/windows/desktop/api/Msi/nf-msi-msisourcelistaddsourcea) can be used to add network sources.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[Source Resiliency](source-resiliency.md)
</dt> </dl>

 

 




