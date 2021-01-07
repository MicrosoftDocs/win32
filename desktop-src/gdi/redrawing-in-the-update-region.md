---
description: You can limit the amount of drawing your application carries out when processing the WM\_PAINT message by determining the size and location of the update region.
ms.assetid: 3407014d-6427-45e9-8be4-b8037ca5438f
title: Redrawing in the Update Region
ms.topic: article
ms.date: 05/31/2018
---

# Redrawing in the Update Region

You can limit the amount of drawing your application carries out when processing the [**WM\_PAINT**](wm-paint.md) message by determining the size and location of the update region. Because the system uses the update region when creating the clipping region for the window's display device context, you can indirectly determine the update region by examining the clipping region.

In the following example, the window procedure draws a triangle, a rectangle, a pentagon, and a hexagon, but only if all or a portion of each figure lies within the update region. The window procedure uses the [**RectVisible**](/windows/desktop/api/Wingdi/nf-wingdi-rectvisible) function and a 100-by-100 rectangle to determine whether a figure is within the clipping region (and therefore the update region) for the common device context retrieved by [**BeginPaint**](/windows/desktop/api/Winuser/nf-winuser-beginpaint).


```C++
POINT aptTriangle[4]  = {50,2, 98,86,  2,86, 50,2}, 
      aptRectangle[5] = { 2,2, 98,2,  98,98,  2,98, 2,2}, 
      aptPentagon[6]  = {50,2, 98,35, 79,90, 21,90, 2,35, 50,2}, 
      aptHexagon[7]   = {50,2, 93,25, 93,75, 50,98, 7,75, 7,25, 50,2}; 
  . 
  . 
  . 
 
        case WM_PAINT: 
            hdc = BeginPaint(hwnd, &ps); 
            SetRect(&rc, 0, 0, 100, 100); 
 
            if (RectVisible(hdc, &rc)) 
                Polyline(hdc, aptTriangle, 4); 
 
            SetViewportOrgEx(hdc, 100, 0, NULL); 
            if (RectVisible(hdc, &rc)) 
                Polyline(hdc, aptRectangle, 5); 
 
            SetViewportOrgEx(hdc, 0, 100, NULL); 
            if (RectVisible(hdc, &rc)) 
                Polyline(hdc, aptPentagon, 6); 
 
            SetViewportOrgEx(hdc, 100, 100, NULL); 
            if (RectVisible(hdc, &rc)) 
                Polyline(hdc, aptHexagon, 7); 
            EndPaint(hwnd, &ps); 
            return 0L; 
 
  . 
  . 
  . 
```



The coordinates of each figure in this example lie within the same 100-by-100 rectangle. Before drawing a figure, the window procedure sets the viewport origin to a different part of the client area by using the [**SetViewportOrgEx**](/windows/desktop/api/Wingdi/nf-wingdi-setviewportorgex) function. This prevents figures from being drawn one on top of the other. Changing the viewport origin does not affect the clipping region, but does affect how the coordinates of the rectangle passed to [**RectVisible**](/windows/desktop/api/Wingdi/nf-wingdi-rectvisible) are interpreted. Changing the origin also allows you to use a single rectangle to check the update region rather than individual rectangles for each figure.

 

 



