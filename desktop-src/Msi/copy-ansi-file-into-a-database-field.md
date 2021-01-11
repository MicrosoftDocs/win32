---
description: The VBScript code sample file WiTextIn.vbs is provided in the Windows SDK Components for Windows Installer Developers.
ms.assetid: ba6c6367-ebb1-4981-ae3a-bcff68aacdbf
title: Copy ANSI File Into a Database Field
ms.topic: article
ms.date: 05/31/2018
---

# Copy ANSI File Into a Database Field

The VBScript code sample file WiTextIn.vbs is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). The sample shows how a script can be used to copy a file into a text field of a Windows Installer database, and demonstrates the processing of primary key data.

The code sample also shows you the following:

-   [**OpenDatabase method (Installer Object)**](installer-opendatabase.md) and the [**LastErrorRecord method**](installer-lasterrorrecord.md) of the [**Installer Object**](installer-object.md)
-   [**OpenView method**](database-openview.md), the [**Commit method**](database-commit.md), and the [**PrimaryKeys property**](database-primarykeys.md) of the [**Database Object**](database-object.md)
-   [**Fetch method**](view-fetch.md) and the [**Modify method**](view-modify.md) of the [**View Object**](view-object.md)
-   [**StringData property**](record-stringdata.md) and [**ReadStream method**](record-readstream.md) of the [**Record Object**](record-object.md)

To use the code sample you need the CScript.exe or WScript.exe version of Windows Script Host.

**To use CScript.exe to run this sample**

-   At the command prompt, type the following syntax:

    **cscript WiTextIn.vbs \[path to database\]\[table name\]\[primary key values\]\[column name\]\[path to file\]**

> [!Note]  
> Help is displayed if the first argument is /? or if too few arguments are specified.

 

**To redirect the output to a file**

-   End the command line with the following: **VBS > \[path to file\]. T**

> [!Note]  
> The sample returns a value of 0 (zero) for success, 1 (one) if Help is invoked, and 2 (two) if the script fails.

 

The following list identifies the items that you must specify:

-   Specify the path to the Windows Installer database.
-   Specify the name of the database table.
-   Specify all the primary key values for the row, in order, and concatenated with colons.
-   Specify a column name that is not a key column. This is the column that you want to receive the data.
-   Specify the path to the text file that is being copied.

> [!Note]  
> If the last argument is omitted, the current value in the field is displayed.

 

For more scripting examples, see [Windows Installer Scripting Examples](windows-installer-scripting-examples.md). For sample utilities that do not require the Windows Script Host, see [Windows Installer Development Tools](windows-installer-development-tools.md).

 

 



