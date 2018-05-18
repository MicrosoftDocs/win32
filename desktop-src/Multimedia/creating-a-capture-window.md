---
title: Creating a Capture Window
description: Creating a Capture Window
ms.assetid: 'a727ce14-9b12-4f21-bab4-fa2eb245dce7'
keywords: ["capCreateCaptureWindow function"]
---

# Creating a Capture Window

The following example creates a capture window by using the [**capCreateCaptureWindow**](capcreatecapturewindow.md) function.


```C++
hWndC = capCreateCaptureWindow (
    TEXT("My Capture Window"),   // window name if pop-up 
    WS_CHILD | WS_VISIBLE,       // window style 
    0, 0, 160, 120,              // window position and dimensions
    (HWND) hwndParent, 
    (int) nID /* child ID */); 
```



## Related topics

<dl> <dt>

[Using Video Capture](using-video-capture.md)
</dt> </dl>

 

 




