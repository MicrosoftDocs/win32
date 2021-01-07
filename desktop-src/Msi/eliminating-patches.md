---
description: A patch that should no longer be used can be eliminated from the patching sequence.
ms.assetid: b1d499d9-4fd3-4996-84a1-c32acefbb98f
title: Eliminating Patches
ms.topic: article
ms.date: 05/31/2018
---

# Eliminating Patches

A patch that should no longer be used can be eliminated from the patching sequence. This prevents the patch from being applied when the target application is patched. This is different than removing a patch that is already applied to an application. For information about removing applied patches, see [Removing Patches](removing-patches.md).

**Windows Installer 3.0 and later:  **

Patches that have the [MsiPatchSequence](msipatchsequence-table.md) table can use this table to eliminate patches from the patching sequence. A patch can eliminate patches that come before it in the patching sequence, and replace the information from those patches with its own information. Both the patch that specifies which patches to eliminate and the patches being eliminated must have a MsiPatchSequence table that contains information.

If the eliminated patches and replacement patch do not have [MsiPatchSequence](msipatchsequence-table.md) tables, the patch package can specify a list of patches to be eliminated from the patching sequence in its [**Revision Number Summary**](revision-number-summary.md) property. Windows Installer 3.0 ignores this list if either the eliminated or replacement patches have a MsiPatchSequence table.

When the patch package contains patches with sequence information in the [MsiPatchSequence](msipatchsequence-table.md) table and some patches without this information, Windows installer 3.0 sequences the patches in the order described in the following section: [Sequencing Patches](sequencing-patches.md).

For example, Patch1, Patch2, and Patch3 can be three patches that do not have the [MsiPatchSequence](msipatchsequence-table.md) table. Patch2 can be a patch that is only applicable if Patch1 has already been applied to the application. Patch3 can be a later patch that has all the information in Patch1 and also eliminates Patch1 from the patching sequence. This means that when Patch3 is applied, Patch 2 also becomes inapplicable, because it requires Patch1. Any information in Patch2 alone does not get delivered to the application.

**Windows Installer 2.0:** Not supported. The only method available is to specify the list of patches to be eliminated from the patching sequence in the [**Revision Number Summary**](revision-number-summary.md) property.

> [!Note]  
> Patch authors should use the [**MsiDeterminePatchSequence**](/windows/desktop/api/Msi/nf-msi-msideterminepatchsequencea) and [**MsiDetermineApplicablePatches**](/windows/desktop/api/Msi/nf-msi-msidetermineapplicablepatchesa) functions to determine the sequence of patches that actually get applied to the product because the elimination of some patches can render other patches inapplicable.

 

 

 



