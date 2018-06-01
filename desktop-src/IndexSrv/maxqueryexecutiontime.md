---
Description: MaxQueryExecutionTime
ms.assetid: 8a288982-b563-4217-8287-98521fc5b7df
title: MaxQueryExecutionTime
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MaxQueryExecutionTime

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MaxQueryExecutionTime** entry is the maximum amount of execution time allowed for a query.

### Summary



|          |                             |
|----------|-----------------------------|
| Type:    | **REG\_DWORD**              |
| Units:   | Milliseconds of CPU time    |
| Default: | 10000 (10 seconds)          |
| Range:   | 0 - 4294967295 (0xFFFFFFFF) |



 

### Remarks

If a query takes more CPU time than specified by the value of the **MaxQueryExecutionTime** entry, processing of the query stops and an error status is returned. The value of zero specifies either that there is no limit for Indexing Service processing or that the client specifies the limit.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 



