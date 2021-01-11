---
description: To respond to a WM\_PAINT message, use code like the following.
ms.assetid: 682d9bc6-8d74-48c4-80fb-bae73d409a6b
title: Painting on a DC That Spans Multiple Displays
ms.topic: article
ms.date: 05/31/2018
---

# Painting on a DC That Spans Multiple Displays

To respond to a **WM\_PAINT** message, use code like the following.


```C++
case WM_PAINT:
hdc = BeginPaint(hwnd, &ps);
EnumDisplayMonitors(hdc, NULL, MyPaintEnumProc, 0);
EndPaint(hwnd, &ps);
 
```



To paint the top half of a window, use code like the following.


```C++
GetClient Rect(hwnd, &rc);
rc.bottom = (rc.bottom - rc.top) / 2;
hdc = GetDC(hwnd);
EnumDisplayMonitors(hdc, &rc, MyPaintEnumProc, 0);
ReleaseDC(hwnd, hdc);
```



To paint the entire virtual screen optimally for each monitor, use code like the following.


```C++
hdc = GetDC(NULL);
EnumDisplayMonitors(hdc, NULL, MyPaintScreenEnumProc, 0);
ReleaseDC(NULL, hdc);
```



 

 



