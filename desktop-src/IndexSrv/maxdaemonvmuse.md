---
title: MaxDaemonVmUse
description: MaxDaemonVmUse
ms.assetid: '9dd0f966-e9f7-4447-b1f0-24b6b8e0fc1d'
---

# MaxDaemonVmUse

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MaxDaemonVmUse** entry is the maximum amount of page-file space allocated to virtual memory for a filter daemon.

### Summary



|          |                                          |
|----------|------------------------------------------|
| Type:    | **REG\_DWORD**                           |
| Units:   | Kilobytes                                |
| Default: | 40960 (40 MB)                            |
| Range:   | 10240 - 4194303 (10 MB to 4 GB - 1 byte) |



 

### Remarks

Attempted allocations beyond the value of the **MaxDaemonVmUse** entry will fail.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




