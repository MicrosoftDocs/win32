---
title: WordlistUserIdle
description: WordlistUserIdle
ms.assetid: 1b9e0b5a-7a79-4d90-a7e8-b168bb31e2e2
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WordlistUserIdle

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **WordlistUserIdle** entry determines whether the filtering process is suspended while the keyboard or mouse is in use and determines when filtering will resume.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Seconds        |
| Default: | 120            |
| Range:   | 0 - 1200       |



 

### Remarks

The process of filtering pauses until both input devices are idle for the set amount of time. Set the value of this entry to zero if you don't want filtering to stop while you are using the mouse or keyboard.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




