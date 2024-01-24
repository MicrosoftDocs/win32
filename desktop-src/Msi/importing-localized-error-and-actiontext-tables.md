---
description: Localized language versions of the Error table and ActionText table are provided by the Windows Installer SDK. The French language versions of these tables, Error.FRA and ActionTe.FRA, are located in the Intl folder of the Windows Installer SDK.
ms.assetid: 8de687c8-c7da-497e-8a90-2404096ad100
title: Importing Localized Error and ActionText Tables
ms.topic: article
ms.date: 05/31/2018
---

# Importing Localized Error and ActionText Tables

Localized language versions of the [Error table](error-table.md) and [ActionText table](actiontext-table.md) are provided by the Windows Installer SDK. The French language versions of these tables, Error.FRA and ActionTe.FRA, are located in the Intl folder of the Windows Installer SDK.

You may use the table editor Orca or the utility Msidb.exe provided with the SDK to import the French versions of these tables into the database.

An example of using [**MsiDatabaseImport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseimporta) and the [**Import Method**](database-import.md) of the [**Database object**](database-object.md) is provided in the Windows Installer SDK as the utility WiImport.vbs. The following snippet, Imp.vbs, also illustrates the use of the Import method and is for use with Windows Script Host.


```VB
'Imp.vbs. Argument(0) is the original database. Argument(1) is the
'    path of the folder containing the file to be imported. Argument(2) is the name of the file to be imported.
'
Option Explicit

' Check arguments
If WScript.Arguments.Count < 2 Then
    WScript.Echo "Usage is imp.vbs [original database] [folder path] [import file]"
    WScript.Quit(1)
End If

' Connect to Windows Installer object
On Error Resume Next
Dim installer : Set installer = Wscript.CreateObject("WindowsInstaller.Installer")
Dim databasePath : databasePath = Wscript.Arguments(0)
Dim folder : folder = Wscript.Arguments(1)
 
' Open database and process file
Dim database : Set database = installer.OpenDatabase(databasePath, 1)
Dim table : table = Wscript.Arguments(2)
database.Import folder, table 
 
' Commit database changes
database.Commit 'commit changes
Wscript.Quit 0
```



To import and replace the Error table with Error.FRA you may use a command line such as the following.

**Cscript Imp.vbs MNPFren.msi C:\\Note\_Installer\\French Error.FRA**

To import and replace the ActionText table with ActionTe.FRA you may use a command line such as the following.

**Cscript Imp.vbs MNPFren.msi C:\\Note\_Installer\\French ActionTe.FRA**

Rerun validation on MNPFren.msi as described in [Validating an Installation Upgrade](validating-an-installation-upgrade.md).

[Continue](localizing-database-columns.md)

 

 



