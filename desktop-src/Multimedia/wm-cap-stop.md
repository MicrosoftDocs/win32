---
title: WM_CAP_STOP message (Vfw.h)
description: The WM\_CAP\_STOP message stops the capture operation. You can send this message explicitly or by using the capCaptureStop macro.
ms.assetid: 0fea82f5-f381-485a-82ae-b081b3a5e402
keywords:
- WM_CAP_STOP message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_STOP
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_STOP message

The **WM\_CAP\_STOP** message stops the capture operation. You can send this message explicitly or by using the [**capCaptureStop**](/windows/desktop/api/Vfw/nf-vfw-capcapturestop) macro.

In step frame capture, the image data that was collected before this message was sent is retained in the capture file. An equivalent duration of audio data is also retained in the capture file if audio capture was enabled.


```C++
WM_CAP_STOP 
wParam = (WPARAM) 0; 
lParam = 0L; 
```



## Return Value

Returns **TRUE** if successful or **FALSE** otherwise.

## Remarks

The capture operation must yield to use this message. Use the [**WM\_CAP\_ABORT**](wm-cap-abort.md) message to abandon the current capture operation.

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

 

 





