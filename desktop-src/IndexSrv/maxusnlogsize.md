---
title: MaxUsnLogSize
description: MaxUsnLogSize
ms.assetid: 27cc616a-6dee-4593-a7b1-56fa9091ff8c
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MaxUsnLogSize

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MaxUsnLogSize** entry is the size of a Unique Synchronization Number (USN) journal to create on an NTFS file system volume when one does not already exist.

### Summary



|          |                             |
|----------|-----------------------------|
| Type:    | **REG\_DWORD**              |
| Units:   | Bytes                       |
| Default: | 8,388,608 (0x800000)        |
| Range:   | 0 - 4294967295 (0xFFFFFFFF) |



 

### Remarks

The **MaxUsnLogSize** entry has no effect if a volume already has a USN journal.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




