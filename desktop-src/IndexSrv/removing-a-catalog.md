---
title: Removing a Catalog
description: Removing a Catalog
ms.assetid: afb6fce5-cb3a-4953-9965-47cb0a364f80
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Removing a Catalog

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment uses the [**RemoveCatalog**](iadminindexserver-removecatalog.md) method of the gCiAdmin [**AdminIndexServer**](iadminindexserver.md) object to remove the catalog. The **RemoveCatalogMethod** procedure is called whenever the option to remove the catalog is selected on the form.


```VB
Private Sub RemoveCatalogMethod()

    ISAdminForm.gCiAdmin.RemoveCatalog Tag, True

...
End Sub
```



 

 




