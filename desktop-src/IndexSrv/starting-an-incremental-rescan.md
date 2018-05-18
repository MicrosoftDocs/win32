---
title: Starting an Incremental Rescan
description: Starting an Incremental Rescan
ms.assetid: 'fe43fe60-4981-439b-b283-584c03aae379'
---

# Starting an Incremental Rescan

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

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



 

 




