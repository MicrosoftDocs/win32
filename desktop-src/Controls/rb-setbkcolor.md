---
title: RB_SETBKCOLOR message (Commctrl.h)
description: Sets a rebar control's default background color.
ms.assetid: 450a1e16-24f6-4f86-8e46-14009da05efc
keywords:
- RB_SETBKCOLOR message Windows Controls
topic_type:
- apiref
api_name:
- RB_SETBKCOLOR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RB\_SETBKCOLOR message

Sets a rebar control's default background color.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

[**COLORREF**](/windows/desktop/gdi/colorref) value that represents the new default background color.

</dd> </dl>

## Return value

Returns a [**COLORREF**](/windows/desktop/gdi/colorref) value that represents the previous default background color.

## Remarks

The rebar control's default background color is used to draw the background in a rebar control and all bands that are added after this message has been sent. The default background color for a particular band can be overridden when a band is added or modified by setting the RBBIM\_COLORS flag in **fMask** and setting **clrBack** in the [**REBARBANDINFO**](/windows/win32/api/commctrl/ns-commctrl-rebarbandinfoa) structure.

When visual styles are enabled, this message has no effect.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**RB\_GETBKCOLOR**](rb-getbkcolor.md)
</dt> </dl>

 

