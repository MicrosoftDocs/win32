---
title: Starting a Full Rescan
description: Starting a Full Rescan
ms.assetid: 51f4547e-d7ab-49f2-81d7-943224576864
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Starting a Full Rescan

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment uses the [**GetCatalogByName**](iadminindexserver-getcatalogbyname.md) method of the gCiAdmin [**AdminIndexServer**](iadminindexserver.md) object to create CiCatalog, a [**CatAdm**](icatadm.md) object. It then uses the [**GetScopeByPath**](icatadm-getscopebypath.md) method of the CiCatalog **CatAdm** object to create CiScope, a [**ScopeAdm**](iscopeadm.md) object for the selected scope. It then uses the [**Rescan**](iscopeadm-rescan.md) method of the CiScope **ScopeAdm** object with **True** specified to perform a full rescan the selected scope. The **StartFullRescan** procedure is called whenever the option to force a full rescan of the scope is selected on the form.


```VB
Private Sub StartFullRescan()
...
    Dim CiCatalog As Object
    Dim CiScope As Object

    Set CiCatalog = ISAdminForm.gCiAdmin.GetCatalogByName(CatName)
    Set CiScope = CiCatalog.GetScopeByPath(ScopeName)

    CiScope.Rescan True
...
End Sub
```



 

 




