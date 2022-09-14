---
description: When installing a patch and one or more customization transforms to an application, the patch is typically installed first, followed by the customization transforms.
ms.assetid: 39a58174-fa62-42e3-a0aa-4cc541c2e36b
title: Patching Customized Applications
ms.topic: article
ms.date: 05/31/2018
---

# Patching Customized Applications

When installing a patch and one or more customization transforms to an application, the patch is typically installed first, followed by the customization transforms. By design, the patch is not broken by the subsequent installation of the customization. However, installing the transforms first, and then the patch, may break the customization.

For example, a break in the customization could occur when a patch is used to update a product from version 1 to version 2 and a customization transform that works for version 1 does not work for version 2. In this case, the version update patch cannot be applied to a customized product without first uninstalling and then reinstalling the original product.

 

 



