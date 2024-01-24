---
description: The MsiPatchOldAssemblyFile table relates a file in the File table to an assembly name in the MsiPatchOldAssemblyName table. Multiple old assembly names can be associated with a single file.
ms.assetid: a3c1e7fb-5f97-41db-bdc8-bd3ddb695c42
title: MsiPatchOldAssemblyFile Table
ms.topic: article
ms.date: 05/31/2018
---

# MsiPatchOldAssemblyFile Table

The MsiPatchOldAssemblyFile table relates a file in the [File table](file-table.md) to an assembly name in the [MsiPatchOldAssemblyName table](msipatcholdassemblyname-table.md). Multiple old assembly names can be associated with a single file.

The MsiPatchOldAssemblyFile table has the following columns.



| Column     | Type                         | Key | Nullable |
|------------|------------------------------|-----|----------|
| File\_     | [Identifier](identifier.md) | Y   | N        |
| Assembly\_ | [Identifier](identifier.md) | Y   | N        |



 

## Columns

<dl> <dt>

<span id="File_"></span><span id="file_"></span><span id="FILE_"></span>File\_
</dt> <dd>

Foreign key to the [File table](file-table.md) that specifies the assembly to be patched. This column is part of the primary key.

</dd> <dt>

<span id="Assembly_"></span><span id="assembly_"></span><span id="ASSEMBLY_"></span>Assembly\_
</dt> <dd>

Foreign key to the [MsiPatchOldAssemblyName table](msipatcholdassemblyname-table.md) that identifies one of the old assembly names for the assembly. This column is part of the primary key.

</dd> </dl>

## Remarks

Windows Installer uses the MsiPatchOldAssemblyFile table and [MsiPatchOldAssemblyName table](msipatcholdassemblyname-table.md) when patching assemblies installed to the Global Assembly Cache (GAC). When releasing a newer version of an assembly, the strong name of the assembly is changed. The two tables together identify the old assembly name for an updated assembly. This allows the Installer to use the old assembly name to find the original file in the GAC and apply a binary patch. Without this information, the installer may have to access the original installation source in order to patch an assembly installed in the GAC.

The MsiPatchOldAssemblyFile table and [MsiPatchOldAssemblyName table](msipatcholdassemblyname-table.md) are not generated automatically by [PatchWiz](patchwiz-dll.md). The update package specified in the [UpgradedImages table](upgradedimages-table-patchwiz-dll-.md) is required to contain these tables for the patch to have this information.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
</dl>

 

 



