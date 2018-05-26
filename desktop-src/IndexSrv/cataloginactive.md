---
title: CatalogInactive
description: CatalogInactive
ms.assetid: ebfb871e-8a67-4ee3-bce9-9a36ad487b5b
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CatalogInactive

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The CatalogInactive entry controls whether a catalog is active in Indexing Service.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Boolean        |
| Default: | 0              |
| Range:   | 0, 1           |



 

### Remarks

The value of the CatalogInactive entry deactivates specific catalogs. Setting the value to one specifies that the catalog is not opened when Indexing Service is started. Setting the value to zero specifies that the catalog is opened when Indexing Service is started.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> </dl>

 

 




