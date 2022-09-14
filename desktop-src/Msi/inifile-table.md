---
description: The IniFile table contains the .ini information that the application needs to set in an .ini file.
ms.assetid: fdb1a627-da6b-4da1-87a7-7f1c94d3836e
title: IniFile Table
ms.topic: article
ms.date: 05/31/2018
---

# IniFile Table

The IniFile table contains the .ini information that the application needs to set in an .ini file.

The IniFile table has the following columns.



| Column      | Type                         | Key | Nullable |
|-------------|------------------------------|-----|----------|
| IniFile     | [Identifier](identifier.md) | Y   | N        |
| FileName    | [FileName](text.md)         | N   | N        |
| DirProperty | [Identifier](identifier.md) | N   | Y        |
| Section     | [Formatted](formatted.md)   | N   | N        |
| Key         | [Formatted](formatted.md)   | N   | N        |
| Value       | [Formatted](formatted.md)   | N   | N        |
| Action      | [Integer](integer.md)       | N   | N        |
| Component\_ | [Identifier](identifier.md) | N   | N        |



 

## Columns

<dl> <dt>

<span id="IniFile"></span><span id="inifile"></span><span id="INIFILE"></span>IniFile
</dt> <dd>

The key for this table.

</dd> <dt>

<span id="FileName"></span><span id="filename"></span><span id="FILENAME"></span>FileName
</dt> <dd>

The localizable name of the .ini file in which to write the information.

</dd> <dt>

<span id="DirProperty"></span><span id="dirproperty"></span><span id="DIRPROPERTY"></span>DirProperty
</dt> <dd>

Name of a property having a value that resolves to the full path of the folder containing the .ini file. The property can be the name of a directory in the [Directory table](directory-table.md), a property set by the [AppSearch table](appsearch-table.md), or any other property that represents a full path. If this field is left blank, the .ini file is created in the folder having the full path specified by the [**WindowsFolder**](windowsfolder.md) property.

</dd> <dt>

<span id="Section"></span><span id="section"></span><span id="SECTION"></span>Section
</dt> <dd>

The localizable .ini file section.

</dd> <dt>

<span id="Key"></span><span id="key"></span><span id="KEY"></span>Key
</dt> <dd>

The localizable .ini file key within the section.

</dd> <dt>

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>Value
</dt> <dd>

The localizable value to be written.

</dd> <dt>

<span id="Action"></span><span id="action"></span><span id="ACTION"></span>Action
</dt> <dd>

The type of modification to be made.



| Constant                         | Hexadecimal | Decimal | Modification                                                                     |
|----------------------------------|-------------|---------|----------------------------------------------------------------------------------|
| **msidbIniFileActionAddLine**    | 0x000       | 0       | Creates or updates a .ini entry.                                                 |
| **msidbIniFileActionCreateLine** | 0x001       | 1       | Creates a .ini entry only if the entry does not already exist.                   |
| **msidbIniFileActionAddTag**     | 0x003       | 3       | Creates a new entry or appends a new comma-separated value to an existing entry. |



 

</dd> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

External key into the first column of the [Component table](component-table.md) referencing the component that controls the installation of the .ini value.

</dd> </dl>

## Remarks

The .ini file information is written out when the corresponding component has been selected to be installed as local or run from source.

This table is referred to when the [WriteIniValues action](writeinivalues-action.md) or the [RemoveIniValues action](removeinivalues-action.md) is executed.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
[ICE46](ice46.md)  
[ICE69](ice69.md)  
[ICE88](ice88.md)  
[ICE91](ice91.md)  
</dl>

 

 



