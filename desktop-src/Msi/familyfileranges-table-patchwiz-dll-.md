---
description: The FamilyFileRanges table contains information about particular files of an upgraded image with ranges that should never be overwritten.
ms.assetid: 2e77605a-d909-4a17-977c-18281a96c36c
title: FamilyFileRanges Table (Patchwiz.dll)
ms.topic: article
ms.date: 05/31/2018
---

# FamilyFileRanges Table (Patchwiz.dll)

The FamilyFileRanges table contains information about particular files of an upgraded image with ranges that should never be overwritten. This table is optional in the patch creation database (.pcp file) and is used by the [UiCreatePatchPackageEx](uicreatepatchpackageex--patchwiz-dll-.md) function.

The FamilyFileRanges table has the following columns.



| Column        | Type | Key | Nullable |
|---------------|------|-----|----------|
| Family        | text | Y   | N        |
| FTK           | text | Y   | N        |
| RetainOffsets | text |     | N        |
| RetainLengths | text |     | N        |



 

## Columns

<dl> <dt>

<span id="Family"></span><span id="family"></span><span id="FAMILY"></span>Family
</dt> <dd>

Foreign key to the Family column of the [ImageFamilies Table (Patchwiz.dll)](imagefamilies-table-patchwiz-dll-.md).

</dd> <dt>

<span id="FTK"></span><span id="ftk"></span>FTK
</dt> <dd>

Foreign key into the [File tables](file-table.md) of all the upgraded images in the image family.

</dd> <dt>

<span id="RetainOffsets"></span><span id="retainoffsets"></span><span id="RETAINOFFSETS"></span>RetainOffsets
</dt> <dd>

The offset of the ranges that cannot be overwritten. The value in this field is a list of the range offset numbers for ranges that are not to be overwritten in the target files. The order and number of the ranges in the list must match the items in the RetainLengths column.

The values can be decimal or hexadecimal. [Patchwiz.dll](patchwiz-dll.md) treats the value as hexadecimal if it is prefixed by "0x". The columns are string columns and Patchwiz.dll will convert the values to ULONGs.

</dd> <dt>

<span id="RetainLengths"></span><span id="retainlengths"></span><span id="RETAINLENGTHS"></span>RetainLengths
</dt> <dd>

The length in bytes of the ranges that cannot be overwritten. The value in this field is a list of range length numbers for ranges to retain in target files. The order and number of the ranges in the list must match the items in the RetainOffsets column.

The values can be decimal or hexadecimal. [Patchwiz.dll](patchwiz-dll.md) treats the value as hexadecimal if it is prefixed by "0x". The columns are string columns and Patchwiz.dll will convert the values to ULONGs.

</dd> </dl>

## Remarks

The offsets and lengths entered in RetainOffsets and RetainLengths must not specify overlapping ranges.

## Related topics

<dl> <dt>

[Patching Selected Regions of a File](patching-selected-regions-of-a-file.md)
</dt> </dl>

 

 



