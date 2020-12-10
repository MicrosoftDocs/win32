---
title: WM_CAP_PAL_MANUALCREATE message (Vfw.h)
description: The WM\_CAP\_PAL\_MANUALCREATE message requests that the capture driver manually sample video frames and create a new palette. You can send this message explicitly or by using the capPaletteManual macro.
ms.assetid: 96b6b2d6-084a-411e-8495-ea27e0c4f04f
keywords:
- WM_CAP_PAL_MANUALCREATE message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_PAL_MANUALCREATE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_PAL\_MANUALCREATE message

The **WM\_CAP\_PAL\_MANUALCREATE** message requests that the capture driver manually sample video frames and create a new palette. You can send this message explicitly or by using the [**capPaletteManual**](/windows/desktop/api/Vfw/nf-vfw-cappalettemanual) macro.


```C++
WM_CAP_PAL_MANUALCREATE 
wParam = (WPARAM) (fGrab); 
lParam = (LPARAM) (DWORD) (iColors); 
```



## Parameters

<dl> <dt>

<span id="fGrab"></span><span id="fgrab"></span><span id="FGRAB"></span>*fGrab*
</dt> <dd>

Palette histogram flag. Set this parameter to **TRUE** for each frame included in creating the optimal palette. After the last frame has been collected, set this parameter to **FALSE** to calculate the optimal palette and send it to the capture driver.

</dd> <dt>

<span id="iColors"></span><span id="icolors"></span><span id="ICOLORS"></span>*iColors*
</dt> <dd>

Number of colors in the palette. The maximum value for this parameter is 256. This value is used only during collection of the first frame in a sequence.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** otherwise.

If an error occurs and an error callback function is set using the [**WM\_CAP\_SET\_CALLBACK\_ERROR**](wm-cap-set-callback-error.md) message, the error callback function is called.

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

 

 





