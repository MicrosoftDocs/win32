---
title: AddCatalog
description: AddCatalog
ms.assetid: e2542cb6-aaa6-4e67-83b1-b2349c57667b
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddCatalog

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The AddCatalog form creates a new catalog. This form appears when the root ("Catalog") of the catalog tree view on the [ISAdminForm](isadminform.md) form is right-clicked. The AddCatalog form contains the following controls.

-   A text box for the name of the catalog.
-   A text box for the location of the catalog.
-   A command button to create the specified catalog.
-   A command button to cancel the operation.

The following code segment for the AddCatalog form creates and adds a catalog to the [ISAdminForm](isadminform.md) form. It uses the [AddCatalog](iadminindexserver-addcatalog.md) method of the [AdminIndexServer](iadminindexserver.md) object to create CiCatalog, a [CatAdm](icatadm.md) object with the catalog name and location specified on the form.


```VB
Private Sub Ok_Click()
...
    Dim CiCatalog As Object

    Set CiCatalog = ISAdminForm.gCiAdmin.AddCatalog(strName, strLocation)
...
End Sub
```



 

 




