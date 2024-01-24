---
description: The WM\_PRINT message is sent to a window to request that it draw itself in the specified device context, most commonly in a printer device context.
ms.assetid: e6be2ecd-603a-405f-8a48-68d971e1f6de
title: WM_PRINT message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_PRINT message

The **WM\_PRINT** message is sent to a window to request that it draw itself in the specified device context, most commonly in a printer device context.

A window receives this message through its [**WindowProc**](/windows/win32/api/winuser/nc-winuser-wndproc) function.


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

The [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function processes this message based on which drawing option is specified: if PRF\_CHECKVISIBLE is specified and the window is not visible, do nothing, if PRF\_NONCLIENT is specified, draw the nonclient area in the specified device context, if PRF\_ERASEBKGND is specified, send the window a [**WM\_ERASEBKGND**](../winmsg/wm-erasebkgnd.md) message, if PRF\_CLIENT is specified, send the window a [**WM\_PRINTCLIENT**](wm-printclient.md) message, if PRF\_CHILDREN is set, send each visible child window a **WM\_PRINT** message, if PRF\_OWNED is set, send each visible owned window a **WM\_PRINT** message.

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

[**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca)
</dt> <dt>

[**WM\_ERASEBKGND**](../winmsg/wm-erasebkgnd.md)
</dt> <dt>

[**WM\_PRINTCLIENT**](wm-printclient.md)
</dt> </dl>

 

 
