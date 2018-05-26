---
title: Starting and Stopping Indexing Service
description: Starting and Stopping Indexing Service
ms.assetid: a7c7de77-ddff-4268-80c4-55a185e09def
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Starting and Stopping Indexing Service

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

These code segments use the [**Start**](iadminindexserver-start.md) and [**Stop**](iadminindexserver-stop.md) methods of the gCiAdmin [**AdminIndexServer**](iadminindexserver.md) object to start and stop the scanning and indexing components of Indexing Service. The **StartCisvc\_Click** procedure is called when the **Start** command is clicked, and the **StopCisvc\_Click** procedure is called when the **Stop** command is clicked.


```VB
Private Sub StartCisvc_Click()
...
    gCiAdmin.Start  ' Start cisvc.exe service.
    Sleep (30000)   ' Give time for cisvc.exe to run.
    StopCisvc.Enabled = True
    StartCisvc.Enabled = False
...
End Sub
...
Private Sub StopCisvc_Click()
...
    gCiAdmin.Stop   ' Stop cisvc.exe service.

    StopCisvc.Enabled = False
    StartCisvc.Enabled = True
...
End Sub
```



 

 




