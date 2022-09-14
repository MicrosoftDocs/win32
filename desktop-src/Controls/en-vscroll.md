---
title: EN_VSCROLL notification code (Winuser.h)
description: Sent when the user clicks an edit control's vertical scroll bar or when the user scrolls the mouse wheel over the edit control.
ms.assetid: 46307dee-3c5c-4020-9c2b-ec4638a0cea5
keywords:
- EN_VSCROLL notification code Windows Controls
topic_type:
- apiref
api_name:
- EN_VSCROLL
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EN\_VSCROLL notification code

Sent when the user clicks an edit control's vertical scroll bar or when the user scrolls the mouse wheel over the edit control. The parent window of the edit control receives this notification code through a [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message. The parent window is notified before the screen is updated.


```C++
EN_VSCROLL

    WPARAM wParam;
    LPARAM lParam;
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) contains the identifier of the edit control. The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) specifies the notification code.

</dd> <dt>

*lParam* 
</dt> <dd>

A handle to the edit control.

</dd> </dl>

## Remarks

This message is sent for the following mouse events on the vertical scroll bar: clicking either arrow button or clicking between the arrow button and the thumb. However, the message is not sent when clicking the scroll bar mouse itself. The message is also sent when a keyboard event causes a change in the view area of the edit control, for example, pressing HOME, END, PAGE UP, PAGE DOWN, UP ARROW, or DOWN ARROW.

The mouse wheel is a mouse that has a center wheel that scrolls. For more information, see "The Mouse Wheel" in [About Mouse Input](/windows/desktop/inputdev/about-mouse-input).

**Rich Edit:** Supported in Microsoft Rich Edit 1.0 and later. To receive EN\_VSCROLL notification codes, specify [**ENM\_SCROLL**](rich-edit-control-event-mask-flags.md) in the mask sent with the [**EM\_SETEVENTMASK**](em-seteventmask.md) message. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

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

[EN\_HSCROLL](en-hscroll.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Using Edit Controls](using-edit-controls.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**WM\_COMMAND**](/windows/desktop/menurc/wm-command)
</dt> </dl>

 

