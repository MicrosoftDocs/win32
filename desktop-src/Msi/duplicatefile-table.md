---
description: The DuplicateFile table contains a list of files that are to be duplicated, either to a different directory than the original file or to the same directory but with a different name. The original file must be a file installed by the InstallFiles action.
ms.assetid: 7fe1b52d-4b06-48cd-afe5-2bd5495bb55e
title: DuplicateFile Table
ms.topic: article
ms.date: 05/31/2018
---

# DuplicateFile Table

The DuplicateFile table contains a list of files that are to be duplicated, either to a different directory than the original file or to the same directory but with a different name. The original file must be a file installed by the [InstallFiles action](installfiles-action.md).

The DuplicateFile table has the following columns.



| Column      | Type                         | Key | Nullable |
|-------------|------------------------------|-----|----------|
| FileKey     | [Identifier](identifier.md) | Y   | N        |
| Component\_ | [Identifier](identifier.md) | N   | N        |
| File\_      | [Identifier](identifier.md) | N   | N        |
| DestName    | [Filename](filename.md)     | N   | Y        |
| DestFolder  | [Identifier](identifier.md) | N   | Y        |



 

## Columns

<dl> <dt>

<span id="FileKey"></span><span id="filekey"></span><span id="FILEKEY"></span>FileKey
</dt> <dd>

A primary key, a non-localized token, identifying a unique DuplicateFile record.

</dd> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

An external key to the first column of the [Component table](component-table.md). If the component identified by the key is not selected for installation or removal, then no action is taken on this DuplicateFile record.

</dd> <dt>

<span id="File_"></span><span id="file_"></span><span id="FILE_"></span>File\_
</dt> <dd>

Foreign key into the [File table](file-table.md) representing the original file that is to be duplicated.

</dd> <dt>

<span id="DestName"></span><span id="destname"></span><span id="DESTNAME"></span>DestName
</dt> <dd>

Localizable name to be given to the duplicate file. If this field is blank, then the destination file is given the same name as the original file.

</dd> <dt>

<span id="DestFolder"></span><span id="destfolder"></span><span id="DESTFOLDER"></span>DestFolder
</dt> <dd>

Name of a property that is the full path to where the duplicate file is to be copied. If this directory is the same as the directory containing the original file and the name for the proposed duplicate file is the same as the original, then no action takes place.

</dd> </dl>

## Remarks

The table is processed by the [DuplicateFiles action](duplicatefiles-action.md) and the [RemoveDuplicateFiles action](removeduplicatefiles-action.md).

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE18](ice18.md)  
[ICE32](ice32.md)  
</dl>

 

 



