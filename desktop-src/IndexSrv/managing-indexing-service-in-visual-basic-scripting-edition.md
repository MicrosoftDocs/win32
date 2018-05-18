---
title: Managing Indexing Service in Visual Basic Scripting Edition
description: Managing Indexing Service in Visual Basic Scripting Edition
ms.assetid: '863a3aef-5b80-45aa-b864-d27d2e9f6439'
---

# Managing Indexing Service in Visual Basic Scripting Edition

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

The QSample.vbs script of the [SQuery Sample](squery-sample.md) executes a query that you specify as part of the script input parameters. This script functions similarly to the [Simple sample](simple-sample.md), which is written in the C++ language. It also performs some managing tasks with Indexing Service.

A major part of the QSample.vbs script is the **Sub** procedure **DoQuery**, which is defined with the following statement.

`sub DoQuery( query, catalog, locale, forceci, forcemerge, shallow, dialect, machine, columns, scope, quiet, sort, stats, uptodate, maxhits )`

A portion of this procedure displays statistics for the catalog, checks if the catalog is up to date, or forces a master merge. The following code segment begins this portion.


```VB
Set a = WScript.CreateObject( "microsoft.ISAdm" )
a.MachineName = machine
Set c = a.GetCatalogByName( catalog )
```



The first statement uses the **CreateObject** method of the **WScript** object to create a, which is an [**AdminIndexServer**](iadminindexserver.md) object, from Ciodm.dll. The second statement sets the [**MachineName**](iadminindexserver-machinename.md) property of the object to the name of the computer specified on the script input. The third statement uses the [**GetCatalogByName**](iadminindexserver-getcatalogbyname.md) method of the **AdminIndexServer** object to create c, which is a [**CatAdm**](icatadm.md) object that represents the catalog.

If the script input specifies to force a master merge, the script uses the [**ForceMasterMerge**](icatadm-forcemastermerge.md) method to start the master merge operation.

`if forcemerge then c.ForceMasterMerge`

When the input to the script specifies to determine whether the catalog is up to date, the script uses the [**IsUpToDate**](icatadm-isuptodate.md) property of the [**CatAdm**](icatadm.md) object to determine and output the status.


```VB
If c.IsUpToDate Then
    out "The catalog is up to date."
Else
    out "The catalog is not up to date."
End If
```



These are just a few examples of using the [Admin Helper API](programming-apis.md#-idxs-admin-helper-api) in scripts to manage Indexing Service.

 

 




