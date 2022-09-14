---
title: Cropping an Image
description: Cropping an Image
ms.assetid: 6600751c-d4b6-481d-bf69-be2d34244c05
keywords:
- MCIWndGetSource macro
- MCIWndPutSource macro
ms.topic: article
ms.date: 05/31/2018
---

# Cropping an Image

The following example creates an MCIWnd window and loads an AVI file. The window includes a crop command in the menu, which crops one-quarter of the height or width from each of the four sides of the frame. The example retrieves the current (initial) dimensions of the source rectangle by using the [**MCIWndGetSource**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetsource) macro. The modified source rectangle is half the original height and width and is centered in the original frame. The call to the [**MCIWndPutSource**](/windows/desktop/api/Vfw/nf-vfw-mciwndputsource) macro redefines the coordinates of the source rectangle.


```C++
// extern RECT rSource, rDest; 
 
case WM_COMMAND: 
    switch (wParam) 
    { 
        case IDM_CREATEMCIWND: 
            g_hwndMCIWnd = MCIWndCreate( hwnd, 
                g_hinst, 
                WS_CHILD | WS_VISIBLE, 
                "sample.avi" ); 
            break; 
        case IDM_CROPIMAGE:                          // crops image 
            MCIWndGetSource(g_hwndMCIWnd, &rSource); // source rectangle
            rDest.left = rSource.left +              // new boundaries
                ((rSource.right - rSource.left) / 4); 
            rDest.right = rSource.right - 
                ((rSource.right - rSource.left) / 4); 
            rDest.top = rSource.top + 
                ((rSource.bottom - rSource.top) / 4); 
            rDest.bottom = rSource.bottom - 
                ((rSource.bottom - rSource.top) / 4); 
 
            MCIWndPutSource(g_hwndMCIWnd, &rDest);   // new source rectangle 
    } 
    break; 

    // Handle other messages here. 
```



 

 




