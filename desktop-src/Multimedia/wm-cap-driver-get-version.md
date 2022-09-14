---
title: WM_CAP_DRIVER_GET_VERSION message (Vfw.h)
description: The WM\_CAP\_DRIVER\_GET\_VERSION message returns the version information of the capture driver connected to a capture window. You can send this message explicitly or by using the capDriverGetVersion macro.
ms.assetid: 762ebe7e-0d09-46ea-ab17-86061f0bd8f9
keywords:
- WM_CAP_DRIVER_GET_VERSION message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_DRIVER_GET_VERSION
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_DRIVER\_GET\_VERSION message

The **WM\_CAP\_DRIVER\_GET\_VERSION** message returns the version information of the capture driver connected to a capture window. You can send this message explicitly or by using the [**capDriverGetVersion**](/windows/desktop/api/Vfw/nf-vfw-capdrivergetversion) macro.


```C++
WM_CAP_DRIVER_GET_VERSION 
wParam = (WPARAM) (wSize); 
lParam = (LPARAM) (LPVOID) (LPSTR) (szVer); 
```



## Parameters

<dl> <dt>

<span id="wSize"></span><span id="wsize"></span><span id="WSIZE"></span>*wSize*
</dt> <dd>

Size, in bytes, of the application-defined buffer referenced by**szVer**.

</dd> <dt>

<span id="szVer"></span><span id="szver"></span><span id="SZVER"></span>*szVer*
</dt> <dd>

Pointer to an application-defined buffer used to return the version information as a null-terminated string.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** if the capture window is not connected to a capture driver.

## Remarks

The version information is a text string retrieved from the driver's resource area. Applications should allocate approximately 40 bytes for this string. If version information is not available, a **NULL** string is returned.

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

 

 





