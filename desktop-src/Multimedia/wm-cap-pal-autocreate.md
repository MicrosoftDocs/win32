---
title: WM_CAP_PAL_AUTOCREATE message (Vfw.h)
description: The WM\_CAP\_PAL\_AUTOCREATE message requests that the capture driver sample video frames and automatically create a new palette. You can send this message explicitly or by using the capPaletteAuto macro.
ms.assetid: b94d245d-adf4-4fe0-b053-87109ef5fd2f
keywords:
- WM_CAP_PAL_AUTOCREATE message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_PAL_AUTOCREATE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_PAL\_AUTOCREATE message

The **WM\_CAP\_PAL\_AUTOCREATE** message requests that the capture driver sample video frames and automatically create a new palette. You can send this message explicitly or by using the [**capPaletteAuto**](/windows/desktop/api/Vfw/nf-vfw-cappaletteauto) macro.


```C++
WM_CAP_PAL_AUTOCREATE 
wParam = (WPARAM) (iFrames); 
lParam = (LPARAM) (DWORD) (iColors); 
```



## Parameters

<dl> <dt>

<span id="iFrames"></span><span id="iframes"></span><span id="IFRAMES"></span>*iFrames*
</dt> <dd>

Number of frames to sample.

</dd> <dt>

<span id="iColors"></span><span id="icolors"></span><span id="ICOLORS"></span>*iColors*
</dt> <dd>

Number of colors in the palette. The maximum value for this parameter is 256.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** otherwise.

If an error occurs and an error callback function is set using the [**WM\_CAP\_SET\_CALLBACK\_ERROR**](wm-cap-set-callback-error.md) message, the error callback function is called.

## Remarks

The sampled video sequence should include all the colors you want in the palette. To obtain the best palette, you might have to sample the whole sequence rather than a portion of it.

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

 

 





