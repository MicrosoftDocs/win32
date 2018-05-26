---
title: Getting the Scopes
description: Getting the Scopes
ms.assetid: 78105827-f541-416b-bcaa-a1749eb39c83
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Getting the Scopes

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment uses the [**GetCatalogByName**](iadminindexserver-getcatalogbyname.md) method of the gCiAdmin [**AdminIndexServer**](iadminindexserver.md) object to create CiCatalog, a [**CatAdm**](icatadm.md) object. It then uses the [**FindFirstScope**](icatadm-findfirstscope.md) and [**FindNextScope**](icatadm-findnextscope.md) methods of the CiCatalog **CatAdm** object to enumerate all scopes of the catalog. For each found scope, it uses the [**GetScope**](icatadm-getscope.md) method of the CiCatalog **CatAdm** object to create CiScope, a [**ScopeAdm**](iscopeadm.md) object. It then adds the [**Path**](iscopeadm-path.md) and other properties of the CiScope **ScopeAdm** object to the list view on the form that describes the scopes of a selected catalog. The **MakeScopesColumns** procedure is called whenever a catalog is selected in the tree view of the form.


```VB
Private Sub MakeScopesColumns(ByVal CatalogName As String)

...
    Dim CiCatalog As Object
    Dim CiScope As Object
    Dim fFound As Boolean
    Dim lItem As ListItem

    ' Get Indexing Service catalog object, then enumerate its scopes.
    Set CiCatalog = gCiAdmin.GetCatalogByName(CatalogName)

    fFound = CiCatalog.FindFirstScope
    While (fFound)
        Set CiScope = CiCatalog.GetScope()

        Set lItem = ListView1.ListItems.Add(, , CiScope.Path)

        lItem.SubItems(1) = CiScope.Alias
        lItem.SubItems(3) = CiScope.VirtualScope
        lItem.Tag = CiCatalog.CatalogName

        If CiScope.ExcludeScope Then
            lItem.SubItems(2) = False
        Else
            lItem.SubItems(2) = True
        End If

        fFound = CiCatalog.FindNextScope

        Set CiScope = Nothing
        Set lItem = Nothing
    Wend
...
End Sub
```



 

 




