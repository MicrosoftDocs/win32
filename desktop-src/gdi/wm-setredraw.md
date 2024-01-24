---
description: You send the **WM_SETREDRAW** message to a window to allow changes in that window to be redrawn, or to prevent changes in that window from being redrawn.
ms.assetid: 0085a55e-7bf6-4eb6-a649-832b685db1cc
title: WM_SETREDRAW message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM_SETREDRAW message

You send the **WM\_SETREDRAW** message to a window to allow changes in that window to be redrawn, or to prevent changes in that window from being redrawn.

To send this message, call the [**SendMessage**](/windows/win32/api/winuser/nf-winuser-sendmessage) function with the following parameters.

```C++
SendMessage(
  (HWND) hWnd,
  WM_SETREDRAW,
  (WPARAM) wParam,
  (LPARAM) lParam
);
```

## Parameters

`wParam`

The redraw state. If this parameter is **TRUE**, then the content can be redrawn after a change. If this parameter is **FALSE**, then the content can't be redrawn after a change.

`lParam`

This parameter isn't used.

## Return value

Your application should return 0 if it processes this message.

## Remarks

This message can be useful if your application must add several items to a list box. Your application can call this message with *wParam* set to **FALSE**, add the items, and then call the message again with *wParam* set to **TRUE**. Finally, your application can call [**RedrawWindow**](/windows/win32/api/Winuser/nf-winuser-redrawwindow)(*hWnd*, **NULL**, **NULL**, RDW\_ERASE \| RDW\_FRAME \| RDW\_INVALIDATE \| RDW\_ALLCHILDREN) to cause the list box to be repainted.

> [!NOTE] 
> You should use [**RedrawWindow**](/windows/win32/api/Winuser/nf-winuser-redrawwindow) with the specified flags, instead of [**InvalidateRect**](/windows/win32/api/Winuser/nf-winuser-invalidaterect), because the former is necessary for some controls that have nonclient area of their own, or have window styles that cause them to be given a nonclient area (such as **WS_THICKFRAME**, **WS_BORDER**, or **WS_EX_CLIENTEDGE**). If the control does not have a nonclient area, then **RedrawWindow** with these flags will do only as much invalidation as **InvalidateRect** would.

Passing a **WM_SETREDRAW** message to the **DefWindowProc** function removes the **WS_VISIBLE** style from the window when *wParam* is set to **FALSE**. Although the window content remains visible on screen, the [**IsWindowVisible**](/windows/win32/api/winuser/nf-winuser-iswindowvisible) function returns **FALSE** when called on a window in this state. 

Passing a **WM_SETREDRAW** message to the **DefWindowProc** function adds the **WS_VISIBLE** style to the window, if not set, when *wParam* is set to **TRUE**. If your application sends the **WM_SETREDRAW** message with *wParam* set to **TRUE** to a hidden window, then the window becomes visible. 

**Windows 10 and later; Windows Server 2016 and later**. The system sets a property named *SysSetRedraw* on a window whose window procedure passes **WM_SETREDRAW** messages to **DefWindowProc**. You can use the [**GetProp**](/windows/win32/api/Winuser/nf-winuser-getpropa) function to get the property value when it's available. **GetProp** returns a non-zero value when redraw is disabled. **GetProp** will return zero when redraw is enabled, or when the window property doesn't exist. 

## Requirements

| Requirement | Value |
|-|-|
| Minimum supported client | Windows 2000 Professional \[desktop apps only\] |
| Minimum supported server | Windows 2000 Server \[desktop apps only\] |
| Header | <dl><dt>Winuser.h (include Windows.h)</dt></dl> |

## See also

* [Painting and drawing overview](painting-and-drawing.md)
* [Painting and drawing messages](painting-and-drawing-messages.md)
* [RedrawWindow](/windows/win32/api/Winuser/nf-winuser-redrawwindow)
