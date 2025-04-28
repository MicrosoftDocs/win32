---
description: Notifies a window that its nonclient area is being destroyed. The DestroyWindow function sends the WM\_NCDESTROY message to the window following the WM\_DESTROY message.
ms.assetid: 64ab268d-0e90-4401-81d3-a4da64196001
title: WM_NCDESTROY message (Winuser.h)
ms.topic: reference
ms.date: 04/28/2025
---

# WM_NCDESTROY message

Notifies a window that its nonclient area is being destroyed.

```C++
#define WM_NCDESTROY                    0x0082
```

## Parameters

*wParam*

This parameter is not used.

*lParam*

This parameter is not used.

## Return value

Type: **LRESULT**

If an application processes this message, it should return zero.

## Remarks

The [**DestroyWindow**](/windows/win32/api/winuser/nf-winuser-destroywindow) function sends the **WM_NCDESTROY** message to the window following the [**WM_DESTROY**](wm-destroy.md) message. **WM_NCDESTROY** is used to free the allocated memory object associated with the window.

The **WM_NCDESTROY** message is sent after the child windows have been destroyed. In contrast, [**WM_DESTROY**](wm-destroy.md) is sent before the child windows are destroyed.

A window receives this message through its [**WindowProc**](/windows/win32/api/winuser/nc-winuser-wndproc) function.

This message frees any memory internally allocated for the window.

## Requirements

| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 2000 Professional [desktop apps only]                                               |
| Minimum supported server | Windows 2000 Server [desktop apps only]                                                     |
| Header                 | Winuser.h (include Windows.h) |

## See also

[**DestroyWindow**](/windows/win32/api/winuser/nf-winuser-destroywindow)

[**WM_DESTROY**](wm-destroy.md)

[**WM_NCCREATE**](wm-nccreate.md)

[Windows](windows.md)
