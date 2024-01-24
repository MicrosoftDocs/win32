---
description: Because the upgrade changes the name of the .msi file and changes the component code of some components, the product code of the upgrade must be changed from that of the original product.
ms.assetid: ebb1a217-fce6-43f0-9139-c0f4422c8fc4
title: Updating Properties for an Upgrade
ms.topic: article
ms.date: 05/31/2018
---

# Updating Properties for an Upgrade

Because the upgrade changes the name of the .msi file and changes the component code of some components, the product code of the upgrade must be changed from that of the original product. For a description of the cases where an upgrade is required to change the [**ProductCode**](productcode.md) property, see [Changing the Product Code](changing-the-product-code.md). An upgrade that changes the ProductCode is referred to as a [Major Upgrade](major-upgrades.md).

The upgrade package's [**ProductName**](productname.md) property, [**ProductVersion**](productversion.md) property, [**ProductLanguage**](productlanguage.md) property, and [**UpgradeCode**](upgradecode.md) property may be changed, or left unchanged, from the original product. Based upon the values of these properties, Windows Installer may determine whether to apply future upgrade packages to the current upgrade.

The property specified in the ActionProperty column of the [Upgrade table](upgrade-table.md) must be added to the [**SecureCustomProperties**](securecustomproperties.md) Property.

Use your database editor to open MNP2001.msi and enter the following data into the [Property table](property-table.md). The list provides links to the reference topics for built-in installer properties. The property names that are not links are author-defined properties. Many of the properties were imported from Uisample.msi that comes with the SDK. For details, see [Importing the User Interface](importing-the-user-interface.md).

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
| [**ProductCode**](productcode.md)               | {34CF587C-1D8F-4DD5-ADFE-440F4B593987}    |
| [**ProductID**](productid.md)                   | none                                      |
| [**ProductLanguage**](productlanguage.md)       | 1033                                      |
| [**ProductName**](productname.md)               | MNP2001                                   |
| [**ProductVersion**](productversion.md)         | 01.50.0000                                |
| Progress1                                        | Installing                                |
| Progress2                                        | installs                                  |
| [**PROMPTROLLBACKCOST**](promptrollbackcost.md) | P                                         |
| RemoveIcon                                       | removico                                  |
| RepairIcon                                       | repairic                                  |
| Setup                                            | Setup                                     |
| True                                             | 1                                         |
| [**UpgradeCode**](upgradecode.md)               | {908E378A-9551-4772-BF1D-5CFAF6FD9CB4}    |
| Wizard                                           | Setup Wizard                              |
| SecureCustomProperties                           | OLDAPPFOUND                               |



 

[Continue](updating-sequence-tables-for-an-upgrade.md)

 

 



