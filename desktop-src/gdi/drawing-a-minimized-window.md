---
Description: You can draw your own minimized windows rather than having the system draw them for you.
ms.assetid: 607d987a-5bdc-46bc-bde7-6dc52745ac79
title: Drawing a Minimized Window
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Drawing a Minimized Window

You can draw your own minimized windows rather than having the system draw them for you. Most applications define a class icon when registering the window class for the window, and the system draws the icon when the window is minimized. If you set the class icon to **NULL**, however, the system sends a [**WM\_PAINT**](wm-paint.md) message to your window procedure whenever the window is minimized, enabling the window procedure to draw in the minimized window.

In the following example, the window procedure draws a star in the minimized window. The procedure uses the [**IsIconic**](https://msdn.microsoft.com/library/ms633527(v=VS.85).aspx) function to determine when the window is minimized. This ensures that the star is drawn only when the window is minimized.


```C++
POINT aptStar[6] = {50,2, 2,98, 98,33, 2,33, 98,98, 50,2}; 
 
  . 
  . 
  . 
 
case WM_PAINT: 
    hdc = BeginPaint(hwnd, &amp;ps); 
 
    // Determine whether the window is minimized.  
 
    if (IsIconic(hwnd)) 
    { 
        GetClientRect(hwnd, &amp;rc); 
        SetMapMode(hdc, MM_ANISOTROPIC); 
        SetWindowExtEx(hdc, 100, 100, NULL); 
        SetViewportExtEx(hdc, rc.right, rc.bottom, NULL); 
        Polyline(hdc, aptStar, 6); 
    } 
    else 
    { 
        TextOut(hdc, 0,0, "Hello, Windows!", 15); 
    } 
    EndPaint(hwnd, &amp;ps); 
    return 0L; 
```



You set the class icon to **NULL** by setting the **hIcon** member of the [**WNDCLASS**](https://msdn.microsoft.com/library/ms633576(v=VS.85).aspx) structure to **NULL** before calling the [**RegisterClass**](https://msdn.microsoft.com/library/ms633586(v=VS.85).aspx) function for the window class.

 

 



