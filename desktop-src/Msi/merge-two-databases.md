---
description: The VBScript file WiMerge.vbs is provided in the Windows SDK Components for Windows Installer Developers. This sample script merges one Windows Installer database into another database. For more information, see Merges and Transforms.
ms.assetid: 31867082-7c1d-4530-a066-236d8ee5f023
title: Merge Two Databases
ms.topic: article
ms.date: 05/31/2018
---

# Merge Two Databases

The VBScript file WiMerge.vbs is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). This sample script merges one Windows Installer database into another database. For more information, see [Merges and Transforms](merges-and-transforms.md).

The [**MsiDatabaseMerge**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabasemergea) function and the [**Merge**](database-merge.md) method of the [**Database**](database-object.md) object cannot be used to merge a module included in the installation package. They should not be used to merge [Merge Modules](merge-modules.md) into a Windows Installer package. To include a merge module in an installation package, authors of installation packages should follow the guidelines that are described in [Applying Merge Modules](applying-merge-modules.md) topic.

The sample demonstrates the use of the following:

-   [**OpenDatabase method (Installer Object)**](installer-opendatabase.md)
-   [**LastErrorRecord method**](installer-lasterrorrecord.md) of the [**Installer object**](installer-object.md)
-   [**OpenView method**](database-openview.md)
-   [**Merge method**](database-merge.md)
-   [**Commit method**](database-commit.md) of the [**Database object**](database-object.md)
-   [**Fetch method**](view-fetch.md)
-   [**View object**](view-object.md)
-   [**StringData property**](record-stringdata.md) of the [**Record object**](record-object.md)

You must have the CScript.exe or WScript.exe version of Windows Script Host to use this sample. To use CScript.exe to run this sample, type a command line at the command prompt using the following syntax. Help is displayed if the first argument is /? or if too few arguments are specified. To redirect the output to a file, end the command line with VBS > \[path to file\]. The sample returns a value of 0 for success, 1 if help is invoked, and 2 if the script fails.

**cscript WiMerge.vbs \[path to database\]\[path to imported database\]\[table name\]**

Specify the path to the Windows Installer database that is receiving the merge. Specify the path to the database being imported into the first. You may specify an optional name for a table to hold the merge errors. If no table name is specified, the installer uses the name \_MergeErrors and drops the table after displaying the contents.

For additional scripting examples, see [Windows Installer Scripting Examples](windows-installer-scripting-examples.md). For sample utilities that do not require Windows Script Host, see [Windows Installer Development Tools](windows-installer-development-tools.md).

 

 



