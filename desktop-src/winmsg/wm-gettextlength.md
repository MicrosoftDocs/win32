---
description: Determines the length, in characters, of the text associated with a window.
ms.assetid: 9e185435-a624-4380-adfd-be4f3645ee5d
title: WM_GETTEXTLENGTH message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_GETTEXTLENGTH message

Determines the length, in characters, of the text associated with a window.


```C++
#define WM_GETTEXTLENGTH                0x000E
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used and must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used and must be zero.

</dd> </dl>

## Return value

Type: **LRESULT**

The return value is the length of the text in characters, not including the terminating null character.

## Remarks

For an edit control, the text to be copied is the content of the edit control. For a combo box, the text is the content of the edit control (or static-text) portion of the combo box. For a button, the text is the button name. For other windows, the text is the window title. To determine the length of an item in a list box, an application can use the [**LB\_GETTEXTLEN**](../controls/lb-gettextlen.md) message.

When the **WM\_GETTEXTLENGTH** message is sent, the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function returns the length, in characters, of the text. Under certain conditions, the **DefWindowProc** function returns a value that is larger than the actual length of the text. This occurs with certain mixtures of ANSI and Unicode, and is due to the system allowing for the possible existence of double-byte character set (DBCS) characters within the text. The return value, however, will always be at least as large as the actual length of the text; you can thus always use it to guide buffer allocation. This behavior can occur when an application uses both ANSI functions and common dialogs, which use Unicode.

To obtain the exact length of the text, use the [**WM\_GETTEXT**](wm-gettext.md), [**LB\_GETTEXT**](../controls/lb-gettext.md), or [**CB\_GETLBTEXT**](../controls/cb-getlbtext.md) messages, or the [**GetWindowText**](/windows/win32/api/winuser/nf-winuser-getwindowtexta) function.

Sending a **WM\_GETTEXTLENGTH** message to a non-text static control, such as a static bitmap or static icon controlc, does not return a string value. Instead, it returns zero.

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

[**GetWindowText**](/windows/win32/api/winuser/nf-winuser-getwindowtexta)
</dt> <dt>

[**GetWindowTextLength**](/windows/win32/api/winuser/nf-winuser-getwindowtextlengtha)
</dt> <dt>

[**WM\_GETTEXT**](wm-gettext.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**CB\_GETLBTEXT**](../controls/cb-getlbtext.md)
</dt> <dt>

[**LB\_GETTEXT**](../controls/lb-gettext.md)
</dt> <dt>

[**LB\_GETTEXTLEN**](../controls/lb-gettextlen.md)
</dt> </dl>

 

 
