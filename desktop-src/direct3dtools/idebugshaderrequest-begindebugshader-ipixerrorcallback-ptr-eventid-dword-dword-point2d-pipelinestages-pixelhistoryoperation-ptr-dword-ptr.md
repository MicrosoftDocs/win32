---
description: Requests to start a shader debugging session for the specified pipeline stage, pixel/vertex if applicable, event, and frame.
MS-HAID: vspixengine.IDebugShaderRequest\_BeginDebugShader\_IPixErrorCallback\_ptr\_EventID\_DWORD\_DWORD\_Point2D\_PipeLineStages\_PixelHistoryOperation\_ptr\_DWORD\_ptr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IDebugShaderRequest::BeginDebugShader method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: CC93D31C-8593-4B03-B974-87B886B9431D
api_name: 
 - IDebugShaderRequest.BeginDebugShader
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.idebugshaderrequest_begindebugshader_ipixerrorcallback_ptr_eventid_dword_dword_point2d_pipelinestages_pixelhistoryoperation_ptr_dword_ptr"></span>IDebugShaderRequest::BeginDebugShader method

Requests to start a shader debugging session for the specified pipeline stage, pixel/vertex if applicable, event, and frame.

## Syntax


```C++
HRESULT BeginDebugShader(
   IPixErrorCallback *     errorCallback,
   EventID                 eventID,
   DWORD                   frameNumber,
   DWORD                   vertex,
   Point2D                 pixel,
   PipeLineStages          stage,
   PixelHistoryOperation * pPixelHistory,
   DWORD *                 pDevice
);
```

## Parameters

*errorCallback*   
The address of a callback for errors that might occur during debugging.

*eventID*   
The specified event.

*frameNumber*   
The specified frame.

*vertex*   
The specified vertex. Only applies when debugging a vertex shader.

*pixel*   
The specified pixel. Only applies when debugging a pixel shader.

*stage*   
The specified pipeline stage.

*pPixelHistory*   
The address of pixel history results used for finding the associated pixel to debug. Only applies when debugging a pixel shader.

*pDevice*   
The address to pass to the debug engine for communicating with this debug session (debug engine readprocessmemory on this address).

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IDebugShaderRequest**](/windows/desktop/direct3dtools/idebugshaderrequest)

 

 
