---
title: ForcedNetPathScanInterval
description: ForcedNetPathScanInterval
ms.assetid: e91bfb3c-edc8-4880-bfb5-a976873c3ad4
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ForcedNetPathScanInterval

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **ForcedNetPathScanInterval** entry is the time interval between forced scans on paths without file-modification notifications.

### Summary



|          |                            |
|----------|----------------------------|
| Type:    | **REG\_DWORD**             |
| Units:   | Minutes                    |
| Default: | 120                        |
| Range:   | 10 - 16777215 (0x00FFFFFF) |



 

### Remarks

The [CiCatalogFlags](cicatalogflags.md) entry controls whether Indexing Service receives file-modification notifications from local or remote hosts.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




