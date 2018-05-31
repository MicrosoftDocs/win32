---
title: FilterDelayInterval
description: FilterDelayInterval
ms.assetid: bb2cc61c-1f0c-4593-bc8e-3c3472c163ca
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FilterDelayInterval

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **FilterDelayInterval** entry determines the number of seconds to suspend filtering when the number of documents left to filter equals the value in the [FilterRemainingThreshold](filterremainingthreshold.md) entry.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Seconds        |
| Default: | 20             |
| Range:   | 0 - 600        |



 

### Remarks

The **FilterDelayInterval** value can prevent Indexing Service from overusing resources while trying to index temporary files created by running applications. Increase the value of this entry if filtering certain files uses more resources than allowed.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




