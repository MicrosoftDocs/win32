---
title: PropertyStoreMappedCache
description: PropertyStoreMappedCache
ms.assetid: '23cff0cf-7117-4bee-acaf-b29ce3a001e9'
---

# PropertyStoreMappedCache

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **PropertyStoreMappedCache** entry is the maximum number of pages from the primary property cache that should be kept in memory at any one time.

### Summary



|          |                             |
|----------|-----------------------------|
| Type:    | **REG\_DWORD**              |
| Units:   | Pages                       |
| Default: | 16                          |
| Range:   | 0 - 4294967295 (0xFFFFFFFF) |



 

### Remarks

The [**SecPropertyStoreMappedCache**](secpropertystoremappedcache.md) entry serves the same function for the secondary property cache.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> <dt>

[SecPropertyStoreMappedCache](secpropertystoremappedcache.md)
</dt> </dl>

 

 




