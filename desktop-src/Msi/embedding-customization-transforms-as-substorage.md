---
description: You may store the customization transform in a storage of the Windows Installer package to guarantee that the transform is always available when the installation package is available.
ms.assetid: d4c022d2-a8c4-4b4e-8a6c-b14e1bc6effe
title: Embedding Customization Transforms as Substorage
ms.topic: article
ms.date: 05/31/2018
---

# Embedding Customization Transforms as Substorage

You may store the customization transform in a storage of the Windows Installer package to guarantee that the transform is always available when the installation package is available. See [Embedded Transforms](embedded-transforms.md). An example of this is provided in the Windows Installer SDK as the utility WiSubStg.vbs. The following snippet, Emb.vbs, also illustrates the use of the [Storages table](-storages-table.md) to add an embedded transform and is for use with Windows Script Host.


```VB
'Emb.vbs. Argument(0) is the original database. Argument(1) is the
'    path to the transform file. Argument(2) is the name of the storage.
'
Option Explicit

' Check arguments
If WScript.Arguments.Count < 2 Then
 WScript.Echo "Usage is emb.vbs [original database] [transform] [storage name]"
 WScript.Quit(1)
End If

' Connect to Windows Installer object
On Error Resume Next
Dim installer : Set installer = Nothing
Set installer = Wscript.CreateObject("WindowsInstaller.Installer")
 
' Evaluate command-line arguments and set open and update modes
Dim databasePath: databasePath = Wscript.Arguments(0)
Dim importPath  : importPath = Wscript.Arguments(1)
Dim storageName : storageName = Wscript.Arguments(2)
 
' Open database and create a view on the _Storages table
Dim sqlQuery : sqlQuery = "SELECT `Name`,`Data` FROM _Storages"
Dim database : Set database = installer.OpenDatabase(databasePath, 1)
Dim view     : Set view = database.OpenView(sqlQuery)
 
'Create and Insert the row.
Dim record   : Set record = installer.CreateRecord(2)
record.StringData(1) = storageName
view.Execute record
 
'Insert storage - copy data into stream
record.SetStream 2, importPath
view.Modify 3, record
database.Commit
Set view = Nothing
Set database = Nothing
```



To add a storage named MNPtrans1 to MNP2000.msi, and containing the transform you created in [Adding Summary Information to Customization Transform](adding-summary-information-to-customization-transform.md), change directories to the folder containing Emb.vbs, the original database, and the transform file, then enter the following command line.

**Cscript.exe Emb.vbs MNP2000.msi MNPtrans.mst MNPtrans1**

This completes the customization transform example. After embedding the transform in MNPtrans.mst, the transform is always available with the installation package. The file MNPtrans.mst does not need to be located at the source to apply the transform.

Remove MNPtrans.mst from the folder containing the sample installation package. Click the MNP2000.msi icon to launch an install or use the following command line.

**msiexec /i MNP2000.msi**

Note that this installs the product without the customizations. To install with the customizations, enter the following command line. Use a colon to indicate that the value of the [**TRANSFORMS**](transforms.md) Property refers to an embedded transform.

msiexec /i MNP2000.msi TRANSFORMS=:MNPtrans1

Note that the Gate feature does not appear in the feature selection tree and that the components of the Gate feature are not installed even if a Complete type of installation is selected in the user interface.

## Next example

[A Small Update Patching Example](a-small-update-patching-example.md)

 

 



