---
title: WM_CAP_SET_USER_DATA message (Vfw.h)
description: The WM\_CAP\_SET\_USER\_DATA message associates a LONG\_PTR data value with a capture window. You can send this message explicitly or by using the capSetUserData macro.
ms.assetid: 067502e3-f009-4cf2-b612-4a0b64624416
keywords:
- WM_CAP_SET_USER_DATA message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_SET_USER_DATA
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_SET\_USER\_DATA message

The **WM\_CAP\_SET\_USER\_DATA** message associates a **LONG\_PTR** data value with a capture window. You can send this message explicitly or by using the [**capSetUserData**](/windows/desktop/api/Vfw/nf-vfw-capsetuserdata) macro.


```C++
WM_CAP_SET_USER_DATA 
wParam = (WPARAM) 0; 
lParam = (LPARAM)lUser; 
```



## Parameters

<dl> <dt>

<span id="lUser"></span><span id="luser"></span><span id="LUSER"></span>*lUser*
</dt> <dd>

Data value to associate with a capture window.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** if streaming capture is in progress.

## Remarks

Typically this message is used to point to a block of data associated with a capture window.

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

 

 





