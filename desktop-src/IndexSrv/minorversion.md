---
title: MinorVersion
description: MinorVersion
ms.assetid: 'd06d3710-b93c-49f9-b883-d7dc7caa5230'
---

# MinorVersion

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MinorVersion** entry indicates the minor version number of the installed Indexing Service.

### Summary



|          |                             |
|----------|-----------------------------|
| Type:    | **REG\_DWORD**              |
| Default: | 0                           |
| Range:   | 0 - 4294967295 (0xFFFFFFFF) |



 

### Remarks

The complete version of Indexing Service is the value of [**MajorVersion**](majorversion.md) combined with the value of the **MinorVersion** entry. For example if there were a Version 3.1, the value of the entry would be 1. This entry should not be changed except by installation of an upgraded version of Indexing Service.

The value of an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog cannot override the value of this entry.

## Related topics

<dl> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




