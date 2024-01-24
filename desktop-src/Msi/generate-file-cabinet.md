---
description: The VBScript file WiMakCab.vbs is provided in the Windows SDK Components for Windows Installer Developers. This sample shows how script is used to generate file cabinets from a Windows Installer database.
ms.assetid: 26671cb9-a200-4520-8b52-4cff3f71a2f2
title: Generate File Cabinet
ms.topic: article
ms.date: 05/31/2018
---

# Generate File Cabinet

The VBScript file WiMakCab.vbs is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). This sample shows how script is used to generate file cabinets from a Windows Installer database.

This sample demonstrates:

-   [**OpenDatabase method (Installer Object)**](installer-opendatabase.md) and the [**LastErrorRecord method**](installer-lasterrorrecord.md) of the [**Installer Object**](installer-object.md)
-   [**Commit method**](database-commit.md), the [**OpenView method**](database-openview.md) and [**SummaryInformation property (Database Object)**](database-summaryinformation.md) of the [**Database Object**](database-object.md)
-   [**Fetch method**](view-fetch.md), [**Execute method**](view-execute.md) and [**Modify method**](view-modify.md) of the [**View Object**](view-object.md)
-   [**StringData property**](record-stringdata.md) and [**IntegerData property**](record-integerdata.md) of the [**Record Object**](record-object.md)
-   [**DoAction method**](session-doaction.md), the [**Property property (Session Object)**](session-session.md), and the [**Mode property**](session-mode.md) of the [**Session Object**](session-object.md)

You'll require the CScript.exe or WScript.exe version of Windows Script Host to use this sample. To use CScript.exe to run this sample, type a command at the command prompt using the following syntax. Help is displayed if the first argument is /? or if too few arguments are specified. To redirect the output to a file, end the command line with VBS > \[*path to file*\]. The sample returns a value of 0 for success, 1 if help is invoked, and 2 if the script fails.

**cscript WiMakCab.vbs \[path to database\]\[base name\]\[optional source locations\]**

In order to generate a cabinet, Makecab.exe must be on the PATH. The Makecab.exe utility is included in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). Note that the sample does not update the [Media table](media-table.md) to handle multiple cabinets. To replace an embedded cabinet, include the options: /R /C /U /E.

Specify the path to the installer database. This must be located at the root of the source tree. Specify the case-sensitive base name for the generated cabinet files. If the source type is compressed, all files are opened at the root. The following options may be specified at any point on the command line.



| Option              | Description                                                                                                                               |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| no option specified |                                                                                                                                           |
| /C                  | Run compression. If /C is not specified, WiMakCab.vbs only generates the DDF file.                                                        |
| /L                  | Use LZX compression instead of MSZIP                                                                                                      |
| /F                  | Limit cabinet size to 1.44 MB floppy size rather than CD-ROM                                                                              |
| /U                  | Update the database to reference the generated cabinet                                                                                    |
| /E                  | Embed the cabinet file in the installer package as a stream                                                                               |
| /S                  | Use sequence numbers in the File table ordered by directories                                                                             |
| /R                  | Revert to non-cabinet install, remove cabinet if /E is specified (The /R option removes the compressed bit - SummaryInfo property 15 & 2) |



 

For additional scripting examples, see [Windows Installer Scripting Examples](windows-installer-scripting-examples.md). For sample utilities that do not require Windows Script Host, see [Windows Installer Development Tools](windows-installer-development-tools.md).

 

 



