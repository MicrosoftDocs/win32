---
description: The VBScript file WiExport.vbs is provided in the Windows SDK Components for Windows Installer Developers.
ms.assetid: 3ff7bd48-cb22-4d5b-a607-39eaeb67c55b
title: Export Files
ms.topic: article
ms.date: 05/31/2018
---

# Export Files

The VBScript file WiExport.vbs is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). This sample shows how to write script to export tables into a Windows Installer database. The script sample connects to an [**Installer**](installer-object.md) object, opens a database and exports tables to archive files.

The sample demonstrates the use of:

-   [**OpenDatabase Method (Installer Object)**](installer-opendatabase.md)
-   [**LastErrorRecord method**](installer-lasterrorrecord.md) of the [**Installer object**](installer-object.md)
-   [**Export method**](database-export.md)
-   [**OpenView method**](database-openview.md) of the [**Database object**](database-object.md)
-   [**Fetch method**](view-fetch.md) of the [**View object**](view-object.md)
-   [**StringData property**](record-stringdata.md) of the [**Record object**](record-object.md)

You'll require the CScript.exe or WScript.exe version of Windows Script Host to use this sample. To use CScript.exe to run this sample, type a command line at the command prompt using the following syntax. Help is displayed if the first argument is /? or if too few arguments are specified. To redirect the output to a file, end the command line with VBS > \[*path to file*\]. The sample returns a value of 0 for success, 1 if help is invoked, and 2 if the script fails.

**cscript WiExport.vbs \[path to database\]\[path to folder\]\[options\]\[table name list\]**

Specify the path to the installer database from which the tables are being exported. Specify the path to the folder into which the exported archive files are to be copied. List the case-sensitive names of the [database tables](database-tables.md) being exported. Specify '\*' to export all the tables including \_SummaryInformation.

The following options may be specified anywhere on the command line before the table name list.



| Option              | Description                                            |
|---------------------|--------------------------------------------------------|
| no option specified | Exported archive files may have a long file name.      |
| /s                  | Force exported archive files to have short file names. |



 

For additional scripting examples, see [Windows Installer Scripting Examples](windows-installer-scripting-examples.md). For sample utilities that do not require Windows Script Host, see [Windows Installer Development Tools](windows-installer-development-tools.md).

 

 



