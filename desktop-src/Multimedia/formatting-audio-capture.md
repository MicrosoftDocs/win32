---
title: Formatting Audio Capture
description: Formatting Audio Capture
ms.assetid: '3bbe34a6-8fd6-4780-b5af-fcf3d34ef701'
keywords: ["capSetAudioFormat macro"]
---

# Formatting Audio Capture

The following example uses [**capSetAudioFormat**](capsetaudioformat.md) to set the audio format to 11-kHz PCM 8-bit, stereo.


```C++
WAVEFORMATEX wfex;

wfex.wFormatTag = WAVE_FORMAT_PCM;
wfex.nChannels = 2;                // Use stereo
wfex.nSamplesPerSec = 11025;
wfex.nAvgBytesPerSec = 22050;
wfex.nBlockAlign = 2;
wfex.wBitsPerSample = 8;
wfex.cbSize = 0;

capSetAudioFormat(hWndC, &amp;wfex, sizeof(WAVEFORMATEX)); 
 
```



## Related topics

<dl> <dt>

[Using Video Capture](using-video-capture.md)
</dt> </dl>

 

 




