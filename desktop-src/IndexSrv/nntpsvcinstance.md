---
title: NNTPSvcInstance
description: NNTPSvcInstance
ms.assetid: 'b61c1172-3642-4654-9b3c-514c3d21fa05'
---

# NNTPSvcInstance

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **NNTPSvcInstance** entry identifies the instance of the Network News Transfer Protocol (NNTP) server whose virtual directories are indexed by the catalog.

### Summary



|          |                             |
|----------|-----------------------------|
| Type:    | **REG\_DWORD**              |
| Default: | 1                           |
| Range:   | 1 - 4294967295 (0xFFFFFFFF) |



 

### Remarks

The **NNTPSvcInstance** entry is effective only when the value of the [**IsIndexingIMAPSvc**](isindexingimapsvc.md) entry is set to one.

Different virtual servers are identified by different values of an **NNTPSvcInstance** entry.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[IsIndexingIMAPSvc](isindexingimapsvc.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




