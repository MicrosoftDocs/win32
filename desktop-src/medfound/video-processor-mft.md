---
Description: The video processor MFT is a Microsoft Media Foundation transform (MFT) that performs colorspace conversion, video resizing, deinterlacing, frame rate conversion, rotation, cropping, spatial left and right view unpacking, and mirroring.
ms.assetid: 1476995A-9692-4B08-8EF7-7DB6321BEC24
title: Video Processor MFT
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Video Processor MFT

The video processor MFT is a Microsoft Media Foundation transform (MFT) that performs colorspace conversion, video resizing, deinterlacing, frame rate conversion, rotation, cropping, spatial left and right view unpacking, and mirroring.

## CLSID

CLSID\_VideoProcessorMFT

## Interfaces

-   [**IMFRealTimeClientEx**](/windows/win32/mfidl/nn-mfidl-imfrealtimeclientex?branch=master)
-   [**IMFTransform**](/windows/win32/mftransform/nn-mftransform-imftransform?branch=master)
-   [**IMFVideoProcessorControl**](/windows/win32/mfidl/nn-mfidl-imfvideoprocessorcontrol?branch=master)

## Input Formats

-   **MFVideoFormat\_ARGB32**
-   **MFVideoFormat\_AYUV**
-   **MFVideoFormat\_I420**
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

## Output Formats

-   **MFVideoFormat\_ARGB32**
-   **MFVideoFormat\_AYUV**
-   **MFVideoFormat\_I420**
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

Not every combination of input and output formats is supported. To test whether a conversion is supported, set the input type and then call [**IMFTransform::GetOutputAvailableType**](/windows/win32/mftransform/nf-mftransform-imftransform-getoutputavailabletype?branch=master).

For more information about these formats, see [Video Subtype GUIDs](video-subtype-guids.md).

## Remarks

An instance of the video processor can be created in one of the following ways:

-   By calling [**MFTEnumEx**](/windows/win32/mfapi/nf-mfapi-mftenumex?branch=master). The video processor is registered under the **MFT\_CATEGORY\_VIDEO\_PROCESSOR** category.
-   By calling the COM function **CoCreateInstance** passing it the CLSID **CLSID\_VideoProcessorMFT**.

The following remarks pertain to working with source rectangles and destination rectangles in the **Video Processor MFT**. Source and destination rectangles are set with [**IMFVideoProcessorControl::SetDestinationRectangle**](/windows/win32/mfidl/nf-mfidl-imfvideoprocessorcontrol-setdestinationrectangle?branch=master) and [**SetSourceRectangle**](/windows/win32/mfidl/nf-mfidl-imfvideoprocessorcontrol-setsourcerectangle?branch=master) and some times with [**IMFMediaEngineEx::UpdateVideoStream**](/windows/win32/mfmediaengine/nf-mfmediaengine-imfmediaengineex-updatevideostream?branch=master).

-   The source rectangle should be aligned and rounded to match the requirements of the color format of the frame inputted to the video processor. This is important because formats like 420 and 422 have requirements about the dimensions and offsets that can be created and accessed. For example, a source rectangle of {1, 0, 319, 240} (left, top, right, bottom) will be rounded to {2, 0, 320, 240} when the input format is 420.
-   Both the destination and source rectangle will always be clamped to fit inside their respective frames—the source rectangle to the source frame and the destination rectangle to the destination frame. This means that negative values are not meaningful—they will be always clamped to 0.
-   The source rectangle is in the destination frame's coordinate system, minus any destination rectangle. This means that transformations like rotation are "undone" on the source rectangle. Therefore, you do not need to know if the video was rotated or 3D unpacked. For example, you could draw a rectangle on top of the video tag, take the relative coordinates (relative to the video tag), normalize them (range 0 to 1) and pass them down as the source rectangle and they should work as expected, even if the video is being rotated.

The video processor supports GPU-accelerated video processing, using Microsoft Direct3D 11. For more information, see [MF\_SA\_D3D11\_AWARE](mf-sa-d3d11-aware.md).

### Stereoscopic Video

The video processor supports the view unpacking operation on 3D video frames:

If the input frame contains two views packed in the same frame, the video processor can split the views into separate buffers, or extract the base view and discard the second view. To enable view unpacking, set the [MF\_ENABLE\_3DVIDEO\_OUTPUT](mf-enable-3dvideo-output.md) attribute to **MF3DVideoOutputType\_Stereo** or **MF3DVideoOutputType\_BaseView**.

## Requirements



|                   |                                                                                              |
|-------------------|----------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Camerauicontrol.h</dt> </dl> |



## See also

<dl> <dt>

[Digital Signal Processors](windowsmediadigitalsignalprocessors.md)
</dt> </dl>

 

 




