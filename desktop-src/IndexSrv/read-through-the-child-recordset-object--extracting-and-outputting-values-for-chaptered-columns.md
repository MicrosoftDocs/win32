---
title: Read through the Child Recordset Object, Extracting and Outputting Values for Chaptered Columns
description: Read through the Child Recordset Object, Extracting and Outputting Values for Chaptered Columns
ms.assetid: 2d0f629f-2f5b-4322-bafb-066cc05a7226
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Read through the Child Recordset Object, Extracting and Outputting Values for Chaptered Columns

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code sub-segment steps through the child objRS\_Child [**Recordset**](https://www.bing.com/search?q=**Recordset**) object until an end of file occurs, and, for each child recordset (of filename, size, and write for this example), outputs the values in the child recordsets.


```VB
intRS_Child_Count = 0;
Do While Not objRS_Child.EOF 
    intRS_Child_Count = intRS_Child_Count + 1
    strRecord = Left(CStr(intRS_Parent_Count) & "." + CStr(intRS_Child_Count) & ".      ", 8)
 
    For intJ = 0 to objRS_Child.Fields.Count - 1
        If objRS_Child(intJ).Name <> "Chapter" Then
            If objRS_Child(intJ).Name <> strGroupBy Then
                strRecord = strRecord & "  " & objRS_Child(intJ).Value
        End If
    Next
 
    WScript.Echo strRecord
    objRS_Child.MoveNext
Loop
```



For the query properties set in this code example, the *strRecord* variable is, for example, the following.

``` syntax
1.1.      learn.asp  4859  Thu Sep 17 01:48:10 PDT 1998
1.2.      exair.asp  4641  Tue Jun 16 06:22:58 PDT 1998
...
```

 

 




