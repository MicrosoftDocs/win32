---
title: Creating an Error Callback Function
description: Creating an Error Callback Function
ms.assetid: a489ec94-c566-44b1-aa93-9b43f23de744
keywords:
- capSetCallbackOnError macro
ms.topic: article
ms.date: 05/31/2018
---

# Creating an Error Callback Function

The following example is a simple error callback function. Register this callback by using the [**capSetCallbackOnError**](/windows/desktop/api/Vfw/nf-vfw-capsetcallbackonerror) macro.


```
TCHAR gachBuffer[100]; // Global buffer.

// ErrorCallbackProc: error callback function. 
// hWnd:              capture window handle. 
// nErrID:            error code for the encountered error. 
// lpErrorText:       error text string for the encountered error. 
// 
LRESULT PASCAL ErrorCallbackProc(HWND hWnd, int nErrID,
    LPTSTR lpErrorText) 
{ 
 
    if (!hWnd) 
        return FALSE; 
 
    if (nErrID == 0)            // Starting a new major function. 
        return TRUE;            // Clear out old errors. 
 
    // Show the error identifier and text. 
    _stprintf_s(gachBuffer, TEXT("Error# %d"), nErrID); 
 
    MessageBox(hWnd, lpErrorText, gachBuffer, 
        MB_OK | MB_ICONEXCLAMATION); 
 
    return (LRESULT) TRUE; 
} 
```



## Related topics

<dl> <dt>

[Using Video Capture](using-video-capture.md)
</dt> </dl>

 

 




