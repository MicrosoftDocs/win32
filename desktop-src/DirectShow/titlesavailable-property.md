---
description: The TitlesAvailable property retrieves the number of titles available on the disc.
ms.assetid: 821ab1dc-7a42-407f-8fcd-8662036a6fa5
title: TitlesAvailable Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# TitlesAvailable Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `TitlesAvailable` property retrieves the number of titles available on the disc.

``` syntax
[ iTitles = ] MSWebDVD.TitlesAvailable
```

## Return Value

Returns the number of available titles as an Integer value from 1 through 99.

## Remarks

This property is read-only with no default value.

 

 



