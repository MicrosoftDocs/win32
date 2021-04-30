---
description: A major upgrade is a comprehensive update of a product that needs a change of the ProductCode Property.
ms.assetid: 0c8f2aad-b301-4404-9051-694d97db1a8d
title: Major Upgrades
ms.topic: article
ms.date: 05/31/2018
---

# Major Upgrades

A major upgrade is a comprehensive update of a product that needs a change of the [**ProductCode**](productcode.md) Property.

A typical major upgrade removes a previous version of an application and installs a new version. A major upgrade can reorganize the feature component tree. For more information, see [**ProductCode**](productcode.md) and [Changing the Product Code](changing-the-product-code.md).

During a major upgrade using Windows Installer, the installer searches the user's computer for applications that are related to the pending upgrade, and when it detects one, it retrieves the version of the installed application from the system registry. The installer then uses information in the upgrade database to determine whether to upgrade the installed application.

To enable the installer upgrade capabilities, each package should have an [**UpgradeCode**](upgradecode.md) Property and an [Upgrade Table](upgrade-table.md). Each stand-alone product or product suite should have its own **UpgradeCode**. For more information about using the **UpgradeCode** see the section [Using an UpgradeCode](using-an-upgradecode.md). Each record in the Upgrade table gives a combination of the upgrade code, product version, and language information used to identify a set of products affected by the upgrade. When the [FindRelatedProducts Action](findrelatedproducts-action.md) detects that an affected product is installed on the system, it appends the product code to a property in the ActionProperty column of the Upgrade table. The [RemoveExistingProducts action](removeexistingproducts-action.md) and the [MigrateFeatureStates Action](migratefeaturestates-action.md) remove or migrate the products listed in the ActionProperty list. Package authors can also follow the procedure described in the topic: [Preparing an Application for Future Major Upgrades](preparing-an-application-for-future-major-upgrades.md).

Windows Installer upgrade packages can be authored such that major upgrades will not install if the user already has a newer version of the application installed. For more information about how to author a package that will not install over a newer version, see [Preventing an Old Package from Installing Over a Newer Version](preventing-an-old-package-from-installing-over-a-newer-version.md)

> [!Note]  
> Windows Installer uses only the first three fields of the product version. See [**ProductVersion**](productversion.md) Property for descriptions of these fields. If you include a fourth field in your product version, the installer ignores the fourth field.

 

The recommended method of applying a major upgrade by installing the full package for the updated product. For information about how to apply a major upgrade by installing the product, see [Applying Major Upgrades by Installing the Product](applying-major-upgrades-by-installing-the-product.md).

A major upgrade applied as a [Patch Package](patch-packages.md) for the product cannot be sequenced with other updates and is not an [uninstallable patch](uninstallable-patches.md). For information about how to apply a major upgrade patch package to a Windows Installer package see [Applying Major Upgrades by Patching the Local Installation of the Product](applying-major-upgrades-by-patching-the-local-installation-of-the-product.md). The application of a major upgrade using a patch package is not recommended, instead apply major upgrades by installing the full product.

> [!Note]  
> If an application is installed in the per-user [installation context](installation-context.md), any major upgrade to the application must also be performed using the per-user context. If an application is installed in the per-machine installation context, any major upgrade to the application must also be performed using the per-machine context. The Windows Installer will not install major upgrades across installation context.

 

You can condition custom actions that are sequenced after [InstallValidate](installvalidate-action.md) to handle major upgrades by using the [**UPGRADINGPRODUCTCODE**](upgradingproductcode.md) property:

-   If you want a custom action to run during an uninstallation of the product, but not during the removal of the product by a major upgrade, use this condition.

    REMOVE="ALL" AND NOT [**UPGRADINGPRODUCTCODE**](upgradingproductcode.md)

-   If you want a custom action to run only during a major upgrade, use this condition.

    [**UPGRADINGPRODUCTCODE**](upgradingproductcode.md)

 

 



