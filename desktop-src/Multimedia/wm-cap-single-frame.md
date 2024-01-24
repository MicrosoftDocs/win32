---
title: WM_CAP_SINGLE_FRAME message (Vfw.h)
description: The WM\_CAP\_SINGLE\_FRAME message appends a single frame to a capture file that was opened using the WM\_CAP\_SINGLE\_FRAME\_OPEN message. You can send this message explicitly or by using the capCaptureSingleFrame macro.
ms.assetid: 95466961-0719-4ff7-afc8-f7bf0e0974ac
keywords:
- WM_CAP_SINGLE_FRAME message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_SINGLE_FRAME
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_SINGLE\_FRAME message

The **WM\_CAP\_SINGLE\_FRAME** message appends a single frame to a capture file that was opened using the [**WM\_CAP\_SINGLE\_FRAME\_OPEN**](wm-cap-single-frame-open.md) message. You can send this message explicitly or by using the [**capCaptureSingleFrame**](/windows/desktop/api/Vfw/nf-vfw-capcapturesingleframe) macro.


```C++
WM_CAP_SINGLE_FRAME 
wParam = (WPARAM) 0; 
lParam = 0L; 
```



## Return Value

Returns **TRUE** if successful or **FALSE** otherwise.

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

 

 





