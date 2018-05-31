---
title: ThreadPriorityMerge
description: ThreadPriorityMerge
ms.assetid: a751191f-a069-4cfa-950d-788911981a1a
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ThreadPriorityMerge

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **ThreadPriorityMerge** entry is the priority level of the merge thread.

### Summary



|                     |                                                                                                                                                                                                                                                     |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type:<br/>    | **REG\_DWORD**<br/>                                                                                                                                                                                                                           |
| Default:<br/> | -2 (**THREAD\_PRIORITY\_LOWEST**)<br/>                                                                                                                                                                                                        |
| Range:<br/>   | -2 (**THREAD\_PRIORITY\_LOWEST**),<br/> -1 (**THREAD\_PRIORITY\_BELOW\_NORMAL**),<br/>  0 (**THREAD\_PRIORITY\_NORMAL**),<br/>  1 (**THREAD\_PRIORITY\_ABOVE\_NORMAL**),<br/>  2 (**THREAD\_PRIORITY\_HIGHEST**)<br/> |



 

### Remarks

The value of the **ThreadPriorityMerge** entry is the only registry entry for controlling the [scheduling priority](_win32_scheduling_priorities) of the merge process.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 





