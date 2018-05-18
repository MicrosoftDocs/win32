---
title: IsReadOnly
description: IsReadOnly
ms.assetid: '731d85ab-b03c-4c30-b0ae-3d2ee399cb48'
---

# IsReadOnly

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **IsReadOnly** entry specifies whether the catalog is query-only.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Boolean        |
| Default: | 0              |
| Range:   | 0, 1           |



 

### Remarks

Setting the value of the **IsReadOnly** entry to one prevents updates to the catalog, but allows queries against the catalog.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




