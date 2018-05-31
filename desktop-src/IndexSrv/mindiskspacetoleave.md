---
title: MinDiskSpaceToLeave
description: MinDiskSpaceToLeave
ms.assetid: ff5176be-a085-441e-8c61-1332c9fc48ad
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MinDiskSpaceToLeave

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MinDiskSpaceToLeave** entry is the minimum amount of free disk space to leave on a disk.

### Summary



|          |                             |
|----------|-----------------------------|
| Type:    | **REG\_DWORD**              |
| Units:   | Megabytes                   |
| Default: | 20                          |
| Range:   | 0 - 4294967295 (0xFFFFFFFF) |



 

### Remarks

When the amount of free disk space falls below the value specified by the **MinDiskSpaceToLeave** entry, additional attempts to extend the allocation for catalog files fail.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




