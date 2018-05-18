---
title: MaxCachedPipes
description: MaxCachedPipes
ms.assetid: '12c41130-f02d-49d7-b522-eb6fe3f615b1'
---

# MaxCachedPipes

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MaxCachedPipes** entry is the maximum number of unconnected instances of named pipes that Indexing Service needs to keep cached.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Named pipes    |
| Default: | 3              |
| Range:   | 0 - 1000       |



 

### Remarks

Because instances of named pipes take up system resources, only the amount needed should be cached for a short period of time.

The value of an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog cannot override the value of this entry.

## Related topics

<dl> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




