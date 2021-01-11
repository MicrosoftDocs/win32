---
description: The IniLocator table holds the information needed to search for a file or directory using an .ini file or to search for a particular .ini entry itself. The .ini file must be present in the default Microsoft Windows directory.
ms.assetid: 5a3c6077-34ef-48c8-b4e6-ecb1deb40f96
title: IniLocator Table
ms.topic: article
ms.date: 05/31/2018
---

# IniLocator Table

The IniLocator table holds the information needed to search for a file or directory using an .ini file or to search for a particular .ini entry itself. The .ini file must be present in the default Microsoft Windows directory.

The IniLocator table has the following columns.



| Column      | Type                         | Key | Nullable |
|-------------|------------------------------|-----|----------|
| Signature\_ | [Identifier](identifier.md) | Y   | N        |
| FileName    | [FileName](text.md)         | N   | N        |
| Section     | [Text](text.md)             | N   | N        |
| Key         | [Text](text.md)             | N   | N        |
| Field       | [Integer](integer.md)       | N   | Y        |
| Type        | [Integer](integer.md)       | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Signature_"></span><span id="signature_"></span><span id="SIGNATURE_"></span>Signature\_
</dt> <dd>

An external key into the first column of the [Signature table](signature-table.md). The Signature\_ represents a unique signature and is also the external key into column one of the Signature table. If this signature is present in the Signature table, then the search is for a file. If this key is absent from the Signature table, and the value of the Type column is **msidbLocatorTypeRawValue**, the search is for the .ini entry specified by the IniLocator table. Otherwise the search is for a directory specified by the IniLocator table.

</dd> <dt>

<span id="FileName"></span><span id="filename"></span><span id="FILENAME"></span>FileName
</dt> <dd>

The .ini file name.

</dd> <dt>

<span id="Section"></span><span id="section"></span><span id="SECTION"></span>Section
</dt> <dd>

Section name within the .ini file.

</dd> <dt>

<span id="Key"></span><span id="key"></span><span id="KEY"></span>Key
</dt> <dd>

Key value within the section.

</dd> <dt>

<span id="Field"></span><span id="field"></span><span id="FIELD"></span>Field
</dt> <dd>

The field in the .ini line. If Field is Null or 0, then the entire line is read. This must be a non-negative number.

</dd> <dt>

<span id="Type"></span><span id="type"></span><span id="TYPE"></span>Type
</dt> <dd>

A value that determines whether the .ini value is a file location, a directory location, or raw .ini value.

The following table lists valid values. If absent, Type is set to be 1.



| Constant                      | Hexadecimal | Decimal | Description           |
|-------------------------------|-------------|---------|-----------------------|
| **msidbLocatorTypeDirectory** | 0x000       | 0       | A directory location. |
| **msidbLocatorTypeFileName**  | 0x001       | 1       | A file location.      |
| **msidbLocatorTypeRawValue**  | 0x002       | 2       | A raw .ini value.     |



 

</dd> </dl>

## Remarks

This table is used with the [AppSearch Table](appsearch-table.md).

This table's columns are generally not localized. If an author decides to search for products in multiple languages, then there can be a separate entry included in the table for each language.

Associated localized text for progress display or logging is specified in the [ActionText table](actiontext-table.md).

See [Searching for Existing Applications, Files, Registry Entries or .ini File Entries](searching-for-existing-applications-files-registry-entries-or--ini-file-entries.md).

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
</dl>

 

 



