---
title: WM\_DWMCOLORIZATIONCOLORCHANGED message
description: Informs all top-level windows that the colorization color has changed.
ms.assetid: '6118d41b-f0b4-4034-aa98-d8757f18ca0d'
keywords: ["WM_DWMCOLORIZATIONCOLORCHANGED message Desktop Window Manager"]
topic_type:
- apiref
api_name:
- WM_DWMCOLORIZATIONCOLORCHANGED
api_location:
- Winuser.h
api_type:
- HeaderDef
---

# WM\_DWMCOLORIZATIONCOLORCHANGED message

Informs all top-level windows that the colorization color has changed.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the new colorization color. The color format is 0xAARRGGBB.

</dd> <dt>

*lParam* 
</dt> <dd>

Specifies whether the new color is blended with opacity.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Remarks

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633573) function.

[**DwmGetColorizationColor**](dwmgetcolorizationcolor.md) is used to determine the current color value.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Winuser.h</dt> </dl> |



 

 





