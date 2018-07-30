---
Description: A callback that notifies the host that ThreadData is unavailable for a particular pipeline stage and event.
MS-HAID: vspixengine.IPipeLineStagesCallback2\_ThreadDataNotAvailableCallback\_PipeLineStageError\_EventID
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPipeLineStagesCallback2::ThreadDataNotAvailableCallback method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.ipipelinestagescallback2_threaddatanotavailablecallback_pipelinestageerror_eventid"></span>IPipeLineStagesCallback2::ThreadDataNotAvailableCallback method

A callback that notifies the host that ThreadData is unavailable for a particular pipeline stage and event.

## Syntax


```C++
);
```

## Parameters

*error*   
The pipeline stage error.

*eid*   
The event represented in the results.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IPipeLineStagesCallback2**](https://msdn.microsoft.com/library/windows/desktop/mt432717)

 

 



