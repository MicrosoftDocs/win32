---
title: Automating Playback for MCIWnd
description: Automating Playback for MCIWnd
ms.assetid: 7e38e8b1-f56d-4008-83a7-4fba8333e328
keywords:
- MCIWndCreate macro
ms.topic: article
ms.date: 05/31/2018
---

# Automating Playback for MCIWnd

You can automate playback for MCIWnd by specifying certain window styles in the [**MCIWndCreate**](/windows/desktop/api/Vfw/nf-vfw-mciwndcreatea) function. To play the device, the window needs a parent window to process notification messages, a playback area to play AVI files, and notification of device mode changes to identify when playback stops. The window does not need a toolbar. You can set these characteristics by specifying the appropriate styles in **MCIWndCreate**.

The following example uses menu commands to create an MCIWnd window to play content from several different types of devices. The **MCIWndCreate** function creates the MCIWnd window, and devices and files are loaded by using the [**MCIWndOpen**](/windows/desktop/api/Vfw/nf-vfw-mciwndopen) macro in the device-specific commands. When a device finishes playing, you close the device by trapping the [**MCIWNDM\_NOTIFYMODE**](mciwndm-notifymode.md) message and issuing the [**MCIWndClose**](/windows/desktop/api/Vfw/nf-vfw-mciwndclose) macro.


```C++
case WM_COMMAND: 
    switch (wParam) 
    { 
        case IDM_CREATEMCIWND: 
            dwMCIWndStyle = WS_CHILD |     // child window
                WS_VISIBLE |               // visible
                MCIWNDF_NOTIFYMODE |       // notifies of mode changes
                MCIWNDF_NOPLAYBAR;            // hides toolbar 
            g_hwndMCIWnd = MCIWndCreate(hwnd, 
                g_hinst, dwMCIWndStyle, NULL); 
            break; 
        case IDM_PLAYCDA: 
            LoadNGoMCIWnd(hwnd, "CDAudio"); 
            break; 
        case IDM_PLAYWAVE: 
            LoadNGoMCIWnd(hwnd, "SoundWave.WAV"); 
            break; 
        case IDM_PLAYMIDI: 
            LoadNGoMCIWnd(hwnd, "MIDIFile.MID"); 
            break; 
        case IDM_PLAYAVI: 
            LoadNGoMCIWnd(hwnd, "AVIFile.AVI"); 
            break; 
        case IDM_EXIT: 
            MCIWndDestroy(g_hwndMCIWnd); 
            DestroyWindow(hwnd); 
            break; 
    } 
    break; 
 
case MCIWNDM_NOTIFYMODE: 
    if (lParam == MCI_MODE_STOP)  // device stopped
    { 
        MessageBox(hwnd,"","Closing Device",MB_OK); 
        MCIWndClose(g_hwndMCIWnd); 
    } 
    break; 

// Handle other messages here. 
 
// LoadNGoMCIWnd - automatically loads and plays a multimedia device 
// 
// hwnd -  handle to the parent window 
// lpstr - pointer to device or filename played by device 
// 
// Global variable 
// extern HINSTANCE g_hwndMCIWnd;  instance handle to MCIWnd window 
 
VOID LoadNGoMCIWnd(HWND hwnd, LPSTR lpstr) 
{ 
    MessageBox(hwnd, lpstr, "Loading Device", MB_OK); 
    MCIWndOpen(g_hwndMCIWnd, lpstr, NULL);   // new device in window 
    MCIWndPlay(g_hwndMCIWnd);                // plays device 
} 
```



 

 




