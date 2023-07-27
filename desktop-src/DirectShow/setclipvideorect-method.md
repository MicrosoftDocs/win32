---
description: The SetClipVideoRect method zooms the video display to the specified subrectangle.
ms.assetid: 3940a382-8d53-4ff9-b024-38de1aa00f54
title: SetClipVideoRect Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# SetClipVideoRect Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `SetClipVideoRect` method zooms the video display to the specified subrectangle.

``` syntax
MSWebDVD.SetClipVideoRect(oRect)
```

## Parameters

<dl> <dt>

<span id="oRect"></span><span id="orect"></span><span id="ORECT"></span>*oRect*
</dt> <dd>

Specifies a [DVDRect](dvdrect-object.md) object, which contains the clipping rectangle.

</dd> </dl>

## Return Value

No return value.

## Remarks

When you set a new clipping rectangle, the object enlarges that area to fit within the application's overall display dimensions. This creates the effect zooming in on a particular area of the screen. To specify the rectangle, create a new [DVDRect](dvdrect-object.md) object and fill in its properties.

The most common rectangle for video display is 720 x 540.

## See also

<dl> <dt>

[**GetClipVideoRect**](getclipvideorect-method.md)
</dt> </dl>

 

 



