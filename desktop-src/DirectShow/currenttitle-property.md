---
description: The CurrentTitle property retrieves the number of the title currently playing.
ms.assetid: 8e401f39-f2ad-40c0-9707-d4a589fc63b2
title: CurrentTitle Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CurrentTitle Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `CurrentTitle` property retrieves the number of the title currently playing.

``` syntax
[ iCurTitle = ] MSWebDVD.CurrentTitle
```

## Return Value

Returns an integer value from 1 through 99 representing the current disc title.

## Remarks

This property is read-only with no default value.

## See also

<dl> <dt>

[**TitlesAvailable**](titlesavailable-property.md)
</dt> </dl>

 

 



