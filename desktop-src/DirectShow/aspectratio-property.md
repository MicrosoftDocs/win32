---
description: The AspectRatio property retrieves the aspect ratio of the current video stream as authored on the disc.
ms.assetid: c341538e-0b33-4173-a5ca-56b3f7305022
title: AspectRatio Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AspectRatio Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `AspectRatio` property retrieves the aspect ratio of the current video stream as authored on the disc.

``` syntax
[  nAspectRatio = ] MSWebDVD.AspectRatio 
```

## Return Value

Returns a number representing the aspect ratio of the current video stream as authored on the disc (1.33 for a 4:3 aspect ratio or 1.78 for a 16:9 aspect ratio).

## Remarks

This property is read-only with no default value.

 

 



