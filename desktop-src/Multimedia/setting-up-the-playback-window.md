---
title: Setting Up the Playback Window
description: Setting Up the Playback Window
ms.assetid: 4cf27099-e5e5-48f8-8d61-0a3d0e0d9499
keywords:
- mciSendCommand function
ms.topic: article
ms.date: 05/31/2018
---

# Setting Up the Playback Window

The following example finds the dimensions needed to play an AVI file, creates a window corresponding to that size, and plays the file in the window by using the MCIAVI driver. It uses the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function


```C++
HWND hwnd; 
MCI_DGV_RECT_PARMS mciRect; 
 
// Get the movie dimensions with MCI_WHERE. 
 
mciSendCommand(wDeviceID, MCI_WHERE, MCI_DGV_WHERE_SOURCE, 
    (DWORD)(LPSTR)&mciRect); 
 
// Create the playback window. Make it bigger for the border. 
// Note that the right and bottom members of RECT structures in MCI 
// are unusual; rc.right is set to the rectangle's width, and 
// rc.bottom is set to the rectangle's height.

hwndMovie = CreateWindow("mywindow", "Playback", 
    WS_CHILD|WS_BORDER, 0,0, 
    mciRect.rc.right+(2*GetSystemMetric(SM_CXBORDER)),
    mciRect.rc.bottom+(2*GetSystemMetric(SM_CYBORDER)), 
    hwndParent, hInstApp, NULL); 
 
if (hwndMovie){ 
    // Window created OK; make it the playback window. 
 
    MCI_DGV_WINDOW_PARMS mciWindow; 
 
    mciWindow.hWnd = hwndMovie; 
    mciSendCommand(wDeviceID, MCI_WINDOW, MCI_DGV_WINDOW_HWND, 
        (DWORD)(LPSTR)&mciWindow); 
 
} 
```



 

 