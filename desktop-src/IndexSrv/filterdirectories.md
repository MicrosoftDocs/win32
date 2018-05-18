---
title: FilterDirectories
description: FilterDirectories
ms.assetid: '64d06424-5fc1-44d7-9f84-5f9cdd8f3a5d'
---

# FilterDirectories

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **FilterDirectories** entry controls whether directories are filtered for system properties.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Boolean        |
| Default: | 1              |
| Range:   | 0, 1           |



 

### Remarks

Set the value of the **FilterDirectories** entry to zero to have Indexing Service ignore directory properties. Set it to a nonzero value to filter and display the properties of directories in query results.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




