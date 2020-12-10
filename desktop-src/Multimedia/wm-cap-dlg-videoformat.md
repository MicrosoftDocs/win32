---
title: WM_CAP_DLG_VIDEOFORMAT message (Vfw.h)
description: The WM\_CAP\_DLG\_VIDEOFORMAT message displays a dialog box in which the user can select the video format.
ms.assetid: 3b44507e-3806-467f-877a-e9992d1337cb
keywords:
- WM_CAP_DLG_VIDEOFORMAT message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_DLG_VIDEOFORMAT
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_DLG\_VIDEOFORMAT message

The **WM\_CAP\_DLG\_VIDEOFORMAT** message displays a dialog box in which the user can select the video format. The Video Format dialog box might be used to select image dimensions, bit depth, and hardware compression options. You can send this message explicitly or by using the [**capDlgVideoFormat**](/windows/desktop/api/Vfw/nf-vfw-capdlgvideoformat) macro.


```C++
WM_CAP_DLG_VIDEOFORMAT 
wParam = (WPARAM) 0; 
lParam = 0L; 
```



## Return Value

Returns **TRUE** if successful or **FALSE** otherwise.

## Remarks

After this message returns, applications might need to update the [**CAPSTATUS**](/windows/win32/api/vfw/ns-vfw-capstatus) structure because the user might have changed the image dimensions.

The Video Format dialog box is unique for each capture driver. Some capture drivers might not support a Video Format dialog box. Applications can determine if the capture driver supports this message by checking the **fHasDlgVideoFormat** member of [**CAPDRIVERCAPS**](/windows/win32/api/vfw/ns-vfw-capdrivercaps).

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

 

 





