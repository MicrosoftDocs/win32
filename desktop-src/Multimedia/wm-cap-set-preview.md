---
title: WM_CAP_SET_PREVIEW message (Vfw.h)
description: The WM\_CAP\_SET\_PREVIEW message enables or disables preview mode.
ms.assetid: ef6218d6-4fff-469f-b2e0-d7990998a3e5
keywords:
- WM_CAP_SET_PREVIEW message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_SET_PREVIEW
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_SET\_PREVIEW message

The **WM\_CAP\_SET\_PREVIEW** message enables or disables preview mode. In preview mode, frames are transferred from the capture hardware to system memory and then displayed in the capture window using GDI functions. You can send this message explicitly or by using the [**capPreview**](/windows/desktop/api/Vfw/nf-vfw-cappreview) macro.


```C++
WM_CAP_SET_PREVIEW 
wParam = (WPARAM) (BOOL) (f); 
lParam = 0L; 
```



## Parameters

<dl> <dt>

<span id="f"></span><span id="F"></span>*f*
</dt> <dd>

Preview flag. Specify **TRUE** for this parameter to enable preview mode or **FALSE** to disable it.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** otherwise.

## Remarks

The preview mode uses substantial CPU resources. Applications can disable preview or lower the preview rate when another application has the focus. The **fLiveWindow** member of the [**CAPSTATUS**](/windows/win32/api/vfw/ns-vfw-capstatus) structure indicates if preview mode is currently enabled.

Enabling preview mode automatically disables overlay mode.

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

 

 





