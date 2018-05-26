---
title: MaxShadowFreeForceMerge
description: MaxShadowFreeForceMerge
ms.assetid: 3cbe7c90-290c-4a3b-bf4c-720eebf5f417
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MaxShadowFreeForceMerge

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MaxShadowFreeForceMerge** entry specifies the percentage of available disk space that can be used by shadow indexes on a catalog drive before a master merge is triggered.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Percent        |
| Default: | 20             |
| Range:   | 5 - 100        |



 

### Remarks

If the percentage of disk space used by shadow indexes exceeds the value of the **MaxShadowFreeForceMerge** entry, and if the total free disk space falls below the minimum set in the [**MinDiskFreeForceMerge**](mindiskfreeforcemerge.md), a master merge begins.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> <dt>

[MaxShadowIndexSize](maxshadowindexsize.md)
</dt> </dl>

 

 




