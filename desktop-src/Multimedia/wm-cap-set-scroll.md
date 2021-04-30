---
title: WM_CAP_SET_SCROLL message (Vfw.h)
description: The WM\_CAP\_SET\_SCROLL message defines the portion of the video frame to display in the capture window.
ms.assetid: 545605e4-6b1f-403a-a3ab-0fd6750ae776
keywords:
- WM_CAP_SET_SCROLL message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_SET_SCROLL
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_SET\_SCROLL message

The **WM\_CAP\_SET\_SCROLL** message defines the portion of the video frame to display in the capture window. This message sets the upper left corner of the client area of the capture window to the coordinates of a specified pixel within the video frame. You can send this message explicitly or by using the [**capSetScrollPos**](/windows/desktop/api/Vfw/nf-vfw-capsetscrollpos) macro.


```C++
WM_CAP_SET_SCROLL 
wParam = (WPARAM) 0; 
lParam = (LPARAM) (LPPOINT) (lpP); 
```



## Parameters

<dl> <dt>

<span id="lpP"></span><span id="lpp"></span><span id="LPP"></span>*lpP*
</dt> <dd>

Address to contain the desired scroll position.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** otherwise.

## Remarks

The scroll position affects the image in both preview and overlay modes.

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

 

 





