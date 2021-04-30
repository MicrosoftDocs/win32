---
description: To apply a major upgrade using Windows Installer, the original product installation package must specify an UpgradeCode Property, described in Preparing an Application for Future Major Upgrades, and the upgrade package must have an Upgrade table.
ms.assetid: 041f5bab-cb13-4e17-8465-484bcd3c6957
title: Updating Upgrade Table for an Upgrade
ms.topic: article
ms.date: 05/31/2018
---

# Updating Upgrade Table for an Upgrade

To apply a major upgrade using Windows Installer, the original product installation package must specify an [**UpgradeCode**](upgradecode.md) Property, described in [Preparing an Application for Future Major Upgrades](preparing-an-application-for-future-major-upgrades.md), and the upgrade package must have an [Upgrade table](upgrade-table.md).

For more information about major upgrades, see [Major Upgrades](major-upgrades.md) in [Patching and Upgrades](patching-and-upgrades.md).

The installation package of MNP2000.msi was assigned an [**UpgradeCode**](upgradecode.md) property, as described in the section [Specifying Properties](specifying-properties.md).

Windows Installer applies the upgrade if the user has already installed the 1.0 to 1.4 versions (inclusive) of English language MNP2000. Windows Installer migrates all of the original product's feature settings to the upgraded product. The installer removes the files belonging to the original products not being used by the product's upgrade.

If your copy of MNP2001.msi does not include an [Upgrade table](upgrade-table.md), use Orca, or another table editor, to import an empty Upgrade table into the database from Schema.msi. The SDK provides a copy of Schema.msi. Use your database editor to open MNP2001.msi and enter the following data into the empty Upgrade table.



| UpgradeCode                            | VersionMin | VersionMax | Language | Attributes | Remove | ActionProperty |
|----------------------------------------|------------|------------|----------|------------|--------|----------------|
| {908E378A-9551-4772-BF1D-5CFAF6FD9CB4} | 01.00.0000 | 01.40.0000 | 1033     | 769        |        | OLDAPPFOUND    |



 

[Continue](updating-properties-for-an-upgrade.md)

 

 



