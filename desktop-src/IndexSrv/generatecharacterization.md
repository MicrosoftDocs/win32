---
title: GenerateCharacterization
description: GenerateCharacterization
ms.assetid: 6419e27d-cbad-4a30-94df-ee82f666a900
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GenerateCharacterization

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **GenerateCharacterization** entry controls whether Indexing Service automatically generates characterizations (also known as abstracts) for files that it indexes.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Boolean        |
| Default: | 1              |
| Range:   | 0, 1           |



 

### Remarks

The results of setting the **GenerateCharacterization** entry to a value of zero can also be attained by setting the [MaxCharacterization](maxcharacterization.md) entry to a value of zero.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




