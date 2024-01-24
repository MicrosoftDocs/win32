---
description: The Volume property sets or retrieves the speaker volume for the audio stream output.
ms.assetid: 'b6e22d07-525b-4af2-898c-ce3ed16ea9c1'
title: Volume Property
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Volume Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `Volume` property sets or retrieves the speaker volume for the audio stream output.

``` syntax
[ iVolume = ] MSWebDVD.Volume
```

## Return Value

Returns the volume level as attenuation in decibels as an Integer.

## Remarks

This property is read/write with a default value of 0. Full volume is 0, and 10,000 is silence; the scale is logarithmic. Multiply the desired decibel level by 100 (for example 10,000 = 100 dB).

 

 



