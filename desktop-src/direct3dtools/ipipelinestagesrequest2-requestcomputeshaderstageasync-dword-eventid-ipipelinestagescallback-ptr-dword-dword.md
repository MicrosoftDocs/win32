---
description: An asynchronous request to get whether the compute shader stage was used for the specified frame and event.
MS-HAID: vspixengine.IPipeLineStagesRequest2\_RequestComputeShaderStageAsync\_DWORD\_EventID\_IPipeLineStagesCallback\_ptr\_DWORD\_DWORD
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPipeLineStagesRequest2::RequestComputeShaderStageAsync method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: EC5695A6-70B5-4F7D-A235-974A0A59A44F
api_name: 
 - IPipeLineStagesRequest2.RequestComputeShaderStageAsync
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.ipipelinestagesrequest2_requestcomputeshaderstageasync_dword_eventid_ipipelinestagescallback_ptr_dword_dword"></span>IPipeLineStagesRequest2::RequestComputeShaderStageAsync method

An asynchronous request to get whether the compute shader stage was used for the specified frame and event.

## Syntax


```C++
HRESULT RequestComputeShaderStageAsync(
   DWORD                     frameNumber,
   EventID                   eventID,
   IPipeLineStagesCallback * requestCallback,
   DWORD                     requestCookie,
   DWORD                     progressIntervalMsecs
);
```

## Parameters

*frameNumber*   
The specified frame.

*eventID*   
The specified event.

*requestCallback*   
The address of callback used to notify the host of results.

*requestCookie*   
A cookie that uniquely identifies the request, and can be used to signal for it to be cancelled.

*progressIntervalMsecs*   
Not used.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IPipeLineStagesRequest2**](/windows/desktop/direct3dtools/ipipelinestagesrequest2)

 

 
