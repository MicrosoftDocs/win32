---
title: BM_SETSTATE message (Winuser.h)
description: Sets the highlight state of a button. The highlight state indicates whether the button is highlighted as if the user had pushed it. You can send this message explicitly or use the Button\_SetState macro.
ms.assetid: 675ebe8d-b381-46ca-b328-ebe9f25d864a
keywords:
- BM_SETSTATE message Windows Controls
topic_type:
- apiref
api_name:
- BM_SETSTATE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# BM\_SETSTATE message

Sets the highlight state of a button. The highlight state indicates whether the button is highlighted as if the user had pushed it. You can send this message explicitly or use the [**Button\_SetState**](/windows/desktop/api/Windowsx/nf-windowsx-button_setstate) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A **BOOL** that specifies whether the button is highlighted. A value of **TRUE** highlights the button. A value of **FALSE** removes any highlighting.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used.

</dd> </dl>

## Return value

This message always returns zero.

## Remarks

Highlighting affects only the appearance of a button. It has no effect on the check state of a radio button or check box.

A button is automatically highlighted when the user positions the cursor over it and presses and holds the left mouse button. The highlighting is removed when the user releases the mouse button.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**BM\_GETSTATE**](bm-getstate.md)
</dt> <dt>

[**BM\_SETCHECK**](bm-setcheck.md)
</dt> </dl>

 

 





