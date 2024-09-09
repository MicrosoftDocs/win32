---
description: The GetAudioLanguage method retrieves a string indicating which language is available on the specified audio stream.
ms.assetid: 5ff12058-eb00-4a2c-8d39-88282f68f001
title: GetAudioLanguage Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# GetAudioLanguage Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `GetAudioLanguage` method retrieves a string indicating which language is available on the specified audio stream.

``` syntax
[ slang = ] MSWebDVD.GetAudioLanguage(iStream)
```

## Parameters

<dl> <dt>

<span id="iStream"></span><span id="istream"></span><span id="ISTREAM"></span>*iStream*
</dt> <dd>

Specifies the audio stream number in the current title as an Integer.

</dd> </dl>

## Return Value

Returns a human-readable string identifying the language of the audio stream in the current title.

 

 



