---
description: To apply the customization transform during an installation of the product, you must add a Summary Information Stream to the transform file MNPtrans.mst generated in Generating a Customization Transform.
ms.assetid: 586f6c43-7449-4d06-9201-9b4b4919871e
title: Adding Summary Information to Customization Transform
ms.topic: article
ms.date: 05/31/2018
---

# Adding Summary Information to Customization Transform

To apply the customization transform during an installation of the product, you must add a [Summary Information Stream](summary-information-stream.md) to the transform file MNPtrans.mst generated in [Generating a Customization Transform](generating-a-customization-transform.md).

You may generate summary information for a transform using [**MsiCreateTransformSummaryInfo**](/windows/desktop/api/Msiquery/nf-msiquery-msicreatetransformsummaryinfoa) or the [**CreateTransformSummaryInfo Method**](database-createtransformsummaryinfo.md). The following snippet, Sum.vbs, illustrates the [**CreateTransformSummaryInfo Method**](database-createtransformsummaryinfo.md) and is for use with Windows Script Host. Note that this example performs no validation and suppresses no error conditions.


```VB
'Sum.vbs. Argument(0) is the original database. Argument(1) is the
'    customized database. Argument(2) is the transform file.
 
Option Explicit

' Check arguments
If WScript.Arguments.Count < 2 Then
    WScript.Echo "Usage is sum.vbs [original database] [customized database] [transform]"
    WScript.Quit(1)
End If

' Connect to Windows Installer object
On Error Resume Next
Dim installer : Set installer = Nothing
Set installer = Wscript.CreateObject("WindowsInstaller.Installer") 
 
' Open databases and transform 
Dim database1 : Set database1 =
    installer.OpenDatabase(Wscript.Arguments(0), 0) 
Dim database2 : Set database2 =
    installer.OpenDatabase(Wscript.Arguments(1), 0) 
Dim transform : transform = Wscript.Arguments(2)
 
' Create and add Summary Information
Dim transinfo : transinfo =
    Database2.CreateTransformSummaryInfo(Database1, transform,0,0)
```



To create and add summary information to the transform file MNPtrans.mst you created in [Generating a Customization Transform](generating-a-customization-transform.md), change directories to the folder containing Gen.vbs, the original database, the updated database, and the transform, and enter the following command line.

**Cscript.exe Sum.vbs MNP2000.msi MNP2000t.msi MNPtrans.mst**

Click the MNP2000.msi icon to launch an install or use the following command line.

**msiexec /i MNP2000.msi**

This installs the product without the customizations. To install with the customization, enter the following command line. Note that the value of the [**TRANSFORMS**](transforms.md) Property refers to transform file located at the source.

**msiexec /i MNP2000.msi TRANSFORMS=MNPtrans.mst**

The Gate feature does not appear in the feature selection tree and the components of the Gate feature are not installed even if a Complete type of installation is selected in the user interface.

[Continue](embedding-customization-transforms-as-substorage.md)

 

 



