---
description: The TargetFiles\_OptionalData table contains information about specific files in a target image. This table is optional in the patch creation database (.pcp file) and is used by the UiCreatePatchPackageEx function.
ms.assetid: 577b1674-1e44-42e1-b011-c0fb561b514c
title: TargetFiles_OptionalData Table (Patchwiz.dll)
ms.topic: article
ms.date: 05/31/2018
---

# TargetFiles\_OptionalData Table (Patchwiz.dll)

The TargetFiles\_OptionalData table contains information about specific files in a target image. This table is optional in the patch creation database (.pcp file) and is used by the [UiCreatePatchPackageEx](uicreatepatchpackageex--patchwiz-dll-.md) function.

The TargetFiles\_OptionalData table has the following columns.



| Column        | Type | Key | Nullable |
|---------------|------|-----|----------|
| Target        | text | Y   | N        |
| FTK           | text | Y   | N        |
| SymbolPaths   | text |     | Y        |
| IgnoreOffsets | text |     | Y        |
| IgnoreLengths | text |     | Y        |
| RetainOffsets | text |     | Y        |



 

## Columns

<dl> <dt>

<span id="Target"></span><span id="target"></span><span id="TARGET"></span>Target
</dt> <dd>

Foreign key to the Target column of the [TargetImages Table (Patchwiz.dll)](targetimages-table-patchwiz-dll-.md).

</dd> <dt>

<span id="FTK"></span><span id="ftk"></span>FTK
</dt> <dd>

Foreign key into the [File table](file-table.md) of target image.

</dd> <dt>

<span id="SymbolPaths"></span><span id="symbolpaths"></span><span id="SYMBOLPATHS"></span>SymbolPaths
</dt> <dd>

The value in this field is added to the semicolon delimited list of folders in the SymbolPaths column of the [TargetImages Table (Patchwiz.dll)](targetimages-table-patchwiz-dll-.md) when the patch is generated, and can be used to add symbol files for a specific file.

</dd> <dt>

<span id="IgnoreOffsets"></span><span id="ignoreoffsets"></span><span id="IGNOREOFFSETS"></span>IgnoreOffsets
</dt> <dd>

The value in this field is a comma delimited list of range offset numbers for the ranges to be ignored in the Target file. The order and number of the ranges in the list must match the items in the IgnoreLengths column. This column is optional.

The values can be decimal or hexadecimal. [Patchwiz.dll](patchwiz-dll.md) treats the value as hexadecimal if it is prefixed by "0x". The columns are string columns and Patchwiz.dll will convert the values to ULONGs.

</dd> <dt>

<span id="IgnoreLengths"></span><span id="ignorelengths"></span><span id="IGNORELENGTHS"></span>IgnoreLengths
</dt> <dd>

The value in this field is a comma delimited list of range lengths in bytes for the ranges to be ignored in the Target file. The order and number of the ranges in the list must match the items in the IgnoreOffsets column. This column is optional.

The values can be decimal or hexadecimal. [Patchwiz.dll](patchwiz-dll.md) treats the value as hexadecimal if it is prefixed by "0x". The columns are string columns and Patchwiz.dll will convert the values to ULONGs.

</dd> <dt>

<span id="RetainOffsets"></span><span id="retainoffsets"></span><span id="RETAINOFFSETS"></span>RetainOffsets
</dt> <dd>

The value in this field is a comma delimited list of range offset numbers for the ranges to be retained in the Target file. The order and number of the ranges in the list must match the items in the RetainOffsets column of the corresponding record in the [FamilyFileRanges Table (Patchwiz.dll)](familyfileranges-table-patchwiz-dll-.md)

The values can be decimal or hexadecimal. [Patchwiz.dll](patchwiz-dll.md) treats the value as hexadecimal if it is prefixed by "0x". The columns are string columns and Patchwiz.dll will convert the values to ULONGs.

</dd> </dl>

## Related topics

<dl> <dt>

[Patching Selected Regions of a File](patching-selected-regions-of-a-file.md)
</dt> </dl>

 

 



