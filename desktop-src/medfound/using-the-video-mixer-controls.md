---
description: Using the Video Mixer Controls
ms.assetid: 475996c6-a205-4133-8882-f55beaf9f8fd
title: Using the Video Mixer Controls
ms.topic: article
ms.date: 05/31/2018
---

# Using the Video Mixer Controls

The EVR mixer provides several interfaces that an application can use to control how the mixer processes video. These interfaces can be used in either DirectShow or Media Foundation.



| Interface                                                      | Description                                                                                                                                                                                                                                 |
|----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IMFVideoMixerBitmap**](/windows/desktop/api/evr9/nn-evr9-imfvideomixerbitmap) interface   | Alpha-blends a static bitmap image onto the video.                                                                                                                                                                                          |
| [**IMFVideoMixerControl**](/windows/desktop/api/evr/nn-evr-imfvideomixercontrol) interface | Controls how the EVR mixes video substreams.                                                                                                                                                                                                |
| [**IMFVideoProcessor**](/windows/desktop/api/evr9/nn-evr9-imfvideoprocessor) interface       | Controls color adjustment, image filters, and other video processing capabilities. This interface provides access to functionality implemented by the graphics driver, so the exact capabilities will depend on the user's graphics driver. |



 

The correct way to get pointers to these interfaces depends on whether you are using the DirectShow version of the EVR or the Media Foundation version. For the Media Foundation EVR, it also depends on whether you are using the EVR directly or using it through the [Media Session](media-session.md). (Typically an application will use the EVR through the Media Session, not directly).

To get a pointer to any of these interfaces, do the following:

1.  Get a pointer to the [**IMFGetService**](/windows/desktop/api/mfidl/nn-mfidl-imfgetservice) interface on the EVR.

    -   If you are using the DirectShow EVR filter, call **QueryInterface** on the filter.

    -   If you are using the EVR media sink directly, call **QueryInterface** on the media sink.

    -   If you are using the Media Session, call **QueryInterface** on the Media Session.

2.  If you are using the Media Session, wait for the Media Session to send the [MESessionTopologyStatus](mesessiontopologystatus.md) event with a status value of MF\_TOPOSTATUS\_READY. (Skip this step if you are not using the Media Session.)

3.  Call [**IMFGetService::GetService**](/windows/desktop/api/mfidl/nf-mfidl-imfgetservice-getservice) to get the mixer interface. Use the service identifier MR\_VIDEO\_MIXER\_SERVICE.

## Alpha Blending a Bitmap onto the Video

You can use the [**IMFVideoMixerBitmap**](/windows/desktop/api/evr9/nn-evr9-imfvideomixerbitmap) interface to alpha blend a static bitmap onto the video during playback. You can store the bitmap in a Direct3D surface, specified as an **IDirect3DSurface9** pointer, or use a GDI bitmap.

If you use a Direct3D surface for the bitmap, the surface can contain per-pixel alpha data, which will be used when the mixer alpha-blends the image. Alternatively, you can define a color key—that is, a single color that will be transparent wherever it appears in the bitmap. Also, you can specify an alpha value that will be applied to the entire image. You can also set a source rectangle to crop the bitmap, and a destination rectangle to position the bitmap within the video frame.

To set the bitmap, call [**IMFVideoMixerBitmap::SetAlphaBitmap**](/windows/desktop/api/evr9/nf-evr9-imfvideomixerbitmap-setalphabitmap). This method takes a pointer to an [**MFVideoAlphaBitmap**](/windows/desktop/api/evr9/ns-evr9-mfvideoalphabitmap) structure that specifies the bitmap and the alpha-blending parameters. For example code, see the reference topic for the **SetAlphaBitmap** method.

After you set the bitmap, you can update the blending parameters, including the source and destination recangles, by calling [**IMFVideoMixerBitmap::UpdateAlphaBitmapParameters**](/windows/desktop/api/evr9/nf-evr9-imfvideomixerbitmap-updatealphabitmapparameters). The update takes effect on the next video frame. The video must be playing for the update to occur. You can use this method to perform simple animations on the bitmap. (If you need more sophisticated effects, consider writing a custom EVR mixer.)

To clear the bitmap, call [**IMFVideoMixerBitmap::ClearAlphaBitmap**](/windows/desktop/api/evr9/nf-evr9-imfvideomixerbitmap-clearalphabitmap).

## Controlling Substreams

The EVR can mix one or more video substreams onto the primary video stream. To control substream mixing, use the [**IMFVideoMixerControl**](/windows/desktop/api/evr/nn-evr-imfvideomixercontrol) interface.

-   Call [**IMFVideoMixerControl::SetStreamOutputRect**](/windows/desktop/api/evr/nf-evr-imfvideomixercontrol-setstreamoutputrect) to set the position of a substream within the composited video frame.

-   Call [**IMFVideoMixerControl::SetStreamZOrder**](/windows/desktop/api/evr/nf-evr-imfvideomixercontrol-setstreamzorder) to set the z-order for the substreams. The EVR draws the video streams in the order of their z-order values, starting with zero. The primary video stream is always first in the z-order.

## Video Processor Settings

The EVR mixer uses DirectX Video Acceleration (DXVA) to perform video processing on the input streams. The exact processing capabilities depend on the graphics driver. Video processing capabilities are described by using the [**DXVA2\_VideoProcessorCaps**](/windows/desktop/api/dxva2api/ns-dxva2api-dxva2_videoprocessorcaps) structure. A particular set of capabilities is called a *video processing mode*, each mode being identified by a GUID. For a list of predefined GUIDs, see [**IDirectXVideoProcessorService::GetVideoProcessorDeviceGuids**](/windows/desktop/api/dxva2api/nf-dxva2api-idirectxvideoprocessorservice-getvideoprocessordeviceguids). The driver might define additional vendor-specific GUIDs, representing different combinations of capabilities.

To find the supported modes and the capabilities of each mode, do the following:

1.  Call [**IMFGetService::GetService**](/windows/desktop/api/mfidl/nf-mfidl-imfgetservice-getservice) to get a pointer to the mixer's [**IMFVideoProcessor**](/windows/desktop/api/evr9/nn-evr9-imfvideoprocessor) interface.

2.  Call [**IMFVideoProcessor::GetAvailableVideoProcessorModes**](/windows/desktop/api/evr9/nf-evr9-imfvideoprocessor-getavailablevideoprocessormodes). This method returns an array of GUIDs, which identify the available video processor modes. The list is returned in descending quality order, the mode with the highest quality appearing first in the list. The list can change depending on the format of the video.

3.  For each GUID in the list, call [**IMFVideoProcessor::GetVideoProcessorCaps**](/windows/desktop/api/evr9/nf-evr9-imfvideoprocessor-getvideoprocessorcaps) to find the capabilities of the corresponding video processor mode. The method fills a [**DXVA2\_VideoProcessorCaps**](/windows/desktop/api/dxva2api/ns-dxva2api-dxva2_videoprocessorcaps) structure with a description of the capabilities.

4.  To select a mode, call [**IMFVideoProcessor::SetVideoProcessorMode**](/windows/desktop/api/evr9/nf-evr9-imfvideoprocessor-setvideoprocessormode). Otherwise, the EVR automatically selects a mode when streaming begins. In that case, you can call [**IMFVideoProcessor::GetVideoProcessorMode**](/windows/desktop/api/evr9/nf-evr9-imfvideoprocessor-getvideoprocessormode) to find which mode was selected.

Most of the fields in the [**DXVA2\_VideoProcessorCaps**](/windows/desktop/api/dxva2api/ns-dxva2api-dxva2_videoprocessorcaps) structure describe low-level driver behavior and are not of interest in a typical application. The following fields are most likely to be of interest:

-   **DeviceCaps**. This field indicates whether video processing is performed in hardware or software, and whether the graphics driver is an older DXVA 1.0 driver.

-   **DeinterlaceTechnology**. This field provides some indication of what level of deinterlacing quality you can expect if the source video is interlaced.

-   **ProcAmpControlCaps**. This field specifies which color adjustment controls are available. For a list of possible color adjustments, see [ProcAmp Settings](procamp-settings.md). If the driver cannot perform color adjustment, this field is zero.

-   **VideoProcessorOperations**. This field contains flags that describe miscellaneous video processing capabilities. Two flags of particular importance are the DXVA2\_VideoProcess\_SubStreams flag and the DXVA2\_VideoProcess\_SubStreams flag. At least one of these flags must be present for the EVR to mix substreams onto the reference video stream. If neither flag is present, the EVR is limited to one video stream.

-   **NoiseFilterTechnology**. This field indicates which noise filters are supported by the graphics driver. If the driver does not support noise filtering, the value is DXVA2\_NoiseFilterTech\_Unsupported.

-   **DetailFilterTechnology**. This field indicates which detail filters are supported by the graphics driver. If the driver does not support noise filtering, the value is DXVA2\_DetailFilterTech\_Unsupported.

## Color Adjustment and Image Filtering

The graphics driver might support color adjustment (also called *process amplification* or simply *ProcAmp*) and image filtering. When performed by the GPU, color adjustment and image filtering can be done in real time with no CPU overhead.

To use these features, perform the following steps:

1.  Select a video processing mode as described in the previous section.

2.  Call [**IMFVideoProcessor::GetVideoProcessorCaps**](/windows/desktop/api/evr9/nf-evr9-imfvideoprocessor-getvideoprocessorcaps) to find the video processing capabilities as described in the previous section. The method fills in a [**DXVA2\_VideoProcessorCaps**](/windows/desktop/api/dxva2api/ns-dxva2api-dxva2_videoprocessorcaps) structure which describes the capabilities, including whether the driver supports color adjustment and image filter.

3.  For each color adjustment that is supported by driver, call [**IMFVideoProcessor::GetProcAmpRange**](/windows/desktop/api/evr9/nf-evr9-imfvideoprocessor-getprocamprange) to find the possible range of value for that setting. This method also returns the default value for the setting. Call [**IMFVideoProcessor::GetProcAmpValues**](/windows/desktop/api/evr9/nf-evr9-imfvideoprocessor-getprocampvalues) to find the current value of the settings. The values do not have specified units. It is up to the driver to define the range of values.

4.  Call [**IMFVideoProcessor::SetFilteringValue**](/windows/desktop/api/evr9/nf-evr9-imfvideoprocessor-setfilteringvalue) to set a color adjustment value.

5.  If the driver supports image filtering, then each filter type (noise and detail) supports three settings—level, radius, and threshold—in both chroma and luma. (See [DXVA Image Filter Settings](dxva-image-filter-settings.md).) For each setting, call [**IMFVideoProcessor::GetFilteringRange**](/windows/desktop/api/evr9/nf-evr9-imfvideoprocessor-getfilteringrange) to get the range of possible values and call [**IMFVideoProcessor::GetFilteringValue**](/windows/desktop/api/evr9/nf-evr9-imfvideoprocessor-getfilteringvalue) to get the current value.

6.  To change an image filter setting, call [**IMFVideoProcessor::SetFilteringValue**](/windows/desktop/api/evr9/nf-evr9-imfvideoprocessor-setfilteringvalue).

## Related topics

<dl> <dt>

[Enhanced Video Renderer](enhanced-video-renderer.md)
</dt> </dl>

 

 



