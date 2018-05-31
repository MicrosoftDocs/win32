---
title: MinClientIdleTime
description: MinClientIdleTime
ms.assetid: f301d03d-e6f5-4372-a549-d782164b8894
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MinClientIdleTime

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MinClientIdleTime** entry is the amount of time a query client can remain idle before it is a candidate for being dropped by the query process.

### Summary



|          |                               |
|----------|-------------------------------|
| Type:    | **REG\_DWORD**                |
| Units:   | Seconds                       |
| Default: | 600 (10 minutes)              |
| Range:   | 600 - 4294967295 (0xFFFFFFFF) |



 

### Remarks

When a query client is idle for longer than the value specified by the **MinClientIdleTime** entry, it only becomes a candidate for being dropped. The query process drops a query client only if it runs out of connections to process new queries.

The value of an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog cannot override the value of this entry.

## Related topics

<dl> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




