---
description: Windows Installer properties are global variables the installer uses during an installation.
ms.assetid: 1c59939b-de0f-4bf4-ab1f-4f1aa2488bfa
title: Specifying Properties
ms.topic: article
ms.date: 05/31/2018
---

# Specifying Properties

Windows Installer properties are global variables the installer uses during an installation. See the sections under [Properties](properties.md). If in the section [Importing a Blank Database](importing-a-blank-database.md) you used uisample.msi from the Windows Installer SDK, the [Property table](property-table.md) in your copy of MNP2000.msi already contains many properties that are used by the user interface. In this section you add additional information to the Property table specific to the installation of the Notepad sample. See also the [Program Information Tables Group](program-information-tables-group.md).

There are five properties that are required in every installation package, and these must be updated for the Notepad sample in the [Property table](property-table.md) of MNP2000.msi:

-   [**ProductCode**](productcode.md)
-   [**ProductLanguage**](productlanguage.md)
-   [**Manufacturer**](manufacturer.md)
-   [**ProductVersion**](productversion.md)
-   [**ProductName**](productname.md)

Although not required by all installation packages, applications that may in the future receive an upgrade should also have an [**UpgradeCode**](upgradecode.md) property. See [Preparing an Application for Future Major Upgrades](preparing-an-application-for-future-major-upgrades.md).

Use your database editor to open MNP2000.msi and enter the following data into the Property table. The list provides links to the reference topics for built-in installer properties. The property names that are not links are author-defined properties. Many of the properties imported from uisample.msi are for the sample user interface. The later section User Interface for the Installation Sample discusses the user interface.

[Property Table](property-table.md)



| Property                                         | Value                                     |
|--------------------------------------------------|-------------------------------------------|
| [**ARPHELPLINK**](arphelplink.md)               | https://www.microsoft.com/management       |
| BannerBitmap                                     | bannrbmp                                  |
| ButtonText\_Back                                 | < &Back                                |
| ButtonText\_Browse                               | Br&owse                                   |
| ButtonText\_Cancel                               | Cancel                                    |
| ButtonText\_Exit                                 | &Exit                                     |
| ButtonText\_Finish                               | &Finish                                   |
| ButtonText\_Ignore                               | &Ignore                                   |
| ButtonText\_Install                              | &Install                                  |
| ButtonText\_Next                                 | &Next >                                |
| ButtonText\_No                                   | &No                                       |
| ButtonText\_OK                                   | OK                                        |
| ButtonText\_Remove                               | &Remove                                   |
| ButtonText\_Reset                                | &Reset                                    |
| ButtonText\_Resume                               | &Resume                                   |
| ButtonText\_Retry                                | &Retry                                    |
| ButtonText\_Return                               | &Return                                   |
| ButtonText\_Yes                                  | &Yes                                      |
| CompleteSetupIcon                                | completi                                  |
| ComponentDownload                                | ftp://anonymous@microsoft.com/components/ |
| CustomSetupIcon                                  | custicon                                  |
| [**DefaultUIFont**](defaultuifont.md)           | DlgFont8                                  |
| DialogBitmap                                     | dlgbmp                                    |
| DlgTitleFont                                     | {&DlgFontBold8}                           |
| ErrorDialog                                      | ErrorDlg                                  |
| ExclamationIcon                                  | exclamic                                  |
| False                                            | 0                                         |
| Iagree                                           | No                                        |
| InfoIcon                                         | info                                      |
| InstallerIcon                                    | insticon                                  |
| [**INSTALLLEVEL**](installlevel.md)             | 3                                         |
| InstallMode                                      | Typical                                   |
| [**Manufacturer**](manufacturer.md)             | Microsoft                                 |
| [**PIDTemplate**](pidtemplate.md)               | 12345<\#\#\#-%%%%%%%>@@@@@          |
| [**ProductCode**](productcode.md)               | {18A9233C-0B34-4127-A966-C257386270BC}    |
| [**ProductID**](productid.md)                   | none                                      |
| [**ProductLanguage**](productlanguage.md)       | 1033                                      |
| [**ProductName**](productname.md)               | MNP2000                                   |
| [**ProductVersion**](productversion.md)         | 01.40.0000                                |
| Progress1                                        | Installing                                |
| Progress2                                        | installs                                  |
| [**PROMPTROLLBACKCOST**](promptrollbackcost.md) | P                                         |
| RemoveIcon                                       | removico                                  |
| RepairIcon                                       | repairic                                  |
| Setup                                            | Setup                                     |
| True                                             | 1                                         |
| [**UpgradeCode**](upgradecode.md)               | {908E378A-9551-4772-BF1D-5CFAF6FD9CB4}    |
| Wizard                                           | Setup Wizard                              |



 

[Continue](importing-the-installexecutesequence.md)

 

 



