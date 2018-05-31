---
title: ThreadClassFilter
description: ThreadClassFilter
ms.assetid: 37554b86-2579-4621-9cc7-df7976f1c069
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ThreadClassFilter

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **ThreadClassFilter** entry is the priority class of the CiDaemon.exe process.

### Summary



|          |                                                                                                                                         |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Type:    | **REG\_DWORD**                                                                                                                          |
| Default: | 0x40 (**IDLE\_PRIORITY\_CLASS**)                                                                                                        |
| Range:   | 0x20 (**NORMAL\_PRIORITY\_CLASS**),<br/> 0x40 (**IDLE\_PRIORITY\_CLASS**),<br/> 0x80 (**HIGH\_PRIORITY\_CLASS**)<br/> |



 

### Remarks

The combination of the value of the **ThreadClassFilter** entry and the value of the [**ThreadPriorityFilter**](threadpriorityfilter.md) entry determines the [scheduling priority](_win32_scheduling_priorities) of the filtering process.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> <dt>

[**ThreadPriorityFilter**](threadpriorityfilter.md)
</dt> </dl>

 

 





