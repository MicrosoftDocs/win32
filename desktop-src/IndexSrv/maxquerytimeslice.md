---
Description: MaxQueryTimeslice
ms.assetid: 40e49c89-5f3e-4411-a82e-080ee869f7fb
title: MaxQueryTimeslice
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MaxQueryTimeslice

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MaxQueryTimeslice** entry is the maximum amount of query execution time for a single time slice.

### Summary



|          |                          |
|----------|--------------------------|
| Type:    | **REG\_DWORD**           |
| Units:   | Milliseconds of CPU time |
| Default: | 50                       |
| Range:   | 1 - 1000                 |



 

### Remarks

If the number of active asynchronous queries is greater than the number of allowed query threads, a query is put back on the pending queue at the end of the time interval specified by the value of the **MaxQueryTimeslice** entry. The end of a time slice usually occurs only after a matching row is found for the query. For some queries, however, many rows may be examined before a match is found. In these cases, the time slice can be exceeded before the time is checked.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 



