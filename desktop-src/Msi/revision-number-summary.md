---
description: For an installation package, the Revision Number Summary property contains the package code for the installer package.
ms.assetid: 79702b44-846a-4672-8e22-9b6e3f4b4678
title: Revision Number Summary property
ms.topic: reference
ms.date: 05/31/2018
---

# Revision Number Summary property

For an installation package, the **Revision Number Summary** property contains the [*package code*](p-gly.md) for the installer package. For more information about package codes, see [Package Codes](package-codes.md).

For a transform, the **Revision Number Summary** property lists the product code GUIDs and version of the new and original products and the upgrade code GUID. The list is separated with semicolons as follows.

"Original-Product-Code Original-Product-Version ; New-Product Code New-Product-Version; Upgrade-Code"

For a patch package, the **Revision Number Summary** property specifies the GUID patch code for the patch. This can be followed by a list of patch code GUIDs for obsolete patches that are to be removed when this patch is applied. The patch codes are concatenated with no delimiters separating GUIDs in the list.

**Windows Installer 3.0:  ** If there is sequencing information present in the [MsiPatchSequence table](msipatchsequence-table.md), Windows Installer 3.0 uses the sequencing information in the table and ignores the list of obsolete patches included in the **Revision Number Summary** property. Windows Installer 3.0 can still use the obsolete patch information in the **Revision Number Summary** property if the package does not contain a MsiPatchSequence table.

**Windows Installer 2.0:  ** The [MsiPatchSequence table](msipatchsequence-table.md) is not supported. Windows Installer 2.0 can still use the obsolete patch information in the **Revision Number Summary** property if the package does not contain a MsiPatchSequence table.

This summary property is required.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |



## See also

<dl> <dt>

[Summary Property Descriptions](summary-property-descriptions.md)
</dt> </dl>

 

 




