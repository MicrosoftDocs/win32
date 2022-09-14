---
title: WM_CAP_ABORT message (Vfw.h)
description: The WM\_CAP\_ABORT message stops the capture operation.
ms.assetid: a0479d73-8422-4833-9e8a-c262ec386f58
keywords:
- WM_CAP_ABORT message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_ABORT
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_ABORT message

The **WM\_CAP\_ABORT** message stops the capture operation. In the case of step capture, the image data collected up to the point of the **WM\_CAP\_ABORT** message will be retained in the capture file, but audio will not be captured. You can send this message explicitly or by using the [**capCaptureAbort**](/windows/desktop/api/Vfw/nf-vfw-capcaptureabort) macro.


```C++
WM_CAP_ABORT 
wParam = (WPARAM) 0; 
lParam = 0L; 
```



## Return Value

Returns **TRUE** if successful or **FALSE** otherwise.

## Remarks

The capture operation must yield to use this message.

Use the [**WM\_CAP\_STOP**](wm-cap-stop.md) message to halt step capture at the current position, and then capture audio.

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

 

 





