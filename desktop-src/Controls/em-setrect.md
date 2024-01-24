---
title: EM_SETRECT message (Winuser.h)
description: EM_SETRECT message - Sets the formatting rectangle of a multiline edit control.
ms.assetid: 4f576e94-3bd3-4416-a960-b7f22da963ea
keywords:
- EM_SETRECT message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETRECT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETRECT message

Sets the [formatting rectangle](about-edit-controls.md) of a multiline edit control. The formatting rectangle is the limiting rectangle into which the control draws the text. The limiting rectangle is independent of the size of the edit control window.

This message is processed only by multiline edit controls. You can send this message to either an edit control or a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

**Rich Edit 2.0 and later:** Indicates whether *lParam* specifies absolute or relative coordinates. A value of zero indicates absolute coordinates. A value of 1 indicates offsets relative to the current formatting rectangle. (The offsets can be positive or negative.)

**Edit controls and Rich Edit 1.0:** This parameter is not used and must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**RECT**](/windows/win32/api/windef/ns-windef-rect) structure that specifies the new dimensions of the rectangle. If this parameter is **NULL**, the formatting rectangle is set to its default values.

</dd> </dl>

## Return value

This message does not return a value.

## Remarks

Setting *lParam* to **NULL** has no effect if a touch device is installed, or if **EM\_SETRECT** is sent from a thread that has a hook installed (see [**SetWindowsHookEx**](/windows/desktop/api/winuser/nf-winuser-setwindowshookexa)). In these cases, *lParam* should contain a valid pointer to a [**RECT**](/windows/win32/api/windef/ns-windef-rect) structure.

The **EM\_SETRECT** message causes the text of the edit control to be redrawn. To change the size of the formatting rectangle without redrawing the text, use the [**EM\_SETRECTNP**](em-setrectnp.md) message.

When an edit control is first created, the formatting rectangle is set to a default size. You can use the **EM\_SETRECT** message to make the formatting rectangle larger or smaller than the edit control window.

If the edit control does not have a horizontal scroll bar, and the formatting rectangle is set to be larger than the edit control window, lines of text exceeding the width of the edit control window (but smaller than the width of the formatting rectangle) are clipped instead of wrapped.

If the edit control contains a border, the formatting rectangle is reduced by the size of the border. If you are adjusting the rectangle returned by an [**EM\_GETRECT**](em-getrect.md) message, you must remove the size of the border before using the rectangle with the **EM\_SETRECT** message.

**Rich Edit:** Supported in Microsoft Rich Edit 1.0 and later. The formatting rectangle does not include the selection bar, which is an unmarked area to the left of each paragraph. When the user clicks in the selection bar, the corresponding line is selected. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

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

[**EM\_GETRECT**](em-getrect.md)
</dt> <dt>

[**EM\_SETRECTNP**](em-setrectnp.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**RECT**](/windows/win32/api/windef/ns-windef-rect)
</dt> </dl>

 

