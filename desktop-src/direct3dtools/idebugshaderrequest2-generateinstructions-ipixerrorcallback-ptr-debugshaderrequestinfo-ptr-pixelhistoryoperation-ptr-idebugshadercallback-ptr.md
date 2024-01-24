---
description: Requests to generate shader trace instructions in a debug request. Trace-based debugging occurs on the CPU (warp) instead of the GPU.
MS-HAID: vspixengine.IDebugShaderRequest2\_GenerateInstructions\_IPixErrorCallback\_ptr\_DebugShaderRequestInfo\_ptr\_PixelHistoryOperation\_ptr\_IDebugShaderCallback\_ptr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IDebugShaderRequest2::GenerateInstructions method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 50685D38-AA85-43D7-9199-12B3776708C2
api_name: 
 - IDebugShaderRequest2.GenerateInstructions
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.idebugshaderrequest2_generateinstructions_ipixerrorcallback_ptr_debugshaderrequestinfo_ptr_pixelhistoryoperation_ptr_idebugshadercallback_ptr"></span>IDebugShaderRequest2::GenerateInstructions method

Requests to generate shader trace instructions in a debug request. Trace-based debugging occurs on the CPU (warp) instead of the GPU.

## Syntax


```C++
HRESULT GenerateInstructions(
   IPixErrorCallback *      errorCallback,
   DebugShaderRequestInfo * requestInfo,
   PixelHistoryOperation *  pPixelHistory,
   IDebugShaderCallback *   pCallback
);
```

## Parameters

*errorCallback*   
The address of a callback for errors that might occur while generating shader trace instructions.

*requestInfo*   
The address of a DebugShaderRequestInfo structure that describes the requested event/vertex/pixel.

*pPixelHistory*   
The address of pixel history results used for finding the associated pixel to debug. Only applies when debugging a pixel shader.

*pCallback*   
The address of a callback used to notify the host of results.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IDebugShaderRequest2**](/windows/desktop/direct3dtools/idebugshaderrequest2)

 

 
