---
Description: MaxWordlistSize
ms.assetid: 106261dc-1687-4226-b8d1-8c0a58cb0c98
title: MaxWordlistSize
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MaxWordlistSize

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MaxWordlistSize** entry is the maximum amount of memory consumed by an individual word list.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | 128 Kilobytes  |
| Default: | 20 (2.5 MB)    |
| Range:   | 10 - 30        |



 

### Remarks

When the limit specified by the value of the **MaxWordlistSize** entry is reached, only the document being filtered is added to the current word list. Additional documents are queued and later placed in another word list.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 



