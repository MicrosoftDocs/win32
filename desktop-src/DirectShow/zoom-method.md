---
description: The Zoom method zooms the video display in or out, centered on a given set of screen coordinates.
ms.assetid: 050f1264-8fbe-4322-970c-184275d5b219
title: Zoom Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Zoom Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `Zoom` method zooms the video display in or out, centered on a given set of screen coordinates.

``` syntax
MSWebDVD.Zoom(iXPos, iYPos, iZoomRatio)
```

## Parameters

<dl> <dt>

<span id="iXPos"></span><span id="ixpos"></span><span id="IXPOS"></span>*iXPos*
</dt> <dd>

Specifies the x-coordinate at the center of the rectangular zoom area as an Integer.

</dd> <dt>

<span id="iYPos"></span><span id="iypos"></span><span id="IYPOS"></span>*iYPos*
</dt> <dd>

Specifies the y-coordinate at the center of the rectangle to be zoomed as an Integer.

</dd> <dt>

<span id="iZoomRatio"></span><span id="izoomratio"></span><span id="IZOOMRATIO"></span>*iZoomRatio*
</dt> <dd>

Specifies the magnification factor applied to the current zoom value as an Integer. The total maximum value depends on what the hardware overlay can support; this is typically a factor of 32 to 64 times the original size.

</dd> </dl>

## Return Value

No return value.

## Remarks

The new zoom ratio stays in effect until it is restored to the original size or changed again. In other words, two calls to this method specifying an *iZoomRatio* of two will result in a zoom ratio four times larger than the original video size. If the user tries to zoom beyond what the hardware can support, this method will succeed but do nothing.

The [**SetClipVideoRect**](setclipvideorect-method.md) method is another way to zoom in; the only difference between the two methods is the way in which the zoom rectangle is specified.

 

 



