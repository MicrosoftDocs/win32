---
title: Creating a Frame Callback Function
description: Creating a Frame Callback Function
ms.assetid: 37002ee0-9907-4aab-93cc-50fe9cd21cff
keywords:
- capSetCallbackOnFrame macro
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Frame Callback Function

The following example is a simple frame callback function. Register this callback by using the [**capSetCallbackOnFrame**](/windows/desktop/api/Vfw/nf-vfw-capsetcallbackonframe) macro.


```
TCHAR gachBuffer[100];  // Global buffer.
DWORD gdwFrameNum = 0;

// FrameCallbackProc: frame callback function. 
// hWnd:              capture window handle. 
// lpVHdr:            pointer to structure containing captured 
//                        frame information. 
// 
LRESULT PASCAL FrameCallbackProc(HWND hWnd, LPVIDEOHDR lpVHdr) 
{ 
    if (!hWnd) 
        return FALSE; 
 
    _stprintf_s(gachBuffer, TEXT("Preview frame# %ld "), gdwFrameNum++); 
    SetWindowText(hWnd, gachBuffer); 
    return (LRESULT) TRUE ; 
} 
```



## Related topics

<dl> <dt>

[Using Video Capture](using-video-capture.md)
</dt> </dl>

 

 




