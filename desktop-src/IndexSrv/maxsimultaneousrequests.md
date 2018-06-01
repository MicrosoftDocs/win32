---
Description: MaxSimultaneousRequests
ms.assetid: 364e20a4-aa35-495e-a1a3-936a541f8117
title: MaxSimultaneousRequests
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MaxSimultaneousRequests

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MaxSimultaneousRequests** entry is the maximum number of simultaneous connections for query requests (using named pipes) that Indexing Service supports.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Named pipes    |
| Default: | 100            |
| Range:   | 1 - 20000      |



 

### Remarks

The value of this entry should be at least as large as the value of the [**IsapiMaxEntriesInQueryCache**](isapimaxentriesinquerycache.md) entry, because cached queries keep a connection open for incoming search requests. No more than 50 simultaneous requests can be established because of connection limits in the system.

The value of an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog cannot override the value of this entry.

## Related topics

<dl> <dt>

[IsapiMaxEntriesInQueryCache](isapimaxentriesinquerycache.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 



