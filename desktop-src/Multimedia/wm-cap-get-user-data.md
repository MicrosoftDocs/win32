---
title: WM_CAP_GET_USER_DATA message (Vfw.h)
description: The WM\_CAP\_GET\_USER\_DATA message retrieves a LONG\_PTR data value associated with a capture window. You can send this message explicitly or by using the capGetUserData macro.
ms.assetid: f7c121ba-44a1-4916-b602-c53d8332c2af
keywords:
- WM_CAP_GET_USER_DATA message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_GET_USER_DATA
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_GET\_USER\_DATA message

The **WM\_CAP\_GET\_USER\_DATA** message retrieves a **LONG\_PTR** data value associated with a capture window. You can send this message explicitly or by using the [**capGetUserData**](/windows/desktop/api/Vfw/nf-vfw-capgetuserdata) macro.


```C++
WM_CAP_GET_USER_DATA 
wParam = (WPARAM) 0; 
lParam = 0L; 
```



## Return Value

Returns a value previously saved by using the [**WM\_CAP\_SET\_USER\_DATA**](wm-cap-set-user-data.md) message.

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

 

 





