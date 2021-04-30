---
title: WM_SETCURSOR message (Winuser.h)
description: Sent to a window if the mouse causes the cursor to move within a window and mouse input is not captured.
ms.assetid: b722689e-925f-40ac-ba4a-55be9dc6a8f8
keywords:
- WM_SETCURSOR message Menus and Other Resources
topic_type:
- apiref
api_name:
- WM_SETCURSOR
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_SETCURSOR message

Sent to a window if the mouse causes the cursor to move within a window and mouse input is not captured.


```C++
#define WM_SETCURSOR                    0x0020
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the window that contains the cursor.

</dd> <dt>

*lParam* 
</dt> <dd>

The low-order word of *lParam* specifies the hit-test result for the cursor position. See the return values for [WM_NCHITTEST](../inputdev/wm-nchittest.md) for possible values.

The high-order word of *lParam* specifies the mouse window message which triggered this event, such as [WM_MOUSEMOVE](../inputdev/wm-mousemove.md). When the window enters menu mode, this value is zero.

</dd> </dl>

## Return value

If an application processes this message, it should return **TRUE** to halt further processing or **FALSE** to continue.

## Remarks

The [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowprocw) function passes the **WM\_SETCURSOR** message to a parent window before processing. If the parent window returns **TRUE**, further processing is halted. Passing the message to a window's parent window gives the parent window control over the cursor's setting in a child window. The **DefWindowProc** function also uses this message to set the cursor to an arrow if it is not in the client area, or to the registered class cursor if it is in the client area. If the low-order word of the *lParam* parameter is **HTERROR** and the high-order word of *lParam* specifies that one of the mouse buttons is pressed, **DefWindowProc** calls the [**MessageBeep**](/windows/desktop/api/winuser/nf-winuser-messagebeep) function.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowprocw)
</dt> <dt>

[**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85))
</dt> <dt>

[**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85))
</dt> <dt>

**Conceptual**
</dt> <dt>

[Cursors](cursors.md)
</dt> </dl>

 

