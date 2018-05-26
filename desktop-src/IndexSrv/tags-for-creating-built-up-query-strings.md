---
title: Tags for Creating Built-up Query Strings
description: Tags for Creating Built-up Query Strings
ms.assetid: 9d476613-05ef-4512-9b3a-5966d65db732
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Tags for Creating Built-up Query Strings

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following tags create built-up query strings for the [**Query**](iixssoquery-query.md) property on an IXSSO **Query** object. In each, *n* is a single digit in the range 0-9. The column, operator, and query for each numeric value make up a query term which is combined with the full-text query string and other query terms using the AND operator.



| Tag      | Description                                                                                 |
|----------|---------------------------------------------------------------------------------------------|
| **c***n* | Column for a built-up query. Used by the [**Query**](iixssoquery-query.md) property.       |
| **o***n* | Operator for a built-up query. Used by the [**Query**](iixssoquery-query.md) property.     |
| **q***n* | Query string for a built-up query. Used by the [**Query**](iixssoquery-query.md) property. |



 

 

 




