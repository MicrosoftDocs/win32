---
title: WM_CAP_SET_OVERLAY message (Vfw.h)
description: The WM\_CAP\_SET\_OVERLAY message enables or disables overlay mode. In overlay mode, video is displayed using hardware overlay. You can send this message explicitly or by using the capOverlay macro.
ms.assetid: b74c0619-2b70-46e0-9acd-43d658529233
keywords:
- WM_CAP_SET_OVERLAY message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_SET_OVERLAY
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_SET\_OVERLAY message

The **WM\_CAP\_SET\_OVERLAY** message enables or disables overlay mode. In overlay mode, video is displayed using hardware overlay. You can send this message explicitly or by using the [**capOverlay**](/windows/desktop/api/Vfw/nf-vfw-capoverlay) macro.


```C++
WM_CAP_SET_OVERLAY 
wParam = (WPARAM) (BOOL) (f); 
lParam = 0L; 
```



## Parameters

<dl> <dt>

<span id="f"></span><span id="F"></span>*f*
</dt> <dd>

Overlay flag. Specify **TRUE** for this parameter to enable overlay mode or **FALSE** to disable it.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** otherwise.

## Remarks

Using an overlay does not require CPU resources.

The **fHasOverlay** member of the [**CAPDRIVERCAPS**](/windows/win32/api/vfw/ns-vfw-capdrivercaps) structure indicates whether the device is capable of overlay. The **fOverlayWindow** member of the [**CAPSTATUS**](/windows/win32/api/vfw/ns-vfw-capstatus) structure indicates whether overlay mode is currently enabled.

Enabling overlay mode automatically disables preview mode.

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

 

 





