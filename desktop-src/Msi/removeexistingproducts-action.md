---
description: The RemoveExistingProducts action goes through the product codes listed in the ActionProperty column of the Upgrade table and removes the products in sequence by invoking concurrent installations.
ms.assetid: 3e96283b-1085-4ace-b004-2fd94310eeb2
title: RemoveExistingProducts Action
ms.topic: article
ms.date: 05/31/2018
---

# RemoveExistingProducts Action

The RemoveExistingProducts action goes through the product codes listed in the ActionProperty column of the [Upgrade table](upgrade-table.md) and removes the products in sequence by invoking concurrent installations. For each concurrent installation the installer sets the [**ProductCode**](productcode.md) property to the product code and sets the [**REMOVE**](remove.md) property to the value in the Remove field of the Upgrade table. If the Remove field is blank, its value defaults to ALL and the installer removes the entire product.

The installer only runs the RemoveExistingProducts action the first time it installs a product. It does not run the action during a [maintenance installation](maintenance-installation.md) or uninstallation.

## Sequence Restrictions

The RemoveExistingProducts action must be scheduled in the action sequence in one of the following locations.

-   Between the [InstallValidate action](installvalidate-action.md) and the [InstallInitialize action](installinitialize-action.md). In this case, the installer removes the old applications entirely before installing the new applications. This is an inefficient placement for the action because all reused files have to be recopied.
-   After the [InstallInitialize action](installinitialize-action.md) and before any actions that generate execution script.
-   Between the [InstallExecute action](installexecute-action.md), or the [InstallExecuteAgain action](installexecuteagain-action.md), and the [InstallFinalize action](installfinalize-action.md). Generally the last three actions are scheduled right after one another: InstallExecute, RemoveExistingProducts, and InstallFinalize. In this case the updated files are installed first and then the old files are removed. However, if the removal of the old application fails, then the installer rolls back both the removal of the old application and the install of the new application.
-   After the [InstallFinalize action](installfinalize-action.md). This is the most efficient placement for the action. In this case, the installer updates files before removing the old applications. Only the files being updated get installed during the installation. If the removal of the old application fails, then the installer only rolls back the uninstallation of the old application.

## ActionData Messages



| Field | Description of action data |
|-------|----------------------------|
| \[1\] | Removed product.           |



 

## Remarks

Windows Installer sets the [**UPGRADINGPRODUCTCODE**](upgradingproductcode.md) Property when it runs this action.

 

 



