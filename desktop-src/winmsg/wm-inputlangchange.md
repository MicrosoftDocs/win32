---
description: Sent to the topmost affected window after an application's input language has been changed. You should make any application-specific settings and pass the message to the DefWindowProc function, which passes the message to all first-level child windows.
ms.assetid: 4d403b1d-f6f7-40d5-9bf5-6a9c4da0803c
title: WM_INPUTLANGCHANGE message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_INPUTLANGCHANGE message

Sent to the topmost affected window after an application's input language has been changed. You should make any application-specific settings and pass the message to the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function, which passes the message to all first-level child windows. These child windows can pass the message to [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) to have it pass the message to their child windows, and so on.

A window receives this message through its [**WindowProc**](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.


```C++
#define WM_INPUTLANGCHANGE              0x0051
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The character set of the new locale.

</dd> <dt>

*lParam* 
</dt> <dd>

The input locale identifier. For more information, see [Languages, Locales, and Keyboard Layouts](../inputdev/about-keyboard-input.md).

</dd> </dl>

## Return value

Type: **LRESULT**

An application should return nonzero if it processes this message.

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

[**WM\_INPUTLANGCHANGEREQUEST**](wm-inputlangchangerequest.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 
