---
description: The VBScript file WiUseXfm.vbs is provided in the Windows SDK Components for Windows Installer Developers. This sample shows how script can be used to apply a transform to a Windows Installer database.
ms.assetid: e647388e-5211-463d-9e3e-b502af01fc0c
title: Apply a Transform
ms.topic: article
ms.date: 05/31/2018
---

# Apply a Transform

The VBScript file WiUseXfm.vbs is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). This sample shows how script can be used to apply a transform to a Windows Installer database.

The sample demonstrates the use of

-   [**OpenDatabase method (Installer Object)**](installer-opendatabase.md)
-   [**LastErrorRecord method**](installer-lasterrorrecord.md) of the [**Installer object**](installer-object.md)
-   [**ApplyTransform method**](database-applytransform.md)
-   [**Commit method**](database-commit.md) of the [**Database object**](database-object.md)

You'll require the CScript.exe or WScript.exe version of Windows Script Host to use this sample. To use CScript.exe to run this sample, type a command line at the command prompt using the following syntax. Help is displayed if the first argument is /? or if too few arguments are specified. To redirect the output to a file, end the command line with VBS > \[*path to file*\]. The sample returns a value of 0 for success, 1 if help is invoked, and 2 if the script fails.

**cscript WiUseXfm.vbs \[path to original database\]\[path to transform file\]\[options\]**

Specify the path to the Windows Installer database. Specify the path to the transform file. If the path to the transform file is omitted, the two databases are only compared. The third argument is an optional numeric value that specifies a set of error conditions that are to be suppressed. Add these values together to suppress multiple conditions.



| Value | Error condition to suppress                   |
|-------|-----------------------------------------------|
| 1     | Adding a row that already exists.             |
| 2     | Deleting a row that does not exist.           |
| 4     | Adding a table that already exists.           |
| 8     | Deleting a table that does not exist.         |
| 16    | Updating a row that does not exist.           |
| 256   | Mismatch of database and transform codepages. |



 

For additional scripting examples, see [Windows Installer Scripting Examples](windows-installer-scripting-examples.md). For sample utilities that do not require Windows Script Host, see [Windows Installer Development Tools](windows-installer-development-tools.md).

 

 



