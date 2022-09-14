---
description: This table contains a list of files to be moved or copied from a specified source directory to a specified destination directory.
ms.assetid: 9ba47bdc-90c8-444a-ba8b-71c723b54556
title: MoveFile Table
ms.topic: article
ms.date: 05/31/2018
---

# MoveFile Table

This table contains a list of files to be moved or copied from a specified source directory to a specified destination directory.

The MoveFile table has the following columns.



| Column       | Type                         | Key | Nullable |
|--------------|------------------------------|-----|----------|
| FileKey      | [Identifier](identifier.md) | Y   | N        |
| Component\_  | [Identifier](identifier.md) | N   | N        |
| SourceName   | [Text](text.md)             | N   | Y        |
| DestName     | [Filename](filename.md)     | N   | Y        |
| SourceFolder | [Identifier](identifier.md) | N   | Y        |
| DestFolder   | [Identifier](identifier.md) | N   | N        |
| Options      | [Integer](integer.md)       | N   | N        |



 

## Columns

<dl> <dt>

<span id="FileKey"></span><span id="filekey"></span><span id="FILEKEY"></span>FileKey
</dt> <dd>

Primary key that uniquely identifies a particular MoveFile record.

</dd> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

External key into the [Component table](component-table.md). If the component referenced by this key is not selected for installation or removal, then no action is taken on this MoveFile entry.

</dd> <dt>

<span id="SourceName"></span><span id="sourcename"></span><span id="SOURCENAME"></span>SourceName
</dt> <dd>

This column contains the localizable name of the source files to be moved or copied. This column may be left blank. See the description of the SourceFolder column. This field must contain a long file name and may contain wildcard characters (\* and ?).

</dd> <dt>

<span id="DestName"></span><span id="destname"></span><span id="DESTNAME"></span>DestName
</dt> <dd>

This column contains the localizable name to be given to the original file after it is moved or copied. If this field is blank, then the destination file is given the same name as the source file.

</dd> <dt>

<span id="SourceFolder"></span><span id="sourcefolder"></span><span id="SOURCEFOLDER"></span>SourceFolder
</dt> <dd>

This column contains the name of a property having a value that resolves to the full path to the source directory. If the SourceName column is left blank, then the property named in the SourceFolder column is assumed to contain the full path to the source file itself (including the file name).

</dd> <dt>

<span id="DestFolder"></span><span id="destfolder"></span><span id="DESTFOLDER"></span>DestFolder
</dt> <dd>

The name of a property whose value resolves to the full path to the destination directory.

</dd> <dt>

<span id="Options"></span><span id="options"></span><span id="OPTIONS"></span>Options
</dt> <dd>

Integer value specifying the operating mode.



| Constant                     | Hexadecimal | Decimal | Meaning               |
|------------------------------|-------------|---------|-----------------------|
| (none)                       | 0x000       | 0       | Copy the source file. |
| **msidbMoveFileOptionsMove** | 0x001       | 1       | Move the source file. |



 

</dd> </dl>

## Remarks

If a "\*" wildcard is entered in the SourceName column of the MoveFile table and a destination file name is specified in the DestName column, all moved or copied files retain the names in the sources.

This table is processed by the [MoveFiles action](movefiles-action.md).

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE18](ice18.md)  
[ICE32](ice32.md)  
[ICE45](ice45.md)  
[ICE85](ice85.md)  
</dl>

 

 



