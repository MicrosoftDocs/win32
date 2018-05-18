---
title: MaxCharacterization
description: MaxCharacterization
ms.assetid: '48c20717-c77b-49ef-a1b4-7fef89ab56e6'
---

# MaxCharacterization

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MaxCharacterization** entry is the number of characters in the automatically generated characterizations (also known as an abstracts) of files that Indexing Service indexes.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Characters     |
| Default: | 160            |
| Range:   | 0 - 500        |



 

### Remarks

Setting the value of the **MaxCharacterization** entry to zero disables the generation of characterizations. This is equivalent to setting the value of the [**GenerateCharacterization**](generatecharacterization.md) entry to a value of zero.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




