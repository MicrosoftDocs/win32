---
description: Adhere to the following guidelines when creating a patch for a Windows Installer small update.
ms.assetid: 0e57c2aa-e86a-4161-9749-c7963182a6d5
title: Creating a Small Update Patch
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Small Update Patch

When creating a patch for [small updates](small-updates.md), authors should adhere to the following guidelines:

-   Small update patches must be designed for a single, target installation.
-   Small update patches should use the earliest version as the target installation.
-   A small update patch should replace and make obsolete any earlier small update patches.

The following scenario illustrates when a small update patch is best.

Your company ships version 1.0 of Myproduct.msi. Shortly thereafter, you ship a [small update](small-updates.md) patch for Myproduct.msi called QFE1. This does not change the [**ProductCode**](productcode.md) property or the [**ProductVersion**](productversion.md) property.

Later, you author a second [small update](small-updates.md) patch for Myproduct.msi called QFE2. This second patch must target Myproduct.msi version 1.0. This second patch must not target both Myproduct.msi version 1.0 and Myproduct.msi version 1.0 + QFE1. When QFE2 is applied it should remove QFE1.

 

 



