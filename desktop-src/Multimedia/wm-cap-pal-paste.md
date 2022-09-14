---
title: WM_CAP_PAL_PASTE message (Vfw.h)
description: The WM\_CAP\_PAL\_PASTE message copies the palette from the clipboard and passes it to a capture driver. You can send this message explicitly or by using the capPalettePaste macro.
ms.assetid: d49c7fd9-be40-4a07-8339-b85f7c4c331e
keywords:
- WM_CAP_PAL_PASTE message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_PAL_PASTE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_PAL\_PASTE message

The **WM\_CAP\_PAL\_PASTE** message copies the palette from the clipboard and passes it to a capture driver. You can send this message explicitly or by using the [**capPalettePaste**](/windows/desktop/api/Vfw/nf-vfw-cappalettepaste) macro.


```C++
WM_CAP_PAL_PASTE 
wParam = (WPARAM) 0; 
lParam = 0L; 
```



## Return Value

Returns **TRUE** if successful or **FALSE** otherwise.

If an error occurs and an error callback function is set using the [**WM\_CAP\_SET\_CALLBACK\_ERROR**](wm-cap-set-callback-error.md) message, the error callback function is called.

## Remarks

A capture driver uses a palette when required by the specified digitized video format.

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

 

 





