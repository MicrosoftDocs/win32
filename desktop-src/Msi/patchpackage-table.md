---
description: The PatchPackage table describes all patch packages that have been applied to this product. For each patch package, the unique identifier for the patch is provided along with information about the media image the on which the patch is located.
ms.assetid: 212d99dd-c80c-42ca-9dfa-819ae1813006
title: PatchPackage Table
ms.topic: article
ms.date: 05/31/2018
---

# PatchPackage Table

The PatchPackage table describes all patch packages that have been applied to this product. For each patch package, the unique identifier for the patch is provided along with information about the media image the on which the patch is located.

The PatchPackage table has the following columns.



| Column  | Type                   | Key | Nullable |
|---------|------------------------|-----|----------|
| PatchId | [GUID](guid.md)       | Y   | N        |
| Media\_ | [Integer](integer.md) | N   | N        |



 

## Columns

<dl> <dt>

<span id="PatchId"></span><span id="patchid"></span><span id="PATCHID"></span>PatchId
</dt> <dd>

This column contains a unique identifier for this particular patch.

</dd> <dt>

<span id="Media_"></span><span id="media_"></span><span id="MEDIA_"></span>Media\_
</dt> <dd>

This column is a foreign key to the DiskId column of the [Media Table](media-table.md) and indicates the disk containing the patch package.

</dd> </dl>

## Remarks

The PatchPackage table is required in every patch package. If the table is missing, attempts to install the patch fail with "Error 2768: Transform in patch package is invalid." This table is usually added to the install package by a transform from a patch package. It is usually not authored directly into an install package.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
</dl>

 

 



