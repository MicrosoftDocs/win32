---
Description: W3SvcInstance
ms.assetid: c715a59b-7485-4d23-8e5a-cdda0f44c4b9
title: W3SvcInstance
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# W3SvcInstance

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **W3SvcInstance** entry identifies the instance of the WWW server whose virtual directories are indexed by the catalog.

### Summary



|          |                             |
|----------|-----------------------------|
| Type:    | **REG\_DWORD**              |
| Default: | 1                           |
| Range:   | 1 - 4294967295 (0xFFFFFFFF) |



 

### Remarks

The **W3SvcInstance** entry is effective only when the value of the [**IsIndexingW3Svc**](isindexingw3svc.md) entry is set to one.

Different virtual servers are identified by different values of the **W3SvcInstance** entry. You can set those values by setting each individual [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey entry to override the main registry entry.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[**IsIndexingW3Svc**](isindexingw3svc.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 



