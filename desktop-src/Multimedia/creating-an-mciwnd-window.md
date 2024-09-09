---
title: Creating an MCIWnd Window
description: Creating an MCIWnd Window
ms.assetid: bd45e813-5807-43cd-bef1-03285df9a018
keywords:
- MCIWnd window,creating
- MCIWndCreate function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Creating an MCIWnd Window

\[The feature associated with this page, [MCIWnd Window Class](/windows/win32/multimedia/mciwnd-window-class), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCIWnd Window Class**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The [**MCIWndCreate**](/windows/desktop/api/Vfw/nf-vfw-mciwndcreatea) function registers and creates an MCIWnd window. The window can be a parent, child, or pop-up window. The following example creates an MCIWnd window as a child window and lets the user control playback by providing access to the trackbar and the **Play**, **Stop**, and **Menu** buttons. The example specifies a handle of a parent window and specifies **NULL** for the window styles, so the default window styles of WS\_CHILD, WS\_BORDER, and WS\_VISIBLE are used to create the MCIWnd window.


```C++
// Global variable and constants 
// extern HINSTANCE g_hinst;       instance handle 
// extern HWND g_hwndMCIWnd;       MCIWnd window handle 
 
case WM_COMMAND: 
    switch (wParam) { 
    case IDM_CREATEMCIWND: 
        g_hwndMCIWnd = MCIWndCreate(hwnd, g_hinst, NULL, 
            "sample.avi"); 
        break;    
    } 
    break; 
```



> [!Note]  
> You could also specify **NULL** for both the parent window handle and the window styles, in which case the default window styles would be WS\_OVERLAPPED and WS\_VISIBLE.

 

 

 




