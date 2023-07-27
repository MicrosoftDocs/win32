---
description: The CanStep method determines whether the MPEG-2 decoder on the local system can perform frame stepping in a specified direction.
ms.assetid: 21721722-0bf4-4cc7-a0e4-96b353888948
title: CanStep Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CanStep Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `CanStep` method determines whether the MPEG-2 decoder on the local system can perform frame stepping in a specified direction.

``` syntax
[ bCanStep = ] MSWebDVD.CanStep(bDirection)
```

## Parameters

<dl> <dt>

<span id="bDirection"></span><span id="bdirection"></span><span id="BDIRECTION"></span>*bDirection*
</dt> <dd>

Boolean used as a flag to specify the direction, forward or backward, of decoder's frame-stepping ability.



| Value | Description                                          |
|-------|------------------------------------------------------|
| true  | Can decoder step backward?                           |
| false | Can decoder step forward? This is the default value. |



 

</dd> </dl>

## Return Value

Returns a Boolean value of true if the decoder can step in the specified direction, and false otherwise.

## Remarks

Not all hardware MPEG-2 decoders support the new frame stepping capabilities in DirectShow® 8.0. This method queries the decoder for its frame stepping capabilities. If the decoder can perform frame stepping, an application can use the [**Step**](step-method.md) method to step through frames. This method will always return **true** if a software decoder is being used.

 

 



