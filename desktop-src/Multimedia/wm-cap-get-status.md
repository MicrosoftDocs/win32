---
title: WM_CAP_GET_STATUS message (Vfw.h)
description: The WM\_CAP\_GET\_STATUS message retrieves the status of the capture window. You can send this message explicitly or by using the capGetStatus macro.
ms.assetid: 31349599-a52c-45ba-8f08-91008773f317
keywords:
- WM_CAP_GET_STATUS message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_GET_STATUS
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_GET\_STATUS message

The **WM\_CAP\_GET\_STATUS** message retrieves the status of the capture window. You can send this message explicitly or by using the [**capGetStatus**](/windows/desktop/api/Vfw/nf-vfw-capgetstatus) macro.


```C++
WM_CAP_GET_STATUS 
wParam = (WPARAM) (wSize); 
lParam = (LPARAM) (LPVOID) (LPCAPSTATUS) (s); 
```



## Parameters

<dl> <dt>

<span id="wSize"></span><span id="wsize"></span><span id="WSIZE"></span>*wSize*
</dt> <dd>

Size, in bytes, of the structure referenced by**s**.

</dd> <dt>

<span id="s"></span><span id="S"></span>*s*
</dt> <dd>

Pointer to a [**CAPSTATUS**](/windows/win32/api/vfw/ns-vfw-capstatus) structure.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** if the capture window is not connected to a capture driver.

## Remarks

The [**CAPSTATUS**](/windows/win32/api/vfw/ns-vfw-capstatus) structure contains the current state of the capture window. Since this state is dynamic and changes in response to various messages, the application should initialize this structure after sending the [**WM\_CAP\_DLG\_VIDEOFORMAT**](wm-cap-dlg-videoformat.md) message (or using the [**capDlgVideoFormat**](/windows/desktop/api/Vfw/nf-vfw-capdlgvideoformat) macro) and whenever it needs to enable menu items or determine the actual state of the window.

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

 

 





