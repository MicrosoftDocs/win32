---
title: Using the Results from the Recordset Object
description: Using the Results from the Recordset Object
ms.assetid: b17ee306-5f5f-4659-963c-d1bbd2d3120f
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using the Results from the Recordset Object

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The resulting RS [**Recordset**](https://www.bing.com/search?q=**Recordset**) object for the query, whether created with the [Query Helper API](https://www.bing.com/search?q=Query Helper API) or directly with the [ActiveX Data Objects (ADO) API](https://www.bing.com/search?q=ActiveX Data Objects (ADO) API), provides the information in the list view of the results on the **Main** form. This code segment uses the [**MoveNext**](https://www.bing.com/search?q=**MoveNext**) method of the RS **Recordset** object to read through the results and provide the selected properties to the list view control.


```VB
...
    Do Until RS.EOF
        Set mItem = ListView1.ListItems.Add()
        mItem.Text = RS("Filename")
        mItem.SubItems(1) = RS("Path")
        mItem.SubItems(2) = RS("Size")
        mItem.SubItems(3) = RS("Write")

        RS.MoveNext
    Loop
...
```



 

 




