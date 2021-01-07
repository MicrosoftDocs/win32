---
description: Copies the text that corresponds to a window into a buffer provided by the caller.
ms.assetid: 117c3d6d-24cd-462f-bdb0-b65d8914273a
title: WM_GETTEXT message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_GETTEXT message

Copies the text that corresponds to a window into a buffer provided by the caller.


```C++
#define WM_GETTEXT                      0x000D
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The maximum number of characters to be copied, including the terminating null character.

ANSI applications may have the string in the buffer reduced in size (to a minimum of half that of the *wParam* value) due to conversion from ANSI to Unicode.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to the buffer that is to receive the text.

</dd> </dl>

## Return value

Type: **LRESULT**

The return value is the number of characters copied, not including the terminating null character.

## Remarks

The [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function copies the text associated with the window into the specified buffer and returns the number of characters copied. Note, for non-text static controls this gives you the text with which the control was originally created, that is, the ID number. However, it gives you the ID of the non-text static control as originally created. That is, if you subsequently used a **STM\_SETIMAGE** to change it the original ID would still be returned.

For an edit control, the text to be copied is the content of the edit control. For a combo box, the text is the content of the edit control (or static-text) portion of the combo box. For a button, the text is the button name. For other windows, the text is the window title. To copy the text of an item in a list box, an application can use the [**LB\_GETTEXT**](../controls/lb-gettext.md) message.

When the **WM\_GETTEXT** message is sent to a static control with the **SS\_ICON** style, a handle to the icon will be returned in the first four bytes of the buffer pointed to by *lParam*. This is true only if the [**WM\_SETTEXT**](wm-settext.md) message has been used to set the icon.

**Rich Edit:** If the text to be copied exceeds 64K, use either the [**EM\_STREAMOUT**](../controls/em-streamout.md) or [**EM\_GETSELTEXT**](../controls/em-getseltext.md) message.

Sending a **WM\_GETTEXT** message to a non-text static control, such as a static bitmap or static icon control, does not return a string value. Instead, it returns zero. In addition, in early versions of Windows, applications could send a **WM\_GETTEXT** message to a non-text static control to retrieve the control's ID. To retrieve a control's ID, applications can use [**GetWindowLong**](/windows/win32/api/winuser/nf-winuser-getwindowlonga) passing **GWL\_ID** as the index value or [**GetWindowLongPtr**](/windows/win32/api/winuser/nf-winuser-getwindowlongptra) using **GWLP\_ID**.

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

[**GetWindowLong**](/windows/win32/api/winuser/nf-winuser-getwindowlonga)
</dt> <dt>

[**GetWindowLongPtr**](/windows/win32/api/winuser/nf-winuser-getwindowlongptra)
</dt> <dt>

[**GetWindowText**](/windows/win32/api/winuser/nf-winuser-getwindowtexta)
</dt> <dt>

[**GetWindowTextLength**](/windows/win32/api/winuser/nf-winuser-getwindowtextlengtha)
</dt> <dt>

[**WM\_GETTEXTLENGTH**](wm-gettextlength.md)
</dt> <dt>

[**WM\_SETTEXT**](wm-settext.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**EM\_GETSELTEXT**](../controls/em-getseltext.md)
</dt> <dt>

[**EM\_STREAMOUT**](../controls/em-streamout.md)
</dt> <dt>

[**LB\_GETTEXT**](../controls/lb-gettext.md)
</dt> </dl>

 

 
