---
title: MinMergeIdleTime
description: MinMergeIdleTime
ms.assetid: 59f2674e-efb8-4119-b1da-a0622ff7b843
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MinMergeIdleTime

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MinMergeIdleTime** entry is the minimum percentage of CPU processing time that must be idle during a merge-check period before Indexing Service can initiate an annealing merge.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Percent        |
| Default: | 90             |
| Range:   | 10 - 100       |



 

### Remarks

Indexing Service uses the value of the **MinMergeIdleTime** entry to delay merges until there are no other heavy demands on the processor.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




