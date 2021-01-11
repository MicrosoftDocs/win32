---
description: The MsiPatchOldAssemblyName table specifies the old name for an assembly.
ms.assetid: e9f22ba1-6be4-4382-abe5-5cfdc68c0855
title: MsiPatchOldAssemblyName Table
ms.topic: article
ms.date: 05/31/2018
---

# MsiPatchOldAssemblyName Table

The MsiPatchOldAssemblyName table specifies the old name for an assembly.

The MsiPatchOldAssemblyName table has the following columns.



| Column   | Type                         | Key | Nullable |
|----------|------------------------------|-----|----------|
| Assembly | [Identifier](identifier.md) | Y   | N        |
| Name     | [Text](text.md)             | Y   | N        |
| Value    | [Text](text.md)             | N   | N        |



 

## Columns

<dl> <dt>

<span id="Assembly"></span><span id="assembly"></span><span id="ASSEMBLY"></span>Assembly
</dt> <dd>

Unique identifier for the old assembly name. This key is used as a mapping between this and the [MsiPatchOldAssemblyFile table](msipatcholdassemblyfile-table.md).

</dd> <dt>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>Name
</dt> <dd>

Name of the attribute associated with the value specified in the Value column.

</dd> <dt>

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>Value
</dt> <dd>

Value associated with the name specified in the Name column.

</dd> </dl>

## Remarks

Windows Installer uses the [MsiPatchOldAssemblyFile table](msipatcholdassemblyfile-table.md) and MsiPatchOldAssemblyName table when patching assemblies installed to the Global Assembly Cache (GAC). When releasing a newer version of an assembly, the strong name of the assembly is changed. The two tables together identify the old assembly name for an updated assembly. This allows the Installer to use the old assembly name to find the original file in the GAC and apply a binary patch. Without this information, the installer may have to access the original installation source in order to patch an assembly installed in the GAC.

The [MsiPatchOldAssemblyFile table](msipatcholdassemblyfile-table.md) and MsiPatchOldAssemblyName table are not generated automatically by [PatchWiz](patchwiz-dll.md). The update package specified in the [UpgradedImages table](upgradedimages-table-patchwiz-dll-.md) is required to contain these tables for the patch to have this information.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
</dl>

 

 



