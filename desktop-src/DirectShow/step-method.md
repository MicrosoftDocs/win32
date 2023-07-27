---
description: The Step method advances the DVD-Video stream by the specified number of frames.
ms.assetid: '6f67335e-51c7-4b81-8ab3-86a3d70ac871'
title: Step Method
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Step Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `Step` method advances the DVD-Video stream by the specified number of frames.

``` syntax
MSWebDVD.Step(iFrames)
```

## Parameters

<dl> <dt>

<span id="iFrames"></span><span id="iframes"></span><span id="IFRAMES"></span>*iFrames*
</dt> <dd>

Specifies the number of frames to step as an Integer.

</dd> </dl>

## Return Value

No return value.

## Remarks

Before calling this method, call [**CanStep**](canstep-method.md) to determine whether the decoder supports frame stepping.

If the DVD-Video is playing in reverse mode when this method is called, and the decoder supports reverse frame stepping, then the frame stepping is done in reverse.

 

 



