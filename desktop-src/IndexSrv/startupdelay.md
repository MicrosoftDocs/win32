---
title: StartupDelay
description: StartupDelay
ms.assetid: 'eb852200-9308-4ace-8a27-e8b9d507f307'
---

# StartupDelay

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **StartupDelay** entry controls the time delay after a system startup before Indexing Service, an automatic system service, starts any scanning or indexing work.

### Summary



|          |                             |
|----------|-----------------------------|
| Type:    | **REG\_DWORD**              |
| Units:   | Milliseconds                |
| Default: | 480000 (8 minutes)          |
| Range:   | 0 - 4294967295 (0xFFFFFFFF) |



 

### Remarks

The value of an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog cannot override the value of this entry.

## Related topics

<dl> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




