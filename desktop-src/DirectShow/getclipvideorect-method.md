---
description: The GetClipVideoRect method retrieves the clipping rectangle currently defined for the video display.
ms.assetid: ea24649f-206e-4557-bff3-9f289710d1b4
title: GetClipVideoRect Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# GetClipVideoRect Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `GetClipVideoRect` method retrieves the clipping rectangle currently defined for the video display.

``` syntax
[ oClipRect = ] MSWebDVD.GetClipVideoRect()
```

## Return Value

Returns a [DVDRect](dvdrect-object.md) object that defines the rectangle.

## See also

<dl> <dt>

[**SetClipVideoRect**](setclipvideorect-method.md)
</dt> </dl>

 

 



