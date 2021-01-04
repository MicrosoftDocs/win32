---
title: WM_CAP_FILE_SET_CAPTURE_FILE message (Vfw.h)
description: The WM\_CAP\_FILE\_SET\_CAPTURE\_FILE message names the file used for video capture. You can send this message explicitly or by using the capFileSetCaptureFile macro.
ms.assetid: d96e498b-6322-4d48-a5d7-156e95f23740
keywords:
- WM_CAP_FILE_SET_CAPTURE_FILE message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_FILE_SET_CAPTURE_FILE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_FILE\_SET\_CAPTURE\_FILE message

The **WM\_CAP\_FILE\_SET\_CAPTURE\_FILE** message names the file used for video capture. You can send this message explicitly or by using the [**capFileSetCaptureFile**](/windows/desktop/api/Vfw/nf-vfw-capfilesetcapturefile) macro.


```C++
WM_CAP_FILE_SET_CAPTURE_FILE 
wParam = (WPARAM) 0; 
lParam = (LPARAM) (LPVOID) (LPSTR) (szName); 
```



## Parameters

<dl> <dt>

<span id="szName"></span><span id="szname"></span><span id="SZNAME"></span>*szName*
</dt> <dd>

Pointer to the null-terminated string that contains the name of the capture file to use.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** if the filename is invalid, or if streaming or single-frame capture is in progress.

## Remarks

This message stores the filename in an internal structure. It does not create, allocate, or open the specified file. The default capture filename is C:\\CAPTURE.AVI.

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

 

 





