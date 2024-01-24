---
title: WM_CAP_FILE_GET_CAPTURE_FILE message (Vfw.h)
description: The WM\_CAP\_FILE\_GET\_CAPTURE\_FILE message returns the name of the current capture file. You can send this message explicitly or by using the capFileGetCaptureFile macro.
ms.assetid: 86ce2904-834d-449f-9ef8-5a158c55bbaa
keywords:
- WM_CAP_FILE_GET_CAPTURE_FILE message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_FILE_GET_CAPTURE_FILE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_FILE\_GET\_CAPTURE\_FILE message

The **WM\_CAP\_FILE\_GET\_CAPTURE\_FILE** message returns the name of the current capture file. You can send this message explicitly or by using the [**capFileGetCaptureFile**](/windows/desktop/api/Vfw/nf-vfw-capfilegetcapturefile) macro.


```C++
WM_CAP_FILE_GET_CAPTURE_FILE 
wParam = (WPARAM) (wSize); 
lParam = (LPARAM) (LPVOID) (LPSTR) (szName); 
```



## Parameters

<dl> <dt>

<span id="wSize"></span><span id="wsize"></span><span id="WSIZE"></span>*wSize*
</dt> <dd>

Size, in bytes, of the application-defined buffer referenced by**szName**.

</dd> <dt>

<span id="szName"></span><span id="szname"></span><span id="SZNAME"></span>*szName*
</dt> <dd>

Pointer to an application-defined buffer used to return the name of the capture file as a null-terminated string.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** otherwise.

## Remarks

The default capture filename is C:\\CAPTURE.AVI.

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

 

 





