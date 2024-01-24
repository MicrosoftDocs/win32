---
description: A small update makes changes to one or more application files that are too minor to warrant changing the product code.
ms.assetid: c74ef2bd-9cf5-4ec0-bfff-1fad0e17ba98
title: Small Updates
ms.topic: article
ms.date: 05/31/2018
---

# Small Updates

A small update makes changes to one or more application files that are too minor to warrant changing the product code. A small update is also commonly referred to as a quick fix engineering (QFE) update. A small update does not permit reorganization of the feature-component tree.

A typical small update changes only one or two files or a registry key. Because a small update changes the information in the .msi file, the installation package code must be changed. The package code is stored in the [**Revision Number Summary**](revision-number-summary.md) property of the [Summary Information Stream](summary-information-stream.md).

The product code is never changed with a small update, so all of the changes introduced by a small update have to be consistent with the guidelines described in [Changing the Product Code](changing-the-product-code.md). An update requires a [major upgrade](major-upgrades.md) to change the [**ProductCode**](productcode.md). If it is necessary to differentiate between products without changing the product code, use a [minor upgrade](minor-upgrades.md).

For information on how to apply a small update patch package to a Windows Installer package, see [Creating a Small Update Patch](creating-a-small-update-patch.md), [Applying Small Updates by Patching the Local Installation of the Product](applying-small-updates-by-patching-the-local-installation-of-the-product.md), [Applying Small Updates by Reinstalling the Product](applying-small-updates-by-reinstalling-the-product.md), and [Applying Small Updates by Patching an Administrative Image](applying-small-updates-by-patching-an-administrative-image.md).

 

 



