---
description: The system is not the only source of WM\_PAINT messages. The InvalidateRect or InvalidateRgn function can indirectly generate WM\_PAINT messages for your windows. These functions mark all or part of a client area as invalid (that must be redrawn).
ms.assetid: 41c2bc07-768b-4d27-a869-69b072f3e033
title: Invalidating the Client Area
ms.topic: article
ms.date: 05/31/2018
---

# Invalidating the Client Area

The system is not the only source of [**WM\_PAINT**](wm-paint.md) messages. The [**InvalidateRect**](/windows/desktop/api/Winuser/nf-winuser-invalidaterect) or [**InvalidateRgn**](/windows/desktop/api/Winuser/nf-winuser-invalidatergn) function can indirectly generate **WM\_PAINT** messages for your windows. These functions mark all or part of a client area as invalid (that must be redrawn).

In the following example, the window procedure invalidates the entire client area when processing [**WM\_CHAR**](../inputdev/wm-char.md) messages. This allows the user to change the figure by typing a number and view the results; these results are drawn as soon as there are no other messages in the application's message queue.


```C++
RECT rc;
POINT aptPentagon[6] = {50,2, 98,35, 79,90, 21,90, 2,35, 50,2}, 
      aptHexagon[7]  = {50,2, 93,25, 93,75, 50,98, 7,75, 7,25, 50,2}; 
POINT *ppt = aptPentagon; 
int cpt = 6; 
 
  . 
  . 
  . 
 
case WM_CHAR: 
    switch (wParam) 
    { 
        case '5': 
            ppt = aptPentagon; 
            cpt = 6; 
            break; 
        case '6': 
            ppt = aptHexagon; 
            cpt = 7; 
            break; 
    } 
    InvalidateRect(hwnd, NULL, TRUE); 
    return 0L; 
 
case WM_PAINT: 
    hdc = BeginPaint(hwnd, &ps); 
    GetClientRect(hwnd, &rc); 
    SetMapMode(hdc, MM_ANISOTROPIC); 
    SetWindowExtEx(hdc, 100, 100, NULL); 
    SetViewportExtEx(hdc, rc.right, rc.bottom, NULL); 
    Polyline(hdc, ppt, cpt); 
    EndPaint(hwnd, &ps); 
    return 0L; 
```



In this example, the **NULL** argument used by [**InvalidateRect**](/windows/desktop/api/Winuser/nf-winuser-invalidaterect) specifies the entire client area; the **TRUE** argument causes the background to be erased. If you do not want the application to wait until the application's message queue has no other messages, use the [**UpdateWindow**](/windows/desktop/api/Winuser/nf-winuser-updatewindow) function to force the [**WM\_PAINT**](wm-paint.md) message to be sent immediately. If there is any invalid part of the client area, **UpdateWindow** sends the **WM\_PAINT** message for the specified window directly to the window procedure.

 

 
