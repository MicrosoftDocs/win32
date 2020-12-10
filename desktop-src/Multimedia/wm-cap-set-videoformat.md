---
title: WM_CAP_SET_VIDEOFORMAT message (Vfw.h)
description: The WM\_CAP\_SET\_VIDEOFORMAT message sets the format of captured video data. You can send this message explicitly or by using the capSetVideoFormat macro.
ms.assetid: 4f9cf90d-7ccb-4fc7-aad5-3d7e082526be
keywords:
- WM_CAP_SET_VIDEOFORMAT message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_SET_VIDEOFORMAT
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_SET\_VIDEOFORMAT message

The **WM\_CAP\_SET\_VIDEOFORMAT** message sets the format of captured video data. You can send this message explicitly or by using the [**capSetVideoFormat**](/windows/desktop/api/Vfw/nf-vfw-capsetvideoformat) macro.


```C++
WM_CAP_SET_VIDEOFORMAT 
wParam = (WPARAM) (wSize); 
lParam = (LPARAM) (LPVOID) (psVideoFormat); 
```



## Parameters

<dl> <dt>

<span id="wSize"></span><span id="wsize"></span><span id="WSIZE"></span>*wSize*
</dt> <dd>

Size, in bytes, of the structure referenced by **s**.

</dd> <dt>

<span id="psVideoFormat"></span><span id="psvideoformat"></span><span id="PSVIDEOFORMAT"></span>*psVideoFormat*
</dt> <dd>

Pointer to a [**BITMAPINFO**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfo) structure.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** otherwise.

## Remarks

Because video formats are device-specific, applications should check the return value from this function to determine if the format is accepted by the driver.

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

 

