---
title: Previewing Video
description: Previewing Video
ms.assetid: '33ae7d07-5fea-47d7-b60d-4ee412e91dec'
keywords: ["capPreview macro", "capPreviewRate macro"]
---

# Previewing Video

The following example uses the [**capPreviewRate**](cappreviewrate.md) macro to set the frame display rate for preview mode to 66 milliseconds per frame and then uses the [**capPreview**](cappreview.md) macro to place the capture window in preview mode.


```C++
// Create the capture window.
HWND hWndC = capCreateCaptureWindow(TEXT("My Capture Window"),
    WS_CHILD | WS_VISIBLE, 0, 0, 160, 120, hwndParent, nID);

capPreviewRate(hWndC, 66);     // rate, in milliseconds
capPreview(hWndC, TRUE);       // starts preview 

// Preview

capPreview(hWndC, FALSE);        // disables preview 
```



## Related topics

<dl> <dt>

[Using Video Capture](using-video-capture.md)
</dt> </dl>

 

 




