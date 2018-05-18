---
title: ForcePathAlias
description: ForcePathAlias
ms.assetid: 'fb297a09-b3af-43c1-b6c1-4692207180de'
---

# ForcePathAlias

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **ForcePathAlias** entry controls under what conditions path aliasing is applied to query results.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Boolean        |
| Default: | 0              |
| Range:   | 0. 1           |



 

### Remarks

Set the value of the **ForcePathAlias** entry to zero if query results are to undergo path aliasing only for remote query clients. Set the value to one if query results are to undergo path aliasing for both local and remote query clients.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




