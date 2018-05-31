---
title: FilterRemainingThreshold
description: FilterRemainingThreshold
ms.assetid: ea5d9671-aec7-4f3f-a88c-0e315d7ad5e3
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FilterRemainingThreshold

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **FilterRemainingThreshold** entry delays filtering if the number of documents to be filtered is less than the number of files set in the value of this registry entry.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Files          |
| Default: | 32             |
| Range:   | 0 - 320        |



 

### Remarks

The delay specified by the value of the **FilterRemainingThreshold** entry prevents Indexing Service from overusing resources while trying to index temporary files created by running applications.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




