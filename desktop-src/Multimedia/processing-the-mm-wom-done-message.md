---
title: Processing the MM_WOM_DONE Message
description: Processing the MM\_WOM\_DONE Message
ms.assetid: 215167d0-3020-453d-b6b3-cee5803836c9
keywords:
- waveform audio,messages
- auxiliary audio,messages
- waveform audio,MM_WOM_DONE message
- auxiliary audio,MM_WOM_DONE message
- MM_WOM_DONE message
ms.topic: article
ms.date: 05/31/2018
---

# Processing the MM\_WOM\_DONE Message

The following example shows how to process the [**MM\_WOM\_DONE**](mm-wom-done.md) message. This example assumes the application does not play multiple data blocks, so it can close the output device after playing a single data block.


```C++
// WndProc--Main window procedure. 
LRESULT FAR PASCAL WndProc(HWND hWnd, UINT msg, WPARAM wParam, 
    LPARAM lParam) 
{ 
switch (msg) 
{ 
    case MM_WOM_DONE: 
 
    // A waveform-audio data block has been played and 
    // can now be freed. 
    waveOutUnprepareHeader((HWAVEOUT) wParam, 
        (LPWAVEHDR) lParam, sizeof(WAVEHDR) ); 
    
    // Free hData memory. 
    
    waveOutClose((HWAVEOUT) wParam); 
    break; 
    } 
    return DefWindowProc(hWnd, msg, wParam, lParam); 
} 
```



 

 




