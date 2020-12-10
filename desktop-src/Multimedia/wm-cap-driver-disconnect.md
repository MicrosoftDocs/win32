---
title: WM_CAP_DRIVER_DISCONNECT message (Vfw.h)
description: The WM\_CAP\_DRIVER\_DISCONNECT message disconnects a capture driver from a capture window. You can send this message explicitly or by using the capDriverDisconnect macro.
ms.assetid: a420f24a-aa7d-4788-9120-2c11e5e2c14c
keywords:
- WM_CAP_DRIVER_DISCONNECT message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_DRIVER_DISCONNECT
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_DRIVER\_DISCONNECT message

The **WM\_CAP\_DRIVER\_DISCONNECT** message disconnects a capture driver from a capture window. You can send this message explicitly or by using the [**capDriverDisconnect**](/windows/desktop/api/Vfw/nf-vfw-capdriverdisconnect) macro.


```C++
WM_CAP_DRIVER_DISCONNECT 
wParam = (WPARAM) 0; 
lParam = 0L; 
```



## Return Value

Returns **TRUE** if successful or **FALSE** if the capture window is not connected to a capture driver.

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

 

 





