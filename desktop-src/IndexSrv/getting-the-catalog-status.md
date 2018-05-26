---
title: Getting the Catalog Status
description: Getting the Catalog Status
ms.assetid: 9101b46a-dd87-4df1-bec6-cf701a782b65
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Getting the Catalog Status

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment uses the [**FindFirstCatalog**](iadminindexserver-findfirstcatalog.md) and [**FindNextCatalog**](iadminindexserver-findnextcatalog.md) methods of the gCiAdmin [**AdminIndexServer**](iadminindexserver.md) object to enumerate all Indexing Service catalogs. For each found catalog, it uses the [**GetCatalog**](iadminindexserver-getcatalog.md) method of the gCiAdmin **AdminIndexServer** object to create CiCatalog, a [**CatAdm**](icatadm.md) object. It then adds the [**CatalogLocation**](icatadm-cataloglocation.md) and other properties of the CiCatalog **CatAdm** object to the list view on the form that describes the status of each found catalog. The **MakeCatalogColumns** procedure is called when the application starts, whenever the **Connect** button is clicked, and at periodic intervals to update the catalog status information.


```VB
Private Sub MakeCatalogColumns()
...
    Dim CiCatalog As Object
    Dim lItem As ListItem
    Dim fFound As Boolean

    ' Loop, getting each catalog status info.
    fFound = gCiAdmin.FindFirstCatalog

    While (fFound)
        Set CiCatalog = gCiAdmin.GetCatalog

        Set lItem = ListView1.ListItems.Add(, , CiCatalog.CatalogLocation)

        If (gCiAdmin.IsRunning) Then
            lItem.SubItems(1) = CiCatalog.IndexSize
            lItem.SubItems(2) = CiCatalog.IsUpToDate
            lItem.SubItems(3) = CiCatalog.PendingScanCount
            lItem.SubItems(4) = CiCatalog.DocumentsToFilter
            lItem.SubItems(5) = CiCatalog.FilteredDocumentCount
            lItem.SubItems(6) = CiCatalog.TotalDocumentCount
            lItem.SubItems(7) = CiCatalog.PctMergeComplete
        End If
...
GetMoreProperties:
        Set CiCatalog = Nothing
        Set lItem = Nothing
        fFound = gCiAdmin.FindNextCatalog
    Wend

...
End Sub
```



 

 




