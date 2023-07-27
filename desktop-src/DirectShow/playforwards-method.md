---
description: The PlayForwards method starts forward playback from the current location at the specified speed.
ms.assetid: 4f1a3e74-b343-413d-8df7-6c4bea39c62d
title: PlayForwards Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PlayForwards Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `PlayForwards` method starts forward playback from the current location at the specified speed.

``` syntax
MSWebDVD.PlayForwards(nSpeed)
```

## Parameters

<dl> <dt>

<span id="nSpeed"></span><span id="nspeed"></span><span id="NSPEED"></span>*nSpeed*
</dt> <dd>

Specifies the speed at which to play as an Integer value. This value is a multiplier—1.0 is normal playback speed; 2.0 is double speed, 0.5 is half speed, and so on. When**nSpeed**does not equal 1.0, audio is muted and the subpicture is turned off.

</dd> </dl>

## Return Value

No return value.

## See also

<dl> <dt>

[**PlayBackwards**](playbackwards-method.md)
</dt> </dl>

 

 



