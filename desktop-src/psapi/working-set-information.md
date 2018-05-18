---
title: Working Set Information
description: The working set of a process is the amount of memory physically mapped to its process context. PSAPI enables you to take snapshots of the working set or to monitor the working set.
ms.assetid: '59ca42c0-ca88-4153-b061-980d961a8ca2'
---

# Working Set Information

The working set of a process is the amount of memory physically mapped to its process context. PSAPI enables you to take snapshots of the working set or to monitor the working set.

The [**QueryWorkingSet**](queryworkingset.md) or [**QueryWorkingSetEx**](queryworkingsetex.md) function fills a buffer with a snapshot of the information for every page in the current working set of the specified process. The function reports only those pages that are physically present at the exact moment it is called.

You can use working set monitoring to find out how much additional RAM a particular operation takes (for example, saving a file). To begin monitoring the working set, call the [**InitializeProcessForWsWatch**](initializeprocessforwswatch.md) function. Not all processes let you read their working set information, so be sure that the function returns a nonzero value before you continue. Next, call the [**GetWsChanges**](getwschanges.md) function. This function reports only the pages that have been loaded in memory since you began monitoring the working set. The function returns data in an array of [**PSAPI\_WS\_WATCH\_INFORMATION**](psapi-ws-watch-information-str.md) structures, one structure for each new page added to the working set of the process. The structure tells you which pages are in memory, and what caused the system to page them in.

The [**EmptyWorkingSet**](emptyworkingset.md) function takes a process handle. It removes as many pages as possible from the process working set. This operation is useful primarily for testing and tuning. Note that the [**SetProcessWorkingSetSize**](https://msdn.microsoft.com/library/windows/desktop/ms686234) function does the same thing if you pass it -1 for the minimum and maximum sizes.

## Related topics

<dl> <dt>

[Working Set](https://msdn.microsoft.com/library/windows/desktop/cc441804)
</dt> </dl>

 

 




