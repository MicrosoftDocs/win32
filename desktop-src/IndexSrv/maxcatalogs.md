---
title: MaxCatalogs
description: MaxCatalogs
ms.assetid: 7d592253-78a9-4671-b5b9-0cf3f197e1e9
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MaxCatalogs

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MaxCatalogs** entry is the maximum number of catalogs that Indexing Service can open at one time.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Catalogs       |
| Default: | 33             |
| Range:   | 1 - 1000       |



 

### Remarks

The value of an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog cannot override the value of this entry.

## Related topics

<dl> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




