---
description: The CurrentDiscSide property retrieves the current side of the disc.
ms.assetid: a5210a58-bbb0-41fa-b546-1597ca0186e4
title: CurrentDiscSide Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CurrentDiscSide Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `CurrentDiscSide` property retrieves the current side of the disc.

``` syntax
[ iCurSide = ] MSWebDVD.CurrentDiscSide
```

## Return Value

Returns an integer value representing the current side; Side A = 1 and Side B = 2.

## Remarks

This property is read-only with no default value.

 

 



