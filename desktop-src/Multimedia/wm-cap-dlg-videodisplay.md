---
title: WM_CAP_DLG_VIDEODISPLAY message (Vfw.h)
description: The WM\_CAP\_DLG\_VIDEODISPLAY message displays a dialog box in which the user can set or adjust the video output.
ms.assetid: 151056f5-a9d1-4594-a8d7-32d4675ae3d6
keywords:
- WM_CAP_DLG_VIDEODISPLAY message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_DLG_VIDEODISPLAY
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_DLG\_VIDEODISPLAY message

The **WM\_CAP\_DLG\_VIDEODISPLAY** message displays a dialog box in which the user can set or adjust the video output. This dialog box might contain controls that affect the hue, contrast, and brightness of the displayed image, as well as key color alignment. You can send this message explicitly or by using the [**capDlgVideoDisplay**](/windows/desktop/api/Vfw/nf-vfw-capdlgvideodisplay) macro.


```C++
WM_CAP_DLG_VIDEODISPLAY 
wParam = (WPARAM) 0; 
lParam = 0L; 
```



## Return Value

Returns **TRUE** if successful or **FALSE** otherwise.

## Remarks

The controls in this dialog box do not affect digitized video data; they affect only the output or redisplay of the video signal.

The Video Display dialog box is unique for each capture driver. Some capture drivers might not support a Video Display dialog box. Applications can determine if the capture driver supports this message by checking the **fHasDlgVideoDisplay** member of the [**CAPDRIVERCAPS**](/windows/win32/api/vfw/ns-vfw-capdrivercaps) structure.

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

 

 





