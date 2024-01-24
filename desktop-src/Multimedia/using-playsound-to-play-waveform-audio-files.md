---
title: Using PlaySound to Play Waveform-Audio Files
description: Using PlaySound to Play Waveform-Audio Files
ms.assetid: 8b7d191b-6b0c-4dff-84de-cb3a5c314b80
keywords:
- waveform audio,PlaySound function
- waveform audio,playing files
- waveform audio,WAV file name extension
- PlaySound function,playing waveform-audio files
- playing waveform-audio files,PlaySound function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using PlaySound to Play Waveform-Audio Files

\[The feature associated with this page, [Waveform Audio](/windows/win32/multimedia/waveform-audio), is a legacy feature. It has been superseded by [WASAPI](/windows/win32/coreaudio/wasapi) and [Audio Graphs](/windows/uwp/audio-video-camera/audio-graphs). **WASAPI** and **Audio Graphs** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **WASAPI** and **Audio Graphs** instead of **Waveform Audio**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Most waveform-audio files use the .WAV filename extension.

The following statement plays the C:\\SOUNDS\\BELLS.WAV file:


```C++
PlaySound("C:\\SOUNDS\\BELLS.WAV", NULL, SND_SYNC); 
```



If the specified file does not exist, or if the file does not fit into the available memory, [**PlaySound**](/previous-versions//dd743680(v=vs.85)) plays the default system sound. If no default system sound has been defined, **PlaySound** fails without producing any sound. If you do not want the default system sound to play, specify the SND\_NODEFAULT flag, as shown in the following example:


```C++
PlaySound("C:\\SOUNDS\\BELLS.WAV", NULL, SND_SYNC | SND_NODEFAULT); 
```



 

 