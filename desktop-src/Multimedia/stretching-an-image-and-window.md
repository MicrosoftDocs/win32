---
title: Stretching an Image and Window
description: Stretching an Image and Window
ms.assetid: 661992eb-b012-47eb-84bc-cd12834c6270
keywords:
- MCIWndGetDest macro
- MCIWndPutDest macro
- GetWindowRect function
- SetWindowPos function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Stretching an Image and Window

\[The feature associated with this page, [MCIWnd Window Class](/windows/win32/multimedia/mciwnd-window-class), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCIWnd Window Class**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following example stretches the images of a video clip and changes the aspect ratio of the displayed frames. The frames displayed in the MCIWnd window are twice the height and three times the width of the original frame. The [**MCIWndGetDest**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetdest) and [**MCIWndPutDest**](/windows/desktop/api/Vfw/nf-vfw-mciwndputdest) macros retrieve and redefine the destination rectangle coordinates. The [GetWindowRect](/windows/win32/api/winuser/nf-winuser-getwindowrect) and [SetWindowPos](/windows/win32/api/winuser/nf-winuser-setwindowpos) functions manage changes to the MCIWnd window dimensions.


```C++
// extern RECT rCurrent, rDest; 
 
case WM_COMMAND: 
   switch (wParam) 
   { 
       case IDM_CREATEMCIWND: 
           g_hwndMCIWnd = MCIWndCreate(hwnd, 
           g_hinst, 
           WS_CHILD | WS_VISIBLE, 
          "sample.avi"); 
           break;    
 
       case IDM_RESIZEWINDOW: // destination RECT and playback area
           GetWindowRect(g_hwndMCIWnd, &rWin);     // window size 
           MCIWndGetDest(g_hwndMCIWnd, &rCurrent); // destination RECT
           rDest.top = rCurrent.top;               // new boundaries 
           rDest.right = rCurrent.right; 
           rDest.left = rCurrent.left + 
               ((rCurrent.left - rCurrent.right) * 3); 
           rDest.bottom = rCurrent.top + 
               ((rCurrent.bottom - rCurrent.top) * 2); 
           MCIWndPutDest(g_hwndMCIWnd, &rDest); // new RECT
           SetWindowPos(g_hwndMCIWnd,           // window to resize 
               NULL,                          // z-order: don't care 
               0, 0,                          // position: don't care
               rDest.right - rDest.left,      // width 
               (rWin.bottom - rWin.top +           // height (window - 
               (rCurrent.bottom - rCurrent.top) +  //  original RECT +
               (rDest.bottom - rDest.top)),        //  new RECT
               SWP_NOMOVE | SWP_NOZORDER | SWP_NOACTIVATE); 
           break; 
   } 
   break; 
 
   // Handle other messages here. 
```



 

 