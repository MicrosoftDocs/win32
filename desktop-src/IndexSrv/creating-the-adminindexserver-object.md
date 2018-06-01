---
Description: Creating the AdminIndexServer Object
ms.assetid: 030f49d6-c11f-41bd-98d7-c5af117b1ce8
title: Creating the AdminIndexServer Object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating the AdminIndexServer Object

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment creates gCiAdmin, a global [**AdminIndexServer**](iadminindexserver.md) object, for use in the sample using the **CreateObject** function. It uses the [**IsRunning**](iadminindexserver-isrunning.md) method of the gCiAdmin **AdminIndexServer** object to set the appropriate states of the command buttons for starting and stopping Indexing Service. The **Connect\_Click** procedure is called when the application starts and whenever the **Connect** button is clicked.


```VB
...
Public gCiAdmin As Object
...
Public Sub Connect_Click()
...
    Set gCiAdmin = Nothing

    ' Create Indexing Service Admin object.
    Set gCiAdmin = CreateObject("Microsoft.ISAdm")

    ' Set MachineName to administer IS, if not local.
    If Text1.Text <> "Local Machine" Then
        gCiAdmin.MachineName = Text1.Text
    End If

    If (gCiAdmin.IsRunning) Then
        StopCisvc.Enabled = True
        StartCisvc.Enabled = False
    Else
        StopCisvc.Enabled = False
        StartCisvc.Enabled = True
    End If
...
End Sub
```



 

 



