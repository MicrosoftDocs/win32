---
title: Creating a Recordset Object with the Query Helper API
description: Creating a Recordset Object with the Query Helper API
ms.assetid: b280c705-8b2b-4e08-b875-57e66bb453a2
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Recordset Object with the Query Helper API

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment executes when the specified query language is either Dialect 1 or 2 of the [Indexing Service query language](indexing-service-query-language.md). It uses the [**CreateRecordset**](iixssoquery-createrecordset.md) method of the [**Query**](iixssoquery.md) object, which creates RS — a [**Recordset**](https://www.bing.com/search?q=**Recordset**) object to represent the results of the query — and executes the query.


```VB
Set RS = Q.CreateRecordset("sequential")
```



 

 




