---
description: The ModuleDependency table keeps a list of other merge modules that are required for this merge module to operate properly.
ms.assetid: 36418331-bec7-40c9-8fdf-fe4b958a1443
title: ModuleDependency Table
ms.topic: article
ms.date: 05/31/2018
---

# ModuleDependency Table

The ModuleDependency table keeps a list of other merge modules that are required for this merge module to operate properly. This table enables a merge or verification tool to ensure that the necessary merge modules are in fact included in the user's installer database. The tool checks by cross referencing this table with the ModuleSignature table in the installer database.

The ModuleDependency table has the following columns.



| Column           | Type                         | Key | Nullable |
|------------------|------------------------------|-----|----------|
| ModuleID         | [Identifier](identifier.md) | Y   | N        |
| ModuleLanguage   | [Integer](integer.md)       | Y   | N        |
| RequiredID       | [Identifier](identifier.md) | Y   | N        |
| RequiredLanguage | [Integer](integer.md)       | Y   | N        |
| RequiredVersion  | [Version](version.md)       |     | Y        |



 

## Columns

<dl> <dt>

<span id="ModuleID"></span><span id="moduleid"></span><span id="MODULEID"></span>ModuleID
</dt> <dd>

Identifier of the merge module. This is a foreign key into the [ModuleSignature table](modulesignature-table.md).

</dd> <dt>

<span id="ModuleLanguage"></span><span id="modulelanguage"></span><span id="MODULELANGUAGE"></span>ModuleLanguage
</dt> <dd>

Decimal language ID of the merge module in ModuleID. This is a foreign key into the [ModuleSignature table](modulesignature-table.md).

</dd> <dt>

<span id="RequiredID"></span><span id="requiredid"></span><span id="REQUIREDID"></span>RequiredID
</dt> <dd>

Identifier of the merge module required by the merge module in ModuleID.

</dd> <dt>

<span id="RequiredLanguage"></span><span id="requiredlanguage"></span><span id="REQUIREDLANGUAGE"></span>RequiredLanguage
</dt> <dd>

Numeric language ID of the merge module in RequiredID. The RequiredLanguage column can specify the language ID for a single language, such as 1033 for U.S. English, or specify the language ID for a language group, such as 9 for any English. If the field contains a group language ID, any merge module with having a language code in that group satisfies the dependency. If the RequiredLanguage is set to 0, any merge module filling the other requirements satisfies the dependency.

</dd> <dt>

<span id="RequiredVersion"></span><span id="requiredversion"></span><span id="REQUIREDVERSION"></span>RequiredVersion
</dt> <dd>

Version of the merge module in RequiredID. If this field is Null, any version fills the dependency.

</dd> </dl>

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE25](ice25.md)  
</dl>

 

 



