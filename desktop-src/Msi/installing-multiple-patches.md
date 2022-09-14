---
description: Beginning with Windows Installer 3.0, multiple patches can be applied to a product in a constant order, regardless of the order that the patches are provided to the system.
ms.assetid: 10af1857-d59f-490d-9b50-49619b1e892c
title: Installing Multiple Patches
ms.topic: article
ms.date: 05/31/2018
---

# Installing Multiple Patches

Beginning with Windows Installer 3.0, multiple patches can be applied to a product in a constant order, regardless of the order that the patches are provided to the system.

**Windows Installer 2.0:** Not supported. Windows Installer versions earlier than version 3.0 always install patches in the order that they are provided to the system.

**Windows Installer 3.0 and later:** The installer can use the information provided in the [MsiPatchSequence](msipatchsequence-table.md) table to determine which patches are applicable to the Windows Installer package and in which order the patches should be applied. Applications can use the [**MsiDetermineApplicablePatches**](/windows/desktop/api/Msi/nf-msi-msidetermineapplicablepatchesa) and [**MsiDeterminePatchSequence**](/windows/desktop/api/Msi/nf-msi-msideterminepatchsequencea) functions.

The [**MsiDetermineApplicablePatches**](/windows/desktop/api/Msi/nf-msi-msidetermineapplicablepatchesa) function determines which patches apply to the Windows Installer package and in what sequence. The function can account for superseded or obsolete patches. This function does not account for products or patches that are installed on the system that are not specified in the set.

The [**MsiDeterminePatchSequence**](/windows/desktop/api/Msi/nf-msi-msideterminepatchsequencea) Sequence function can determine the best sequence of application for the patches to a specified installed product. This function accounts for patches that have already been applied to the product, and accounts for obsolete and superseded patches.

When the patch package does not have a [MsiPatchSequence](msipatchsequence-table.md) table, the installer always applies the patches in the order that they are provide to the system.

When the patch package contains a mixture of patches with sequence information in the [MsiPatchSequence](msipatchsequence-table.md) table and some patches without this information, Windows installer version 3.0 sequences the patches in the order described in the following section: [Sequencing Patches](sequencing-patches.md).

A Windows Installer package can install no more than 127 patches when installing or updating an application. When many updates are necessary, they should be combined and previous obsolete patches should be eliminated from the patching sequence.

A patch that should not be used can be eliminated from the patching sequence. This prevents the patch from being applied when the target application is patched. This is different than removing a patch that has already been applied to an application. For more information about eliminating patches from the patching sequence, see [Eliminating Patches](eliminating-patches.md). For information about removing applied patches, see [Removing Patches](removing-patches.md).

For an example of how Windows Installer applies multiple patches when all have [MsiPatchSequence](msipatchsequence-table.md) tables, see the [Multiple Patching Example](multiple-patching-example.md).

 

 



