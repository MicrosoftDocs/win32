---
description: The DrLocator table holds the information needed to find a file or directory by searching the directory tree.
ms.assetid: 2b779ff7-f410-4af0-899d-4432b015d526
title: DrLocator Table
ms.topic: article
ms.date: 05/31/2018
---

# DrLocator Table

The DrLocator table holds the information needed to find a file or directory by searching the directory tree.

The DrLocator table has the following columns.



| Column      | Type                         | Key | Nullable |
|-------------|------------------------------|-----|----------|
| Signature\_ | [Identifier](identifier.md) | Y   | N        |
| Parent      | [Identifier](identifier.md) | Y   | Y        |
| Path        | [AnyPath](anypath.md)       | Y   | Y        |
| Depth       | [Integer](integer.md)       | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Signature_"></span><span id="signature_"></span><span id="SIGNATURE_"></span>Signature\_
</dt> <dd>

The Signature\_ column is an external key to the first column of the [Signature table](signature-table.md). This field may represent a unique file signature listed in the Signature table. If the value in this column is absent from the Signature table, then the search is assumed to be for a directory pointed to by the DrLocator table.

</dd> <dt>

<span id="Parent"></span><span id="parent"></span><span id="PARENT"></span>Parent
</dt> <dd>

This column is the signature of the parent directory of the file or directory in the Signature\_ column. If this field is null, and the Path column does not expand to a full path, then all the fixed drives of the user's system are searched by using the Path.

This field is a key into one of the following tables: the [RegLocator](reglocator-table.md), the [IniLocator](inilocator-table.md), the [CompLocator](complocator-table.md), or the DrLocator tables.

</dd> <dt>

<span id="Path"></span><span id="path"></span><span id="PATH"></span>Path
</dt> <dd>

The Path column contains the path on the user's system. This is a either a full path or a relative subpath below the directory specified in the Parent column. See the restrictions on the [AnyPath](anypath.md) data type.

</dd> <dt>

<span id="Depth"></span><span id="depth"></span><span id="DEPTH"></span>Depth
</dt> <dd>

The depth below the path that the installer searches for the file or directory specified in the Signature\_ column. The value used in the Depth field is based on zero. For example, if the Path field is c:/Program Files/bin, the Depth column must be set to 0 or greater, to detect a file located inside the folder bin. If the Depth field is empty, the depth is assumed to be zero.

</dd> </dl>

## Remarks

This table is used with the [AppSearch Table](appsearch-table.md).

This table's columns are generally not localized. If an author decides to search for products in multiple languages, then there must be a separate entry included in the table for each language.

See [Searching for Existing Applications, Files, Registry Entries or .ini File Entries](searching-for-existing-applications-files-registry-entries-or--ini-file-entries.md).

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE46](ice46.md)  
</dl>

 

 



