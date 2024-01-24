---
description: The FileSFPCatalog table associates specified files with the catalog files used by system file protection.
ms.assetid: 70c8b64a-cf15-411c-8388-4a7e3051f45c
title: FileSFPCatalog Table
ms.topic: article
ms.date: 05/31/2018
---

# FileSFPCatalog Table

The FileSFPCatalog table associates specified files with the catalog files used by system file protection.

**Windows Vista, Windows Server 2003 and Windows XP:** Not supported.

The FileSFPCatalog table has the following columns.



| Column       | Type                         | Key | Nullable |
|--------------|------------------------------|-----|----------|
| File\_       | [Identifier](identifier.md) | Y   | N        |
| SFPCatalog\_ | [Filename](filename.md)     | Y   | N        |



 

## Columns

<dl> <dt>

<span id="File_"></span><span id="file_"></span><span id="FILE_"></span>File\_
</dt> <dd>

Foreign key to the [File table](file-table.md).

</dd> <dt>

<span id="SFPCatalog_"></span><span id="sfpcatalog_"></span><span id="SFPCATALOG_"></span>SFPCatalog\_
</dt> <dd>

Foreign key to the [SFPCatalog table](sfpcatalog-table.md).

</dd> </dl>

## Remarks

The [InstallSFPCatalogFile action](installsfpcatalogfile-action.md) queries the [Component table](component-table.md), [File table](file-table.md), FileSFPCatalog table and [SFPCatalog table](sfpcatalog-table.md).

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
[ICE66](ice66.md)  
[ICE76](ice76.md)  
</dl>

 

 



