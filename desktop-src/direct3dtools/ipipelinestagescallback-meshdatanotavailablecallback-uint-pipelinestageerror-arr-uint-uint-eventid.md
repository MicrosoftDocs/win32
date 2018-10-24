---
Description: A callback that notifies the host of which pipeline stages are not able to return mesh data for the event specified in the associated request.
MS-HAID: vspixengine.IPipeLineStagesCallback\_MeshDataNotAvailableCallback\_UINT\_PipeLineStageError\_arr\_UINT\_UINT\_EventID
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPipeLineStagesCallback::MeshDataNotAvailableCallback method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.ipipelinestagescallback_meshdatanotavailablecallback_uint_pipelinestageerror_arr_uint_uint_eventid"></span>IPipeLineStagesCallback::MeshDataNotAvailableCallback method

A callback that notifies the host of which pipeline stages are not able to return mesh data for the event specified in the associated request.

## Syntax


```C++
);
```

## Parameters

*numberStages*   
The number of stage errors returned.

*count0\_errors*   
The pipeline stage errors.

*width*   
The width of the swap chain assocaited with the draw call. This is used when requesting pipeline preview images.

*height*   
The height of the swap chain assocaited with the draw call. This is used when requesting pipeline preview images.

*eid*   
The event represented in the results.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IPipeLineStagesCallback**](https://msdn.microsoft.com/library/windows/desktop/mt432716)

 

 



