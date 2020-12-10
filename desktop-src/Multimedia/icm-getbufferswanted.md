---
title: ICM_GETBUFFERSWANTED message (Vfw.h)
description: The ICM\_GETBUFFERSWANTED message queries a driver for the number of buffers to allocate. You can send this message explicitly or by using the ICGetBuffersWanted macro.
ms.assetid: 109e8627-7ed4-4f17-bf7f-e77f42dfc8c7
keywords:
- ICM_GETBUFFERSWANTED message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_GETBUFFERSWANTED
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_GETBUFFERSWANTED message

The **ICM\_GETBUFFERSWANTED** message queries a driver for the number of buffers to allocate. You can send this message explicitly or by using the [**ICGetBuffersWanted**](/windows/desktop/api/Vfw/nf-vfw-icgetbufferswanted) macro.


```C++
ICM_GETBUFFERSWANTED 
wParam = (DWORD_PTR) (LPVOID) lpdwBuffers; 
lParam = 0; 
```



## Parameters

<dl> <dt>

<span id="lpdwBuffers"></span><span id="lpdwbuffers"></span><span id="LPDWBUFFERS"></span>*lpdwBuffers*
</dt> <dd>

Address to contain the number of samples the driver needs to efficiently render the data.

</dd> </dl>

## Return Value

Returns ICERR\_OK if successful or ICERR\_UNSUPPORTED otherwise.

## Remarks

This message is used by drivers that use hardware to render data and want to ensure a minimal time lag caused by waiting for buffers to arrive. For example, if a driver controls a video decompression board that can hold 10 frames of video, it could return 10 for this message. This instructs applications to try to stay 10 frames ahead of the frame it currently needs.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[Video Compression Manager](video-compression-manager.md)
</dt> <dt>

[Video Compression Messages](video-compression-messages.md)
</dt> </dl>

 

 





