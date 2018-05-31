---
title: LowResourceSleep
description: LowResourceSleep
ms.assetid: 0cf42902-9be7-4b33-96cc-498d70fbd359
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LowResourceSleep

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **LowResourceSleep** entry is the time interval that Indexing Service waits after low-resource conditions occur before retrying the affected processing.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Seconds        |
| Default: | 180            |
| Range:   | 5 - 1200       |



 

### Remarks

When system resource limitations (such as low memory or heavy I/O initiated by the end user) occur, Indexing Service suspends processing for a time interval equal to the value of the **LowResourceSleep** entry before trying to resume the processing.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[LowResourceCheckInterval](lowresourcecheckinterval.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




