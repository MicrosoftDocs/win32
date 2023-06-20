---
description: Stream Control
ms.assetid: b529b38c-a25c-42dd-aee1-5d263c94202d
title: Stream Control
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Stream Control

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The [**IVMRVideoStreamControl**](/windows/desktop/api/Strmif/nn-strmif-ivmrvideostreamcontrol) interface on the VMR's input pin(s) enables applications and upstream filters to control the behavior of the mixer component, including the Z-order and the active state of the VMR's input streams. Although this interface is exposed on the pins, it operates on the VMR's mixer component, so it is only available when the mixer is loaded, which is when the VMR is processing multiple input streams. Upstream filters use the [**SetColorKey**](/windows/desktop/api/Strmif/nf-strmif-ivmrvideostreamcontrol-setcolorkey) and [**GetColorKey**](/windows/desktop/api/Strmif/nf-strmif-ivmrvideostreamcontrol-getcolorkey) methods to control the source color key. These methods enable effects such as the overlay of animation over video. Simply set the color key to the animation stream's background color, and the VMR will mix that stream with another video stream. Applications should take care not to change the color key to some value that is different than the value being used by an upstream filter, such as a decoder.

Filters use the [**GetStreamActiveState**](/windows/desktop/api/Strmif/nf-strmif-ivmrvideostreamcontrol-getstreamactivestate) and [**SetStreamActiveState**](/windows/desktop/api/Strmif/nf-strmif-ivmrvideostreamcontrol-setstreamactivestate) methods to tell the mixer whether to expect input data from a specified pin. For example, the Line21 Decoder uses these methods to activate the VMR's input pin for Line21 data only when that data is present in the stream. Setting a pin to an inactive state instructs the mixer not to wait for data from a specified pin before compositing the image.

 

 



