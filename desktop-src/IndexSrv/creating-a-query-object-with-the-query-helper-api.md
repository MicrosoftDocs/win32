---
Description: Creating a Query Object with the Query Helper API
ms.assetid: 9bfc91d9-ed65-4f79-8275-017150307e36
title: Creating a Query Object with the Query Helper API
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Query Object with the Query Helper API

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment executes when the specified query language is either Dialect 1 or 2 of the [Indexing Service query language](indexing-service-query-language.md). The first portion of the code segment uses the **CreateObject** function to create Q, a [Query](iixssoquery.md) object, and to create Util, a [Utility](iixssoutil.md) object, from the [Query Helper API](https://www.bing.com/search?q=Query Helper API).


```VB
...
    If InStr(Dialect.Text, "Dialect") <> 0 Then

        ' Create the query and execute.
        Dim Q As Object
        Set Q = CreateObject("ixsso.Query")

        Dim Util As Object
        Set Util = CreateObject("ixsso.Util")
...
```



The next portion of the code segment sets several properties of the Q **Query** object, adds the scope to the query using the [AddScopeToQuery](iixssoutil-addscopetoquery.md) method of the **Utility** object, and sets the selected Dialect for the query.


```VB
...
        Q.Query = QueryText.Text
        Q.Columns = "Filename, Path, Size, Write"
        If Sort.ListIndex = 2 Then
            Q.SortBy = "Rank[d]"
        Else
            Q.SortBy = Sort.Text
        End If
        Util.AddScopeToQuery Q, Scope.Text, "DEEP"

        If 0 = sc Then
            Q.Catalog = CatalogName.Text
        End If

        If StrComp(Dialect.Text, "Dialect 2") = 0 Then
            Q.Dialect = 2   ' Dialect 2.
        Else
            Q.Dialect = 1   ' Dialect 1.
        End If
...
```



 

 



