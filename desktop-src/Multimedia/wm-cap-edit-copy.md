---
title: WM_CAP_EDIT_COPY message (Vfw.h)
description: The WM\_CAP\_EDIT\_COPY message copies the contents of the video frame buffer and associated palette to the clipboard. You can send this message explicitly or by using the capEditCopy macro.
ms.assetid: 16f1dd7d-af4d-4096-add8-eec5f0a0607f
keywords:
- WM_CAP_EDIT_COPY message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_EDIT_COPY
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_EDIT\_COPY message

The **WM\_CAP\_EDIT\_COPY** message copies the contents of the video frame buffer and associated palette to the clipboard. You can send this message explicitly or by using the [**capEditCopy**](/windows/desktop/api/Vfw/nf-vfw-capeditcopy) macro.


```C++
WM_CAP_EDIT_COPY 
wParam = (WPARAM) 0; 
lParam = 0L; 
```



## Return Value

Returns **TRUE** if successful or **FALSE** otherwise.

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

 

 





