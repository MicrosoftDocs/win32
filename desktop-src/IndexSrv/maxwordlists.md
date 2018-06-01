---
Description: MaxWordLists
ms.assetid: 5cbf089f-07c0-49a0-b3e3-0464efb595dd
title: MaxWordLists
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MaxWordLists

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MaxWordLists** entry is the maximum number of word lists that can exist.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Word lists     |
| Default: | 20             |
| Range:   | 10 - 30        |



 

### Remarks

Exceeding the limit specified in the value of the **MaxWordLists** entry triggers a shadow merge to the master index.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 



