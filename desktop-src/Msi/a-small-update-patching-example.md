---
description: This example illustrates how to create a patch package that applies a small update to the sample installation package discussed in An Installation Example.
ms.assetid: 17dadd64-6e81-444a-985e-1b340e4f2ee5
title: A Small Update Patching Example
ms.topic: article
ms.date: 05/31/2018
---

# A Small Update Patching Example

This example illustrates how to create a [patch package](patch-packages.md) that applies a [small update](small-updates.md) to the sample installation package discussed in [An Installation Example](an-installation-example.md). A small update makes changes to one or more application files that are judged to be too minor to warrant changing the product code. For more information see [Patching and Upgrades](patching-and-upgrades.md).

This example illustrates how to create a Windows Installer patch package that updates the Concert feature of the hypothetical product MNP2000 to fix an error in the original product. The example patch package applies a small update to the product that does not require changing the product code. See the topic on [Major Upgrades](major-upgrades.md) in the [Patching and Upgrades](patching-and-upgrades.md) section for more information about major upgrades.

The sample upgrade package has the following specifications:

-   It corrects a minor error in the Concert schedule displayed by the Concert feature.
-   It updates the package code to reflect the installation package has changed.
-   The small update can be applied by patching the local installation of the product.

[Continue](planning-a-small-update-patch.md)

 

 



