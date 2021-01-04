---
title: WM_CAP_PAL_SAVE message (Vfw.h)
description: The WM\_CAP\_PAL\_SAVE message saves the current palette to a palette file. Palette files typically use the filename extension .PAL. You can send this message explicitly or by using the capPaletteSave macro.
ms.assetid: b1fa3978-9147-403f-aa08-db1a803aa5ac
keywords:
- WM_CAP_PAL_SAVE message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_PAL_SAVE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_PAL\_SAVE message

The **WM\_CAP\_PAL\_SAVE** message saves the current palette to a palette file. Palette files typically use the filename extension .PAL. You can send this message explicitly or by using the [**capPaletteSave**](/windows/desktop/api/Vfw/nf-vfw-cappalettesave) macro.


```C++
WM_CAP_PAL_SAVE 
wParam = (WPARAM) 0; 
lParam = (LPARAM) (LPVOID) (LPSTR) (szName); 
```



## Parameters

<dl> <dt>

<span id="szName"></span><span id="szname"></span><span id="SZNAME"></span>*szName*
</dt> <dd>

Pointer to a null-terminated string containing the palette filename.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** otherwise.

If an error occurs and an error callback function is set using the [**WM\_CAP\_SET\_CALLBACK\_ERROR**](wm-cap-set-callback-error.md) message, the error callback function is called.

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

 

 





