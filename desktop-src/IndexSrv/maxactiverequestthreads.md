---
title: MaxActiveRequestThreads
description: MaxActiveRequestThreads
ms.assetid: 5a2f1914-e422-4a9a-82a6-f479bb6f717d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MaxActiveRequestThreads

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MaxActiveRequestThreads** entry is the maximum number of active threads to process incoming requests to Indexing Service.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Threads        |
| Default: | 2              |
| Range:   | 1 - 1000       |



 

### Remarks

Request types include queries, query result retrievals, and administrative operations.

The value of an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog cannot override the value of this entry.

## Related topics

<dl> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> <dt>

[MinIdleRequestThreads](minidlerequestthreads.md)
</dt> </dl>

 

 




