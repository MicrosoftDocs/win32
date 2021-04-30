---
description: Beginning with Windows Installer 3.0, authors can add patch sequencing information to the patch package database in the MsiPatchSequence table.
ms.assetid: 9cdcb25f-2c3d-411e-9aae-bdd52df38a97
title: Sequencing Patches
ms.topic: article
ms.date: 05/31/2018
---

# Sequencing Patches

Beginning with Windows Installer 3.0, authors can add patch sequencing information to the patch package database in the [MsiPatchSequence](msipatchsequence-table.md) table. The installer can use this information to determine which patches are applicable to an installation package, to determine the best patching sequence, and to install patches in an constant order independent of the order they are provided to the system.

**Windows Installer 2.0:** Not supported. Windows Installer versions previous to Windows Installer 3.0 install patches in the order that they are provided to the system regardless of whether they contain an [MsiPatchSequence](msipatchsequence-table.md) table.

The following are required to use the patch sequencing functionality.

-   [Patch packages](patch-packages.md) (.msp files) must have a [MsiPatchSequence](msipatchsequence-table.md) table containing sequencing information. The installer installs patches that do not have a MsiPatchSequence table in the order that they are provided to the system.
-   Patches are installed using Windows Installer 3.0 or later.

Windows Installer version 3.0 has the following functions that applications can use to determine the best patching sequence.

-   The [**MsiDeterminePatchSequence**](/windows/desktop/api/Msi/nf-msi-msideterminepatchsequencea) function takes a list of patches and determines in what sequence they can be applied to an installed product. This function accounts for any patches or products that have already been installed on the system.
-   The [**MsiDetermineApplicablePatches**](/windows/desktop/api/Msi/nf-msi-msidetermineapplicablepatchesa) function takes a list of patches and determines in what sequence they can be applied to an installed product. This function does not account for any patches or products that have already been installed on the system.

Windows Installer version 3.0 can apply multiple patches to a product in a single patching installation. The group of patches can contain patches that include patching sequence information (a [MsiPatchSequence](msipatchsequence-table.md) table) and patches that do not. The Windows Installer installs the patch packages without this table in the order that they are provided to the system. The installer accounts for patch packages that lack a MsiPatchSequence table, but that have been marked as obsolete or superseded patches by the method described in the following section.

When Windows Installer version 3.0 installs multiple patches, it follows these steps to determine the sequence in which individual patches are applied to the product:

1.  Installed patches without a [MsiPatchSequence](msipatchsequence-table.md) table are put in the sequence in the order that they were applied to the product. The first patch that was applied is placed first in the sequence.
2.  New patches without a [MsiPatchSequence table](msipatchsequence-table.md) are put in the sequence. These patches are being applied by the current patching installation. They are put in the order that they are provided to the system, and placed after all the patches in step 1.
3.  Obsolete patches are eliminated from the sequence of patches.
    > [!Note]  
    > A patch package can specify in the [**Revision Number Summary**](revision-number-summary.md) property an explicit list of obsolete patches to be removed by the patch. This list is intended for use by Windows Installer versions earlier than version 3.0. Windows Installer version 3.0 removes the patches marked as obsolete from the sequence, only if the patches do not have the [MsiPatchSequence table](msipatchsequence-table.md).

     

4.  The installer steps through the patching sequence and determines which patches are applicable in the given sequence. When multiple patches are applied to a product, each patch in the sequence also transforms the product's installation database (.msi file). A patch is applicable in a particular sequence only if its database transform is capable of taking the [product code](product-codes.md), [**version**](productversion.md), [**language**](productlanguage.md), and [**upgradecode**](upgradecode.md) that result from applying the transforms of all preceding [patch packages](patch-packages.md) to the product database. The installer eliminates any inapplicable patches from the sequence.
5.  The installer begins placing patches that have sequencing information in their [MsiPatchSequence](msipatchsequence-table.md) table. [Minor upgrade](minor-upgrades.md) patches that have the MsiPatchSequence table are placed in the sequence after the patches that were sequenced in previous steps and in the order of their lowest to highest product versions after being upgraded. Windows Installer then eliminates any minor upgrade patches that are inapplicable in this sequence.
6.  [Small update](small-updates.md) patches targeting [minor upgrades](minor-upgrades.md) having a [MsiPatchSequence](msipatchsequence-table.md) table, are assigned to the highest version of the minor upgrade patch in the sequence.
7.  All [small update](small-updates.md) patches that remain unassigned after the previous steps, and that have the [MsiPatchSequence](msipatchsequence-table.md) table, are put in the sequence before the first [minor upgrade](minor-upgrades.md) that has the MsiPatchSequence table, and after the .msi installation database and any patches without the MsiPatchSequence table. Windows Installer then eliminates any small update patches that are inapplicable in this sequence.
8.  Windows Installer version 3.0 eliminates superseded patches from the sequence. When a patch supersedes patches that occur earlier in the patch sequence, the patch contains all the fixes in the earlier patches. The earlier patches are no longer required. The Windows Installer requires the information in the [MsiPatchSequence](msipatchsequence-table.md) table to eliminate superseded patches.
    > [!Note]  
    > Patches intended to supersede an earlier set of patches must be authored to supersede the earlier patches in all patch families. [Small update](small-updates.md) patches can only supersede small updates. [Minor upgrades](minor-upgrades.md) can supersede both small updates and other minor upgrades.

     

9.  [Small update](small-updates.md) patches that carry [MsiPatchSequence](msipatchsequence-table.md) tables, get sequenced within product versions according to the sequencing information in their MsiPatchSequence tables. This determines the final patching sequence.

A patch that should no longer be used can be eliminated from the patching sequence. For more information about how to eliminate patches from the patching sequence, see [Eliminating Patches](eliminating-patches.md).

For an example of how the [MsiPatchSequence](msipatchsequence-table.md) table can be used to apply patches in the order in which they are authored, see the [Multiple Patching Example](multiple-patching-example.md).

 

 



