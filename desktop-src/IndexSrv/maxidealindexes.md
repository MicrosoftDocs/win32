---
title: MaxIdealIndexes
description: MaxIdealIndexes
ms.assetid: 'b9f5fc4a-a1db-44ce-9130-cbd7f4ea0a8d'
---

# MaxIdealIndexes

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MaxIdealIndexes** entry is the maximum number of indexes considered acceptable in a well-tuned system.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Indexes        |
| Default: | 5              |
| Range:   | 2 - 100        |



 

### Remarks

When the number of indexes exceeds the value of the **MaxIdealIndexes** entry and the system is idle, an annealing merge takes place to bring the total count of indexes back to this number or lower.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




