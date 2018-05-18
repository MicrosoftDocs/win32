---
title: ThreadPriorityFilter
description: ThreadPriorityFilter
ms.assetid: '2b72f367-95f7-49fc-ae3f-0b3f51d09305'
---

# ThreadPriorityFilter

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **ThreadPriorityFilter** entry is the priority level of the filtering thread within the CiDaemon.exe process.

### Summary



|                     |                                                                                                                                                                                                                                                     |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type:<br/>    | **REG\_DWORD**<br/>                                                                                                                                                                                                                           |
| Default:<br/> | 1 (**THREAD\_PRIORITY\_ABOVE\_NORMAL**)<br/>                                                                                                                                                                                                  |
| Range:<br/>   | -2 (**THREAD\_PRIORITY\_LOWEST**),<br/> -1 (**THREAD\_PRIORITY\_BELOW\_NORMAL**),<br/>  0 (**THREAD\_PRIORITY\_NORMAL**),<br/>  1 (**THREAD\_PRIORITY\_ABOVE\_NORMAL**),<br/>  2 (**THREAD\_PRIORITY\_HIGHEST**)<br/> |



 

### Remarks

The combination of the value of the **ThreadPriorityFilter** entry and the value of the [**ThreadClassFilter**](threadclassfilter.md) entry controls the [scheduling priority](_win32_scheduling_priorities) of the filtering process.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> <dt>

[**ThreadClassFilter**](threadclassfilter.md)
</dt> </dl>

 

 





