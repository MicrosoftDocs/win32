---
title: IsIndexingNNTPSvc
description: IsIndexingNNTPSvc
ms.assetid: 'e3d9ad9e-1c7d-448f-a245-6e37dfdc3252'
---

# IsIndexingNNTPSvc

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **IsIndexingNNTPSvc** entry determines whether Indexing Service configures itself to work with Network News Transfer Protocol (NNTP) messages.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Boolean        |
| Default: | 0              |
| Range:   | 0, 1           |



 

### Remarks

Set the value of the **IsIndexingNNTPSvc** entry to one to configure the catalog to work with NNTP messages. Set it to zero to bypass indexing of NNTP messages.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




