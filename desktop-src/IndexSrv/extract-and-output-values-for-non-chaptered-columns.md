---
Description: Extract and Output Values for Non-Chaptered Columns
ms.assetid: 5251ad35-bb8d-403c-9c3f-d9085f0d3bd9
title: Extract and Output Values for Non-Chaptered Columns
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Extract and Output Values for Non-Chaptered Columns

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code sub-segment iterates through all the fields of the objRS\_Parent [**Recordset**](https://www.bing.com/search?q=**Recordset**) object and concatenates the values of the columns in the parent recordset, excluding any chaptered columns.


```VB
For intI = 0 to objRS_Parent.Fields.Count - 1 
    If objRS_Parent(intI).Name <> "Chapter" Then 
        strRecord = strRecord & "  " & objRS_Parent(intI).Value
    End If
Next
 
WScript.Echo(strRecord);
```



For the query properties set in this example, the *strRecord* variable is, for example, the following.

``` syntax
1.    c:\inetpub\iissamples\default
```

 

 



