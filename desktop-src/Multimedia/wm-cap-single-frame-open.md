---
title: WM_CAP_SINGLE_FRAME_OPEN message (Vfw.h)
description: The WM\_CAP\_SINGLE\_FRAME\_OPEN message opens the capture file for single-frame capturing. Any previous information in the capture file is overwritten. You can send this message explicitly or by using the capCaptureSingleFrameOpen macro.
ms.assetid: 4814737c-4395-4c01-a68e-fac43dd291fd
keywords:
- WM_CAP_SINGLE_FRAME_OPEN message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_SINGLE_FRAME_OPEN
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_SINGLE\_FRAME\_OPEN message

The **WM\_CAP\_SINGLE\_FRAME\_OPEN** message opens the capture file for single-frame capturing. Any previous information in the capture file is overwritten. You can send this message explicitly or by using the [**capCaptureSingleFrameOpen**](/windows/desktop/api/Vfw/nf-vfw-capcapturesingleframeopen) macro.


```C++
WM_CAP_SINGLE_FRAME_OPEN 
wParam = (WPARAM) 0; 
lParam = 0L; 
```



## Return Value

Returns **TRUE** if successful or **FALSE** otherwise.

## Remarks

For information about installing callback functions, see the [**WM\_CAP\_SET\_CALLBACK\_ERROR**](wm-cap-set-callback-error.md) and [**WM\_CAP\_SET\_CALLBACK\_FRAME**](wm-cap-set-callback-frame.md) messages.

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

 

 





