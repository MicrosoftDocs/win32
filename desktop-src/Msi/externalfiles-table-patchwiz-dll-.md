---
description: The ExternalFiles table contains information about specific files that are not part of a regular target image.
ms.assetid: c75591c2-5266-4a99-8104-53815f6550e2
title: ExternalFiles Table (Patchwiz.dll)
ms.topic: article
ms.date: 05/31/2018
---

# ExternalFiles Table (Patchwiz.dll)

The ExternalFiles table contains information about specific files that are not part of a regular target image. These files may exist in products that have been updated by another product, upgrade, or patch. This table is optional in the patch creation database (.pcp file) and is used by the [UiCreatePatchPackageEx](uicreatepatchpackageex--patchwiz-dll-.md) function.

The ExternalFiles table has the following columns.



| Column        | Type    | Key | Nullable |
|---------------|---------|-----|----------|
| Family        | text    | Y   | N        |
| FTK           | text    | Y   | N        |
| FilePath      | text    | Y   | N        |
| SymbolPaths   | text    |     | Y        |
| IgnoreOffsets | text    |     | Y        |
| IgnoreLengths | text    |     | Y        |
| RetainOffsets | text    |     | N        |
| Order         | integer |     | Y        |



 

## Columns

<dl> <dt>

<span id="Family"></span><span id="family"></span><span id="FAMILY"></span>Family
</dt> <dd>

Foreign key to the Family column of the [ImageFamilies Table (Patchwiz.dll)](imagefamilies-table-patchwiz-dll-.md).

</dd> <dt>

<span id="FTK"></span><span id="ftk"></span>FTK
</dt> <dd>

Foreign key into [File table](file-table.md) of the .msi file of the upgraded image.

</dd> <dt>

<span id="FilePath"></span><span id="filepath"></span><span id="FILEPATH"></span>FilePath
</dt> <dd>

Full path of the external file including the file name. FilePath field is used to locate the file specified in the FTK column.

</dd> <dt>

<span id="SymbolPaths"></span><span id="symbolpaths"></span><span id="SYMBOLPATHS"></span>SymbolPaths
</dt> <dd>

Full path searched for symbol files of the file specified in the FTK column.

</dd> <dt>

<span id="IgnoreOffsets"></span><span id="ignoreoffsets"></span><span id="IGNOREOFFSETS"></span>IgnoreOffsets
</dt> <dd>

The value in this field is a comma-delimited list of range offset numbers for the ranges to be ignored in the external file. The order and number of the ranges in the list must match the items in the IgnoreLengths column. This column is optional.

The values can be decimal or hexadecimal. [Patchwiz.dll](patchwiz-dll.md) treats the value as hexadecimal if it is prefixed by "0x". The columns are string columns and Patchwiz.dll will convert the values to ULONGs.

</dd> <dt>

<span id="IgnoreLengths"></span><span id="ignorelengths"></span><span id="IGNORELENGTHS"></span>IgnoreLengths
</dt> <dd>

The value in this field is a comma-delimited list of range lengths in bytes for the ranges to be ignored in the external file. The order and number of the ranges in the list must match the items in the IgnoreOffsets column. This column is optional.

The values can be decimal or hexadecimal. [Patchwiz.dll](patchwiz-dll.md) treats the value as hexadecimal if it is prefixed by "0x". The columns are string columns and Patchwiz.dll will convert the values to ULONGs.

</dd> <dt>

<span id="RetainOffsets"></span><span id="retainoffsets"></span><span id="RETAINOFFSETS"></span>RetainOffsets
</dt> <dd>

The value in this field is a comma-delimited list of range offset numbers for the ranges to be retained in the External file. The order and number of the ranges in the list must match the items in the RetainOffsets column of the corresponding record in the [FamilyFileRanges Table (Patchwiz.dll)](familyfileranges-table-patchwiz-dll-.md).

The values can be decimal or hexadecimal. [Patchwiz.dll](patchwiz-dll.md) treats the value as hexadecimal if it is prefixed by "0x". The columns are string columns and Patchwiz.dll will convert the values to ULONGs.

</dd> <dt>

<span id="Order"></span><span id="order"></span><span id="ORDER"></span>Order
</dt> <dd>

If two or more versions are specified for the same external file, the table may contain multiple records with matching values in the FTK and Family fields. In this case, the Order field may specify the order of external files to use when creating the patch. The order is from the oldest to the most recent version.

</dd> </dl>

## Remarks

This table accepts environment variables as paths beginning with version 4.0 of Patchwiz.dll.

## Related topics

<dl> <dt>

[Patching Selected Regions of a File](patching-selected-regions-of-a-file.md)
</dt> </dl>

 

 



