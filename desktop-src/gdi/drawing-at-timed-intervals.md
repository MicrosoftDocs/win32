---
description: You can draw at timed intervals by creating a timer with the SetTimer function.
ms.assetid: 82f9aa5e-8e42-49cf-bcd0-785bc78fe159
title: Drawing at Timed Intervals
ms.topic: article
ms.date: 05/31/2018
---

# Drawing at Timed Intervals

You can draw at timed intervals by creating a timer with the [**SetTimer**](/windows/win32/api/winuser/nf-winuser-settimer) function. By using a timer to send [**WM\_TIMER**](../winmsg/wm-timer.md) messages to the window procedure at regular intervals, an application can carry out simple animation in the client area while other applications continue running.

In the following example, the application bounces a star from side to side in the client area. Each time the window procedure receives a [**WM\_TIMER**](../winmsg/wm-timer.md) message, the procedure erases the star at the current position, calculates a new position, and draws the star within the new position. The procedure starts the timer by calling [**SetTimer**](/windows/win32/api/winuser/nf-winuser-settimer) while processing the [**WM\_CREATE**](../winmsg/wm-create.md) message.


```C++
RECT rcCurrent = {0,0,20,20}; 
POINT aptStar[6] = {10,1, 1,19, 19,6, 1,6, 19,19, 10,1}; 
int X = 2, Y = -1, idTimer = -1; 
BOOL fVisible = FALSE; 
HDC hdc; 
 
LRESULT APIENTRY WndProc(HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam) 
{ 
    PAINTSTRUCT ps; 
    RECT rc; 
 
    switch (message) 
    { 
        case WM_CREATE: 
 
            // Calculate the starting point.  
 
            GetClientRect(hwnd, &rc); 
            OffsetRect(&rcCurrent, rc.right / 2, rc.bottom / 2); 
 
            // Initialize the private DC.  
 
            hdc = GetDC(hwnd); 
            SetViewportOrgEx(hdc, rcCurrent.left, 
                rcCurrent.top, NULL); 
            SetROP2(hdc, R2_NOT); 
 
            // Start the timer.  
 
            SetTimer(hwnd, idTimer = 1, 10, NULL); 
            return 0L; 
 
        case WM_DESTROY: 
            KillTimer(hwnd, 1); 
            PostQuitMessage(0); 
            return 0L; 
 
        case WM_SIZE: 
            switch (wParam) 
            { 
                case SIZE_MINIMIZED: 
 
                    // Stop the timer if the window is minimized. 
 
                    KillTimer(hwnd, 1); 
                    idTimer = -1; 
                    break; 
 
                case SIZE_RESTORED: 
 
                    // Move the star back into the client area  
                    // if necessary.  
 
                    if (rcCurrent.right > (int) LOWORD(lParam)) 
                    {
                        rcCurrent.left = 
                            (rcCurrent.right = 
                                (int) LOWORD(lParam)) - 20; 
                    }
                    if (rcCurrent.bottom > (int) HIWORD(lParam)) 
                    {
                        rcCurrent.top = 
                            (rcCurrent.bottom = 
                                (int) HIWORD(lParam)) - 20; 
                    }
 
                    // Fall through to the next case.  
 
                case SIZE_MAXIMIZED: 
 
                    // Start the timer if it had been stopped.  
 
                    if (idTimer == -1) 
                        SetTimer(hwnd, idTimer = 1, 10, NULL); 
                    break; 
            } 
            return 0L; 
 
        case WM_TIMER: 
 
            // Hide the star if it is visible.  
 
            if (fVisible) 
                Polyline(hdc, aptStar, 6); 
 
            // Bounce the star off a side if necessary.  
 
            GetClientRect(hwnd, &rc); 
            if (rcCurrent.left + X < rc.left || 
                rcCurrent.right + X > rc.right) 
                X = -X; 
            if (rcCurrent.top + Y < rc.top || 
                rcCurrent.bottom + Y > rc.bottom) 
                Y = -Y; 
 
            // Show the star in its new position.  
 
            OffsetRect(&rcCurrent, X, Y); 
            SetViewportOrgEx(hdc, rcCurrent.left, 
                rcCurrent.top, NULL); 
            fVisible = Polyline(hdc, aptStar, 6); 
 
            return 0L; 
 
        case WM_ERASEBKGND: 
 
            // Erase the star.  
 
            fVisible = FALSE; 
            return DefWindowProc(hwnd, message, wParam, lParam); 
 
        case WM_PAINT: 
 
            // Show the star if it is not visible. Use BeginPaint  
            // to clear the update region.  
 
            BeginPaint(hwnd, &ps); 
            if (!fVisible) 
                fVisible = Polyline(hdc, aptStar, 6); 
            EndPaint(hwnd, &ps); 
            return 0L; 
    } 
    return DefWindowProc(hwnd, message, wParam, lParam); 
} 
```



This application uses a private device context to minimize the time required to prepare the device context for drawing. The window procedure retrieves and initializes the private device context when processing the [**WM\_CREATE**](../winmsg/wm-create.md) message, setting the binary raster operation mode to allow the star to be erased and drawn using the same call to the [**Polyline**](/windows/desktop/api/Wingdi/nf-wingdi-polyline) function. The window procedure also sets the viewport origin to allow the star to be drawn using the same set of points regardless of the star's position in the client area.

The application uses the [**WM\_PAINT**](wm-paint.md) message to draw the star whenever the window must be updated. The window procedure draws the star only if it is not visible; that is, only if it has been erased by the [**WM\_ERASEBKGND**](../winmsg/wm-erasebkgnd.md) message. The window procedure intercepts the **WM\_ERASEBKGND** message to set the *fVisible* variable, but passes the message to [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) so that the system can draw the window background.

The application uses the [**WM\_SIZE**](../winmsg/wm-size.md) message to stop the timer when the window is minimized and to restart the timer when the minimized window is restored. The window procedure also uses the message to update the current position of the star if the size of the window has been reduced so that the star is no longer in the client area. The application keeps track of the star's current position by using the structure specified by rcCurrent, which defines the bounding rectangle for the star. Keeping all corners of the rectangle in the client area keeps the star in the area. The window procedure initially centers the star in the client area when processing the [**WM\_CREATE**](../winmsg/wm-create.md) message.

 

 
