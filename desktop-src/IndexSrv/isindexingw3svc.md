---
title: IsIndexingW3SVC
description: IsIndexingW3SVC
ms.assetid: 'ab8917f4-5faa-42cc-a151-a78ce967c8fe'
---

# IsIndexingW3SVC

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **IsIndexingW3SVC** entry determines whether Indexing Service configures itself to index the files on web servers.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Boolean        |
| Default: | 1              |
| Range:   | 0, 1           |



 

### Remarks

Set the value of the **IsIndexingW3SVC** entry to one to configure the catalog to work with web servers. Set it to zero to bypass indexing of web servers.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




