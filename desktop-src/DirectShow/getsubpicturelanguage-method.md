---
description: The GetSubpictureLanguage method retrieves the language for the specified subpicture stream.
ms.assetid: 2a2e6961-99c3-4200-b462-b381f9e37066
title: GetSubpictureLanguage Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# GetSubpictureLanguage Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `GetSubpictureLanguage` method retrieves the language for the specified subpicture stream.

``` syntax
[ sLang = ] MSWebDVD.GetSubpictureLanguage(iStream)
```

## Parameters

<dl> <dt>

<span id="iStream"></span><span id="istream"></span><span id="ISTREAM"></span>*iStream*
</dt> <dd>

Specifies the subpicture stream number whose text language you want to retrieve as an Integer.

</dd> </dl>

## Return Value

Returns a human-readable string identifying the language of the audio stream in the current title.

 

 



