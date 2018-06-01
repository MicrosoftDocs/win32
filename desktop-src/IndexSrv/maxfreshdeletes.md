---
Description: MaxFreshDeletes
ms.assetid: f4843097-bb43-4272-bbc9-00fbb8589cb4
title: MaxFreshDeletes
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MaxFreshDeletes

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MaxFreshDeletes** entry is the maximum number of files deleted from the master index before the master index is updated.

### Summary



|          |                              |
|----------|------------------------------|
| Type:    | **REG\_DWORD**               |
| Units:   | Files                        |
| Default: | 320                          |
| Range:   | 10 - 4294967295 (0xFFFFFFFF) |



 

### Remarks

When the value of the **MaxFreshDeletes** entry is reached, a merge is started.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 



