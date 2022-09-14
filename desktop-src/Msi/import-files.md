---
description: The VBScript file WiImport.vbs is provided in the Windows SDK Components for Windows Installer Developers. This sample shows how to write a script to import tables into a Windows Installer database.
ms.assetid: 37580bd6-30c7-4239-9717-223a381ba021
title: Import Files
ms.topic: article
ms.date: 05/31/2018
---

# Import Files

The VBScript file WiImport.vbs is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). This sample shows how to write a script to import tables into a Windows Installer database.

The script connects to an [**Installer**](installer-object.md) object, opens a database, processes a list of files, and commits the changes before closing the database.

The sample demonstrates the use of:

-   [**OpenDatabase Method (Installer Object)**](installer-opendatabase.md)
-   [**LastErrorRecord method**](installer-lasterrorrecord.md) of the [**Installer object**](installer-object.md)
-   [**Import method**](database-import.md)
-   [**Commit method**](database-commit.md) of the [**Database object**](database-object.md)

You'll require the CScript.exe or WScript.exe version of Windows Script Host to use this sample. To use CScript.exe to run this sample, use the following syntax at the command prompt.

**cscript WiImport.vbs \[path to database\]\[path to folder\]\[options\] \[archive file list**\]

Help is displayed if the first argument is /? or if too few arguments are specified. To redirect the output to a file, end the command line with VBS > \[path to file\].The sample returns a value of 0 for success, 1 if help is invoked, and 2 if the script fails.

Specify the path to a Windows installer database that is to be created or that is to receive the imported tables. Specify the path to the folder containing the archive files of the tables that are being imported. List the names of the archive files that are being imported. Wildcard file names, such as \*.idt, can be used to import multiple files.

The following options may be specified anywhere on the command line before the file list.



| Option              | Description                                                                                                                          |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| no option specified | Import the list of table archive files from the specified folder into the Windows Installer database.                                |
| /c                  | Create a Windows Installer database and then import the list of table archive files from the specified folder into the new database. |



 

For more information, see [Windows Installer Scripting Examples](windows-installer-scripting-examples.md) for additional scripting examples. For sample utilities that do not require Windows Script Host, see [Windows Installer Development Tools](windows-installer-development-tools.md).

Note that [A Localization Example](a-localization-example.md) also demonstrates [Importing Localized Error and ActionText Tables](importing-localized-error-and-actiontext-tables.md).

 

 



