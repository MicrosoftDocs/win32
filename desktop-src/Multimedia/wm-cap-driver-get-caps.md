---
title: WM_CAP_DRIVER_GET_CAPS message (Vfw.h)
description: The WM\_CAP\_DRIVER\_GET\_CAPS message returns the hardware capabilities of the capture driver currently connected to a capture window. You can send this message explicitly or by using the capDriverGetCaps macro.
ms.assetid: 898a800c-1109-47cd-bcc9-cb61d86a4a2e
keywords:
- WM_CAP_DRIVER_GET_CAPS message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_DRIVER_GET_CAPS
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_DRIVER\_GET\_CAPS message

The **WM\_CAP\_DRIVER\_GET\_CAPS** message returns the hardware capabilities of the capture driver currently connected to a capture window. You can send this message explicitly or by using the [**capDriverGetCaps**](/windows/desktop/api/Vfw/nf-vfw-capdrivergetcaps) macro.


```C++
WM_CAP_DRIVER_GET_CAPS 
wParam = (WPARAM) (wSize); 
lParam = (LPARAM) (LPVOID) (LPCAPDRIVERCAPS) (psCaps); 
```



## Parameters

<dl> <dt>

<span id="wSize"></span><span id="wsize"></span><span id="WSIZE"></span>*wSize*
</dt> <dd>

Size, in bytes, of the structure referenced by**s**.

</dd> <dt>

<span id="psCaps"></span><span id="pscaps"></span><span id="PSCAPS"></span>*psCaps*
</dt> <dd>

Pointer to the [**CAPDRIVERCAPS**](/windows/win32/api/vfw/ns-vfw-capdrivercaps) structure to contain the hardware capabilities.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** if the capture window is not connected to a capture driver.

## Remarks

The capabilities returned in [**CAPDRIVERCAPS**](/windows/win32/api/vfw/ns-vfw-capdrivercaps) are constant for a given capture driver. Applications need to retrieve this information once when the capture driver is first connected to a capture window.

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

 

 





