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
ms.date: 05/31/2018
---

# Using PlaySound to Play Waveform-Audio Files

Most waveform-audio files use the .WAV filename extension.

The following statement plays the C:\\SOUNDS\\BELLS.WAV file:


```C++
PlaySound("C:\\SOUNDS\\BELLS.WAV", NULL, SND_SYNC); 
```



If the specified file does not exist, or if the file does not fit into the available memory, [**PlaySound**](/previous-versions//dd743680(v=vs.85)) plays the default system sound. If no default system sound has been defined, **PlaySound** fails without producing any sound. If you do not want the default system sound to play, specify the SND\_NODEFAULT flag, as shown in the following example:


```C++
PlaySound("C:\\SOUNDS\\BELLS.WAV", NULL, SND_SYNC | SND_NODEFAULT); 
```



 

 