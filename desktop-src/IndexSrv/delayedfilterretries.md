---
title: DelayedFilterRetries
description: DelayedFilterRetries
ms.assetid: '3023a3c3-8ca5-4cfc-a959-221648f495de'
---

# DelayedFilterRetries

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DelayedFilterRetries** entry controls the number of times Indexing Service tries to index a document that has been placed in the secondary indexing queue because the first attempt to index it failed.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Retries        |
| Default: | 240            |
| Range:   | 0 - 32000      |



 

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[FilterRetryInterval](filterretryinterval.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




