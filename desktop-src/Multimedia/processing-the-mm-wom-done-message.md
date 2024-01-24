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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Processing the MM\_WOM\_DONE Message

\[The feature associated with this page, [Waveform Audio](/windows/win32/multimedia/waveform-audio), is a legacy feature. It has been superseded by [WASAPI](/windows/win32/coreaudio/wasapi) and [Audio Graphs](/windows/uwp/audio-video-camera/audio-graphs). **WASAPI** and **Audio Graphs** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **WASAPI** and **Audio Graphs** instead of **Waveform Audio**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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



 

 




