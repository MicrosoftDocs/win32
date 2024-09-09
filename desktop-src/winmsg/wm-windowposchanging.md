---
description: Sent to a window whose size, position, or place in the Z order is about to change as a result of a call to the SetWindowPos function or another window-management function.
ms.assetid: 45ecd966-5222-4738-9e99-8a6edbdd435a
title: WM_WINDOWPOSCHANGING message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_WINDOWPOSCHANGING message

Sent to a window whose size, position, or place in the Z order is about to change as a result of a call to the [**SetWindowPos**](/windows/win32/api/winuser/nf-winuser-setwindowpos) function or another window-management function.

A window receives this message through its [**WindowProc**](/windows/win32/api/winuser/nc-winuser-wndproc) function.


```C++
#define WM_WINDOWPOSCHANGING            0x0046
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**WINDOWPOS**](/windows/win32/api/winuser/ns-winuser-windowpos) structure that contains information about the window's new size and position.

</dd> </dl>

## Return value

Type: **LRESULT**

If an application processes this message, it should return zero.

## Remarks

For a window with the [**WS\_OVERLAPPED**](window-styles.md) or **WS\_THICKFRAME** style, the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function sends the [**WM\_GETMINMAXINFO**](wm-getminmaxinfo.md) message to the window. This is done to validate the new size and position of the window and to enforce the [CS\_BYTEALIGNCLIENT](about-window-classes.md) and CS\_BYTEALIGNWINDOW client styles. By not passing the **WM\_WINDOWPOSCHANGING** message to the **DefWindowProc** function, an application can override these defaults.

While this message is being processed, modifying any of the values in [**WINDOWPOS**](/windows/win32/api/winuser/ns-winuser-windowpos) affects the window's new size, position, or place in the Z order. An application can prevent changes to the window by setting or clearing the appropriate bits in the **flags** member of **WINDOWPOS**.

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

[**EndDeferWindowPos**](/windows/win32/api/winuser/nf-winuser-enddeferwindowpos)
</dt> <dt>

[**SetWindowPos**](/windows/win32/api/winuser/nf-winuser-setwindowpos)
</dt> <dt>

[**WINDOWPOS**](/windows/win32/api/winuser/ns-winuser-windowpos)
</dt> <dt>

[**WM\_GETMINMAXINFO**](wm-getminmaxinfo.md)
</dt> <dt>

[**WM\_MOVE**](wm-move.md)
</dt> <dt>

[**WM\_SIZE**](wm-size.md)
</dt> <dt>

[**WM\_WINDOWPOSCHANGED**](wm-windowposchanged.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 
