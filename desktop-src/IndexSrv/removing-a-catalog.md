---
Description: Removing a Catalog
ms.assetid: afb6fce5-cb3a-4953-9965-47cb0a364f80
title: Removing a Catalog
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Removing a Catalog

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment uses the [**RemoveCatalog**](iadminindexserver-removecatalog.md) method of the gCiAdmin [**AdminIndexServer**](iadminindexserver.md) object to remove the catalog. The **RemoveCatalogMethod** procedure is called whenever the option to remove the catalog is selected on the form.


```VB
Private Sub RemoveCatalogMethod()

    ISAdminForm.gCiAdmin.RemoveCatalog Tag, True

...
End Sub
```



 

 



