---
description: The MsiPatchSequence table contains all the information the installer requires to determine the sequence of application of a small update patch relative to all other patches.
ms.assetid: ae8319ad-8136-4201-9fcf-ea58ce05f88b
title: MsiPatchSequence Table
ms.topic: article
ms.date: 05/31/2018
---

# MsiPatchSequence Table

The MsiPatchSequence table contains all the information the installer requires to determine the sequence of application of a [small update](small-updates.md) patch relative to all other patches. The table must be in the database of the patch file and not in a transform in the patch. The installer ignores this table when applying a [major upgrade](major-upgrades.md) patch. When applying a [minor upgrade](minor-upgrades.md) patch, the installer only uses this table to identify superseded patches that must not be sequenced.

The **MsiPatchSequence table** has the following columns.



| Column      | Type                         | Key | Nullable |
|-------------|------------------------------|-----|----------|
| PatchFamily | [Identifier](identifier.md) | Y   | N        |
| ProductCode | [GUID](guid.md)             | Y   | Y        |
| Sequence    | [Version](version.md)       | N   | N        |
| Attributes  | [Integer](integer.md)       | N   | Y        |



 

## Columns

<dl> <dt>

<span id="PatchFamily"></span><span id="patchfamily"></span><span id="PATCHFAMILY"></span>PatchFamily
</dt> <dd>

Specifies that the patch is a member of the patch family named in this field. Patches in the same patch family that target the same product version are sorted by the values in the Sequence column. The patches within the patch family are applied to the target product in the order of increasing sequence. The PatchFamily is also used to determine which patches are to be superseded. A patch may be listed in multiple rows and belong to multiple patch families if it applies to more than one product or includes multiple fixes.

The Windows Installer does not interpret the PatchFamily value in any way other than comparisons for equality against other PatchFamily values. A PatchFamily value must be unique within the ProductCode targeted by the set of patches. In the complex patching scenarios the PatchFamily identifier may need to be globally unique.

</dd> <dt>

<span id="ProductCode"></span><span id="productcode"></span><span id="PRODUCTCODE"></span>ProductCode
</dt> <dd>

A value in this field is optional. If a [product code](product-codes.md) GUID is entered in this field and the patch is being applied to the specified product, the patch is sorted and applied as a member of the specified PatchFamily. If a product code GUID is entered in this field and the patch is not being applied to the product specified by ProductCode, this row is ignored. If the value in ProductCode is NULL, the patch is sorted and applied as a member of PatchFamily for all targets of the patch regardless of the product code.

A patch can have multiple rows in the same PatchFamily and a different ProductCode for each product targeted by the patch. One row for the PatchFamily can specify NULL for ProductCode. If the target product matches a row with a non-NULL ProductCode, the installer uses the matching row and ignores the row with the NULL ProductCode. If none of the specified product codes match the target, the patch is sorted and applied as a member of PatchFamily for all targets of the patch regardless of the product code.

</dd> <dt>

<span id="Sequence"></span><span id="sequence"></span><span id="SEQUENCE"></span>Sequence
</dt> <dd>

The value in the Sequence column specifies the sequence of this patch within the specified PatchFamily. The value in Sequence is expressed in the format of [Version](version.md) data. The value contains between 1 and 4 fields and each field has a range of 0 to 65535. Members of PatchFamily are sorted and applied to the target product in the order of increasing Sequence values. For example, the following six values are increasing: 1, 1.1, 1.2, 2.01, 2.01.1, 2.01.1.1.

</dd> <dt>

<span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes
</dt> <dd>

The presence of the **msidbPatchSequenceSupersedeEarlier** attribute in a row indicates that the [small update](small-updates.md) patch supersedes the updates provided by all patches with lesser Sequence values in the same PatchFamily. This patch contains all fixes provided by earlier patches in the specified PatchFamily. This attribute does not mean that this patch supersedes the earlier patches in all cases because the earlier patches can belong to multiple patch families.

A [small update](small-updates.md) patch cannot supersede a [minor upgrade](minor-upgrades.md) or [major upgrade](major-upgrades.md) patch under any circumstances, even if the **msidbPatchSequenceSupersedeEarlier** is set. 

| Name                                   | Value | Meaning                                                           |
|----------------------------------------|-------|-------------------------------------------------------------------|
|                                        | 0x00  | Indicates a simple sequencing value.                              |
| **msidbPatchSequenceSupersedeEarlier** | 0x01  | Indicates a patch that supersedes earlier patches in this family. |



 

</dd> </dl>

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
</dl>

## Related topics

<dl> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 



