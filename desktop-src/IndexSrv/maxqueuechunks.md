---
title: MaxQueueChunks
description: MaxQueueChunks
ms.assetid: 3aac1ba5-21bb-483f-8914-daee6aa10994
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MaxQueueChunks

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MaxQueueChunks** entry is the maximum number of buffers in memory that can be used for keeping track of unfiltered documents.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Buffers        |
| Default: | 20             |
| Range:   | 10 - 30        |



 

### Remarks

The larger the value of the **MaxQueueChunks** entry, the less frequently data needs to be written to disk.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




