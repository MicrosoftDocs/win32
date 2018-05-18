---
title: Maximum Retries
description: Maximum Retries
ms.assetid: 'e345dece-47e9-467a-83a4-dcffc3c41cf0'
---

# Maximum Retries

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

If a document cannot be filtered, it will be retried a certain maximum number of times. If the document then still cannot be filtered, it will be considered an unfiltered file. The registry key **FilterRetries** determines the maximum number of retries for a document.

Unfiltered documents can be found by defining the property

Unfiltered (DBTYPE\_BOOL, 1) = 49691c90-7e17-101a-a91c-08002b2ecda97, and then issuing the query

``` syntax
@unfiltered = true
```

 

 




