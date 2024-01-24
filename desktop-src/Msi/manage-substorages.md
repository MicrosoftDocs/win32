---
description: The VBScript file WiSubStg.vbs is provided in the Windows SDK Components for Windows Installer Developers.
ms.assetid: a0248dfb-e406-4ce6-ab11-1e428aa67af4
title: Manage Substorages
ms.topic: article
ms.date: 05/31/2018
---

# Manage Substorages

The VBScript file WiSubStg.vbs is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). This sample shows how script can be used to manage substorages in a Windows Installer database. A transform can be added to an existing Windows Installer database as a substorage.

The sample demonstrates the use of:

-   [\_Storages table](-storages-table.md)
-   [**OpenDatabase method (Installer Object)**](installer-opendatabase.md)
-   [**CreateRecord method**](installer-createrecord.md)
-   [**LastErrorRecord method**](installer-lasterrorrecord.md) of the [**Installer object**](installer-object.md)
-   [**OpenView method**](database-openview.md)
-   [**Commit method**](database-commit.md) of the [**Database object**](database-object.md)
-   [**Fetch method**](view-fetch.md)
-   [**Modify method**](view-modify.md)
-   [**Execute method**](view-execute.md) of the [**View object**](view-object.md)
-   [**StringData property**](record-stringdata.md)
-   [**SetStream method**](record-setstream.md) of the [**Record object**](record-object.md)

You'll require the CScript.exe or WScript.exe version of Windows Script Host to use this sample. To use CScript.exe to run this sample, type a command line at the command prompt using the following syntax. Help is displayed if the first argument is /? or if too few arguments are specified. To redirect the output to a file, end the command line with VBS > \[*path to file*\]. The sample returns a value of 0 for success, 1 if help is invoked, and 2 if the script fails.

**cscript WiSubStg.vbs \[path to database\]\[path to file\]\[options\]\[substorage name\]**

Specify the path to the Windows Installer database to add or remove substorage. Specify a path to the transform or database file that is being added as substorage. To list the substorages in the Windows Installer database, omit the path to this file. You may specify an optional substorage name, if this is omitted the substorage name defaults to the file name.

The following option may be specified.



| Option              | Description                                                                                         |
|---------------------|-----------------------------------------------------------------------------------------------------|
| no option specified | Add a substorage to the Windows Installer database.                                                 |
| /d                  | Remove a substorage. This option flag must be followed by the name of the substorage to be removed. |



 

For additional scripting examples, see [Windows Installer Scripting Examples](windows-installer-scripting-examples.md). For sample utilities that do not require Windows Script Host, see [Windows Installer Development Tools](windows-installer-development-tools.md).

Note that [A Localization Example](a-localization-example.md) demonstrates [Embedding Customization Transforms as Substorage](embedding-customization-transforms-as-substorage.md).

 

 



