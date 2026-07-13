---
description: The video processor MFT is a Microsoft Media Foundation transform (MFT) that performs colorspace conversion, video resizing, deinterlacing, frame rate conversion, rotation, cropping, spatial left and right view unpacking, and mirroring.
ms.assetid: 1476995A-9692-4B08-8EF7-7DB6321BEC24
title: Video Processor MFT (Camerauicontrol.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Video Processor MFT

The video processor MFT is a Microsoft Media Foundation transform (MFT) that performs colorspace conversion, tone mapping, video resizing, deinterlacing, frame rate conversion, rotation, cropping, spatial left and right view unpacking, mirroring, renderer effect processing, and sphere mapping.

## CLSID

CLSID\_VideoProcessorMFT

## Interfaces

-   [**IMFRealTimeClientEx**](/windows/desktop/api/mfidl/nn-mfidl-imfrealtimeclientex)
-   [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform)
-   [**IMFVideoProcessorControl**](/windows/desktop/api/mfidl/nn-mfidl-imfvideoprocessorcontrol)
-   [**IMFVideoProcessorControl2**](/windows/desktop/api/mfidl/nn-mfidl-imfvideoprocessorcontrol2)
-   [**IMFVideoProcessorControl3**](/windows/desktop/api/mfidl/nn-mfidl-imfvideoprocessorcontrol3)
-   [**IMFVideoRendererEffectControl**](/windows/desktop/api/mfidl/nn-mfidl-imfvideorenderereffectcontrol)

## Input Formats

The following formats are supported values for the **MF\_MT\_SUBTYPE** value of the media type set via [**IMFTransform::SetInputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setinputtype)
-   **MFVideoFormat\_ABGR32**
-   **MFVideoFormat\_ARGB32**
-   **MFVideoFormat\_AYUV**
-   **MFVideoFormat\_I420**
-   **MFVideoFormat\_I422**
-   **MFVideoFormat\_I444**
-   **MFVideoFormat\_IYUV**
-   **MFVideoFormat\_NV11**
-   **MFVideoFormat\_NV12**
-   **MFVideoFormat\_RGB24**
-   **MFVideoFormat\_RGB32**
-   **MFVideoFormat\_RGB555**
-   **MFVideoFormat\_RGB565**
-   **MFVideoFormat\_RGB8**
-   **MFVideoFormat\_UYVY**
-   **MFVideoFormat\_v410**
-   **MFVideoFormat\_Y216**
-   **MFVideoFormat\_Y41P**
-   **MFVideoFormat\_Y41T**
-   **MFVideoFormat\_Y42T**
-   **MFVideoFormat\_YUY2**
-   **MFVideoFormat\_YV12**
-   **MFVideoFormat\_YVYU**
-   **MFVideoFormat\_P010**
-   **MFVideoFormat\_P016**
-   **MFVideoFormat\_A16B16G16R16F**
-   **MFVideoFormat\_A2R10G10B10**
-   **MFVideoFormat\_Y210**
-   **MFVideoFormat\_Y410**
-   **MFVideoFormat\_Y416**
-   **MFVideoFormat\_L8**
-   **MFVideoFormat\_L16**
-   **MFVideoFormat\_D16**

## Output Formats

The following formats are supported values for the **MF\_MT\_SUBTYPE** value of the media type set via [**IMFTransform::SetOutputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setoutputtype)
-   **MFVideoFormat\_ARGB32**
-   **MFVideoFormat\_AYUV**
-   **MFVideoFormat\_I420**
-   **MFVideoFormat\_I422**
-   **MFVideoFormat\_I444**
-   **MFVideoFormat\_IYUV**
-   **MFVideoFormat\_NV12**
-   **MFVideoFormat\_RGB24**
-   **MFVideoFormat\_RGB32**
-   **MFVideoFormat\_RGB555**
-   **MFVideoFormat\_RGB565**
-   **MFVideoFormat\_UYVY**
-   **MFVideoFormat\_Y216**
-   **MFVideoFormat\_YUY2**
-   **MFVideoFormat\_YV12**
-   **MFVideoFormat\_P010**
-   **MFVideoFormat\_P016**
-   **MFVideoFormat\_A16B16G16R16F**
-   **MFVideoFormat\_A2R10G10B10**
-   **MFVideoFormat\_Y210**
-   **MFVideoFormat\_Y410**
-   **MFVideoFormat\_Y416**

Not every combination of input and output formats is supported. To test whether a conversion is supported, set the input type and then call [**IMFTransform::GetOutputAvailableType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputavailabletype).

For more information about these formats, see [Video Subtype GUIDs](video-subtype-guids.md).

## Color Space Transforms

The following attributes can be set on either the input or output types to change the color space of the content:
-  **MF\_MT\_VIDEO\_PRIMARIES**
-  **MF\_MT\_TRANSFER\_FUNCTION**
-  **MF\_MT\_YUV\_MATRIX**
-  **MF\_MT\_VIDEO\_CHROMA\_SITING**
-  **MF\_MT\_VIDEO\_NOMINAL\_RANGE**
-  **MF\_MT\_MAX\_MASTERING\_LUMINANCE**
-  **MF\_MT\_MAX\_LUMINANCE\_LEVEL**
-  **MF\_MT\_CUSTOM\_VIDEO\_PRIMARIES**
-  **MF\_MT\_PALETTE**

## Image Transforms

The following attributes can be set on either the input or output types to perform spatial transforms on the video:
-  **MF\_MT\_PIXEL\_ASPECT\_RATIO**
-  **MF\_MT\_VIDEO\_ROTATION**
-  **MF\_MT\_PAN\_SCAN\_APERTURE**
-  **MF\_MT\_GEOMETRIC\_APERTURE**
-  **MF\_MT\_MINIMUM\_DISPLAY\_APERTURE**
-  **MF\_MT\_VIDEO\_3D**
-  **MF\_MT\_VIDEO\_3D\_FORMAT**

## Framerate Transforms

The following attributes can be set on either the input or output types to perform temporal transforms on the video:
-  **MF\_MT\_INTERLACE\_MODE**
-  **MF\_MT\_FRAME\_RATE**

Note that if **MF\_XVP\_DISABLE\_FRC** is set to TRUE then frame rate conversion is disabled, but deinterlacing will still be performed.

## Transform Attributes

The following attributes can be set on the transform using **IMFTransform::GetAttributes**:
-  **MF\_XVP\_DISABLE\_FRC**
-  **MF\_XVP\_CALLER\_ALLOCATES\_OUTPUT**
-  **MF\_LOW\_LATENCY**
-  **MF\_XVP\_SAMPLE\_LOCK\_TIMEOUT**
-  **MF\_ENABLE\_3DVIDEO\_OUTPUT**
-  **MF\_VIDEO\_PROCESSOR\_ALGORITHM**

## Remarks

An instance of the video processor can be created in one of the following ways:

-   By calling [**MFTEnumEx**](/windows/desktop/api/mfapi/nf-mfapi-mftenumex). The video processor is registered under the **MFT\_CATEGORY\_VIDEO\_PROCESSOR** category.
-   By calling the COM function **CoCreateInstance** passing it the CLSID **CLSID\_VideoProcessorMFT**.

The following remarks pertain to working with source rectangles and destination rectangles in the **Video Processor MFT**. Source and destination rectangles are set with [**IMFVideoProcessorControl::SetDestinationRectangle**](/windows/desktop/api/mfidl/nf-mfidl-imfvideoprocessorcontrol-setdestinationrectangle) and [**SetSourceRectangle**](/windows/desktop/api/mfidl/nf-mfidl-imfvideoprocessorcontrol-setsourcerectangle) and sometimes with [**IMFMediaEngineEx::UpdateVideoStream**](/windows/desktop/api/mfmediaengine/nf-mfmediaengine-imfmediaengineex-updatevideostream).

-   The source rectangle should be aligned and rounded to match the requirements of the color format of the frame inputted to the video processor. This is important because formats like 420 and 422 have requirements about the dimensions and offsets that can be created and accessed. For example, a source rectangle of {1, 0, 319, 240} (left, top, right, bottom) will be rounded to {2, 0, 320, 240} when the input format is 420.
-   Both the destination and source rectangle will always be clamped to fit inside their respective frames—the source rectangle to the source frame and the destination rectangle to the destination frame. This means that negative values are not meaningful—they will be always clamped to 0.
-   The source rectangle is in the destination frame's coordinate system, minus any destination rectangle. This means that transformations like rotation are "undone" on the source rectangle. Therefore, you do not need to know if the video was rotated or 3D unpacked. For example, you could draw a rectangle on top of the video tag, take the relative coordinates (relative to the video tag), normalize them (range 0 to 1) and pass them down as the source rectangle and they should work as expected, even if the video is being rotated.

The video processor supports GPU-accelerated video processing, using Microsoft Direct3D 11, or Direct3D 12. For more information, see [MF\_SA\_D3D11\_AWARE](mf-sa-d3d11-aware.md) and [MF\_SA\_D3D12\_AWARE](mf-sa-d3d12-aware.md).

The video processor is used as the front-end converter for video rendering when using SVR which is exposed by the [MediaPlayer](/uwp/api/windows.media.playback.mediaplayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine) components.  Decoders, plugins or sources used by either of these components 

### Renderer Effects

The Video Processor MFT is the host component for Renderer effects.  Renderer effects allow applications to plugin to the normal video transform and rendering process.  For typical applications a video plugin (see: [IMFMediaEngineEx::InsertVideoEffect](/windows/desktop/api/mfmediaengine/nf-mfmediaengine-imfmediaengineex-insertvideoeffect)) is sufficient.  But some scenarios require more information about the exact conditions that a video is being rendered in.
Consider a renderer effect for the following situations:
-  The plugin needs to know the resolution that the video is rendered at (e.g. to perform a special scaling operation like super resolution)
-  The plugin needs to know properties of the display that the video is being rendered on (e.g. to perform accurate tone mapping)
-  The plugin needs to know exactly the final output format of the presented video

To load a renderer effect configure the **MF\_MT\_VIDEO\_RENDERER\_EXTENSION\_PROFILE** attribute on the input type of the Video Processor MFT.

### Stereoscopic Video

The video processor supports the view unpacking operation on 3D video frames:

If the input frame contains two views packed in the same frame, the video processor can split the views into separate buffers, or extract the base view and discard the second view. To enable view unpacking, set the [MF\_ENABLE\_3DVIDEO\_OUTPUT](mf-enable-3dvideo-output.md) attribute to **MF3DVideoOutputType\_Stereo** or **MF3DVideoOutputType\_BaseView**.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Camerauicontrol.h</dt> </dl> |



## See also

<dl> <dt>

[Digital Signal Processors](windowsmediadigitalsignalprocessors.md)
</dt> </dl>

 

 




