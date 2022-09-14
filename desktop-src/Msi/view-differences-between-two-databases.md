---
description: The VBScript file WiDiffDb.vbs is provided in the Windows SDK Components for Windows Installer Developers. This sample script generates a temporary transform file between two Windows Installer databases and displays the transform.
ms.assetid: 9750ddc6-de8d-48e9-a984-892f0cf4ac3b
title: View Differences Between Two Databases
ms.topic: article
ms.date: 05/31/2018
---

# View Differences Between Two Databases

The VBScript file WiDiffDb.vbs is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). This sample script generates a temporary transform file between two Windows Installer databases and displays the transform.

The sample demonstrates the use of:

-   [**OpenDatabase method (Installer Object)**](installer-opendatabase.md)
-   [**LastErrorRecord method**](installer-lasterrorrecord.md) of the [**Installer object**](installer-object.md)
-   [**OpenView method**](database-openview.md)
-   [**SummaryInformation property (Database Object)**](database-summaryinformation.md)
-   [**GenerateTransform method**](database-generatetransform.md)
-   [**ApplyTransform method**](database-applytransform.md)
-   [**Database object**](database-object.md)
-   [**Fetch method**](view-fetch.md) of the [**View object**](view-object.md)
-   [**IsNull property**](record-isnull.md)
-   [**StringData property**](record-stringdata.md) of the [**Record object**](record-object.md)
-   [\_TransformView table](-transformview-table.md)

Using this sample requires the CScript.exe version of Windows Script Host. To use CScript.exe to run this sample, type a command at the command prompt using the following syntax. Help is displayed if the first argument is /? or if too few arguments are specified. To redirect the output to a file, end the command line with VBS > \[*path to file*\]. The sample returns a value of 0 for success, 1 if help is invoked, and 2 if the script fails.

**cscript WiDiffDb.vbs** *\[path to original database\]\[path to revised database\]*

Specify the path to the original Windows Installer database. Specify the path to the revised database. The sample script will display the transform.

For additional scripting examples, see [Windows Installer Scripting Examples](windows-installer-scripting-examples.md). For sample utilities that do not require Windows Script Host, see [Windows Installer Development Tools](windows-installer-development-tools.md).

 

 



