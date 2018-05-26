---
title: Removing a Scope
description: Removing a Scope
ms.assetid: 43c9f941-743b-46db-abf6-a3f6c84f0b4f
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Removing a Scope

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment uses the [**GetCatalogByName**](iadminindexserver-getcatalogbyname.md) method of the gCiAdmin [**AdminIndexServer**](iadminindexserver.md) object to create CiCatalog, a [**CatAdm**](icatadm.md) object. It then uses the [**RemoveScope**](icatadm-removescope.md) method of the CiCatalog **CatAdm** object to remove the selected scope from the catalog. The **RemoveScopeMethod** procedure is called whenever the option to remove the scope is selected on the form.


```VB
Private Sub RemoveScopeMethod()
...
    Dim CiCatalog As Object

    Set CiCatalog = ISAdminForm.gCiAdmin.GetCatalogByName(CatName)

    CiCatalog.RemoveScope (ScopeName)
...
End Sub
```



 

 




