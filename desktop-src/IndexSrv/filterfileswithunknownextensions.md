---
title: FilterFilesWithUnknownExtensions
description: FilterFilesWithUnknownExtensions
ms.assetid: ebadd5f6-82a7-43f1-98bc-14fb6921b532
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FilterFilesWithUnknownExtensions

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **FilterFilesWithUnknownExtensions** entry determines whether files with extensions that have not been registered will be filtered.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Boolean        |
| Default: | 1              |
| Range:   | 0, 1           |



 

### Remarks

Set the value of the **FilterFilesWithUnknownExtensions** entry to zero if only registered file types are to be filtered. Set the value to one if unregistered file types are also to be filtered.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




