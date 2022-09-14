---
description: Although you can specify any color for a pen when creating it, the system uses only colors that are available on the device.
ms.assetid: 2ea32786-f769-4096-8f60-f924c83ca9c8
title: Creating Colored Pens and Brushes
ms.topic: article
ms.date: 05/31/2018
---

# Creating Colored Pens and Brushes

Although you can specify any color for a pen when creating it, the system uses only colors that are available on the device. This means the system uses the closest matching color when it realizes the pen for drawing. When creating brushes, the system generates a dithered color if you specify a color that the device does not support. In either case, you can use the [**RGB**](/windows/desktop/api/Wingdi/nf-wingdi-rgb) macro to specify a color when creating a pen or brush.


```C++
LRESULT CALLBACK WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    int wmId, wmEvent;
    PAINTSTRUCT ps;
    HDC hdc;
    RECT clientRect;
    RECT textRect;
    HRGN bgRgn;
    HBRUSH hBrush;
    HPEN hPen;


    switch (message)
    {
    
    case WM_PAINT:
        {
        hdc = BeginPaint(hWnd, &ps);
        
        // Fill the client area with a brush
        GetClientRect(hWnd, &clientRect);
        bgRgn = CreateRectRgnIndirect(&clientRect);
        hBrush = CreateSolidBrush(RGB(200,200,200));
        FillRgn(hdc, bgRgn, hBrush);

        
        hPen = CreatePen(PS_DOT,1,RGB(0,255,0));
        SelectObject(hdc, hPen);
        SetBkColor(hdc, RGB(0,0,0));
        Rectangle(hdc, 10,10,200,200);
        
        // Text caption
        SetBkColor(hdc, RGB(255,255,255));
        SetRect(&textRect, 10, 210, 200,200);
        DrawText(hdc,TEXT("PS_DOT"),-1,&textRect, DT_CENTER | DT_NOCLIP);

        
        hPen = CreatePen(PS_DASHDOTDOT,1,RGB(0,255,255));
        SelectObject(hdc, hPen);
        SetBkColor(hdc, RGB(255,0,0));
        SelectObject(hdc,CreateSolidBrush(RGB(0,0,0)));
        Rectangle(hdc, 210,10,400,200);
        
        // Text caption
        SetBkColor(hdc, RGB(255,200,200));
        SetRect(&textRect, 210, 210, 400,200);
        DrawText(hdc,TEXT("PS_DASHDOTDOT"),-1,&textRect, DT_CENTER | DT_NOCLIP);
        

        hPen = CreatePen(PS_DASHDOT,1,RGB(255,0,0));
        SelectObject(hdc, hPen);
        SetBkColor(hdc, RGB(255,255,0));
        SelectObject(hdc,CreateSolidBrush(RGB(100,200,255)));
        Rectangle(hdc, 410,10,600,200);
        
        // Text caption
        SetBkColor(hdc, RGB(200,255,200));
        SetRect(&textRect, 410, 210, 600,200);
        DrawText(hdc,TEXT("PS_DASHDOT"),-1,&textRect, DT_CENTER | DT_NOCLIP);
        

        // When fnPenStyle is PS_SOLID, nWidth may be more than 1.
        // Also, if you set the width of any pen to be greater than 1, 
        // then it will draw a solid line, even if you try to select another style.
        hPen = CreatePen(PS_SOLID,5,RGB(255,0,0));
        SelectObject(hdc, hPen);
        // Setting the background color doesn't matter 
        // when the style is PS_SOLID
        SetBkColor(hdc, RGB(255,255,255));
        SelectObject(hdc,CreateSolidBrush(RGB(200,100,50)));
        Rectangle(hdc, 10,300,200,500);
        
        // Text caption
        SetBkColor(hdc, RGB(200,200,255));
        SetRect(&textRect, 10, 510, 200,500);
        DrawText(hdc,TEXT("PS_SOLID"),-1,&textRect, DT_CENTER | DT_NOCLIP);
    
        hPen = CreatePen(PS_DASH,1,RGB(0,255,0));
        SelectObject(hdc, hPen);
        SetBkColor(hdc, RGB(0,0,0));
        SelectObject(hdc,CreateSolidBrush(RGB(200,200,255)));
        Rectangle(hdc, 210,300,400,500);
        
        // Text caption
        SetBkColor(hdc, RGB(255,255,200));
        SetRect(&textRect, 210, 510, 400,200);
        DrawText(hdc,TEXT("PS_DASH"),-1,&textRect, DT_CENTER | DT_NOCLIP);

        hPen = CreatePen(PS_NULL,1,RGB(0,255,0));
        SelectObject(hdc, hPen);
        // Setting the background color doesn't matter 
        // when the style is PS_NULL
        SetBkColor(hdc, RGB(0,0,0));
        SelectObject(hdc,CreateSolidBrush(RGB(255,255,255)));
        Rectangle(hdc, 410,300,600,500);
        
        // Text caption
        SetBkColor(hdc, RGB(200,255,255));
        SetRect(&textRect, 410, 510, 600,500);
        DrawText(hdc,TEXT("PS_NULL"),-1,&textRect, DT_CENTER | DT_NOCLIP);
        
        
        // Clean up
        DeleteObject(bgRgn);
        DeleteObject(hBrush);
        DeleteObject(hPen);

        GetStockObject(WHITE_BRUSH);
        GetStockObject(DC_PEN);

        EndPaint(hWnd, &ps);
        break;
        }
    

    case WM_DESTROY:
        PostQuitMessage(0);
        break;
    default:
        return DefWindowProc(hWnd, message, wParam, lParam);
    }
    return 0;
}
```



 

 



