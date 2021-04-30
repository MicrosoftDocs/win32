---
description: You can have your application redraw the entire contents of the client area whenever the window changes size by setting the CS\_HREDRAW and CS\_VREDRAW styles for the window class.
ms.assetid: ed68b85e-8382-4450-b07d-0422b44dc2e3
title: Redrawing the Entire Client Area
ms.topic: article
ms.date: 05/31/2018
---

# Redrawing the Entire Client Area

You can have your application redraw the entire contents of the client area whenever the window changes size by setting the CS\_HREDRAW and CS\_VREDRAW styles for the window class. Applications that adjust the size of the drawing based on the size of the window use these styles to ensure that they start with a completely empty client area when drawing.

In the following example, the window procedure draws a five-pointed star that fits neatly in the client area. It uses a common device context and must set the mapping mode as well as window and viewport extents each time the [**WM\_PAINT**](wm-paint.md) message is processed.


```C++
LRESULT APIENTRY WndProc(HWMD hwnd, UINT message, WPARAM wParam, LPARAM lParam) 
{ 
    PAINTSTRUCT ps; 
    HDC hdc; 
    RECT rc; 
    POINT aptStar[6] = {50,2, 2,98, 98,33, 2,33, 98,98, 50,2}; 
 
    . 
    . 
    . 
 
        case WM_PAINT: 
            hdc = BeginPaint(hwnd, &ps); 
            GetClientRect(hwnd, &rc); 
            SetMapMode(hdc, MM_ANISOTROPIC); 
            SetWindowExtEx(hdc, 100, 100, NULL); 
            SetViewportExtEx(hdc, rc.right, rc.bottom, NULL); 
            Polyline(hdc, aptStar, 6); 
            EndPaint(hwnd, &ps); 
            return 0L; 
 
        . 
        . 
        . 
} 
 
 
int APIENTRY WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) 
{ 
    WNDCLASS wc; 
 
    . 
    . 
    . 
 
        wc.style = CS_HREDRAW | CS_VREDRAW; 
        wc.lpfnWndProc = (WNDPROC) WndProc; 
 
    . 
    . 
    . 
 
        RegisterClass(&wc); 
 
    . 
    . 
    . 
 
    return msg.wParam; 
} 
```



 

 



