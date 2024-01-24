---
description: The RemoveIniFile table contains the information an application needs to delete from a .ini file.
ms.assetid: 702cf86e-02f4-4ea7-8573-b500ac550aae
title: RemoveIniFile Table
ms.topic: article
ms.date: 05/31/2018
---

# RemoveIniFile Table

The RemoveIniFile table contains the information an application needs to delete from a .ini file.

The RemoveIniFile table has the following columns.



| Column        | Type                         | Key | Nullable |
|---------------|------------------------------|-----|----------|
| RemoveIniFile | [Identifier](identifier.md) | Y   | N        |
| FileName      | [FileName](text.md)         | N   | N        |
| DirProperty   | [Identifier](identifier.md) | N   | Y        |
| Section       | [Formatted](formatted.md)   | N   | N        |
| Key           | [Formatted](formatted.md)   | N   | N        |
| Value         | [Formatted](formatted.md)   | N   | Y        |
| Action        | [Integer](integer.md)       | N   | N        |
| Component\_   | [Identifier](identifier.md) | N   | N        |



 

## Columns

<dl> <dt>

<span id="RemoveIniFile"></span><span id="removeinifile"></span><span id="REMOVEINIFILE"></span>RemoveIniFile
</dt> <dd>

The key for this table.

</dd> <dt>

<span id="FileName"></span><span id="filename"></span><span id="FILENAME"></span>FileName
</dt> <dd>

The .ini file name in which to delete the information.

</dd> <dt>

<span id="DirProperty"></span><span id="dirproperty"></span><span id="DIRPROPERTY"></span>DirProperty
</dt> <dd>

Name of a property whose value is assumed to resolve to the full path to the folder of the .ini file to be removed. The property can be the name of a directory in the [Directory table](directory-table.md), a property set by the [AppSearch table](appsearch-table.md), or any other property that represents a full path.

</dd> <dt>

<span id="Section"></span><span id="section"></span><span id="SECTION"></span>Section
</dt> <dd>

The localizable .ini file section.

</dd> <dt>

<span id="Key"></span><span id="key"></span><span id="KEY"></span>Key
</dt> <dd>

The localizable .ini file key below the section.

</dd> <dt>

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>Value
</dt> <dd>

The localizable value to be deleted. The value is required when Action is 4.

</dd> <dt>

<span id="Action"></span><span id="action"></span><span id="ACTION"></span>Action
</dt> <dd>

The type of modification to be made.



| Constant                         | Hexadecimal | Decimal | Meaning                          |
|----------------------------------|-------------|---------|----------------------------------|
| **msidbIniFileActionRemoveLine** | 0x002       | 2       | Deletes .ini entry.              |
| **msidbIniFileActionRemoveTag**  | 0x004       | 4       | Deletes a tag from a .ini entry. |



 

</dd> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

External key into first column of the [Component table](component-table.md) referencing the component that controls the deletion of the .ini value.

</dd> </dl>

## Remarks

The .ini file information is deleted when the corresponding Component has been selected to be installed, either locally or run from source.

This table is referred to when the [RemoveIniValues action](removeinivalues-action.md) is executed.

If the Directory\_ column is specified as null, the ini file location is the standard Windows ini location which is the Windows directory by default.

Removing the last value from a section deletes that section. There is no other way to delete an entire section other than removing all its values.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
[ICE40](ice40.md)  
[ICE46](ice46.md)  
[ICE69](ice69.md)  
</dl>

 

 



