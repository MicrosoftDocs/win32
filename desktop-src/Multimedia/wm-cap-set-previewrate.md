---
title: WM_CAP_SET_PREVIEWRATE message (Vfw.h)
description: The WM\_CAP\_SET\_PREVIEWRATE message sets the frame display rate in preview mode. You can send this message explicitly or by using the capPreviewRate macro.
ms.assetid: 1189ad4a-1f32-4684-920b-ee3c26ef97f8
keywords:
- WM_CAP_SET_PREVIEWRATE message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_SET_PREVIEWRATE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_SET\_PREVIEWRATE message

The **WM\_CAP\_SET\_PREVIEWRATE** message sets the frame display rate in preview mode. You can send this message explicitly or by using the [**capPreviewRate**](/windows/desktop/api/Vfw/nf-vfw-cappreviewrate) macro.


```C++
WM_CAP_SET_PREVIEWRATE 
wParam = (WPARAM) (wMS); 
lParam = 0L; 
```



## Parameters

<dl> <dt>

<span id="wMS"></span><span id="wms"></span><span id="WMS"></span>*wMS*
</dt> <dd>

Rate, in milliseconds, at which new frames are captured and displayed.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** if the capture window is not connected to a capture driver.

## Remarks

The preview mode uses substantial CPU resources. Applications can disable preview or lower the preview rate when another application has the focus. During streaming video capture, the previewing task is lower priority than writing frames to disk, and preview frames are displayed only if no other buffers are available for writing.

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

 

 





