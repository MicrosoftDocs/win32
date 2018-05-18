---
title: StompLastAccessDelay
description: StompLastAccessDelay
ms.assetid: '50c6088e-6d61-4f15-8b9d-9880f34a1636'
---

# StompLastAccessDelay

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **StompLastAccessDelay** entry determines whether Indexing Service updates the [last access time](_win32_file_times) of a file after indexing it.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Days           |
| Default: | 7              |
| Range:   | 0 - 1000000000 |



 

### Remarks

Files with last access times before the time determined by the value of the **StompLastAccessDelay** entry don't have their last access times modified by the filter daemon. When you rely on storage management systems (for example, backup utilities) that use Hierarchical Storage Management (HSM), the decision of which files to copy to secondary storage depends on the last access time. Not updating the last access time when an "old" file is filtered keeps such a file from unnecessarily being backed up.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




