---
title: MinIdleRequestThreads
description: MinIdleRequestThreads
ms.assetid: 'f1a481ba-1faf-4498-9d20-0499d4812008'
---

# MinIdleRequestThreads

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MinIdleRequestThreads** entry is the minimum number of idle threads that must be kept available to process incoming requests to Indexing Service.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Threads        |
| Default: | 1              |
| Range:   | 0 - 1000       |



 

### Remarks

Request types include queries, query result retrievals, and administrative operations.

The value of an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog cannot override the value of this entry.

## Related topics

<dl> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> <dt>

[MaxActiveRequestThreads](maxactiverequestthreads.md)
</dt> </dl>

 

 




