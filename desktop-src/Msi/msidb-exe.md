---
description: Msidb.exe uses MsiDatabaseImport and MsiDatabaseExport to import and export database tables and streams.
ms.assetid: 2eee535f-e7f6-4e1a-9667-df4b8067b132
title: Msidb.exe
ms.topic: article
ms.date: 05/31/2018
---

# Msidb.exe

Msidb.exe uses [**MsiDatabaseImport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseimporta) and [**MsiDatabaseExport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseexporta) to import and export [database tables](database-tables.md) and streams.

If the mode, folder, database and table list are specified on the command line, Msidb.exe does not bring up any user interface and operates as a silent command-line utility suitable for build script.

## Syntax

**MsiDb** *{option}***...***{option}***...** *{table}***...***{table}*

## Command Line Options

Msidb.exe uses the following case-insensitive command line options. A slash delimiter may also be used in place of a dash.



| Option | Description                                                                                                                                                                                                                                                                                                                         |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -i     | Import text archive files from folder into database. Table names for import are file names 8 characters long with an ".idt" extension. Longer names are truncated to 8 characters if supplied by command for import. Standard wild card specifications may be used.                                                                 |
| -e     | Export selected tables from database into text archive files in folder. Table names for export are table names. Only the wildcard specification, "\*", may be used. Tables may be exported from a read only database.                                                                                                               |
| -c     | Creates a new database file and imports tables. Overwrites an existing database file.                                                                                                                                                                                                                                               |
| -f     | Specifies the folder containing the text archive files for tables and streams. If the folder containing the text archive files is not specified, the utility prompts the user for the folder.                                                                                                                                       |
| -d     | Fully qualified path to the database file.                                                                                                                                                                                                                                                                                          |
| -m     | Fully qualified path to the database that is to be merged in. This option is available only in silent command line mode. Multiple instances of this option may occur to a maximum of 10. If the database is not specified on the command-line, the utility prompts the user for the database.                                       |
| -t     | Fully qualified path to the transform to be applied. This option is available only in silent command line mode. Multiple instances of this option may occur to a maximum of 10.                                                                                                                                                     |
| -j     | Name of storage to remove from the database. This option is available only in silent command line mode. Multiple instances of this option may occur to a maximum of 10.                                                                                                                                                             |
| -k     | Name of stream to remove from the database. This option available only in silent command line mode. Multiple instances of this option may occur to a maximum of 10.                                                                                                                                                                 |
| -x     | Name of stream to save to a disk file in the current directory. This option is available only in silent command line mode. Binary data streams are stored as separate files with the extension ".ibd". Binary filename used is primary key data for the row containing the stream.                                                  |
| -w     | Name of storage to save to a disk file in the current directory. This option is available only in silent command line mode.                                                                                                                                                                                                         |
| -a     | Name of file to add to the database as a stream. This option is available only in silent command line mode. Multiple instances of this option may occur to a maximum of 10. Binary data streams are stored as separate files with the extension ".ibd". Binary filename used is primary key data for the row containing the stream. |
| -r     | Name of storage to add to the database as a substorage. This option available only in silent command line mode. Multiple instances of this option may occur to a maximum of 10.                                                                                                                                                     |
| -s     | Truncate table names to 8 characters on export to an .idt. The table name is truncated to 8 characters and the extension ".idt" is added.                                                                                                                                                                                           |
| -?     | Displays the command line help dialog                                                                                                                                                                                                                                                                                               |



 

> [!Note]  
> When using long filenames with spaces, use quotes around them. For example, for a database that is in the "My Documents" folder, specify it as "c:\\my documents".

 

This tool is only available in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md).

## Related topics

<dl> <dt>

[Windows Installer Development Tools](windows-installer-development-tools.md)
</dt> <dt>

[Released Versions, Tools, and Redistributables](released-versions-tools-and-redistributables.md)
</dt> </dl>

 

 



