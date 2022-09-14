---
description: The VBScript file WiFeatur.vbs is provided in the Windows SDK Components for Windows Installer Developers.
ms.assetid: 797cb383-22c0-42b4-82c1-d5bcc3a8bafb
title: List Features
ms.topic: article
ms.date: 05/31/2018
---

# List Features

The VBScript file WiFeatur.vbs is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). This sample shows how script is used to list the features in a Windows Installer database. This sample demonstrates adding temporary columns to a read-only Windows Installer database.

This sample demonstrates:

-   [**OpenDatabase method (Installer Object)**](installer-opendatabase.md), the [**CreateRecord method**](installer-createrecord.md), and the [**LastErrorRecord method**](installer-lasterrorrecord.md) of the [**Installer Object**](installer-object.md)
-   [**Execute method**](view-execute.md) and the [**Fetch method**](view-fetch.md) of the [**View Object**](view-object.md)
-   [**OpenView method**](database-openview.md), the [**TablePersistent property**](database-tablepersistent.md), and the [**PrimaryKeys property**](database-primarykeys.md) of the [**Database Object**](database-object.md)
-   [**FieldCount property**](record-fieldcount.md), [**IntegerData property**](record-integerdata.md), and the [**StringData property**](record-stringdata.md) of the [**Record Object**](record-object.md)

Using this sample requires the CScript.exe or WScript.exe version of Windows Script Host. To use CScript.exe to run this sample, type a command at the command prompt using the following syntax. Help is displayed if the first argument is /? or if too few arguments are specified. To redirect the output to a file, end the command line with VBS > \[*path to file*\]. The sample returns a value of 0 for success, 1 if help is invoked, and 2 if the script fails.

**cscript WiFeatur.vbs \[path to database\]\[feature name\]**

Specify path to the Windows Installer database. Specify the name of the feature. This must be listed in the Feature column of the [Feature table](feature-table.md). If the name of the feature is omitted, all the features are listed as a feature tree. If an asterisk (\*) is used as the feature name, WiFeatur.vbs lists the composition of all features. Note that large databases are better displayed using CScript rather than WScript.

For more information, see [Windows Installer Scripting Examples](windows-installer-scripting-examples.md) for additional scripting examples. For sample utilities that do not require Windows Script Host see [Windows Installer Development Tools](windows-installer-development-tools.md).

 

 



