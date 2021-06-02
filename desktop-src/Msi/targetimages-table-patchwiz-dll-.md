---
description: The TargetImages table contains information about the target images of the product. A Windows Installer patch package updates a target image into an upgraded image.
ms.assetid: 4681715e-9918-4d7b-8f33-1cca2bb34eb7
title: TargetImages Table (Patchwiz.dll)
ms.topic: article
ms.date: 05/31/2018
---

# TargetImages Table (Patchwiz.dll)

The TargetImages table contains information about the target images of the product. A Windows Installer patch package updates a target image into an upgraded image.

A TargetImages table containing at least one record is required in every patch creation database (.pcp file). This table is used by the [UiCreatePatchPackage](uicreatepatchpackage-patchwiz-dll-.md) function.

The TargetImages table has the following columns.



| Column                | Type    | Key | Nullable |
|-----------------------|---------|-----|----------|
| Target                | text    | Y   | N        |
| MsiPath               | text    |     | N        |
| SymbolPaths           | text    |     | Y        |
| Upgraded              | text    |     | N        |
| Order                 | integer |     | N        |
| ProductValidateFlags  | text    |     | Y        |
| IgnoreMissingSrcFiles | integer |     | N        |



 

## Columns

<dl> <dt>

<span id="Target"></span><span id="target"></span><span id="TARGET"></span>Target
</dt> <dd>

Identifier for a target image. The patch package updates the target image specified in this column to the upgraded image specified in the Upgraded column. There are one or more target images for each upgraded image. The target image must be a fully uncompressed setup image of the product, such as an administrative image or an uncompressed setup image on a CD-ROM. Note that the [UiCreatePatchPackageEx](uicreatepatchpackageex--patchwiz-dll-.md) function does not generate binary patches for files in cabinets. The value in this field is used with the value in the Upgraded field to generate the names of the transforms that the installer adds to the patch package.

</dd> <dt>

<span id="MsiPath"></span><span id="msipath"></span><span id="MSIPATH"></span>MsiPath
</dt> <dd>

This field specifies the full path, including the file name, to the location of the .msi file for the target image. This is the location of the source files for the target image.

</dd> <dt>

<span id="SymbolPaths"></span><span id="symbolpaths"></span><span id="SYMBOLPATHS"></span>SymbolPaths
</dt> <dd>

A semicolon delimited list of folders that are to be searched for symbol files that may be used to optimize the generation of the binary patch. Note that the subdirectories of folders specified in this field are not searched. An optimized binary patch may be smaller. Microsoft Visual C++ must be installed on the computer generating the patch and used to create the symbol files. This field is optional, and the installer creates a binary patch even if no symbol files are specified or if the symbol files become unavailable to Patchwiz.dll.

</dd> <dt>

<span id="Upgraded"></span><span id="upgraded"></span><span id="UPGRADED"></span>Upgraded
</dt> <dd>

Foreign key to the Upgraded column of the [UpgradedImages table](upgradedimages-table-patchwiz-dll-.md). The [UiCreatePatchPackageEx](uicreatepatchpackageex--patchwiz-dll-.md) function ignores any upgraded image that is not referenced by at least one record of the TargetImages table.

</dd> <dt>

<span id="Order"></span><span id="order"></span><span id="ORDER"></span>Order
</dt> <dd>

Relative order of the target image. Because multiple targets can be patched to an upgraded image, the Order field provides a means to sequence the transforms in the patch transforms list. Commonly, the order is from oldest to newest image.

</dd> <dt>

<span id="ProductValidateFlags"></span><span id="productvalidateflags"></span><span id="PRODUCTVALIDATEFLAGS"></span>ProductValidateFlags
</dt> <dd>

The ProductValidateFlags field is used to specify product checking to avoid applying irrelevant transforms. The value entered in this field must be an 8-digit hex integer and one of the valid values for the *iValidation* parameter of the [**MsiCreateTransformSummaryInfo**](/windows/desktop/api/Msiquery/nf-msiquery-msicreatetransformsummaryinfoa) function. The default value is 0x00000922 which equals **MSITRANSFORM\_VALIDATE\_UPDATEVERSION** + **MSITRANSFORM\_VALIDATE\_NEWEQUALBASEVERSION** + **MSITRANSFORM\_VALIDATE\_UPGRADECODE** + **MSITRANSFORM\_VALIDATE\_PRODUCT**.

</dd> <dt>

<span id="IgnoreMissingSrcFiles"></span><span id="ignoremissingsrcfiles"></span><span id="IGNOREMISSINGSRCFILES"></span>IgnoreMissingSrcFiles
</dt> <dd>

If this field is set to a nonzero value, files missing from the target image are ignored by the installer and left unchanged during patching. This enables patches to be made without requiring the entire image; only the changed files of the product and the .msi file are required. This may reduce the time required to generate the patch.

> [!Note]  
> Do not use the IgnoreMissingSrcFiles value with TrustMsi set to 1 in the [Properties Table](properties-table-patchwiz-dll-.md).

 

</dd> </dl>

## Remarks

This table accepts environment variables as paths beginning with version 4.0 of Patchwiz.dll.

 

 



