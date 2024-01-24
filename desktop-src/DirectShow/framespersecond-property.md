---
description: The FramesPerSecond property retrieves the video frame rate for the current DVD title.
ms.assetid: c5d36308-1447-4636-9b3a-4a3f93d27789
title: FramesPerSecond Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# FramesPerSecond Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `FramesPerSecond` property retrieves the video frame rate for the current DVD title.

``` syntax
[ iFramesPerSec = ] MSWebDVD.FramesPerSecond
```

## Return Value

Returns an integer value representing the video frame rate; either 25 or 30 frames per second.

## Remarks

This property is read-only with no default value. NTSC video signals are displayed at 30 frames per second. PAL is displayed at 25 frames per second. A disc is encoded to play on either NTSC or PAL, but cannot play on both.

 

 



