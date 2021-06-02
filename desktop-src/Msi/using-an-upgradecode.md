---
description: The UpgradeCode is primarily used for supporting major upgrades, although small and minor upgrade patches may use the UpgradeCode for product validation.
ms.assetid: de62bb80-56a0-4652-9509-5d36ed171c69
title: Using an UpgradeCode
ms.topic: article
ms.date: 05/31/2018
---

# Using an UpgradeCode

The [**UpgradeCode**](upgradecode.md) is primarily used for supporting major upgrades, although small and minor upgrade patches may use the **UpgradeCode** for product validation. During major upgrades, the [FindRelatedProducts](findrelatedproducts-action.md), [MigrateFeatureStates](migratefeaturestates-action.md), and [RemoveExistingProducts](removeexistingproducts-action.md) actions detect, migrate, and remove previous versions of the product. The FindRelatedProducts action searches for products using criteria based upon the **UpgradeCode**, [**ProductLanguage**](productlanguage.md), and [**ProductVersion**](productversion.md). These criteria are specified in the [Upgrade](upgrade-table.md) table.

Given the criteria used by the [FindRelatedProducts](findrelatedproducts-action.md) action, the [**UpgradeCode**](upgradecode.md) can be the same for different languages and versions of a single product. This is because the [Upgrade](upgrade-table.md) table allows for differentiating between products along version and language lines.

Across different versions of the same product, you may never need to change the [**UpgradeCode**](upgradecode.md). Each stand-alone product should have its own **UpgradeCode**. A product suite should also have its own **UpgradeCode**. Doing so will allow the suite to upgrade previous versions of the suite or stand-alone products by using multiple rows in the [Upgrade table](upgrade-table.md).

The following two scenarios illustrate the use of the [**UpgradeCode**](upgradecode.md).

-   Product A and Product B were shipped with the same [**ProductLanguage**](productlanguage.md), [**ProductVersion**](productversion.md), and [**UpgradeCode**](upgradecode.md). Product A and Product B have different [**ProductCodes**](productcode.md). Because the products were assigned the same **UpgradeCode**, the [Upgrade](upgrade-table.md) table cannot be authored to differentiate the older version of Product A from the older version of Product B. In this case, you will be unable to have an upgrade installation of Product A that ignores Product B. Because these were different products, they should have each been assigned a different **UpgradeCode**.
-   The English and French versions of Product A were shipped with the same [**ProductVersion**](productversion.md) and [**UpgradeCode**](upgradecode.md). Both the English and French versions of Product A have different [**ProductLanguages**](productlanguage.md) and [**ProductCodes**](productcode.md). Even though both the English and French language versions share the same **UpgradeCode**, it is possible to author the [Upgrade](upgrade-table.md) table such that only the older English language version will be detected and upgraded and the older French version ignored. Different language versions of a product can use the same **UpgradeCode**.

 

 



