---
title: Opening the Playback Window
description: Opening the Playback Window
ms.assetid: 180f3fb9-cdcb-49ec-a708-84a597295b2f
keywords:
- MCI_OPEN command
ms.topic: article
ms.date: 05/31/2018
---

# Opening the Playback Window

The following example shows how to use the [**MCI\_OPEN**](mci-open.md) command to set a parent window and create a child of that window.


```C++
MCI_DGV_OPEN_PARMS    mciOpen; 
 
mciOpen.lpstrElementName = lpstrFile;  // Set the filename.
mciOpen.dwStyle = WS_CHILD;            // Set the style. 
mciOpen.hWndParent = hWnd;             // Give a window handle. 
 
if (mciSendCommand(0, MCI_OPEN, 
   (DWORD)(MCI_OPEN_ELEMENT|MCI_DGV_OPEN_PARENT|MCI_DGV_OPEN), 
   (DWORD)(LPSTR)&mciOpen) == 0)
{ 
    // Open operation is successful. Continue. 
} 
```



 

 




