---
Description: Populating the Catalog Tree View
ms.assetid: 0acd38e7-f02f-406f-98b6-93045725b457
title: Populating the Catalog Tree View
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Populating the Catalog Tree View

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment uses the [**FindFirstCatalog**](iadminindexserver-findfirstcatalog.md) and [**FindNextCatalog**](iadminindexserver-findnextcatalog.md) methods of the gCiAdmin [**AdminIndexServer**](iadminindexserver.md) object to enumerate all Indexing Service catalogs. For each found catalog, it uses the [**GetCatalog**](iadminindexserver-getcatalog.md) method of the gCiAdmin **AdminIndexServer** object to create CiCatalog, a [**CatAdm**](icatadm.md) object. It then uses the [**CatalogName**](icatadm-catalogname.md) and [**CatalogLocation**](icatadm-cataloglocation.md) properties of the CiCatalog **CatAdm** object to add the name and location of each found catalog to the tree view and list view on the form. The **PopulateCatalogTreeView** procedure is called when the application starts and whenever the **Connect** button is clicked.


```VB
Private Sub PopulateCatalogTreeView()
...
    Dim fFound As Boolean

    ' Loop through Indexing Service catalogs populating the tree control.
    fFound = gCiAdmin.FindFirstCatalog

    Dim CiCatalog As Object
    Dim lItem     As ListItem
    mTVNodeCount = 1

    While (fFound)

        mTVNodeCount = mTVNodeCount + 1

        Set CiCatalog = gCiAdmin.GetCatalog()

        Set nodX = TreeView1.Nodes.Add(mtcIndex, tvwChild, , CiCatalog.CatalogName)

        nodX.Tag = CiCatalog.CatalogLocation

        Set lItem = ListView1.ListItems.Add(, , CiCatalog.CatalogLocation)

        Set CiCatalog = Nothing

        fFound = gCiAdmin.FindNextCatalog

    Wend
...
End Sub
```



 

 



