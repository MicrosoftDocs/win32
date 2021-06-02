---
description: The UpgradedImages table contains information about the upgraded images of the product.
ms.assetid: f4ee2cc8-8a49-4e4a-b8cf-b4ae2bc7e753
title: UpgradedImages Table (Patchwiz.dll)
ms.topic: article
ms.date: 05/31/2018
---

# UpgradedImages Table (Patchwiz.dll)

The UpgradedImages table contains information about the upgraded images of the product. The upgraded image should be a fully uncompressed setup image of the latest version of the product, for example, an administrative image or an uncompressed setup image from a CD-ROM. A Windows Installer patch package updates a target image into an upgraded image. The UpgradedImages table is required in the patch creation database (.pcp file) and is used by [UiCreatePatchPackageEx](uicreatepatchpackageex--patchwiz-dll-.md).

An UpgradedImages table containing at least one record is required in every patch creation database (.pcp file). This table is used by [UiCreatePatchPackageEx](uicreatepatchpackageex--patchwiz-dll-.md).

The UpgradedImages table has the following columns.



| Column       | Type | Key | Nullable |
|--------------|------|-----|----------|
| Upgraded     | text | Y   | N        |
| MsiPath      | text |     | N        |
| PatchMsiPath | text |     | Y        |
| SymbolPaths  | text |     | Y        |
| Family       | text |     | N        |



 

## Columns

<dl> <dt>

<span id="Upgraded"></span><span id="upgraded"></span><span id="UPGRADED"></span>Upgraded
</dt> <dd>

The Upgraded field is an arbitrary identifier to connect the target images with an upgraded image of the product.

</dd> <dt>

<span id="MsiPath"></span><span id="msipath"></span><span id="MSIPATH"></span>MsiPath
</dt> <dd>

This field specifies the full path, including the file name, to the location of the .msi file for the upgraded image. This is the location of the source files for the upgraded image.

</dd> <dt>

<span id="PatchMsiPath"></span><span id="patchmsipath"></span><span id="PATCHMSIPATH"></span>PatchMsiPath
</dt> <dd>

The optional patchMsiPath points to a modified copy of the upgraded installation database that contains additional authoring specific to the patch installation process. For example, additional dialogs or custom actions conditioned on the [**PATCH**](patch.md) property.

</dd> <dt>

<span id="SymbolPaths"></span><span id="symbolpaths"></span><span id="SYMBOLPATHS"></span>SymbolPaths
</dt> <dd>

A semicolon delimited list of folders that are to be searched for symbol files that may be used to optimize the generation of the binary patch. Note that the subdirectories of folders specified in this field are not searched. An optimized binary patch may be smaller. Visual C++ must be installed on the computer generating the patch and used to create the symbol files. This field is optional, and the installer creates a binary patch even if no symbol files are specified or if the symbol files become unavailable to Patchwiz.dll.

</dd> <dt>

<span id="Family"></span><span id="family"></span><span id="FAMILY"></span>Family
</dt> <dd>

Foreign key into the [ImageFamilies table](imagefamilies-table-patchwiz-dll-.md). Each upgraded image must belong to only one family.

</dd> </dl>

## Remarks

Although each upgraded image can be grouped into a separate image family, grouping upgraded images that share files together may make the .msp smaller.

This table accepts environment variables as paths beginning with version 4.0 of Patchwiz.dll.

 

 



