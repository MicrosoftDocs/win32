---
description: The ModuleSignature Table is a required table.
ms.assetid: 09802282-72ad-43f1-8cce-4cdc68b01e87
title: ModuleSignature Table
ms.topic: article
ms.date: 05/31/2018
---

# ModuleSignature Table

The ModuleSignature Table is a required table. It contains all the information necessary to identify a merge module. The merge tool adds this table to the .msi file if one does not already exist. The ModuleSignature table in a merge module has only one row containing the ModuleID, Language, and Version. However, the ModuleSignature table in an .msi file has a row containing this information for each .msm file that has been merged into it.

Merge and verification tools check the ModuleSignature table in .msi files to determine if it has all of the dependent merge modules required by the current merge module (see [ModuleDependency Table](moduledependency-table.md)) and whether the installation package was previously merged with any conflicting merge modules (see [ModuleExclusion Table](moduleexclusion-table.md)).

The ModuleSignature table has the following columns.



| Column   | Type                         | Key | Nullable |
|----------|------------------------------|-----|----------|
| ModuleID | [Identifier](identifier.md) | Y   | N        |
| Language | [Integer](integer.md)       | Y   | N        |
| Version  | [Version](version.md)       |     | N        |



 

## Columns

<dl> <dt>

<span id="ModuleID"></span><span id="moduleid"></span><span id="MODULEID"></span>ModuleID
</dt> <dd>

An identifier that uniquely identifies the merge module. Two merge modules cannot have the same ModuleID unless the merge module is entirely backward compatible with its predecessor. You can create a GUID for this field using a utility such as GUIDGEN. The ModuleID column is a primary key for the table and therefore it must follow the naming convention in [Naming Primary Keys in Merge Module Databases](naming-primary-keys-in-merge-module-databases.md). For example, if the readable name of the merge module is MyLibrary and the GUID is {880DE2F0-CDD8-11D1-A849-006097ABDE17}, the entry in the ModuleID column becomes MyLibrary.880DE2F0\_CDD8\_11D1\_A849\_006097ABDE17.

</dd> <dt>

<span id="Language"></span><span id="language"></span><span id="LANGUAGE"></span>Language
</dt> <dd>

The Language identifier specifies the default language for the merge module. The language identifier is in decimal format, for example, U.S. English is 1033. The language used by the merge module can be changed by applying a transform to the merge module before merging.

</dd> <dt>

<span id="Version"></span><span id="version"></span><span id="VERSION"></span>Version
</dt> <dd>

The Version field contains a string that describes the major and minor versions of the merge module.

</dd> </dl>

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE25](ice25.md)  
</dl>

## Related topics

<dl> <dt>

[Multiple Language Merge Modules](multiple-language-merge-modules.md)
</dt> </dl>

 

 



