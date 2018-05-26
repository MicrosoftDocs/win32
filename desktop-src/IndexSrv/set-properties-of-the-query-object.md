---
title: Set Properties of the Query Object
description: Set Properties of the Query Object
ms.assetid: 539d5e25-afb3-49bf-974b-616843132c21
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Set Properties of the Query Object

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment sets several properties of the objQ [Query](iixssoquery.md) object. The [Columns](iixssoquery-columns.md) property specifies to return the filename, directory, size, and write time columns in the results, and the [GroupBy](iixssoquery-groupby.md) property specifies to group the results in a hierarchical recordset by values of the directory column, in ascending order. This creates a query with a parent recordset consisting of directory names and the chaptered filename, size, and write time columns. The chaptered columns are a child recordset of the parent directory.


```VB
objQ.Columns = "filename, directory, size, write"
objQ.Query   = "#filename *.asp"
objQ.GroupBy = "directory[a]"
objQ.Catalog = "system"
objQ.OptimizeFor      = "recall"
objQ.AllowEnumeration = TRUE
objQ.MaxRecords       = 20000
```



The [Query](iixssoquery-query.md) property specifies the query text "\#filename \*.asp", which is in query language Dialect 1 by default, and which is a [pattern-matching query](pattern-matching-queries.md) that uses a UNIX-style regular expression.

 

 




