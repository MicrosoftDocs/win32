---
Description: MinimizeWorkingSet
ms.assetid: ea21f0b3-6d8d-4176-8fdc-620f08aaae31
title: MinimizeWorkingSet
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MinimizeWorkingSet

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MinimizeWorkingSet** entry controls whether to minimize the size of the working set (the set of memory pages in physical RAM memory visible to a process) when Indexing Service is idle.

### Summary



|                     |                                                                                                                     |
|---------------------|---------------------------------------------------------------------------------------------------------------------|
| Type:<br/>    | **REG\_DWORD**                                                                                                      |
| Units:<br/>   | Boolean<br/>                                                                                                  |
| Default:<br/> | 1 on Windows 2000 Professional, Windows XP,<br/> 0 on Windows 2000 Server and Windows Server 2003.<br/> |
| Range:<br/>   | 0, 1<br/>                                                                                                     |



 

### Remarks

If the value of the **MinimizeWorkingSet** entry is nonzero, the working set for Indexing Service is kept to a minimum to keep the indexing process unobtrusive.

The value of an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog cannot override the value of this entry.

## Related topics

<dl> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




