---
Description: Updating the Catalog Status
ms.assetid: bdef20fc-3502-4336-9d7b-9c40d182e7eb
title: Updating the Catalog Status
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Updating the Catalog Status

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment uses the [**IsRunning**](iadminindexserver-isrunning.md) method of the gCiAdmin [**AdminIndexServer**](iadminindexserver.md) object to decide whether to update the status of the all catalogs in the list view on the form. The **Timer1\_Timer** procedure is called when the timer event occurs, which is at five second intervals.


```VB
Private Sub Timer1_Timer()
    If (gCiAdmin.IsRunning) Then
        Call MakeCatalogColumns
    End If
End Sub
```



 

 



