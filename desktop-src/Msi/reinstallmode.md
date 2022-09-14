---
description: The REINSTALLMODE property is a string that contains letters specifying the type of reinstall to perform.
ms.assetid: 756d2899-2cfe-473a-bebf-a7f7bbe7d229
title: REINSTALLMODE property
ms.topic: reference
ms.date: 05/31/2018
---

# REINSTALLMODE property

The **REINSTALLMODE** property is a string that contains letters specifying the type of reinstall to perform. Options are case-insensitive and order-independent. This property should normally always be used in conjunction with the [**REINSTALL**](reinstall.md) property. However, this property can also be used during installation, not just reinstall.

> [!Note]  
> The Windows Installer ignores the **REINSTALLMODE** property during an [administrative installation](administrative-installation.md).

 

## Reinstall Option Codes

By default the **REINSTALLMODE** is "omus".



| Code | Option                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| p    | Reinstall only if the file is missing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| o    | Reinstall if the file is missing or is an older version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| e    | Reinstall if the file is missing, or is an equal or older version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| d    | Reinstall if the file is missing or a different version is present.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| c    | Verify the checksum values, and reinstall the file if they are missing or corrupt. This flag only repairs files that have msidbFileAttributesChecksum in the Attributes column of the [File Table](file-table.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| a    | Force all files to be reinstalled, regardless of checksum or version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| u    | Rewrite all required registry entries from the [Registry Table](registry-table.md) that go to the**HKEY\_CURRENT\_USER**<br/> or **HKEY\_USERS**<br/> registry hive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| m    | Rewrite all required registry entries from the [Registry Table](registry-table.md) that go to the **HKEY\_LOCAL\_MACHINE**<br/> or **HKEY\_CLASSES\_ROOT**<br/> registry hive. Rewrite all information from the [Class Table](class-table.md), [Verb Table](verb-table.md), [PublishComponent Table](publishcomponent-table.md), [ProgID Table](progid-table.md), [MIME Table](mime-table.md), [Icon Table](icon-table.md), [Extension Table](extension-table.md), and [AppID Table](appid-table.md) regardless of machine or user assignment. Reinstall all [**qualified components.**](/windows/desktop/api/Msi/nf-msi-msiprovidequalifiedcomponenta)When reinstalling an application, this option runs the [RegisterTypeLibraries](registertypelibraries-action.md) and [InstallODBC](installodbc-action.md) actions.<br/> |
| s    | Reinstall all shortcuts and re-cache all icons overwriting any existing shortcuts and icons.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| v    | Use to run from the source package and re-cache the local package. Do not use the v reinstall option code for the first installation of an application or feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |



 

If the **REINSTALLMODE** property is defined without also defining the [**REINSTALL**](reinstall.md) property, then the specified "detection" modes still apply and specify the "overwrite" mode for a normal installation. The **REINSTALLMODE** property only affects those features that are selected normally for installation. The presence of the **REINSTALLMODE** property does not reinstall features. The reinstallation of features requires the presence of the **REINSTALL** property.

The option codes for this property correspond to the [command-line option](command-line-options.md) '/f'. The command-line option has a default value of 'pecms'.

> [!Note]  
> Only those files containing checksum information are ever verified and repaired. The REINSTALLMODE\_FILEVERIFY flag (the ccode above) only repairs files that have msidbFileAttributesChecksum in the Attributes column of the [File Table](file-table.md).

 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




