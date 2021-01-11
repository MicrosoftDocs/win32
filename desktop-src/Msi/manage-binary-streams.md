---
description: The VBScript file WiStream.vbs is provided in the Windows SDK Components for Windows Installer Developers.
ms.assetid: f96d1fdd-81c8-4fb2-a23e-fda49ace8bef
title: Manage Binary Streams
ms.topic: article
ms.date: 05/31/2018
---

# Manage Binary Streams

The VBScript file WiStream.vbs is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). This sample shows how script can be used to manage binary streams in a Windows Installer database. The sample may be used to enter compressed file cabinets into a database. This sample demonstrates the operation of the [\_Streams table](-streams-table.md) in the Windows Installer database.

The sample also demonstrates the use of:

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

**cscript WiStream.vbs \[path to database\]\[path to file\]\[options\]\[stream name\]**

Specify the path to the Windows Installer database that is to receive the stream. Specify a path to the binary file containing the stream data. To list the streams in the installer database, omit this path. You may specify an optional stream name, if this is omitted it defaults to the file name.

The following option may be specified.



| Option              | Description                                                                                     |
|---------------------|-------------------------------------------------------------------------------------------------|
| no option specified | Add a stream to the Windows Installer database.                                                 |
| /d                  | Remove a stream. This option flag must be followed by the name of the substorage being removed. |



 

For additional scripting examples, see [Windows Installer Scripting Examples](windows-installer-scripting-examples.md). For sample utilities that do not require Windows Script Host, see [Windows Installer Development Tools](windows-installer-development-tools.md).

 

 



