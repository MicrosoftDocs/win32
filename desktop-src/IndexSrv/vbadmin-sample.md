---
title: VBAdmin Sample
description: VBAdmin Sample
ms.assetid: d66c2431-e26a-4c13-80c6-4ea60bce2229
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# VBAdmin Sample

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The VBAdmin sample is an example Windows application written in Visual Basic that illustrates how to administer Indexing Service using the [AdminIndexServer](iadminindexserver.md), [CatAdm](icatadm.md), and [ScopeAdm](iscopeadm.md) automation objects of the [Admin Helper API](programming-apis.md#-idxs-admin-helper-api).

Source: mssdk\\samples\\winbase\\indexing\\VBAdmin\\

**To build and run the sample**

1.  In the Visual Basic development environment, open the VBAdmin.vbp project in the source path of the sample.
2.  In the **File** menu, click **Make VBAdmin.exe**.
3.  In the **Make Project** dialog box, click **OK**.
4.  In the **Run** menu, click **Start**.

**To start or stop Indexing Service using the sample**

1.  Click **Start** to start Indexing Service if it isn't running.
2.  Click **Stop** to stop Indexing Service if it is running.

**To create a new catalog using the sample**

1.  In the tree view of the catalog structure, right-click **Catalogs**.
2.  In the **Create New Catalog** dialog box, enter the name and location of the new catalog.
3.  Click **OK**.

**To delete a catalog using the sample**

1.  In the tree view of the catalog structure, right-click the catalog you want to delete.
2.  In the **Catalog Administration** dialog box, select **Remove Catalog**.
3.  Click **OK**.

## Programming Notes

The VBAdmin sample illustrates how you can use the [AdminIndexServer](iadminindexserver.md), [CatAdm](icatadm.md), and [ScopeAdm](iscopeadm.md) automation objects of the Admin Helper API to administer catalogs and scopes.

 

 




