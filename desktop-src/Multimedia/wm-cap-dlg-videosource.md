---
title: WM\_CAP\_DLG\_VIDEOSOURCE message
description: The WM\_CAP\_DLG\_VIDEOSOURCE message displays a dialog box in which the user can control the video source.
ms.assetid: 8dc2f271-1f48-4e63-badf-9f3322063018
keywords:
- WM_CAP_DLG_VIDEOSOURCE message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_DLG_VIDEOSOURCE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WM\_CAP\_DLG\_VIDEOSOURCE message

The **WM\_CAP\_DLG\_VIDEOSOURCE** message displays a dialog box in which the user can control the video source. The Video Source dialog box might contain controls that select input sources; alter the hue, contrast, brightness of the image; and modify the video quality before digitizing the images into the frame buffer. You can send this message explicitly or by using the [**capDlgVideoSource**](/windows/win32/Vfw/nf-vfw-capdlgvideosource?branch=master) macro.


```C++
WM_CAP_DLG_VIDEOSOURCE 
wParam = (WPARAM) 0; 
lParam = 0L; 
```



## Return Value

Returns **TRUE** if successful or **FALSE** otherwise.

## Remarks

The Video Source dialog box is unique for each capture driver. Some capture drivers might not support a Video Source dialog box. Applications can determine if the capture driver supports this message by checking the **fHasDlgVideoSource** member of the [**CAPDRIVERCAPS**](/windows/win32/Vfw/ns-vfw-tagcapdrivercaps?branch=master) structure.

## Requirements



|                                     |                                                                                  |
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

 

 





