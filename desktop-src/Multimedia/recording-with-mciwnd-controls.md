---
title: Recording with MCIWnd Controls
description: Recording with MCIWnd Controls
ms.assetid: 65a57400-aeea-4a27-8d51-37d3d9e9bd55
keywords:
- MCIWndCreate function
- MCIWndNew macro
ms.topic: article
ms.date: 05/31/2018
---

# Recording with MCIWnd Controls

The following example records waveform audio using the built-in controls of the MCIWnd window. The example creates an MCIWnd window by using the MCIWNDF\_RECORD window style with the [**MCIWndCreate**](/windows/desktop/api/Vfw/nf-vfw-mciwndcreatea) function to add a **Record** button to the toolbar. The [**MCIWndNew**](/windows/desktop/api/Vfw/nf-vfw-mciwndnew) macro indicates a new file is associated with the MCIWnd window and that a waveform-audio device will provide its content. A second menu command, IDM\_SAVEMCIWND, lets the user save the recording and select a filename by using the [**MCIWndSaveDialog**](/windows/desktop/api/Vfw/nf-vfw-mciwndsavedialog) macro.


```C++
case WM_COMMAND: 
    switch (wParam) { 
    case IDM_CREATEMCIWND: 
        g_hwndMCIWnd = MCIWndCreate(hwnd, g_hinst, 
            WS_VISIBLE | MCIWNDF_RECORD, NULL); 
        MCIWndNew(g_hwndMCIWnd, "waveaudio"); 
        break;    
    case IDM_SAVEMCIWND: 
        MCIWndSaveDialog(g_hwndMCIWnd); 
        break; 
    } 
```



 

 




