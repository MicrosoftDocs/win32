---
title: WM_CAP_GET_VIDEOFORMAT message (Vfw.h)
description: The WM\_CAP\_GET\_VIDEOFORMAT message retrieves a copy of the video format in use or the size required for the video format. You can send this message explicitly or by using the capGetVideoFormat and capGetVideoFormatSize macros.
ms.assetid: ac72dfdb-fe1a-4007-bdce-41e5e67d076a
keywords:
- WM_CAP_GET_VIDEOFORMAT message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_GET_VIDEOFORMAT
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_GET\_VIDEOFORMAT message

The **WM\_CAP\_GET\_VIDEOFORMAT** message retrieves a copy of the video format in use or the size required for the video format. You can send this message explicitly or by using the [**capGetVideoFormat**](/windows/desktop/api/Vfw/nf-vfw-capgetvideoformat) and [**capGetVideoFormatSize**](/windows/desktop/api/Vfw/nf-vfw-capgetvideoformatsize) macros.


```C++
WM_CAP_GET_VIDEOFORMAT 
wParam = (WPARAM) (wSize); 
lParam = (LPARAM) (LPVOID) (psVideoFormat); 
```



## Parameters

<dl> <dt>

<span id="wSize"></span><span id="wsize"></span><span id="WSIZE"></span>*wSize*
</dt> <dd>

Size, in bytes, of the structure referenced by**s**.

</dd> <dt>

<span id="psVideoFormat"></span><span id="psvideoformat"></span><span id="PSVIDEOFORMAT"></span>*psVideoFormat*
</dt> <dd>

Pointer to a [**BITMAPINFO**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfo) structure. You can also specify **NULL** to retrieve the number of bytes needed.

</dd> </dl>

## Return Value

Returns the size, in bytes, of the video format or zero if the capture window is not connected to a capture driver. For video formats that require a palette, the current palette is also returned.

## Remarks

Because compressed video formats vary in size requirements applications must first retrieve the size, then allocate memory, and finally request the video format data.

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

 

