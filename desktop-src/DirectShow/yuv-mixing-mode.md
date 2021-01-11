---
description: YUV Mixing Mode
ms.assetid: 296b1d96-1824-4000-8bec-158925555177
title: YUV Mixing Mode
ms.topic: article
ms.date: 05/31/2018
---

# YUV Mixing Mode

This topic applies to Windows XP Service Pack 2 or later.

Starting in Windows XP Service Pack 2, the VMR supports a mixing mode called YUV mixing mode. This mode is most useful for advanced TV or DVD applications. It trades some of the power of the VMR mixer for better performance on low end graphics hardware that uses a unified memory architecture design. YUV mixing mode is supported on both the VMR-7 and VMR-9.

**Advantages**

YUV mixing mode has several advantages relating to rendering performance over the original RGB mixing mode supported by the VMR:

-   When the VMR is in YUV mixing mode, all de-interlacing and video stream composition operations are performed in YUV color space. YUV surfaces typically require from 50% to 60% less memory bandwidth than equivalent RGB surfaces.
-   The deinterlacing and stream composition are performed by a single call to the graphics driver. The driver can use the graphics hardware's multi-texturing capabilities, resulting in additional memory bandwidth savings.

Although any video application can use YUV mixing mode, it is primarily intended for two types of video playback application:

1.  TV applications that display closed captions or teletext.
2.  DVD applications display DVD subpicture data or closed captions.

**Restrictions**

A number of restrictions are enforced by the VMR when it is put into YUV mixing mode:

-   Stream 0 (the stream connected to Input Pin 0) can be progressive or interlaced; all other streams must be progressive.
-   GUID\_NULL (weave mode) is not allowed for stream 0.
-   DeinterlacePref\_Weave cannot be used as a fallback mode because this could prevent a de-interlace device from being created. YUV mixing mode requires a deinterlace device even if the incoming video is not interlaced.
-   No changes can be made to the planar alpha value associated with each VMR input stream.
-   The user cannot alter the Z-order of the connected video streams. The default Z-order is taken from the pin order.
-   Color keying is not supported.
-   Input pin 0 must receive the video stream.
-   The other inputs pins can only receive video sub-stream data such as DVD sub-picture, closed captions or teletext.
-   The other inputs pins can only accept per-pixel alpha YUV formats, such as AYUV, AI44 and IA44.
-   None of the VMR's input pins can accept any RGB formats.
-   Application supplied bitmap images can no longer be combined with the video prior to presentation to the display.
-   Individual sub-streams cannot be inverted horizontally or vertically using the VMR's mixer "output rectangle" functions. "Normal" stream re-positioning and re-sizing is supported.
-   The mixing background color (specified by [**IVMRMixerControl::SetBackgroundClr**](/windows/desktop/api/Strmif/nf-strmif-ivmrmixercontrol-setbackgroundclr)) is still specified in the RGB color space, just as in RGB mixing mode.

**Configuration**

Applications must explicitly configure the VMR to take advantage of YUV mixing mode; the original RGB mixing mode remains the default mixing mode. To enable YUV mixing mode in the VMR-7, call [**IVMRMixerControl::SetMixingPrefs**](/windows/desktop/api/Strmif/nf-strmif-ivmrmixercontrol-setoutputrect) with the MixerPref\_RenderTargetYUV flag. This call must be made before any of the VMR's input pins are connected. To enable YUV mixing mode in the VMR-9, call [**IVMRMixerControl9::SetMixingPrefs**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrmixercontrol9-setmixingprefs) with the MixerPref9\_RenderTargetYUV flag.

The only way to determine if the VMR-7 supports the new YUV mixing mode is to try setting the VMR into that mode. If the call succeeds, you can still put the VMR back into RGB mixing mode if necessary. After it is set into YUV mixing mode, the VMR can only be changed back to RGB mixing mode after all input pins have been disconnected.

In YUV mixing mode, you can reduce the load on the graphics processing unit (GPU) by applying the following flags in the **SetMixingPrefs** method:



| Flag                                                                                 | Description                                                      |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------|
| VMR-7: MixerPref\_DynamicSwitchToBOBVMR-9: MixerPref9\_DynamicSwitchToBOB<br/> | Switch to bob deinterlacing.                                     |
| VMR-7: MixerPref\_DynamicDecimateBy2VMR-9: MixerPref\_DynamicDecimateBy2<br/>  | Decimate the image by a factor of 2 horizontally and vertically. |



 

You can add or remove these flags while the filter graph is running; the change is applied when the VMR mixer composes the next video frame. The flags are not mutually exclusive. These settings reduce the quality of the image, so typically you would apply them only when video quality is less important — for example, if video is playing in a small portion of the user interface.

## Related topics

<dl> <dt>

[Using VMR Mixing Mode](using-vmr-mixing-mode.md)
</dt> </dl>

 

 




