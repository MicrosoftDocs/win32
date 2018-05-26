---
title: Customizing the Recording Process
description: Customizing the Recording Process
ms.assetid: 9453b9d3-ae9c-4f57-8dd6-f84b9a76618e
keywords:
- MCIWndCreate function
- MCIWndNew macro
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Customizing the Recording Process

You can customize the recording process, taking complete control of most everything — from creating the MCIWnd window to saving the recorded information in a file. The following example queries the MCI device for recording and saving capabilities, and includes menu commands to record at the beginning or end of the content.

The following example uses the [**MCIWndCreate**](/windows/win32/Vfw/nf-vfw-mciwndcreatea?branch=master) function to create a new window and allows you to specify an existing file to store the recorded data and the [**MCIWndNew**](/windows/win32/Vfw/nf-vfw-mciwndnew?branch=master) macro to associate a new file with the window. Alternatively, you can use the [**MCIWndOpen**](/windows/win32/Vfw/nf-vfw-mciwndopen?branch=master) or [**MCIWndOpenDialog**](/windows/win32/Vfw/nf-vfw-mciwndopendialog?branch=master) macro to specify a file.

The example uses the [**MCIWndCanRecord**](/windows/win32/Vfw/nf-vfw-mciwndcanrecord?branch=master) macro to verify that the device can record and the [**MCIWndCanSave**](/windows/win32/Vfw/nf-vfw-mciwndcansave?branch=master) macro to verify that the device save information. The example sets the current playback position by using the [**MCIWndHome**](/windows/win32/Vfw/nf-vfw-mciwndhome?branch=master) and [**MCIWndEnd**](/windows/win32/Vfw/nf-vfw-mciwndend?branch=master) macros. The example starts recording by using the [**MCIWndRecord**](/windows/win32/Vfw/nf-vfw-mciwndrecord?branch=master) macro. After the information is recorded, the example saves it by using the [**MCIWndSaveDialog**](/windows/win32/Vfw/nf-vfw-mciwndsavedialog?branch=master) macro.


```C++
case WM_COMMAND: 
    switch (wParam) 
    { 
        case IDM_CREATEMCIWND: 
            g_hwndMCIWnd = MCIWndCreate( hwnd, g_hinst, 
                WS_VISIBLE | WS_CHILD | 
                MCIWNDF_RECORD,                   // add Record button
                NULL ); 
 
            MCIWndNew(g_hwndMCIWnd, "waveaudio"); // new file 
 
            if( MCIWndCanRecord(g_hwndMCIWnd) ) 
            { 
                MessageBox( hwnd, 
                "Press the red button on the toolbar to record.", 
                "MCIWnd Record", 
                MB_OK ); 
            } 
            else 
            { 
                MessageBox( hwnd, 
                    "This device doesn't record.", 
                    "MCIWnd Record", 
                    MB_OK ); 
            } 
            break; 
        case IDM_RECORDATSTART: 
            if( MCIWndCanRecord(g_hwndMCIWnd) ) 
            { 
                MCIWndHome(g_hwndMCIWnd); 
                MCIWndRecord(g_hwndMCIWnd); 
            } 
            else 
            { 
                MessageBox( hwnd, 
                    "This device doesn't record.", 
                    "MCIWnd Record", 
                    MB_OK); 
            } 
            break; 
        case IDM_RECORDATEND: 
            if( MCIWndCanRecord(g_hwndMCIWnd) ) 
            { 
                MCIWndEnd(g_hwndMCIWnd); 
                MCIWndRecord(g_hwndMCIWnd); 
            } 
            else 
            { 
                MessageBox( hwnd, 
                    "This device doesn't record.", 
                    "MCIWnd Record", 
                    MB_OK); 
            } 
            break; 
        case IDM_SAVEMCIWND: 
            if( MCIWndCanSave(g_hwndMCIWnd) ) 
                MCIWndSaveDialog(g_hwndMCIWnd); 
    } 
    break; 
 
    // Handle other messages here. 
```



 

 




