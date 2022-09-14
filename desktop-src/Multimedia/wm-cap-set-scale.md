---
title: WM_CAP_SET_SCALE message (Vfw.h)
description: The WM\_CAP\_SET\_SCALE message enables or disables scaling of the preview video images.
ms.assetid: f15f1d18-2c5a-40c1-baa1-0d18549bee23
keywords:
- WM_CAP_SET_SCALE message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_SET_SCALE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_SET\_SCALE message

The **WM\_CAP\_SET\_SCALE** message enables or disables scaling of the preview video images. If scaling is enabled, the captured video frame is stretched to the dimensions of the capture window. You can send this message explicitly or by using the [**capPreviewScale**](/windows/desktop/api/Vfw/nf-vfw-cappreviewscale) macro.


```C++
WM_CAP_SET_SCALE 
wParam = (WPARAM) (BOOL)f; 
lParam = 0L; 
```



## Parameters

<dl> <dt>

<span id="f"></span><span id="F"></span>*f*
</dt> <dd>

Preview scaling flag. Specify **TRUE** for this parameter to stretch preview frames to the size of the capture window or **FALSE** to display them at their natural size.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** otherwise.

## Remarks

Scaling preview images controls the immediate presentation of captured frames within the capture window. It has no effect on the size of the frames saved to file.

Scaling has no effect when using overlay to display video in the frame buffer.

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

 

 





