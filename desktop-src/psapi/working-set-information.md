---
title: Working Set Information
description: The working set of a process is the amount of memory physically mapped to its process context. PSAPI enables you to take snapshots of the working set or to monitor the working set.
ms.assetid: '33c42f79-cc77-4d44-84c3-8bf0a4a60019'
ms.topic: article
ms.date: 05/31/2018
---

# Working Set Information

The working set of a process is the amount of memory physically mapped to its process context. PSAPI enables you to take snapshots of the working set or to monitor the working set.

The [**QueryWorkingSet**](/windows/desktop/api/Psapi/nf-psapi-queryworkingset) or [**QueryWorkingSetEx**](/windows/desktop/api/Psapi/nf-psapi-queryworkingsetex) function fills a buffer with a snapshot of the information for every page in the current working set of the specified process. The function reports only those pages that are physically present at the exact moment it is called.

You can use working set monitoring to find out how much additional RAM a particular operation takes (for example, saving a file). To begin monitoring the working set, call the [**InitializeProcessForWsWatch**](/windows/desktop/api/Psapi/nf-psapi-initializeprocessforwswatch) function. Not all processes let you read their working set information, so be sure that the function returns a nonzero value before you continue. Next, call the [**GetWsChanges**](/windows/desktop/api/Psapi/nf-psapi-getwschanges) function. This function reports only the pages that have been loaded in memory since you began monitoring the working set. The function returns data in an array of [**PSAPI\_WS\_WATCH\_INFORMATION**](/windows/desktop/api/Psapi/ns-psapi-psapi_ws_watch_information) structures, one structure for each new page added to the working set of the process. The structure tells you which pages are in memory, and what caused the system to page them in.

The [**EmptyWorkingSet**](/windows/desktop/api/Psapi/nf-psapi-emptyworkingset) function takes a process handle. It removes as many pages as possible from the process working set. This operation is useful primarily for testing and tuning. Note that the [**SetProcessWorkingSetSize**](/windows/desktop/api/memoryapi/nf-memoryapi-setprocessworkingsetsize) function does the same thing if you pass it -1 for the minimum and maximum sizes.

## Related topics

<dl> <dt>

[Working Set](/windows/desktop/Memory/working-set)
</dt> </dl>

 

 