---
description: The PatchSequence Table is used to generate the MsiPatchSequence Table in a patch. The table requires the version of PATCHWIZ.DLL that is available with Windows Installer&\#160;3.0.
ms.assetid: bdeccb3b-57c0-4424-9602-348b8048fd46
title: PatchSequence Table (PATCHWIZ.DLL)
ms.topic: article
ms.date: 05/31/2018
---

# PatchSequence Table (PATCHWIZ.DLL)

The PatchSequence Table is used to generate the [MsiPatchSequence Table](msipatchsequence-table.md) in a patch. The table requires the version of [PATCHWIZ.DLL](patchwiz-dll.md) that is available with Windows Installer 3.0.

The following table identifies the columns of the PatchSequence Table.



| Column      | Type       | Key | Nullable |
|-------------|------------|-----|----------|
| PatchFamily | Identifier | Y   | N        |
| Target      | Text       | Y   | Y        |
| Sequence    | Version    |     | Y        |
| Supersede   | Integer    |     | Y        |



 

### Columns

<dl> <dt>

<span id="PatchFamily"></span><span id="patchfamily"></span><span id="PATCHFAMILY"></span>PatchFamily
</dt> <dd>

The identifier that indicates the sequence families to which this patch belongs.

The values in the Target and PatchFamily columns together define the primary key for the table. A patch that belongs to multiple sequence families, or has different sequences depending on the product code of the target, can have one row for each pairing. This value is used to populate the PatchFamily column of the [MsiPatchSequence Table](msipatchsequence-table.md) that belongs to the patch.

</dd> <dt>

<span id="Target"></span><span id="target"></span><span id="TARGET"></span>Target
</dt> <dd>

The Target column is used to filter the PatchFamily by product code.

A NULL value in this column indicates that this PatchFamily applies to all targets of the patch. If this column contains a foreign key to the [TargetImages Table](targetimages-table-patchwiz-dll-.md), the product code of the specified image is retrieved and used to populate the product code value in the new patch's row of the [MsiPatchSequence Table](msipatchsequence-table.md). If this column contains a GUID, the GUID is used to populate the product code value of the row in the MsiPatchSequence Table.

</dd> <dt>

<span id="Sequence"></span><span id="sequence"></span><span id="SEQUENCE"></span>Sequence
</dt> <dd>

The value in the Sequence column is used to populate the Sequence column of the [MsiPatchSequence Table](msipatchsequence-table.md) of the new patch file.

If the value is NULL, a sequence number is generated automatically.

</dd> <dt>

<span id="Supersede"></span><span id="supersede"></span><span id="SUPERSEDE"></span>Supersede
</dt> <dd>

A value of **msidbPatchSequenceSupersedeEarlier** or 1 in this field indicates that this patch supersedes earlier [small updates](small-updates.md) in the sequence families to which this patch belongs.

The value in this column is used to set the Attributes column of the new patch's row in the [MsiPatchSequence Table](msipatchsequence-table.md) .

</dd> </dl>

### Remarks

Available beginning in Windows Installer 3.0.

 

 



