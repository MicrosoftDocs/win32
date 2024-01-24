---
description: The VBScript file WiCompon.vbs is provided in the Windows SDK Components for Windows Installer Developers. This sample script can be used to list the components in a Windows Installer database.
ms.assetid: 4e6cc6f4-821a-4a10-a897-5c6aace1f702
title: List Components
ms.topic: article
ms.date: 05/31/2018
---

# List Components

The VBScript file WiCompon.vbs is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). This sample script can be used to list the components in a Windows Installer database.

This sample demonstrates using the various primary key in the [Component table](component-table.md).

The sample also demonstrates:

-   [**OpenDatabase method (Installer Object)**](installer-opendatabase.md), the [**CreateRecord method**](installer-createrecord.md), and the [**LastErrorRecord method**](installer-lasterrorrecord.md) of the [**Installer Object**](installer-object.md).
-   [**OpenView method**](database-openview.md), the [**TablePersistent property**](database-tablepersistent.md), and the [**PrimaryKeys property**](database-primarykeys.md) of the [**Database Object**](database-object.md).
-   [**Execute method**](view-execute.md) and the [**Fetch method**](view-fetch.md) of the [**View Object**](view-object.md).
-   [**StringData property**](record-stringdata.md) property of the [**Record Object**](record-object.md).

Using this sample requires the CScript.exe or WScript.exe version of Windows Script Host. To use CScript.exe to run this sample, type a command at the command prompt using the following syntax. Help is displayed if the first argument is /? or if too few arguments are specified. To redirect the output to a file, end the command line with VBS > \[*path to file*\]. The sample returns a value of 0 for success, 1 if help is invoked, and 2 if the script fails.

**cscript WiCompon.vbs \[path to database\]\[component name\]**

Specify path to the Windows Installer database. Specify the name of the component. The name must be listed in the Component column of the [Component table](component-table.md). If the name of the component is omitted all the components are listed. If an asterisk (\*) is used as the component name, WiCompon.vbs lists the composition of all components. Note that large databases are better displayed using CScript rather than WScript.

For additional scripting examples, see [Windows Installer Scripting Examples](windows-installer-scripting-examples.md). For sample utilities that do not require Windows Script Host, see [Windows Installer Development Tools](windows-installer-development-tools.md).

 

 



