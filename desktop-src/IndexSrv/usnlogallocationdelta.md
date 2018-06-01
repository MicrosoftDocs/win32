---
Description: UsnLogAllocationDelta
ms.assetid: 412b9f2c-6475-48df-ab1f-22184de8fe32
title: UsnLogAllocationDelta
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# UsnLogAllocationDelta

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **UsnLogAllocationDelta** entry is the size allocated for the next entry to the USN journal.

### Summary



|          |                             |
|----------|-----------------------------|
| Type:    | **REG\_DWORD**              |
| Units:   | Bytes                       |
| Default: | 1048576 (1 MB)              |
| Range:   | 1 - 4294967295 (0xFFFFFFFF) |



 

### Remarks

If, during NTFS file system checkpoints, the journal has grown to its maximum allocation, the number of bytes specified by the value of the **UsnLogAllocationDelta** entry is removed from the front of the file to make room for more entries.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 



