---
description: The ModuleExclusion table keeps a list of other merge modules that are incompatible in the same installer database.
ms.assetid: c28d9afa-152c-43b5-9892-7a38fae8c593
title: ModuleExclusion Table
ms.topic: article
ms.date: 05/31/2018
---

# ModuleExclusion Table

The ModuleExclusion table keeps a list of other merge modules that are incompatible in the same installer database. This table enables a merge or verification tool to check that conflicting merge modules are not merged in the user's installer database. The tool checks by cross-referencing this table with the ModuleSignature table in the installer database.

The ModuleExclusion table has the following columns.



| Column             | Type                         | Key | Nullable |
|--------------------|------------------------------|-----|----------|
| ModuleID           | [Identifier](identifier.md) | Y   | N        |
| ModuleLanguage     | [Integer](integer.md)       | Y   | N        |
| ExcludedID         | [Identifier](identifier.md) | Y   | N        |
| ExcludedLanguage   | [Integer](integer.md)       | Y   | N        |
| ExcludedMinVersion | [Version](version.md)       |     | Y        |
| ExcludedMaxVersion | [Version](version.md)       |     | Y        |



 

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

<span id="ExcludedID"></span><span id="excludedid"></span><span id="EXCLUDEDID"></span>ExcludedID
</dt> <dd>

Identifier of an excluded merge module.

</dd> <dt>

<span id="ExcludedLanguage"></span><span id="excludedlanguage"></span><span id="EXCLUDEDLANGUAGE"></span>ExcludedLanguage
</dt> <dd>

Numeric language ID of the merge module in ExcludedID. The ExcludedLanguage column can specify the language ID for a single language, such as 1033 for U.S. English, or specify the language ID for a language group, such as 9 for any English. The ExcludedLanguage column can accept negative language IDs. The meaning of the value in the ExcludedLanguage column is as follows.



| ExcludedLanguage | Meaning                                                              |
|------------------|----------------------------------------------------------------------|
| > 0           | Exclude the language IDs specified by ExcludedLanguage.              |
| = 0              | Exclude no language IDs.                                             |
| < 0           | Exclude all language IDs except those specified by ExcludedLanguage. |



 

</dd> <dt>

<span id="ExcludedMinVersion"></span><span id="excludedminversion"></span><span id="EXCLUDEDMINVERSION"></span>ExcludedMinVersion
</dt> <dd>

Minimum version excluded from a range. If the ExcludedMinVersion field is Null, all versions before ExcludedMaxVersion are excluded. If both ExcludedMinVersion and ExcludedMaxVersion are Null there is no exclusion based on version.

</dd> <dt>

<span id="ExcludedMaxVersion"></span><span id="excludedmaxversion"></span><span id="EXCLUDEDMAXVERSION"></span>ExcludedMaxVersion
</dt> <dd>

Maximum version excluded from a range. If the ExcludedMaxVersion field is Null, all versions after ExcludedMinVersion are excluded. If both ExcludedMinVersion and ExcludedMaxVersion are Null there is no exclusion based on version.

</dd> </dl>

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE25](ice25.md)  
</dl>

 

 



