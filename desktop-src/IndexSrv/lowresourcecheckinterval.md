---
title: LowResourceCheckInterval
description: LowResourceCheckInterval
ms.assetid: '8af2e26c-95e7-494b-a2ab-a223b57f4d3e'
---

# LowResourceCheckInterval

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **LowResourceCheckInterval** entry is the minimum time interval available for creating wordlists during the indexing process before Indexing Service checks system resources.

### Summary



|          |                             |
|----------|-----------------------------|
| Type:    | **REG\_DWORD**              |
| Units:   | Seconds                     |
| Default: | 60                          |
| Range:   | 5 - 4294967295 (0xFFFFFFFF) |



 

### Remarks

After an interval specified by the value of the **LowResourceCheckInterval** entry passes, the indexing process checks system resource limitations such as low memory or heavy I/O initiated by the end user.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[LowResourceSleep](lowresourcesleep.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




