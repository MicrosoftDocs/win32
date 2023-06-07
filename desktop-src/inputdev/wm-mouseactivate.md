---
title: WM_MOUSEACTIVATE message (Winuser.h)
description: Sent when the cursor is in an inactive window and the user presses a mouse button. The parent window receives this message only if the child window passes it to the DefWindowProc function.
ms.assetid: 335c0819-a655-4dd1-9511-1f148b87271c
keywords:
- WM_MOUSEACTIVATE message Keyboard and Mouse Input
topic_type:
- apiref
api_name:
- WM_MOUSEACTIVATE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_MOUSEACTIVATE message

Sent when the cursor is in an inactive window and the user presses a mouse button. The parent window receives this message only if the child window passes it to the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function.

A window receives this message through its [**WindowProc**](/windows/win32/api/winuser/nc-winuser-wndproc) function.


```C++
#define WM_MOUSEACTIVATE                0x0021
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the top-level parent window of the window being activated.

</dd> <dt>

*lParam* 
</dt> <dd>

The low-order word specifies the hit-test value returned by the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function as a result of processing the [**WM\_NCHITTEST**](wm-nchittest.md) message. For a list of hit-test values, see **WM\_NCHITTEST**.

The high-order word specifies the identifier of the mouse message generated when the user pressed a mouse button. The mouse message is either discarded or posted to the window, depending on the return value.

</dd> </dl>

## Return value

The return value specifies whether the window should be activated and whether the identifier of the mouse message should be discarded. It must be one of the following values.



| Return code/value                                                                                                                                          | Description                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| <dl> <dt>**MA\_ACTIVATE**</dt> <dt>1</dt> </dl>         | Activates the window, and does not discard the mouse message.<br/>         |
| <dl> <dt>**MA\_ACTIVATEANDEAT**</dt> <dt>2</dt> </dl>   | Activates the window, and discards the mouse message.<br/>                 |
| <dl> <dt>**MA\_NOACTIVATE**</dt> <dt>3</dt> </dl>       | Does not activate the window, and does not discard the mouse message.<br/> |
| <dl> <dt>**MA\_NOACTIVATEANDEAT**</dt> <dt>4</dt> </dl> | Does not activate the window, but discards the mouse message.<br/>         |



 

## Remarks

The [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function passes the message to a child window's parent window before any processing occurs. The parent window determines whether to activate the child window. If it activates the child window, the parent window should return **MA\_NOACTIVATE** or **MA\_NOACTIVATEANDEAT** to prevent the system from processing the message further.

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

[**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca)
</dt> <dt>

[**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85))
</dt> <dt>

[**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85))
</dt> <dt>

[**WM\_NCHITTEST**](wm-nchittest.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Mouse Input](mouse-input.md)
</dt> </dl>

 

