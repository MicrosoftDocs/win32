---
Description: Requests to debug a shader on the GPU (live debugging) vs CPU (trace-based debugging).
MS-HAID: vspixengine.IDebugLiveShaderRequest\_BeginDebugLiveShader\_DebugShaderRequestInfo\_ptr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IDebugLiveShaderRequest::BeginDebugLiveShader method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.idebugliveshaderrequest_begindebugliveshader_debugshaderrequestinfo_ptr"></span>IDebugLiveShaderRequest::BeginDebugLiveShader method

Requests to debug a shader on the GPU (live debugging) vs CPU (trace-based debugging).

## Syntax


```C++
);
```

## Parameters

*requestInfo*   
The address of a DebugShaderRequestInfo structure that describes the requested event/vertex/pixel.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IDebugLiveShaderRequest**](https://msdn.microsoft.com/library/windows/desktop/mt422654)

 

 



