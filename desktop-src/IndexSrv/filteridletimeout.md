---
title: FilterIdleTimeOut
description: FilterIdleTimeOut
ms.assetid: 10e7dc11-b2cf-4e48-99aa-4a7d28c5cbb6
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FilterIdleTimeOut

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **FilterIdleTimeOut** entry controls the time interval after which unused [**IFilter**](/windows/win32/Filter/nn-filter-ifilter?branch=master) DLLs loaded by the CiDaemon.exe process are released.

### Summary



|          |                             |
|----------|-----------------------------|
| Type:    | **REG\_DWORD**              |
| Units:   | Milliseconds                |
| Default: | 900,000 (15 minutes)        |
| Range:   | 0 - 4294967295 (0xFFFFFFFF) |



 

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




