---
description: This section contains sample code that demonstrates the appearance of lines drawn using various pen styles and attributes.
ms.assetid: c60a8e14-400c-40db-869b-b8fea7a03f38
title: Using Pens
ms.topic: article
ms.date: 05/31/2018
---

# Using Pens

This section contains sample code that demonstrates the appearance of lines drawn using various pen styles and attributes.


```C++
LRESULT CALLBACK WndProc(HWND hWnd, UINT uMsg, WPARAM wParam, 
                             LPARAM lParam) 
{ 
    PAINTSTRUCT ps; 
    LOGBRUSH lb; 
    RECT rc; 
    HDC hdc; 
    int i; 
    HGDIOBJ hPen = NULL;
    HGDIOBJ hPenOld; 
    DWORD dwPenStyle[] = { 
                           PS_DASH, 
                           PS_DASHDOT, 
                           PS_DOT, 
                           PS_INSIDEFRAME, 
                           PS_NULL, 
                           PS_SOLID 
                        }; 
    UINT uHatch[] = { 
                      HS_BDIAGONAL, 
                      HS_CROSS, 
                      HS_DIAGCROSS, 
                      HS_FDIAGONAL, 
                      HS_HORIZONTAL, 
                      HS_VERTICAL     
                     }; 
 
    switch (uMsg) 
    { 
        case WM_PAINT: 
        { 
            GetClientRect(hWnd, &rc); 
            rc.left += 10; 
            rc.top += 10; 
            rc.bottom -= 10; 
 
            // Initialize the pen's brush.
            lb.lbStyle = BS_SOLID; 
            lb.lbColor = RGB(255,0,0); 
            lb.lbHatch = 0; 
 
            hdc = BeginPaint(hWnd, &ps); 
            for (i = 0; i < 6; i++) 
            { 
                hPen = ExtCreatePen(PS_COSMETIC | dwPenStyle[i], 
                                    1, &lb, 0, NULL); 
                hPenOld = SelectObject(hdc, hPen); 
                MoveToEx(hdc, rc.left + (i * 20), rc.top, NULL); 
                LineTo(hdc, rc.left + (i * 20), rc.bottom); 
                SelectObject(hdc, hPenOld); 
                DeleteObject(hPen); 
            } 
            rc.left += 150; 
            for (i = 0; i < 6; i++) 
            { 
                lb.lbStyle = BS_HATCHED; 
                lb.lbColor = RGB(0,0,255);     
                lb.lbHatch = uHatch[i]; 
                hPen = ExtCreatePen(PS_GEOMETRIC, 
                                    5, &lb, 0, NULL); 
                hPenOld = SelectObject(hdc, hPen); 
                MoveToEx(hdc, rc.left + (i * 20), rc.top, NULL); 
                LineTo(hdc, rc.left + (i * 20), rc.bottom); 
                SelectObject(hdc, hPenOld); 
                DeleteObject(hPen); 
            } 
            EndPaint(hWnd, &ps); 
 
        } 
        break; 
 
        case WM_DESTROY: 
            DeleteObject(hPen); 
            PostQuitMessage(0); 
            break; 
 
        default: 
            return DefWindowProc(hWnd, uMsg, wParam, lParam); 
    } 
 
    return FALSE; 
} 
```



 

 



