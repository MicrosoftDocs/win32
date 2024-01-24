---
description: The VBScript file WiFilVer.vbs is provided in the Windows SDK Components for Windows Installer Developers. The sample shows you how you can use a script to report or update the file version, size, and language information.
ms.assetid: 21550eea-c30b-4738-9201-ab500356fabf
title: Manage File Sizes and Versions
ms.topic: article
ms.date: 05/31/2018
---

# Manage File Sizes and Versions

The VBScript file WiFilVer.vbs is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). The sample shows you how you can use a script to report or update the file version, size, and language information.

The sample also shows you Windows Installer actions, how to access a Windows Installer database, and the use of the following:

-   [**Installer.OpenDatabase**](installer-opendatabase.md) method of the [**Installer Object**](installer-object.md)
-   [**Installer.FileAttributes**](installer-fileattributes.md) property
-   [**Installer.FileHash**](installer-filehash.md) method
-   [**Installer.FileVersion**](installer-fileversion.md) method
-   [**Installer.LastErrorRecord**](installer-lasterrorrecord.md) method of the [**Installer Object**](installer-object.md)
-   [**Database.OpenView**](database-openview.md) method
-   [**Database.SummaryInformation**](database-summaryinformation.md) property of the [**Database Object**](database-object.md)
-   [**Session.DoAction**](session-doaction.md) method
-   [**Session.Property**](session-session.md)
-   [**Session.SourcePath**](session-sourcepath.md) property
-   [**Session.Mode**](session-mode.md) property of the [**Session Object**](session-object.md)
-   [**Record.StringData**](record-stringdata.md) property
-   [**Record.IntegerData**](record-integerdata.md) property of the [**Record Object**](record-object.md)

Using this sample requires the CScript.exe or WScript.exe version of Windows Script Host. To use CScript.exe to run this sample, type a command at the command prompt by using the following syntax:

**cscript WiFilVer.vbs \[path to database\]\[optional source locations\]**

Also be aware of the following:

-   Help is displayed if the first argument is /? or if too few arguments are specified.
-   To redirect the output to a file, end the command line with VBS > \[*path to file*\].
-   The sample returns a value of 0 (zero) for success, 1 (one) if help is invoked, and 2 (two) if the script fails.

Specify the Windows Installer database that you want to be updated, which must be located at the source file root. However, you can specify sources for the database at separate locations. If the source is compressed, all the files are opened at the root.

The following options can be specified at any location on the command line.



| Option                | Description                                                                              |
|-----------------------|------------------------------------------------------------------------------------------|
| *no option specified* | Display the file information of the database.                                            |
| /u                    | Update the file size, version, and language information in the database from the source. |



 

For more information, see [Windows Installer Scripting Examples](windows-installer-scripting-examples.md) and [Windows Installer Development Tools](windows-installer-development-tools.md).

 

 



