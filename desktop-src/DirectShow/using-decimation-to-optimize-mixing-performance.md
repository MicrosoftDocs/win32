---
description: Using Decimation to Optimize Mixing Performance
ms.assetid: 94d4ce86-9d60-4fd4-ab01-851dc073680b
title: Using Decimation to Optimize Mixing Performance
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using Decimation to Optimize Mixing Performance

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!IMPORTANT]
> The optimization described in this section is highly dependent on the underlying hardware. Unless you can guarantee what type of graphics hardware will be used with the application, it may seriously degrade the appearance of the video image.

 

HDTV requires a lot of processing power, which on newer systems is provided mostly by the graphics card. But even if the graphics card and the decoder can support resolutions of 1920x1080, the user may not always have their monitor set to this resolution. In this case, the graphics chip is required to create a 1920 x 1080 image, and then reduce the resolution before sending it to the frame buffer.

Since this is a waste of processing power, the VMR provides a way to decimate (reduce) the image at the time it is being rendered onto the DirectDraw surface. This eliminates the extra memory copy required if the image has to be resized after it has been rendered.

**VMR-7:** To enable decimation, call [**IVMRMixerControl::SetMixingPrefs**](/windows/desktop/api/Strmif/nf-strmif-ivmrmixercontrol-setoutputrect) with the MixerPref\_DecimateOutput flag.

**VMR-9:** To enable decimation, call [**IVMRMixerControl9::SetMixingPrefs**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrmixercontrol9-setmixingprefs) with the MixerPref9\_DecimateOutput flag.

The **SetMixingPrefs** method must be called before the VMR is connected. The mixing preference flags cannot be changed once the graph is running.

## Related topics

<dl> <dt>

[Using VMR Mixing Mode](using-vmr-mixing-mode.md)
</dt> </dl>

 

 



