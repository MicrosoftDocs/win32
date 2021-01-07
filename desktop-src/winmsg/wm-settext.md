---
description: Sets the text of a window.
ms.assetid: 1b48c309-6903-4139-bf42-e8526963e681
title: WM_SETTEXT message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_SETTEXT message

Sets the text of a window.


```C++
#define WM_SETTEXT                      0x000C
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a null-terminated string that is the window text.

</dd> </dl>

## Return value

Type: **LRESULT**

The return value is **TRUE** if the text is set. It is **FALSE** (for an edit control), **LB\_ERRSPACE** (for a list box), or **CB\_ERRSPACE** (for a combo box) if insufficient space is available to set the text in the edit control. It is **CB\_ERR** if this message is sent to a combo box without an edit control.

## Remarks

The [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function sets and displays the window text. For an edit control, the text is the contents of the edit control. For a combo box, the text is the contents of the edit-control portion of the combo box. For a button, the text is the button name. For other windows, the text is the window title.

This message does not change the current selection in the list box of a combo box. An application should use the [**CB\_SELECTSTRING**](../controls/cb-selectstring.md) message to select the item in a list box that matches the text in the edit control.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca)
</dt> <dt>

[**WM\_GETTEXT**](wm-gettext.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**CB\_SELECTSTRING**](../controls/cb-selectstring.md)
</dt> </dl>

 

 
