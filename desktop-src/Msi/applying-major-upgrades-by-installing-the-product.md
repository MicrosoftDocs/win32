---
description: A major upgrade can be applied by installing the new installation package for the upgraded product.
ms.assetid: f4fb28be-5ec0-4eac-9d4d-eccf5bd61ac4
title: Applying Major Upgrades by Installing the Product
ms.topic: article
ms.date: 05/31/2018
---

# Applying Major Upgrades by Installing the Product

A major upgrade can be applied by installing the new installation package for the upgraded product. Because major upgrades get a different product code than the original product, installing the upgrade must be treated as an installation of a new product. The upgrade can simply be installed like another product. You can have the new installation package handle the removal of the old product by including the [Upgrade table](upgrade-table.md) and the [FindRelatedProducts action](findrelatedproducts-action.md) and [RemoveExistingProducts action](removeexistingproducts-action.md).

**To propagate a major upgrade to current users from the command line**

-   From the command line, use: **msiexec /i \[***path to updated msi file***\]**

**To propagate a major upgrade to current users from a program**

-   From a program, call [**MsiInstallProduct**](/windows/desktop/api/Msi/nf-msi-msiinstallproducta) and specify the path to the updated msi file.

 

 



