---
title: Using PlaySound to Loop Sounds
description: Using PlaySound to Loop Sounds
ms.assetid: 747b9a76-5ff3-488e-ba85-c4d926e1e723
keywords:
- waveform audio,PlaySound function
- waveform audio,looping sounds
- waveform audio,fdwSound parameter
- PlaySound function,looping sounds
- PlaySound function,fdwSound parameter
- looping waveform-audio sounds
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using PlaySound to Loop Sounds

\[The feature associated with this page, [Waveform Audio](/windows/win32/multimedia/waveform-audio), is a legacy feature. It has been superseded by [WASAPI](/windows/win32/coreaudio/wasapi) and [Audio Graphs](/windows/uwp/audio-video-camera/audio-graphs). **WASAPI** and **Audio Graphs** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **WASAPI** and **Audio Graphs** instead of **Waveform Audio**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

If you specify the SND\_LOOP and SND\_ASYNC flags for the *fdwSound* parameter of the [**PlaySound**](/previous-versions//dd743680(v=vs.85)) function, the sound will continue to play repeatedly as shown in the following example:


```C++
PlaySound("C:\\SOUNDS\\BELLS.WAV", NULL, SND_LOOP | SND_ASYNC); 
```



If you want to loop a sound, you must play it asynchronously; you cannot use the SND\_SYNC flag with the SND\_LOOP flag. A looped sound will continue to play until you call **PlaySound** to play another sound. To stop playing a sound (looped or asynchronous) without playing another sound, use the following statement:


```C++
PlaySound(NULL, NULL, 0); 
```



 

 