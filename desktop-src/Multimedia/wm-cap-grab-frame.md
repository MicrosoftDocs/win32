---
title: WM_CAP_GRAB_FRAME message (Vfw.h)
description: The WM\_CAP\_GRAB\_FRAME message retrieves and displays a single frame from the capture driver. After capture, overlay and preview are disabled. You can send this message explicitly or by using the capGrabFrame macro.
ms.assetid: 91d58c1c-53b9-4813-88c2-7a1acf641d96
keywords:
- WM_CAP_GRAB_FRAME message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_GRAB_FRAME
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_GRAB\_FRAME message

The **WM\_CAP\_GRAB\_FRAME** message retrieves and displays a single frame from the capture driver. After capture, overlay and preview are disabled. You can send this message explicitly or by using the [**capGrabFrame**](/windows/desktop/api/Vfw/nf-vfw-capgrabframe) macro.


```C++
WM_CAP_GRAB_FRAME 
wParam = (WPARAM)0; 
lParam = (LPARAM)0L; 
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

 

 





