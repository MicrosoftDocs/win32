---
description: The IsAudioStreamEnabled method retrieves a value indicating whether the specified audio stream is enabled in the current title.
ms.assetid: df6c69a7-6eb0-4662-a3aa-f3f895b42cbc
title: IsAudioStreamEnabled Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IsAudioStreamEnabled Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `IsAudioStreamEnabled` method retrieves a value indicating whether the specified audio stream is enabled in the current title.

``` syntax
[bEnabled = ] MSWebDVD.IsAudioStreamEnabled(iStream)
```

## Parameters

<dl> <dt>

<span id="iStream"></span><span id="istream"></span><span id="ISTREAM"></span>*iStream*
</dt> <dd>

Specifies the audio stream as an Integer value from 0 through 7.

</dd> </dl>

## Return Value

Returns a Boolean value indicating whether the specified audio stream is available for the current title. True means it is available.

## Remarks

Although a disc can contain up to eight independent audio streams, each stream is not necessarily available for each title. For example, a main movie title might have three audio streams for English, Spanish, and Japanese, but the "Coming Attractions" title might have only one audio stream in English. Always verify that a stream is available for a title before setting the [**CurrentAudioStream**](currentaudiostream-property.md) property.

 

 



