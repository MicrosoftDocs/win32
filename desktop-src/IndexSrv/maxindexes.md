---
title: MaxIndexes
description: MaxIndexes
ms.assetid: 0d4019e9-a7c5-4622-9391-1ac5a43d252d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MaxIndexes

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MaxIndexes** entry is the maximum number of persistent indexes allowed in the catalog.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Indexes        |
| Default: | 25             |
| Range:   | 10 - 150       |



 

### Remarks

Usually, a shadow merge combines all existing word lists into a new shadow index. When the total number of indexes exceeds the value of the **MaxIndexes** entry, a shadow merge is performed to bring the total below this number.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




