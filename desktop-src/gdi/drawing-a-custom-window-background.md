---
Description: 'You can draw your own window background rather than having the system draw it for you.'
ms.assetid: '72a342dc-2766-4ec9-b4c6-5ac3c550ea25'
title: Drawing a Custom Window Background
---

# Drawing a Custom Window Background

You can draw your own window background rather than having the system draw it for you. Most applications specify a brush handle or system color value for the class background brush when registering the window class; the system uses the brush or color to draw the background. If you set the class background brush to **NULL**, however, the system sends a [**WM\_ERASEBKGND**](_win32_wm_erasebkgnd_cpp) message to your window procedure whenever the window background must be drawn, letting you draw a custom background.

In the following example, the window procedure draws a large checkerboard pattern that fits neatly in the window. The procedure fills the client area with a white brush and then draws thirteen 20-by-20 rectangles using a gray brush. The display device context to use when drawing the background is specified in the *wParam* parameter for the message.


```C++
HBRUSH hbrWhite, hbrGray; 
 
  . 
  . 
  . 
 
case WM_CREATE: 
    hbrWhite = GetStockObject(WHITE_BRUSH); 
    hbrGray  = GetStockObject(GRAY_BRUSH); 
    return 0L; 
 
case WM_ERASEBKGND: 
    hdc = (HDC) wParam; 
    GetClientRect(hwnd, &amp;rc); 
    SetMapMode(hdc, MM_ANISOTROPIC); 
    SetWindowExtEx(hdc, 100, 100, NULL); 
    SetViewportExtEx(hdc, rc.right, rc.bottom, NULL); 
    FillRect(hdc, &amp;rc, hbrWhite); 
 
    for (i = 0; i < 13; i++) 
    { 
        x = (i * 40) % 100; 
        y = ((i * 40) / 100) * 20; 
        SetRect(&amp;rc, x, y, x + 20, y + 20); 
        FillRect(hdc, &amp;rc, hbrGray); 
    } 
  return 1L; 
```



If the application draws its own minimized window, the system also sends the [**WM\_ERASEBKGND**](_win32_wm_erasebkgnd_cpp) message to the window procedure to draw the background for the minimized window. You can use the same technique used by [**WM\_PAINT**](wm-paint.md) to determine whether the window is minimized that is, call the [**IsIconic**](_win32_isiconic_cpp) function and check for the return value **TRUE**.

 

 



