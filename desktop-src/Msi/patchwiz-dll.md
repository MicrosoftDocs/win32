---
description: To generate a patch package, it is recommended that you use a patch creation tool such as Msimsp.exe and Patchwiz.dll.
ms.assetid: aca3bbd2-440a-405f-bddc-5f9cc831b811
title: Patchwiz.dll
ms.topic: article
ms.date: 05/31/2018
---

# Patchwiz.dll

To generate a patch package, it is recommended that you use a patch creation tool such as [Msimsp.exe](msimsp-exe.md) and Patchwiz.dll. Patchwiz.dll version 4.0 is compatible with packages and patches that were authored using earlier versions of the Patchwiz.dll. The Patchwiz.dll tool is only available in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md).

Patchwiz.dll version 4.0 has one new function, [UiCreatePatchPackageEx (Patchwiz.dll)](uicreatepatchpackageex--patchwiz-dll-.md), that extends the functionality of [UiCreatePatchPackage (Patchwiz.dll)](uicreatepatchpackage-patchwiz-dll-.md). These functions take a patch creation properties file (.pcp file) and generate an installer [Patch Package](patch-packages.md).

The .pcp file is a binary database file with the same format as a Windows Installer database (.msi file), but with a different database schema. Therefore a .pcp file can be authored by using the same tools used for an installer database.

You can create a .pcp file by using a table editor such as [Orca.exe](orca-exe.md) to enter information into the blank .pcp database provided with the Windows Installer SDK, Template.pcp. For more information, see [A Small Update Patching Example](a-small-update-patching-example.md).

The following database tables are required in every .pcp file:

-   [Properties Table (Patchwiz.dll)](properties-table-patchwiz-dll-.md)
-   [ImageFamilies Table (Patchwiz.dll)](imagefamilies-table-patchwiz-dll-.md)
-   [UpgradedImages Table (Patchwiz.dll)](upgradedimages-table-patchwiz-dll-.md)
-   [TargetImages Table (Patchwiz.dll)](targetimages-table-patchwiz-dll-.md)

The following database tables are optional:

-   [UpgradedFiles\_OptionalData Table (Patchwiz.dll)](upgradedfiles-optionaldata-table-patchwiz-dll-.md)
-   [FamilyFileRanges Table (Patchwiz.dll)](familyfileranges-table-patchwiz-dll-.md)
-   [TargetFiles\_OptionalData Table (Patchwiz.dll)](targetfiles-optionaldata-table-patchwiz-dll-.md)
-   [ExternalFiles Table (Patchwiz.dll)](externalfiles-table-patchwiz-dll-.md)
-   [UpgradedFilesToIgnore Table (Patchwiz.dll)](upgradedfilestoignore-table-patchwiz-dll-.md)

The following table is required in .pcp files that have a MinimumRequiredMsiVersion equal to 300 in the [Properties](properties-table-patchwiz-dll-.md) table.

-   [PatchMetadata Table (Patchwiz.dll)](patchmetadata-table--patchwiz-dll-.md)

> [!Note]  
> The table is optional if MinimumRequiredMsiVersion is not equal to 300.

 

The version of Patchwiz.dll released with Windows Installer 3.0 can automatically generate patch sequencing information and add it to the [MsiPatchSequence Table](msipatchsequence-table.md) of a new patch. The [PatchSequence Table](patchsequence-table--patchwiz-dll-.md) can be used to manually add patch sequencing information the MsiPatchSequence Table. For more information, see [Generating Patch Sequence Information](generating-patch-sequence-information---patchwiz-dll-.md).

Beginning with Patchwiz.dll version 2.0, you can increase the speed of subsequent patch creation by using [Patch Information Caching (Patchwiz.dll)](patch-information-caching-patchwiz-dll-.md).

Using public symbols for your target and upgrade image binaries can reduce binary patch sizes by approximately one half. For more information, see [Using Symbols to Reduce Binary Patch Size](using-symbols-to-reduce-binary-patch-size.md).

You can specify that certain regions of the target file be preserved from being overwritten during patching and that the information in those regions be retained. For more information, see [Patching Selected Regions of a File](patching-selected-regions-of-a-file.md).

## Related topics

<dl> <dt>

[Released Versions, Tools, and Redistributables](released-versions-tools-and-redistributables.md)
</dt> </dl>

 

 



