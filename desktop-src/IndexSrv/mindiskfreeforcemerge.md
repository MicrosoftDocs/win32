---
Description: MinDiskFreeForceMerge
ms.assetid: 3579e82a-d493-4e6a-a024-8f32171acfca
title: MinDiskFreeForceMerge
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MinDiskFreeForceMerge

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MinDiskFreeForceMerge** entry is the minimum percentage of free space that must be available on the catalog drive to keep Indexing Service from beginning a master merge.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Percent        |
| Default: | 15             |
| Range:   | 5 - 25         |



 

### Remarks

If the free space falls below the value specified by the **MinDiskFreeForceMerge** entry and the disk space occupied by the shadow indexes exceeds [**MaxShadowFreeForceMerge**](maxshadowfreeforcemerge.md), a master merge is started.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> <dt>

[MaxShadowIndexSize](maxshadowindexsize.md)
</dt> </dl>

 

 



