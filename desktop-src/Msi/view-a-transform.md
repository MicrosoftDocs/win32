---
description: The VBScript file WiLstXfm.vbs is provided in the Windows SDK Components for Windows Installer Developers. This script sample can be used to view a transform file.
ms.assetid: c2e3dd56-b0e5-481a-b7b8-5000fa686850
title: View a Transform
ms.topic: article
ms.date: 05/31/2018
---

# View a Transform

The VBScript file WiLstXfm.vbs is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). This script sample can be used to view a transform file.

The sample demonstrates the use of:

-   [\_TransformView table](-transformview-table.md)
-   [**OpenDatabase method (Installer Object)**](installer-opendatabase.md)
-   [**LastErrorRecord method**](installer-lasterrorrecord.md) of the [**Installer object**](installer-object.md)
-   [**ApplyTransform method**](database-applytransform.md)
-   [**OpenView method**](database-openview.md)
-   [**Commit method**](database-commit.md) of the [**Database object**](database-object.md)
-   [**IsNull property**](record-isnull.md)
-   [**StringData property**](record-stringdata.md) of the [**Record object**](record-object.md)

Using this sample requires the CScript.exe version of Windows Script Host. To use CScript.exe to run this sample, type a command at the command prompt using the following syntax. Help is displayed if the first argument is /? or if too few arguments are specified. To redirect the output to a file, end the command line with VBS > \[*path to file*\]. The sample returns a value of 0 for success, 1 if help is invoked, and 2 if the script fails.

**cscript WiLstXfm.vbs** *\[path to reference database\]\[option\]\[path to transform to be viewed\]*

Specify the path to the reference Windows Installer database. Specify a list of paths to transform files that are being viewed. Each path in the list may by preceded by an optional numeric value. This value specifies a set of error conditions that are to be suppressed. You may add these values together to suppress multiple conditions. If no numeric option is specified, all the error conditions are suppressed. The arguments in this list are executed in the left-to-right order in which they appear on the command line.



| Value | Error condition to suppress                   |
|-------|-----------------------------------------------|
| 1     | Adding a row that already exists.             |
| 2     | Deleting a row that does not exist.           |
| 4     | Adding a table that already exists.           |
| 8     | Deleting a table that does not exist.         |
| 16    | Updating a row that does not exist.           |
| 256   | Mismatch of database and transform codepages. |



 

For additional scripting examples, see [Windows Installer Scripting Examples](windows-installer-scripting-examples.md). For sample utilities that do not require Windows Script Host, see [Windows Installer Development Tools](windows-installer-development-tools.md).

 

 



