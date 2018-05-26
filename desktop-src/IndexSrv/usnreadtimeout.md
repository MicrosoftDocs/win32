---
title: UsnReadTimeout
description: UsnReadTimeout
ms.assetid: c4ad7f3b-5c6a-4506-a6d4-cfb29a177cee
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# UsnReadTimeout

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **UsnReadTimeout** entry is the maximum interval of time for the indexing process to wait before processing change notifications in the USN journal.

### Summary



|          |                      |
|----------|----------------------|
| Type:    | **REG\_DWORD**       |
| Units:   | Seconds              |
| Default: | 300 (5 minutes)      |
| Range:   | 0 - 43200 (12 hours) |



 

### Remarks

The processing of change notifications proceeds when either an interval of time equal to the value of the **UsnReadTimeout** entry has passed (and there are entries in the USN journal) or the size of the USN journal reaches the value of the [**UsnReadMinSize**](usnreadminsize.md) entry.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> <dt>

[**UsnReadMinSize**](usnreadminsize.md)
</dt> </dl>

 

 




