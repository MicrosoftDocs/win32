---
description: The VBScript file WiLstScr.vbs is provided in the Windows SDK Components for Windows Installer Developers. This sample script demonstrates the Windows Installer script viewer.
ms.assetid: 18989c16-e0c8-4d11-b915-730951b6845b
title: View Installer Script
ms.topic: article
ms.date: 05/31/2018
---

# View Installer Script

The VBScript file WiLstScr.vbs is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). This sample script demonstrates the Windows Installer script viewer.

The sample demonstrates the use of:

-   [**OpenDatabase method (Installer Object)**](installer-opendatabase.md)
-   [**LastErrorRecord**](installer-lasterrorrecord.md) method of the [**Installer**](installer-object.md) object
-   [**OpenView**](database-openview.md) method of the [**Database**](database-object.md) object
-   [**Fetch**](view-fetch.md) method of the [**View**](view-object.md) object
-   [**FormatText**](record-formattext.md) method
-   [**FieldCount**](record-fieldcount.md) property
-   [**StringData**](record-stringdata.md) property of the [**Record**](record-object.md) object
-   [\_TransformView table](-transformview-table.md)

Using this sample requires the CScript.exe version of Windows Script Host. To use CScript.exe to run this sample, type a command at the command prompt using the following syntax. Help is displayed if the first argument is /? or if too few arguments are specified. To redirect the output to a file, end the command line with VBS > \[*path to file*\]. The sample returns a value of 0 for success, 1 if help is invoked, and 2 if the script fails.

**cscript WiLstScr.vbs** *\[path to Windows Installer execution script\]*

Specify the path to the installer execution script.

For additional scripting examples, see [Windows Installer Scripting Examples](windows-installer-scripting-examples.md). For sample utilities that do not require Windows Script Host, see [Windows Installer Development Tools](windows-installer-development-tools.md).

 

 



