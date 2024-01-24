---
title: WM_CAP_SET_CALLBACK_VIDEOSTREAM message (Vfw.h)
description: The WM\_CAP\_SET\_CALLBACK\_VIDEOSTREAM message sets a callback function in the application.
ms.assetid: 590089b8-7a8d-476b-9b81-f96bf73b0369
keywords:
- WM_CAP_SET_CALLBACK_VIDEOSTREAM message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_SET_CALLBACK_VIDEOSTREAM
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_SET\_CALLBACK\_VIDEOSTREAM message

The **WM\_CAP\_SET\_CALLBACK\_VIDEOSTREAM** message sets a callback function in the application. AVICap calls this procedure during streaming capture when a video buffer is filled. You can send this message explicitly or by using the [**capSetCallbackOnVideoStream**](/windows/desktop/api/Vfw/nf-vfw-capsetcallbackonvideostream) macro.


```C++
WM_CAP_SET_CALLBACK_VIDEOSTREAM 
wParam = (WPARAM) 0; 
lParam = (LPARAM) (LPVOID) (fpProc); 
```



## Parameters

<dl> <dt>

<span id="fpProc"></span><span id="fpproc"></span><span id="FPPROC"></span>*fpProc*
</dt> <dd>

Pointer to the video-stream callback function, of type [**capVideoStreamCallback**](/windows/desktop/api/Vfw/nc-vfw-capvideocallback). Specify **NULL** for this parameter to disable a previously installed video-stream callback function.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** if streaming capture or a single-frame capture session is in progress.

## Remarks

The capture window calls the callback function before writing the captured frame to disk. This allows applications to modify the frame if desired.

If a video stream callback function is used for streaming capture, the procedure must be installed before starting the capture session and it must remain enabled for the duration of the session. It can be disabled after streaming capture ends.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[Video Capture](video-capture.md)
</dt> <dt>

[Video Capture Messages](video-capture-messages.md)
</dt> </dl>

 

 





