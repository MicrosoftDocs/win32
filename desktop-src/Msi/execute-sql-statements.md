---
description: The VBScript file WiRunSQL.vbs is provided in the Windows SDK Components for Windows Installer Developers.
ms.assetid: 1027b187-1237-43d1-9905-8fcdaec63903
title: Execute SQL Statements
ms.topic: article
ms.date: 05/31/2018
---

# Execute SQL Statements

The VBScript file WiRunSQL.vbs is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). This sample shows how script is used to run SQL queries and updates against a Windows Installer database. For more information, see [SQL Syntax](sql-syntax.md) and [Examples of Database Queries Using SQL and Script](examples-of-database-queries-using-sql-and-script.md).

The sample script demonstrates:

-   [**OpenDatabase method (Installer Object)**](installer-opendatabase.md) and the [**LastErrorRecord method**](installer-lasterrorrecord.md) of the [**Installer Object**](installer-object.md)
-   [**OpenView method**](database-openview.md), and the [**Commit method**](database-commit.md) of the [**Database Object**](database-object.md)
-   [**Execute method**](view-execute.md) of the [**View Object**](view-object.md)
-   [**StringData property**](record-stringdata.md) propertyof the [**Record Object**](record-object.md)

Using this sample requires the CScript.exe or WScript.exe version of Windows Script Host. To use CScript.exe to run this sample, type a command at the command prompt using the following syntax. Help is displayed if the first argument is /? or if too few arguments are specified. To redirect the output to a file, end the command line with VBS > \[*path to file*\]. The sample returns a value of 0 for success, 1 if help is invoked, and 2 if the script fails.

**cscript WiRunSQL.vbs \[path to database\]\[SQL queries\]**

Specify the path to a Windows Installer database. Specify the SQL queries that are to be executed. Note that the SQL query must be enclosed in double quotes. SELECT queries display the rows of the result list specified in the query. Binary data columns selected by a query are not displayed.

For additional scripting examples, see [Windows Installer Scripting Examples](windows-installer-scripting-examples.md). For sample utilities that do not require Windows Script Host, see [Windows Installer Development Tools](windows-installer-development-tools.md).

For more information, see [Working with Queries](working-with-queries.md) and [Examples of Database Queries Using SQL and Script](examples-of-database-queries-using-sql-and-script.md). The sample [A Localization Example](a-localization-example.md) demonstrates using SQL for [Localizing Database Columns](localizing-database-columns.md) and [Updating a Summary Information Stream](updating-a-summary-information-stream.md).

 

 



