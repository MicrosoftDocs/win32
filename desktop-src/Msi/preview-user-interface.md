---
description: The VBScript file WiDialog.vbs is provided in the Windows SDK Components for Windows Installer Developers. This sample shows how script is used to preview dialogs in a Windows Installer database.
ms.assetid: b3d72ba1-1d19-4460-8b9b-94f72214e8b1
title: Preview User Interface
ms.topic: article
ms.date: 05/31/2018
---

# Preview User Interface

The VBScript file WiDialog.vbs is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). This sample shows how script is used to preview dialogs in a Windows Installer database.

This sample demonstrates:

-   [**OpenDatabase method (Installer Object)**](installer-opendatabase.md), the [**CreateRecord method**](installer-createrecord.md), and the [**LastErrorRecord method**](installer-lasterrorrecord.md) of the [**Installer Object**](installer-object.md)
-   [**OpenView method**](database-openview.md) and the [**EnableUIpreview method**](database-enableuipreview.md) of the [**Database Object**](database-object.md)
-   [**Execute method**](view-execute.md) and the [**Fetch method**](view-fetch.md) of the [**View Object**](view-object.md)
-   [**StringData property**](record-stringdata.md) propertyof the [**Record Object**](record-object.md)

This sample requires the CScript.exe or WScript.exe version of Windows Script Host. To use CScript.exe for this sample, type a command at the command prompt using the following syntax. Help is displayed if the first argument is /? or if too few arguments are specified. To redirect the output to a file, end the command line with VBS > \[*path to file*\]. The sample returns a value of 0 for success, 1 if help is invoked, and 2 if the script fails.

**cscript WiDialog.vbs** *\[path to database\]\[Dialog names\]*

Specify the path to a Windows Installer database. Specify the name of a dialog. This name must be listed in the Dialog column of the [Dialog table](dialog-table.md). To view a billboard, append the dialog's name with the control's name from the [Control table](control-table.md) and append this to the name of the billboard in the [Billboard table](billboard-table.md). If no dialogs are specified, all dialogs in Dialog table are displayed sequentially.

For additional scripting examples, see [Windows Installer Scripting Examples](windows-installer-scripting-examples.md). For sample utilities that do not require Windows Script Host, see [Windows Installer Development Tools](windows-installer-development-tools.md).

 

 



