---
Description: Starting an Incremental Rescan
ms.assetid: fe43fe60-4981-439b-b283-584c03aae379
title: Starting an Incremental Rescan
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Starting an Incremental Rescan

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment uses the [**GetCatalogByName**](iadminindexserver-getcatalogbyname.md) method of the gCiAdmin [**AdminIndexServer**](iadminindexserver.md) object to create CiCatalog, a [**CatAdm**](icatadm.md) object. It then uses the [**GetScopeByPath**](icatadm-getscopebypath.md) method of the CiCatalog **CatAdm** object to create CiScope, a [**ScopeAdm**](iscopeadm.md) object for the selected scope. It then uses the [**Rescan**](iscopeadm-rescan.md) method of the CiScope **ScopeAdm**object with **False** specified to perform an incremental rescan the selected scope. The **StartIncRescan** procedure is called whenever the option to perform an incremental rescan of the scope is selected on the form.


```VB
Private Sub StartIncRescan()
...
    Dim CiCatalog As Object
    Dim CiScope As Object

    Set CiCatalog = ISAdminForm.gCiAdmin.GetCatalogByName(CatName)
    Set CiScope = CiCatalog.GetScopeByPath(ScopeName)

    CiScope.Rescan False
...
End Sub
```



 

 



