---
description: You may generate a transform file by using MsiDatabaseGenerateTransform or the GenerateTransform method of the Database object.
ms.assetid: c016fcba-0d54-4b99-bcdd-36967b2c9da0
title: Generating a Customization Transform
ms.topic: article
ms.date: 05/31/2018
---

# Generating a Customization Transform

You may generate a transform file by using [**MsiDatabaseGenerateTransform**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabasegeneratetransforma) or the [**GenerateTransform method**](database-generatetransform.md) of the [**Database object**](database-object.md). An example of this is provided in the Windows Installer SDK as the utility WiGenXfm.vbs. The following snippet, Gen.vbs, also illustrates the **GenerateTransform** method and is for use with Windows Script Host.


```VB
'Gen.vbs. Argument(0) is the original database. Argument(1) is the
'    customized database. Argument(2) is the transform file.
 
Option Explicit

' Check arguments
If WScript.Arguments.Count < 2 Then
    WScript.Echo "Usage is gen.vbs [original database] [customized database] [transform file]"
    WScript.Quit(1)
End If

' Connect to Windows Installer object
On Error Resume Next
Dim installer : Set installer = Nothing
Set installer = Wscript.CreateObject("WindowsInstaller.Installer") 
' Open databases
Dim database1 : Set database1 = 
    installer.OpenDatabase(Wscript.Arguments(0), 0) 
Dim database2 : Set database2 = 
    installer.OpenDatabase(Wscript.Arguments(1), 0) 
' Generate transform
Dim transform : transform = Database2.GenerateTransform(Database1,
    Wscript.Arguments(2))
```



To generate the transform file MNPtrans.mst from the original MNP2000.msi database and the MNP2000t.msi database you modified in [Customizing an Original Database](customizing-an-original-database.md), change directories to the folder containing Gen.vbs, the original database, and the updated installer database and enter the following command line.

**Cscript.exe Gen.vbs MNP2000.msi MNP2000t.msi MNPtrans.mst**

[Continue](adding-summary-information-to-customization-transform.md)

 

 



