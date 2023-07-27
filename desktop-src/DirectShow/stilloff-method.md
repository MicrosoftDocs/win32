---
description: The StillOff method resumes playback, canceling still mode.
ms.assetid: 62091aad-8a78-4543-a844-a4227aed81df
title: StillOff Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# StillOff Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `StillOff` method resumes playback, canceling still mode.

``` syntax
MSWebDVD.StillOff()
```

## Return Value

No return value.

## Remarks

The [DVD Navigator](dvd-navigator-filter.md) goes into still mode when it encounters a still frame authored on the disc. It notifies your application by sending an EC\_DVD\_STILL\_ON event. Still mode is different from the DVD Navigator being in a paused state because of a user operation. Calling `StillOff` resumes playback from still mode but does not restart the DVD Navigator when it is in a paused state.

 

 



