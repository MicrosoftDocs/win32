---
description: Authors of installation packages should include upgrading information in their .msi files to ensure that their installation package can take advantage of the full upgrading functionality available with the Microsoft Windows Installer.
ms.assetid: 88bb2709-a1bf-4140-a145-ae6bee85dde1
title: Preparing an Application for Future Major Upgrades
ms.topic: article
ms.date: 05/31/2018
---

# Preparing an Application for Future Major Upgrades

Authors of installation packages should include upgrading information in their .msi files to ensure that their installation package can take advantage of the full upgrading functionality available with the Microsoft Windows Installer.

Every application, or suite of applications, should be assigned an [**UpgradeCode**](upgradecode.md) Property, [**ProductVersion**](productversion.md) Property, and [**ProductLanguage**](productlanguage.md) Property. The [**UpgradeCode**](upgradecode.md) property indicates a family of related applications consisting of different versions and different language versions of the same product. For more information about using the [**UpgradeCode**](upgradecode.md) property, see [Using an UpgradeCode](using-an-upgradecode.md).

**Preparing an application for future major upgrades**

1.  Determine a new package code value for the application. For more information about package codes, see [Package Codes](package-codes.md). Enter the new package code into the [**Revision Number Summary**](revision-number-summary.md) Property of the [Summary Information Stream](summary-information-stream.md).
2.  Determine a new [**ProductCode**](productcode.md) property for the application. See [Changing the Product Code](changing-the-product-code.md) for more information. Enter [**ProductCode**](productcode.md) and its value into the [Property table](property-table.md).
3.  Determine the application's version and the [**ProductVersion**](productversion.md) property. The [**ProductVersion**](productversion.md) should increase with each new version of the application. Note that the installer uses only the first three fields of the product version. If you include a fourth field in your product version, the installer ignores the fourth field. Enter [**ProductVersion**](productversion.md) and its value into the Property table.
4.  Determine the language of the package and the [**ProductLanguage**](productlanguage.md) property. The value of this property must be a numeric language identifier (LANGID). Enter [**ProductLanguage**](productlanguage.md) and its value into the [Property table](property-table.md). Note that the [FindRelatedProducts action](findrelatedproducts-action.md) uses the language returned by [**MsiGetProductInfo**](/windows/desktop/api/Msi/nf-msi-msigetproductinfoa). For FindRelatedProducts to work correctly, the package author must be sure that the [**ProductLanguage**](productlanguage.md) property is set in the Property table to a language that is also listed in the [**Template Summary**](template-summary.md) property.
5.  If you are authoring an installation package for the first version of your product, use a new [**UpgradeCode**](upgradecode.md). If your package is intended for a newer version of an existing product, or is the same version as an existing product in a different language, use the same [**UpgradeCode**](upgradecode.md) as the existing product. No two products with the same [**ProductVersion**](productversion.md) and the same [**ProductLanguage**](productlanguage.md) can have the same [**UpgradeCode**](upgradecode.md), unless one is a [small update](small-updates.md) of the other.
6.  The [**UpgradeCode**](upgradecode.md) has the format of a [GUID](guid.md). Enter the [**UpgradeCode**](upgradecode.md) GUID into the Property table.

For more information, see [Preventing an Old Package from Installing Over a Newer Version](preventing-an-old-package-from-installing-over-a-newer-version.md).

 

 



