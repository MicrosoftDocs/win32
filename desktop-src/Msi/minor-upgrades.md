---
description: A minor upgrade is an update that makes changes to many resources.
ms.assetid: 74c962f9-93cd-40ed-a8fe-141ccac79d79
title: Minor Upgrades
ms.topic: article
ms.date: 05/31/2018
---

# Minor Upgrades

A minor upgrade is an update that makes changes to many resources. None of the changes can require changing the [**ProductCode**](productcode.md). An update requires a [major upgrade](major-upgrades.md) to change the **ProductCode**. A minor upgrade can be used to add new features and components but cannot reorganize the feature-component tree. Minor upgrades provide product differentiation without actually defining a different product. A typical minor upgrade includes all fixes in previous small updates combined into a patch. A minor upgrade is also commonly referred to as a service pack (SP) update. For more information about which updates do not require changing the **ProductCode** see [Changing the Product Code](changing-the-product-code.md).

A minor upgrade changes the [**ProductVersion**](productversion.md) property. Changing the product version of the application means that the different updates have an order. For example, if a patch existed to update v 9.0 to v 9.1, and another patch existed to patch v 9.1 to v 9.2, the installer can enforce the correct order by checking the product version before applying the patch. This also prevents the v 9.1 to v 9.2 patch from being applied to v 9.0. For patches, this ordering is enforced through the product version–validation bits set in the transforms included in the [patch package](patch-packages.md).

A minor upgrade and a small update differ in that a minor upgrade changes the package code and product version. See [Small Updates](small-updates.md) for guidelines on the kinds of updates that can be handled by a small update or minor upgrade. Minor upgrades are shipped as a full product installation package or as a [patch package](patch-packages.md). However, a minor upgrade cannot use a different volume label for the new version.

For information on how to apply a minor upgrade, see the following topics:

-   [Applying Small Updates by Patching the Local Installation of the Product](applying-small-updates-by-patching-the-local-installation-of-the-product.md)
-   [Applying Small Updates by Reinstalling the Product](applying-small-updates-by-reinstalling-the-product.md)
-   [Applying Small Updates by Patching an Administrative Image](applying-small-updates-by-patching-an-administrative-image.md)

 

 



