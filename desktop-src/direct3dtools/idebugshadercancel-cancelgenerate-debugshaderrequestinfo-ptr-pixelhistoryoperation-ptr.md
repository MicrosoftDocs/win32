---
description: Requests to cancel generation of shader trace instructions in a debug request.
MS-HAID: vspixengine.IDebugShaderCancel\_CancelGenerate\_DebugShaderRequestInfo\_ptr\_PixelHistoryOperation\_ptr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IDebugShaderCancel::CancelGenerate method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 10DA5080-3AA6-47AA-BFE7-774BC26C7F95
api_name: 
 - IDebugShaderCancel.CancelGenerate
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.idebugshadercancel_cancelgenerate_debugshaderrequestinfo_ptr_pixelhistoryoperation_ptr"></span>IDebugShaderCancel::CancelGenerate method

Requests to cancel generation of shader trace instructions in a debug request.

## Syntax


```C++
HRESULT CancelGenerate(
   DebugShaderRequestInfo * requestInfo,
   PixelHistoryOperation *  pPixelHistory
);
```

## Parameters

*requestInfo*   
The address of a DebugShaderRequestInfo structure that describes the requested event/vertex/pixel.

*pPixelHistory*   
The address of pixel history results used for finding the associated pixel to debug. Only applies when debugging a pixel shader.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IDebugShaderCancel**](/windows/desktop/direct3dtools/idebugshadercancel)

 

 
