---
description: A callback that notifies the host of framebuffer information returned by the associated request.
MS-HAID: vspixengine.IFrameBufferCallback\_ResultCallback\_DWORD\_DWORD\_DWORD\_DWORD\_double\_DWORD\_BYTE\_arr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IFrameBufferCallback::ResultCallback method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: F0276125-2DA9-45BC-A295-BD67C21EE601
api_name: 
 - IFrameBufferCallback.ResultCallback
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.iframebuffercallback_resultcallback_dword_dword_dword_dword_double_dword_byte_arr"></span>IFrameBufferCallback::ResultCallback method

A callback that notifies the host of framebuffer information returned by the associated request.

## Syntax


```C++
HRESULT ResultCallback(
   DWORD   frameNumber,
   DWORD   width,
   DWORD   height,
   DWORD   renderTargetPtr,
   double  frameDuraction,
   DWORD   size,
   BYTE [] count5_buffer
);
```

## Parameters

*frameNumber*   
The frame number.

*width*   
The width of the frame.

*height*   
The height of the frame.

*renderTargetPtr*   
The render target that the results come from. It is always a slot specified by the frame buffer request, or if not a draw call, then the first RTV bount to the output source.

*frameDuraction*   
Not used.

*size*   
The size of the output buffer in bytes.

*count5\_buffer*   
The contents of the render target in R8G8B8A8\_UNORM format.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IFrameBufferCallback**](/windows/desktop/direct3dtools/iframebuffercallback)

 

 
