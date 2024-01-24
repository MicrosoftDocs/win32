---
description: You can permit the user to draw lines with the mouse by having your window procedure draw while processing the WM\_MOUSEMOVE message.
ms.assetid: 5e8a54b6-05cc-4446-b82e-2b3e550d780a
title: Drawing with the Mouse
ms.topic: article
ms.date: 05/31/2018
---

# Drawing with the Mouse

You can permit the user to draw lines with the mouse by having your window procedure draw while processing the [**WM\_MOUSEMOVE**](../inputdev/wm-mousemove.md) message. The system sends the **WM\_MOUSEMOVE** message to the window procedure whenever the user moves the cursor within the window. To draw lines, the window procedure can retrieve a display device context and draw a line in the window between the current and previous cursor positions.

In the following example, the window procedure prepares for drawing when the user presses and holds the left mouse button (sending the [**WM\_LBUTTONDOWN**](../inputdev/wm-lbuttondown.md) message). As the user moves the cursor within the window, the window procedure receives a series of [**WM\_MOUSEMOVE**](../inputdev/wm-mousemove.md) messages. For each message, the window procedure draws a line connecting the previous position and the current position. To draw the line, the procedure uses [**GetDC**](/windows/desktop/api/Winuser/nf-winuser-getdc) to retrieve a display device context; then, as soon as drawing is complete and before returning from the message, the procedure uses the [**ReleaseDC**](/windows/desktop/api/Winuser/nf-winuser-releasedc) function to release the display device context. As soon as the user releases the mouse button, the window procedure clears the flag, and the drawing stops (which sends the [**WM\_LBUTTONUP**](../inputdev/wm-lbuttonup.md) message).


```C++
BOOL fDraw = FALSE; 
POINT ptPrevious; 
 
  . 
  . 
  . 
 
case WM_LBUTTONDOWN: 
    fDraw = TRUE; 
    ptPrevious.x = LOWORD(lParam); 
    ptPrevious.y = HIWORD(lParam); 
    return 0L; 
 
case WM_LBUTTONUP: 
    if (fDraw) 
    { 
        hdc = GetDC(hwnd); 
        MoveToEx(hdc, ptPrevious.x, ptPrevious.y, NULL); 
        LineTo(hdc, LOWORD(lParam), HIWORD(lParam)); 
        ReleaseDC(hwnd, hdc); 
    } 
    fDraw = FALSE; 
    return 0L; 
 
case WM_MOUSEMOVE: 
    if (fDraw) 
    { 
        hdc = GetDC(hwnd); 
        MoveToEx(hdc, ptPrevious.x, ptPrevious.y, NULL); 
        LineTo(hdc, ptPrevious.x = LOWORD(lParam), 
          ptPrevious.y = HIWORD(lParam)); 
        ReleaseDC(hwnd, hdc); 
    } 
    return 0L; 
```



An application that enables drawing, as in this example, typically records either the points or lines so that the lines can be redrawn whenever the window is updated. Drawing applications often use a memory device context and an associated bitmap to store lines that were drawn by using a mouse.

 

 
