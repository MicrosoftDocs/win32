---
title: MaxFilesizeMultiplier
description: MaxFilesizeMultiplier
ms.assetid: e7ce8f5b-d6e5-4bb0-9edf-ef3bcda744f5
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MaxFilesizeMultiplier

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MaxFilesizeMultiplier** entry determines the maximum amount of data that can be generated from a single file, based on its size.

### Summary



|          |                             |
|----------|-----------------------------|
| Type:    | **REG\_DWORD**              |
| Default: | 8                           |
| Range:   | 4 - 4294967295 (0xFFFFFFFF) |



 

### Remarks

The value of the **MaxFilesizeMultiplier** entry is a multiplier, which means that a value of four indicates that a file can generate up to four times its size in Indexing Service data. The use of this value allows a graceful recovery from indexing certain kinds of corrupt files.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




