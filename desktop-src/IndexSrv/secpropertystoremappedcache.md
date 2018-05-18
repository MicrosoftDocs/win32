---
title: SecPropertyStoreMappedCache
description: SecPropertyStoreMappedCache
ms.assetid: 'bea0c1e3-d1ec-467e-90a7-46f5732b4630'
---

# SecPropertyStoreMappedCache

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **SecPropertyStoreMappedCache** entry is the maximum number of pages from the secondary property cache that are to be kept in memory at any one time.

### Summary



|          |                             |
|----------|-----------------------------|
| Type:    | **REG\_DWORD**              |
| Units:   | Pages                       |
| Default: | 16                          |
| Range:   | 0 - 4294967295 (0xFFFFFFFF) |



 

### Remarks

The [**PropertyStoreMappedCache**](propertystoremappedcache.md) entry serves the same function for the primary property cache.

For more details, see [**PropertyStoreBackupSize**](propertystorebackupsize.md).

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> <dt>

[**PropertyStoreBackupSize**](propertystorebackupsize.md)
</dt> <dt>

[**PropertyStoreMappedCache**](propertystoremappedcache.md)
</dt> </dl>

 

 




