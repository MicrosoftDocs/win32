---
description: The WM\_PRINTCLIENT message is sent to a window to request that it draw its client area in the specified device context, most commonly in a printer device context.
ms.assetid: 8703ee74-812a-4ca2-8ee3-a3b8779739e7
title: WM_PRINTCLIENT message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_PRINTCLIENT message

The **WM\_PRINTCLIENT** message is sent to a window to request that it draw its client area in the specified device context, most commonly in a printer device context.

Unlike [**WM\_PRINT**](wm-print.md), **WM\_PRINTCLIENT** is not processed by [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca). A window should process the **WM\_PRINTCLIENT** message through an application-defined [**WindowProc**](/windows/win32/api/winuser/nc-winuser-wndproc) function for it to be used properly.


```C++
LRESULT CALLBACK WindowProc(
  HWND hwnd, 
  UINT  uMsg, 
  WPARAM wParam, 
  LPARAM lParam     
);
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the device context to draw in.

</dd> <dt>

*lParam* 
</dt> <dd>

The drawing options. This parameter can be one or more of the following values.



| Value                                                                                                                                                                  | Meaning                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <span id="PRF_CHECKVISIBLE"></span><span id="prf_checkvisible"></span><dl> <dt>**PRF\_CHECKVISIBLE**</dt> </dl> | Draws the window only if it is visible.<br/>          |
| <span id="PRF_CHILDREN"></span><span id="prf_children"></span><dl> <dt>**PRF\_CHILDREN**</dt> </dl>             | Draws all visible children windows.<br/>              |
| <span id="PRF_CLIENT"></span><span id="prf_client"></span><dl> <dt>**PRF\_CLIENT**</dt> </dl>                   | Draws the client area of the window.<br/>             |
| <span id="PRF_ERASEBKGND"></span><span id="prf_erasebkgnd"></span><dl> <dt>**PRF\_ERASEBKGND**</dt> </dl>       | Erases the background before drawing the window.<br/> |
| <span id="PRF_NONCLIENT"></span><span id="prf_nonclient"></span><dl> <dt>**PRF\_NONCLIENT**</dt> </dl>          | Draws the nonclient area of the window.<br/>          |
| <span id="PRF_OWNED"></span><span id="prf_owned"></span><dl> <dt>**PRF\_OWNED**</dt> </dl>                      | Draws all owned windows.<br/>                         |



 

</dd> </dl>

## Remarks

A window can process this message in much the same manner as [**WM\_PAINT**](./wm-paint.md), except that [**BeginPaint**](/windows/desktop/api/Winuser/nf-winuser-beginpaint) and [**EndPaint**](/windows/desktop/api/Winuser/nf-winuser-endpaint) need not be called (a device context is provided), and the window should draw its entire client area rather than just the invalid region.

Windows that can be used anywhere in the system, such as controls, should process this message. It is probably worthwhile for other windows to process this message as well because it is relatively easy to implement.

The [AnimateWindow](/windows/desktop/api/winuser/nf-winuser-animatewindow) function requires that the window being animated implements the **WM\_PRINTCLIENT** message.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Painting and Drawing Overview](painting-and-drawing.md)
</dt> <dt>

[Painting and Drawing Messages](painting-and-drawing-messages.md)
</dt> <dt>

[**AnimateWindow**](/windows/win32/api/winuser/nf-winuser-animatewindow)
</dt> <dt>

[**BeginPaint**](/windows/desktop/api/Winuser/nf-winuser-beginpaint)
</dt> <dt>

[**EndPaint**](/windows/desktop/api/Winuser/nf-winuser-endpaint)
</dt> <dt>

[**WM\_PAINT**](wm-paint.md)
</dt> </dl>

 

 
