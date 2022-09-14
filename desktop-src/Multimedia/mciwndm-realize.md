---
title: MCIWNDM_REALIZE message (Vfw.h)
description: The MCIWNDM\_REALIZE message realizes the palette currently used by the MCI device in an MCIWnd window. This macro is defined with the MCIWNDM\_REALIZE message. You can send this message explicitly or by using the MCIWndRealize macro.
ms.assetid: fe8803b5-3500-44b4-97f7-784bedf0b362
keywords:
- MCIWNDM_REALIZE message Windows Multimedia
topic_type:
- apiref
api_name:
- MCIWNDM_REALIZE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCIWNDM\_REALIZE message

The **MCIWNDM\_REALIZE** message realizes the palette currently used by the MCI device in an MCIWnd window. This macro is defined with the **MCIWNDM\_REALIZE** message. You can send this message explicitly or by using the [**MCIWndRealize**](/windows/desktop/api/Vfw/nf-vfw-mciwndrealize) macro.


```C++
MCIWNDM_REALIZE 
wParam = (WPARAM) (BOOL) fBkgnd; 
lParam = 0; 
```



## Parameters

<dl> <dt>

<span id="fBkgnd"></span><span id="fbkgnd"></span><span id="FBKGND"></span>*fBkgnd*
</dt> <dd>

Background flag. Specify **TRUE** for this parameter if the window is a background application.

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

**MCIWNDM\_REALIZE** uses the palette of the MCI device and calls the [**RealizePalette**](/windows/desktop/api/wingdi/nf-wingdi-realizepalette) function. If your application explicitly handles the [**WM\_PALETTECHANGED**](/windows/desktop/gdi/wm-palettechanged) and [**WM\_QUERYNEWPALETTE**](/windows/desktop/gdi/wm-querynewpalette) messages, you should use this message in your application instead of using **RealizePalette**. If the body of one of these message handlers contains only **RealizePalette**, forward the message to the MCIWnd window, which will automatically realize the palette.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndRealize**](/windows/desktop/api/Vfw/nf-vfw-mciwndrealize)
</dt> <dt>

[**RealizePalette**](/windows/desktop/api/wingdi/nf-wingdi-realizepalette)
</dt> <dt>

[**WM\_PALETTECHANGED**](/windows/desktop/gdi/wm-palettechanged)
</dt> <dt>

[**WM\_QUERYNEWPALETTE**](/windows/desktop/gdi/wm-querynewpalette)
</dt> </dl>

 

