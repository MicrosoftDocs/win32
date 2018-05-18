---
title: Locating the Catalog for the Selected Scope
description: Locating the Catalog for the Selected Scope
ms.assetid: '28a889af-1a5c-4d0d-85c4-65534b75daea'
---

# Locating the Catalog for the Selected Scope

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment uses the [**LocateCatalogs**](locatecatalogs.md) function of the [OLE DB Helper API](programming-apis.md#-idxs-ole-db-helper-api) to locate the Indexing Service catalog for a specified scope. The first portion of the code segment declares a reference to the **LocateCatalog** function as an external procedure in Query.dll


```VB
...
Private Declare Function LocateCatalogs Lib "Query" Alias "LocateCatalogsA" _
      (ByVal Scope As String, _
       ByVal Bmk As Long, _
       ByVal Machine As String, _
       ByRef ccMachine As Long, _
       ByVal Catalog As String, _
       ByRef ccCatalog As Long) As Long
...
```



The next portion of the code segment uses the [**LocateCatalogs**](locatecatalogs.md) function to determine the machine and catalog given the scope.


```VB
    sc = LocateCatalogs(Scope.Text, 0, Machine, ccMachine, Catalog, ccCatalog)
    Machine = Left(Machine, ccMachine - 1)
    Catalog = Left(Catalog, ccCatalog - 1)

    If 0 = sc Then
        If ccMachine > 2 Then
            CatalogName.Text = "query://" + Machine + "/" + Catalog
        Else
            CatalogName.Text = Catalog
        End If
    Else
        CatalogName.Text = "<default>"
    End If
...
```



The final portion of the code segment declares the RS object variable as an **Object**, because it can be created in either of two ways.


```VB
...
    Dim RS As Object
...
```



 

 




