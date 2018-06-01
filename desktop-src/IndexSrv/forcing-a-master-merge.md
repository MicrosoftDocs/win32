---
Description: Forcing a Master Merge
ms.assetid: da0c1b86-6ac6-42fa-a376-ca11e61c79e4
title: Forcing a Master Merge
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Forcing a Master Merge

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment uses the [**GetCatalogByName**](iadminindexserver-getcatalogbyname.md) method of the gCiAdmin [**AdminIndexServer**](iadminindexserver.md) object to create CiCatalog, a global [**CatAdm**](icatadm.md) object. It then uses the [**ForceMasterMerge**](icatadm-forcemastermerge.md) method of the CiCatalog **CatAdm** object to force a master merge of the catalog. The **ForceMasterMergeMethod** procedure is called whenever the option to force a master merge of the catalog is selected on the form.


```VB
Private Sub ForceMasterMergeMethod()
...
    Dim CiCatalog As Object

    Set CiCatalog = ISAdminForm.gCiAdmin.GetCatalogByName(Tag)

    CiCatalog.ForceMasterMerge
...
End Sub
```



 

 



