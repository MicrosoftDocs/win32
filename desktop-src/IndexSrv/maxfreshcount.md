---
Description: MaxFreshCount
ms.assetid: 1fbc10de-e7c1-476a-b72b-43618e1fae3a
title: MaxFreshCount
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MaxFreshCount

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MaxFreshCount** entry is the maximum number of files for which the latest indexed data is not in the master index.

### Summary



|          |                                |
|----------|--------------------------------|
| Type:    | **REG\_DWORD**                 |
| Units:   | Files                          |
| Default: | 20000                          |
| Range:   | 1000 - 4294967295 (0xFFFFFFFF) |



 

### Remarks

When the value of the **MaxFreshCount** entry is reached, a master merge is started.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 



