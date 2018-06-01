---
title: Querying with Visual J++
description: Querying with Visual J++
ms.assetid: 8998143b-5d8b-4741-ae51-855e858d7e1e
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Querying with Visual J++

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The [VJQuery Sample](vjquery-sample.md) executes an Indexing Service query using the SQL language and the [ActiveX Data Objects API](https://www.bing.com/search?q=ActiveX Data Objects API). Depending on the parameters specified on the command line when the sample is run, it executes one of three different SQL queries.

-   If the command line doesn't specify a query, it executes the following default query.
    ```sql
    SELECT Filename, Size, Write, Path
      FROM SCOPE('DEEP TRAVERSAL OF "\"')
      WHERE CONTAINS('"Indexing Service"')
    ```

    

-   If the command line doesn't contain the *-s* parameter, but includes query text for a WHERE clause, it executes the following query.
    ```sql
    SELECT Filename, Size, Write, Path
      FROM SCOPE('DEEP TRAVERSAL OF "\"')
      WHERE where-clause-text
    ```

    

-   If the command line contains the *-s* parameter, it executes whatever complete SQL statement the command line contains.

The Query.java module defines the public class **Query**, which encapsulates setting up, executing, and displaying a query. The following topics discuss the methods of the **Query** class that involve Indexing Service in the sample.

-   [Query.Execute in Query.java](query-execute-in-query-java.md)
-   [Query.Display in Query.java](query-display-in-query-java.md)

 

 




