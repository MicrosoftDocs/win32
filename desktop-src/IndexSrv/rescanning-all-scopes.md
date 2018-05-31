---
title: Rescanning All Scopes
description: Rescanning All Scopes
ms.assetid: 3fba1f33-004f-41eb-a56b-bdddba888922
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Rescanning All Scopes

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment uses the [**GetCatalogByName**](iadminindexserver-getcatalogbyname.md) method of the gCiAdmin [**AdminIndexServer**](iadminindexserver.md) object to create CiCatalog, a [**CatAdm**](icatadm.md) object. It then uses the [**FindFirstScope**](icatadm-findfirstscope.md) and [**FindNextScope**](icatadm-findnextscope.md) methods of the CiCatalog **CatAdm** object to enumerate all scopes of the catalog. For each found scope, it uses the [**GetScope**](icatadm-getscope.md) method of the CiCatalog **CatAdm** object to create CiScope, a [**ScopeAdm**](iscopeadm.md) object. It then uses the [**Rescan**](iscopeadm-rescan.md) method of the **ScopeAdm** object to rescan the scope. The **ScanAllScopes** procedure is called whenever the option to force a full rescan of all scopes of the catalog is selected on the form.


```VB
Private Sub ScanAllScopes()
...
    Dim CiCatalog As Object
    Dim CiScope   As Object
    Dim fFound    As Boolean

    Set CiCatalog = ISAdminForm.gCiAdmin.GetCatalogByName(Tag)

    fFound = CiCatalog.FindFirstScope
    While (fFound)
        Set CiScope = CiCatalog.GetScope()
        CiScope.Rescan True ' Full rescan.
        Set CiScope = Nothing

        fFound = CiCatalog.FindNextScope
    Wend
...
End Sub
```



 

 




