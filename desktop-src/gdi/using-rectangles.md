---
description: The example in this section illustrates how to use the rectangle functions. It consists of the main window procedure from an application that enables the user to move and size a bitmap.
ms.assetid: e8861240-9345-43e6-820d-d237247d1bd7
title: Using Rectangles (Windows GDI)
ms.topic: article
ms.date: 05/31/2018
---

# Using Rectangles (Windows GDI)

The example in this section illustrates how to use the rectangle functions. It consists of the main window procedure from an application that enables the user to move and size a bitmap.

When the application starts, it draws a 32-pixel by 32-pixel bitmap in the upper left corner of the screen. The user can move the bitmap by dragging it. To size the bitmap, the user creates a target rectangle by dragging the mouse, then drags the bitmap and "drops" it on the target rectangle. The application responds by copying the bitmap into the target rectangle.

The window procedure that allows the user to move and size the bitmap is given in the following example.


```C++
LRESULT CALLBACK MainWndProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) 
{ 
    HDC hdc;                 // device context (DC) for window  
    RECT rcTmp;              // temporary rectangle  
    PAINTSTRUCT ps;          // paint data for BeginPaint and EndPaint  
    POINT ptClientUL;        // client area upper left corner  
    POINT ptClientLR;        // client area lower right corner  
    static HDC hdcCompat;    // DC for copying bitmap  
    static POINT pt;         // x and y coordinates of cursor  
    static RECT rcBmp;       // rectangle that encloses bitmap  
    static RECT rcTarget;    // rectangle to receive bitmap  
    static RECT rcClient;    // client-area rectangle  
    static BOOL fDragRect;   // TRUE if bitmap rect. is dragged  
    static HBITMAP hbmp;     // handle of bitmap to display  
    static HBRUSH hbrBkgnd;  // handle of background-color brush  
    static COLORREF crBkgnd; // color of client-area background  
    static HPEN hpenDot;     // handle of dotted pen  
 
    switch (uMsg) 
    { 
        case WM_CREATE: 
 
            // Load the bitmap resource.  
 
            hbmp = LoadBitmap(hinst, MAKEINTRESOURCE(1)); 
 
            // Create a device context (DC) to hold the bitmap.  
            // The bitmap is copied from this DC to the window's DC  
            // whenever it must be drawn.  
 
            hdc = GetDC(hwnd); 
            hdcCompat = CreateCompatibleDC(hdc); 
            SelectObject(hdcCompat, hbmp); 
 
            // Create a brush of the same color as the background  
            // of the client area. The brush is used later to erase  
            // the old bitmap before copying the bitmap into the  
            // target rectangle.  
 
            crBkgnd = GetBkColor(hdc); 
            hbrBkgnd = CreateSolidBrush(crBkgnd); 
            ReleaseDC(hwnd, hdc); 
 
            // Create a dotted pen. The pen is used to draw the  
            // bitmap rectangle as the user drags it.  
 
            hpenDot = CreatePen(PS_DOT, 1, RGB(0, 0, 0)); 
 
            // Set the initial rectangle for the bitmap. Note that  
            // this application supports only a 32- by 32-pixel  
            // bitmap. The rectangle is slightly larger than the  
            // bitmap.  
 
            SetRect(&rcBmp, 1, 1, 34, 34); 
            return 0; 
 
        case WM_PAINT: 
 
            // Draw the bitmap rectangle and copy the bitmap into  
            // it. The 32-pixel by 32-pixel bitmap is centered  
            // in the rectangle by adding 1 to the left and top  
            // coordinates of the bitmap rectangle, and subtracting 2  
            // from the right and bottom coordinates.  
 
            BeginPaint(hwnd, &ps); 
            Rectangle(ps.hdc, rcBmp.left, rcBmp.top, 
                rcBmp.right, rcBmp.bottom); 
            StretchBlt(ps.hdc, rcBmp.left + 1, rcBmp.top + 1, 
                (rcBmp.right - rcBmp.left) - 2, 
                (rcBmp.bottom - rcBmp.top) - 2, hdcCompat, 
                0, 0, 32, 32, SRCCOPY); 
            EndPaint(hwnd, &ps); 
            break; 
 
        case WM_MOVE: 
        case WM_SIZE: 
 
            // Convert the client coordinates of the client-area  
            // rectangle to screen coordinates and save them in a  
            // rectangle. The rectangle is passed to the ClipCursor  
            // function during WM_LBUTTONDOWN processing.  
 
            GetClientRect(hwnd, &rcClient); 
            ptClientUL.x = rcClient.left; 
            ptClientUL.y = rcClient.top; 
            ptClientLR.x = rcClient.right; 
            ptClientLR.y = rcClient.bottom; 
            ClientToScreen(hwnd, &ptClientUL); 
            ClientToScreen(hwnd, &ptClientLR); 
            SetRect(&rcClient, ptClientUL.x, ptClientUL.y, 
                ptClientLR.x, ptClientLR.y); 
            return 0; 
 
        case WM_LBUTTONDOWN: 
 
            // Restrict the mouse cursor to the client area. This  
            // ensures that the window receives a matching  
            // WM_LBUTTONUP message.  
 
            ClipCursor(&rcClient); 
 
            // Save the coordinates of the mouse cursor.  
 
            pt.x = (LONG) LOWORD(lParam); 
            pt.y = (LONG) HIWORD(lParam); 
 
            // If the user has clicked the bitmap rectangle, redraw  
            // it using the dotted pen. Set the fDragRect flag to  
            // indicate that the user is about to drag the rectangle.  
 
            if (PtInRect(&rcBmp, pt)) 
            { 
                hdc = GetDC(hwnd); 
                SelectObject(hdc, hpenDot); 
                Rectangle(hdc, rcBmp.left, rcBmp.top, rcBmp.right, 
                    rcBmp.bottom); 
                fDragRect = TRUE; 
                ReleaseDC(hwnd, hdc); 
            } 
            return 0; 
 
        case WM_MOUSEMOVE: 
 
            // Draw a target rectangle or drag the bitmap rectangle,  
            // depending on the status of the fDragRect flag.  
 
            if ((wParam && MK_LBUTTON) 
                    && !fDragRect) 
            {
                // Set the mix mode so that the pen color is the  
                // inverse of the background color. The previous  
                // rectangle can then be erased by drawing  
                // another rectangle on top of it.  
 
                hdc = GetDC(hwnd); 
                SetROP2(hdc, R2_NOTXORPEN); 
 
                // If a previous target rectangle exists, erase  
                // it by drawing another rectangle on top of it.  
 
                if (!IsRectEmpty(&rcTarget)) 
                { 
                    Rectangle(hdc, rcTarget.left, rcTarget.top, 
                        rcTarget.right, rcTarget.bottom); 
                } 
 
                // Save the coordinates of the target rectangle. Avoid  
                // invalid rectangles by ensuring that the value of  
                // the left coordinate is lesser than the  
                // right coordinate, and that the value of the top 
                // coordinate is lesser than the bottom coordinate. 
 
                if ((pt.x < (LONG) LOWORD(lParam)) && 
                        (pt.y > (LONG) HIWORD(lParam))) 
                {
                    SetRect(&rcTarget, pt.x, HIWORD(lParam), 
                        LOWORD(lParam), pt.y); 
                }
                else if ((pt.x > (LONG) LOWORD(lParam)) && 
                        (pt.y > (LONG) HIWORD(lParam))) 
                {
                    SetRect(&rcTarget, LOWORD(lParam), 
                        HIWORD(lParam), pt.x, pt.y); 
                }
                else if ((pt.x > (LONG) LOWORD(lParam)) && 
                        (pt.y < (LONG) HIWORD(lParam))) 
                { 
                    SetRect(&rcTarget, LOWORD(lParam), pt.y, 
                        pt.x, HIWORD(lParam)); 
                }
                else 
                {
                    SetRect(&rcTarget, pt.x, pt.y, LOWORD(lParam), 
                        HIWORD(lParam)); 
                }
 
                // Draw the new target rectangle.  
 
                Rectangle(hdc, rcTarget.left, rcTarget.top, 
                    rcTarget.right, rcTarget.bottom); 
                ReleaseDC(hwnd, hdc); 
            } 
            else if ((wParam && MK_LBUTTON) 
                    && fDragRect) 
            {
 
                // Set the mix mode so that the pen color is the  
                // inverse of the background color.  
 
                hdc = GetDC(hwnd); 
                SetROP2(hdc, R2_NOTXORPEN); 
 
                // Select the dotted pen into the DC and erase  
                // the previous bitmap rectangle by drawing  
                // another rectangle on top of it.  
 
                SelectObject(hdc, hpenDot); 
                Rectangle(hdc, rcBmp.left, rcBmp.top, 
                    rcBmp.right, rcBmp.bottom); 
 
                // Set the new coordinates of the bitmap rectangle,  
                // then redraw it.  
 
                OffsetRect(&rcBmp, LOWORD(lParam) - pt.x, 
                    HIWORD(lParam) - pt.y); 
                Rectangle(hdc, rcBmp.left, rcBmp.top, 
                    rcBmp.right, rcBmp.bottom); 
                ReleaseDC(hwnd, hdc); 
 
                // Save the coordinates of the mouse cursor.  
 
                pt.x = (LONG) LOWORD(lParam); 
                pt.y = (LONG) HIWORD(lParam); 
            } 
            return 0; 
 
        case WM_LBUTTONUP: 
 
            // If the bitmap rectangle and target rectangle  
            // intersect, copy the bitmap into the target  
            // rectangle. Otherwise, copy the bitmap into the  
            // rectangle bitmap at its new location.  
 
            if (IntersectRect(&rcTmp, &rcBmp, &rcTarget)) 
            { 
 
                // Erase the bitmap rectangle by filling it with  
                // the background color.  
 
                hdc = GetDC(hwnd); 
                FillRect(hdc, &rcBmp, hbrBkgnd); 
 
                // Redraw the target rectangle because the part  
                // that intersected with the bitmap rectangle was  
                // erased by the call to FillRect.  
 
                Rectangle(hdc, rcTarget.left, rcTarget.top, 
                    rcTarget.right, rcTarget.bottom); 
 
                // Copy the bitmap into the target rectangle.  
 
                StretchBlt(hdc, rcTarget.left + 1, rcTarget.top + 1, 
                    (rcTarget.right - rcTarget.left) - 2, 
                    (rcTarget.bottom - rcTarget.top) - 2, hdcCompat, 
                    0, 0, 32, 32, SRCCOPY); 
 
                // Copy the target rectangle to the bitmap  
                // rectangle, set the coordinates of the target  
                // rectangle to 0, then reset the fDragRect flag.  
 
                CopyRect(&rcBmp, &rcTarget); 
                SetRectEmpty(&rcTarget); 
                ReleaseDC(hwnd, hdc); 
                fDragRect = FALSE; 
            } 
 
            else if (fDragRect) 
            { 
 
                // Draw the bitmap rectangle, copy the bitmap into  
                // it, and reset the fDragRect flag.  
 
                hdc = GetDC(hwnd); 
                Rectangle(hdc, rcBmp.left, rcBmp.top, 
                    rcBmp.right, rcBmp.bottom); 
                StretchBlt(hdc, rcBmp.left + 1, rcBmp.top + 1, 
                    (rcBmp.right - rcBmp.left) - 2, 
                    (rcBmp.bottom - rcBmp.top) - 2, hdcCompat, 
                    0, 0, 32, 32, SRCCOPY); 
                ReleaseDC(hwnd, hdc); 
                fDragRect = FALSE; 
            } 
 
            // Release the mouse cursor.  
 
            ClipCursor((LPRECT) NULL); 
            return 0; 
 
        case WM_DESTROY: 
 
            // Destroy the background brush, compatible bitmap,  
            // and the bitmap.  
 
            DeleteObject(hbrBkgnd); 
            DeleteDC(hdcCompat); 
            DeleteObject(hbmp); 
            PostQuitMessage(0); 
            break; 
 
        default: 
            return DefWindowProc(hwnd, uMsg, wParam, lParam); 
    } 
    return (LRESULT) NULL; 
} 
```



 

 



