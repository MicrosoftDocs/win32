---
title: WM_CAP_FILE_ALLOCATE message (Vfw.h)
description: The WM\_CAP\_FILE\_ALLOCATE message creates (preallocates) a capture file of a specified size. You can send this message explicitly or by using the capFileAlloc macro.
ms.assetid: 31ebe824-4a30-4212-9479-a5cbd8fc1e1d
keywords:
- WM_CAP_FILE_ALLOCATE message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_FILE_ALLOCATE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_FILE\_ALLOCATE message

The **WM\_CAP\_FILE\_ALLOCATE** message creates (preallocates) a capture file of a specified size. You can send this message explicitly or by using the [**capFileAlloc**](/windows/desktop/api/Vfw/nf-vfw-capfilealloc) macro.


```C++
WM_CAP_FILE_ALLOCATE 
wParam = (WPARAM) 0; 
lParam = (LPARAM) (DWORD) (dwSize); 
```



## Parameters

<dl> <dt>

<span id="dwSize"></span><span id="dwsize"></span><span id="DWSIZE"></span>*dwSize*
</dt> <dd>

Size, in bytes, to create the capture file.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** otherwise.

If an error occurs and an error callback function is set using the [**WM\_CAP\_SET\_CALLBACK\_ERROR**](wm-cap-set-callback-error.md) message, the error callback function is called.

## Remarks

You can improve streaming capture performance significantly by preallocating a capture file large enough to store an entire video clip and by defragmenting the capture file before capturing the clip.

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

 

 





