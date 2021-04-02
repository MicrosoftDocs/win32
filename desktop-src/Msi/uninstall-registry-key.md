---
description: A list of the Windows Installer properties giving values written under the Uninstall registry key.
ms.assetid: f831cc62-4b19-4285-8bb1-6080567ac985
title: Windows Installer Properties for the Uninstall Registry Key
ms.topic: article
ms.date: 05/31/2018
ms.custom: contperf-fy21q3
---

# Windows Installer Properties for the Uninstall Registry Key

The following installer properties give the values written under the registry key:

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**Windows**\\**CurrentVersion**\\**Uninstall**

The values are stored in a subkey identified by the application's product code GUID.



| Value               | Windows Installer property                                                                                                                                                                                                                                                                                                                                           |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DisplayName         | [**ProductName**](productname.md) property                                                                                                                                                                                                                                                                                                                          |
| DisplayVersion      | Derived from [**ProductVersion**](productversion.md) property                                                                                                                                                                                                                                                                                                       |
| Publisher           | [**Manufacturer**](manufacturer.md) property                                                                                                                                                                                                                                                                                                                        |
| VersionMinor        | Derived from [**ProductVersion**](productversion.md) property                                                                                                                                                                                                                                                                                                       |
| VersionMajor        | Derived from [**ProductVersion**](productversion.md) property                                                                                                                                                                                                                                                                                                       |
| Version             | Derived from [**ProductVersion**](productversion.md) property                                                                                                                                                                                                                                                                                                       |
| HelpLink            | [**ARPHELPLINK**](arphelplink.md) property                                                                                                                                                                                                                                                                                                                          |
| HelpTelephone       | [**ARPHELPTELEPHONE**](arphelptelephone.md) property                                                                                                                                                                                                                                                                                                                |
| InstallDate         | The last time this product received service. The value of this property is replaced each time a patch is applied or removed from the product or the /v [Command-Line Option](command-line-options.md) is used to repair the product. If the product has received no repairs or patches this property contains the time this product was installed on this computer. |
| InstallLocation     | [**ARPINSTALLLOCATION**](arpinstalllocation.md) property                                                                                                                                                                                                                                                                                                            |
| InstallSource       | [**SourceDir**](sourcedir.md) property                                                                                                                                                                                                                                                                                                                              |
| URLInfoAbout        | [**ARPURLINFOABOUT**](arpurlinfoabout.md) property                                                                                                                                                                                                                                                                                                                  |
| URLUpdateInfo       | [**ARPURLUPDATEINFO**](arpurlupdateinfo.md) property                                                                                                                                                                                                                                                                                                                |
| AuthorizedCDFPrefix | [**ARPAUTHORIZEDCDFPREFIX**](arpauthorizedcdfprefix.md) property                                                                                                                                                                                                                                                                                                    |
| Comments            | [**ARPCOMMENTS**](arpcomments.md) property <br/> Comments provided to the **Add or Remove Programs** control panel.<br/>                                                                                                                                                                                                                                |
| Contact             | [**ARPCONTACT**](arpcontact.md) property <br/> Contact provided to the **Add or Remove Programs** control panel.<br/>                                                                                                                                                                                                                                   |
| EstimatedSize       | Determined and set by the Windows Installer.                                                                                                                                                                                                                                                                                                                         |
| Language            | [**ProductLanguage**](productlanguage.md) property                                                                                                                                                                                                                                                                                                                  |
| ModifyPath          | Determined and set by the Windows Installer.                                                                                                                                                                                                                                                                                                                         |
| Readme              | [**ARPREADME**](arpreadme.md) property <br/> Readme provided to the **Add or Remove Programs** control panel.<br/>                                                                                                                                                                                                                                      |
| UninstallString     | Determined and set by Windows Installer.                                                                                                                                                                                                                                                                                                                             |
| SettingsIdentifier  | [**MSIARPSETTINGSIDENTIFIER**](msiarpsettingsidentifier.md) property                                                                                                                                                                                                                                                                                                |



 

## Related topics

<dl> <dt>

[About Properties](about-properties.md)
</dt> <dt>

[Configuring Add/Remove Programs with Windows Installer](configuring-add-remove-programs-with-windows-installer.md)
</dt> <dt>

[Property Reference](property-reference.md)
</dt> <dt>

[Using Properties](using-properties.md)
</dt> </dl>

 

 




