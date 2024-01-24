---
description: The FindRelatedProducts action runs through each record of the Upgrade table in sequence and compares the upgrade code, product version, and language in each row to products installed on the system.
ms.assetid: 7efcb767-9bdf-43a4-83b8-61b6fc84adf6
title: FindRelatedProducts Action
ms.topic: article
ms.date: 05/31/2018
---

# FindRelatedProducts Action

The FindRelatedProducts action runs through each record of the [Upgrade table](upgrade-table.md) in sequence and compares the upgrade code, product version, and language in each row to products installed on the system. When FindRelatedProducts detects a correspondence between the upgrade information and an installed product, it appends the product code to the property specified in the ActionProperty column of the UpgradeTable.

The FindRelatedProducts action only runs the first time the product is installed. The FindRelatedProducts action does not run during maintenance mode or uninstallation.

## Database Tables Queried

This action queries the following table:

[Upgrade Table](upgrade-table.md)

## Properties Used

The FindRelatedProducts action uses the [**UpgradeCode**](upgradecode.md) property and the version and language information authored into the Upgrade table to detect installed products affected by the pending upgrade. It appends the product code of detected products to the property in the ActionProperty column of the UpgradeTable.

FindRelatedProducts only recognizes existing products that have been installed using the Windows Installer with an .msi that defines an [**UpgradeCode**](upgradecode.md) property, a [**ProductVersion**](productversion.md) property, and a value for the [**ProductLanguage**](productlanguage.md) property that is one of the languages listed in the [**Template Summary**](template-summary.md) Property.

Note that FindRelatedProducts uses the language returned by [**MsiGetProductInfo**](/windows/desktop/api/Msi/nf-msi-msigetproductinfoa). For FindRelatedProducts to work correctly, the package author must be sure that the [**ProductLanguage**](productlanguage.md) property in the [Property table](property-table.md) is set to a language that is also listed in the [**Template Summary**](template-summary.md) Property. See [Preparing an Application for Future Major Upgrades](preparing-an-application-for-future-major-upgrades.md).

## Sequence Restrictions

FindRelatedProducts should be authored into the [InstallUISequence table](installuisequence-table.md) and [InstallExecuteSequence](installexecutesequence-table.md) tables. The installer prevents FindRelated Products from running in InstallExecuteSequence if the action has already run in InstallUISequence. The FindRelatedProducts action must come before the [MigrateFeatureStates action](migratefeaturestates-action.md) and the [RemoveExistingProducts action](removeexistingproducts-action.md).

## ActionData Messages

FindRelatedProducts sends an action data message for each related product it detects on the system.

 

 



