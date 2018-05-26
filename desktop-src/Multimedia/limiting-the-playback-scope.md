---
title: Limiting the Playback Scope
description: Limiting the Playback Scope
ms.assetid: 080ab96f-1cb5-48d4-ac0a-8fd9ba68a31a
keywords:
- MCIWndPlayFrom macro
- MCIWndPlayTo macro
- MCIWndPlayFromTo macro
- MCI playback commands
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Limiting the Playback Scope

Controlling playback begins with the [**MCIWndPlay**](/windows/win32/Vfw/nf-vfw-mciwndplay?branch=master) macro, which plays the content or file associated with an MCIWnd window from the current playback position to the end of the content. If you want to limit playback to a specific portion of the content or file, you can choose from the other playback MCIWnd macros: [**MCIWndPlayFrom**](/windows/win32/Vfw/nf-vfw-mciwndplayfrom?branch=master), [**MCIWndPlayTo**](/windows/win32/Vfw/nf-vfw-mciwndplayto?branch=master), and [**MCIWndPlayFromTo**](/windows/win32/Vfw/nf-vfw-mciwndplayfromto?branch=master).

You also need to set an appropriate time format. The time format determines whether the content is measured in frames, milliseconds, tracks, or some other units.

The following example creates an MCIWnd window and provides menu commands to play the last third, first third, or middle third of the content. These menu commands use **MCIWndPlayFrom**, **MCIWndPlayTo**, and **MCIWndPlayFromTo** to play the content segments. The example also uses the [**MCIWndGetStart**](/windows/win32/Vfw/nf-vfw-mciwndgetstart?branch=master) and [**MCIWndGetEnd**](/windows/win32/Vfw/nf-vfw-mciwndgetend?branch=master) macros to identify the beginning and end of the content, and it uses the [**MCIWndHome**](/windows/win32/Vfw/nf-vfw-mciwndhome?branch=master) macro to move the playback position to the beginning of the content.

The [**MCIWndCreate**](/windows/win32/Vfw/nf-vfw-mciwndcreatea?branch=master) function uses the WS\_CAPTION and MCIWNDF\_SHOWALL styles in addition to the standard window styles to display the filename, mode, and current playback position in the title bar of the MCIWnd window.


```C++
case WM_COMMAND: 
    switch (wParam) 
    { 
        case IDM_CREATEMCIWND: 
            g_hwndMCIWnd = MCIWndCreate(hwnd, 
                g_hinst, 
                WS_CHILD | WS_VISIBLE | WS_CAPTION | 
                MCIWNDF_SHOWALL, 
                "sample.avi"); 
            break;
        case IDM_PLAYFROM:                // plays last third of clip 
            MCIWndUseTime(g_hwndMCIWnd);  // millisecond format 
 
        // Get media start and end positions. 
            lStart = MCIWndGetStart(g_hwndMCIWnd); 
            lEnd = MCIWndGetEnd(g_hwndMCIWnd); 
 
        // Determine playback end position. 
            lPlayStart = 2 * (lEnd - lStart) / 3 + lStart; 
 
            MCIWndPlayFrom(g_hwndMCIWnd, lPlayStart); 
            break; 
        case IDM_PLAYTO:                  // plays first third of clip 
            MCIWndUseTime(g_hwndMCIWnd);  // millisecond format 
 
        // Get media start and end positions. 
            lStart = MCIWndGetStart(g_hwndMCIWnd); 
            lEnd = MCIWndGetEnd(g_hwndMCIWnd); 
 
        // Determine playback start position. 
            lPlayEnd = (lEnd - lStart) / 3 + lStart;
 
            MCIWndHome(g_hwndMCIWnd); 
            MCIWndPlayTo(g_hwndMCIWnd, lPlayEnd); 
            break; 
        case IDM_PLAYSOME:               // plays middle third of clip 
            MCIWndUseTime(g_hwndMCIWnd); // millisecond format 
 
        // Get media start and end positions. 
            lStart = MCIWndGetStart(g_hwndMCIWnd); 
            lEnd = MCIWndGetEnd(g_hwndMCIWnd); 
 
        // Determine playback start and end positions. 
            lPlayStart = (lEnd - lStart) / 3 + lStart;
            lPlayEnd = 2 * (lEnd - lStart) / 3 + lStart; 
 
            MCIWndPlayFromTo(g_hwndMCIWnd, lPlayStart, lPlayEnd); 
            break; 
    
    // Handle other commands here. 
    } 
```



 

 




