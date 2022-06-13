---
description: The video stabilization MFT is a Microsoft Media Foundation transform (MFT) that performs image stabilization on a video stream.
ms.assetid: BBC42190-08E4-4C3B-972A-FD30621A6CC1
title: Video Stabilization MFT (Camerauicontrol.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Video Stabilization MFT

The video stabilization MFT is a Microsoft Media Foundation transform (MFT) that performs image stabilization on a video stream.

## CLSID

CLSID\_CMSVideoDSPMFT

## Interfaces

-   [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform)
-   [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes)
-   [**IMFQualityAdvise**](/windows/desktop/api/mfidl/nn-mfidl-imfqualityadvise)
-   [**IMFQualityAdvise2**](/windows/desktop/api/mfidl/nn-mfidl-imfqualityadvise2)
-   [**IMediaExtension**](/uwp/api/Windows.Media.IMediaExtension)

## Input Formats

The input media type and sub-type combinations accepted by the video stabilization MFT for uncompressed video are:

-   **MEDIATYPE\_VIDEO**
-   **MEDIASUBTYPE\_NV12**
-   **MEDIASUBTYPE\_YUY2**

## Output Formats

The output media type and sub-type combinations accepted by the video stabilization MFT are:

-   **MEDIATYPE\_VIDEO**
-   **MEDIASUBTYPE\_NV12**

The input media type must be set before the output media type. In most situations, the limited format support is not an issue because the pipeline automatically inserts the necessary color conversions.

The video stabilization MFT component is capable of dynamic format change when input changes. When the input picture size changes or the subtype changes, it will trigger a dynamic format change on the output stream.

The video stabilization MFT will do color conversion in the following cases:

-   When the input format is **MEDIASUBTYPE\_YUY2**.
-   When Microsoft DirectX 9.0 compatibility mode is used.

### Attributes

The following attributes are supported by the video stabilization MFT through the [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes) interface.

-   The attribute [MF\_VIDEODSP\_MODE](mf-videodsp-mode.md) puts the video stabilization MFT into either stabilization mode or pass-through mode. The application should call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32) on the GUID **MF\_VIDEODSP\_TYPE** with an integer corresponding to one of the following valid values: **MFVideoDSPMode\_Stabilization** = 4, **MFVideoDSPMode\_Passthrough** = 1. MF\_VIDEODSP\_MODE can be changed at any time during playback. This causes a dynamic mode change. The output will switch to either stabilized or pass through after either 16 or 2 frames (depending on the latency mode) after the attribute is changed.
-   The attribute [MF\_LOW\_LATENCY](mf-low-latency.md) puts the video stabilization MFT into either low latency mode or high quality mode. The application should call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32) on the GUID **MF\_LOW\_LATENCY** with an integer corresponding to one of the following valid values: Low latency = 1 High Quality = 0
-   The attribute [MF\_SA\_D3D11\_BINDFLAGS](mf-sa-d3d11-bindflags.md) is used by the pipeline to specify the D3D11 bind flags to create the output samples with. Any combination of values from the [**D3D11\_BIND\_FLAG**](/windows/win32/api/d3d11/ne-d3d11-d3d11_bind_flag) enumeration is valid.
-   The attribute **MF\_SA\_MINIMUM\_OUTPUT\_SAMPLE\_COUNT** is used by the pipeline to specify the minimum number of samples that this component must support on output.
-   The attribute [MFSampleExtension\_VideoDSPMode](mfsampleextension-videodspmode.md) is set on every sample produced by stabilization to indicate the effective [MF\_VIDEODSP\_MODE](mf-videodsp-mode.md) applied to that sample (whether or not the sample was stabilized). Under certain conditions, samples may not be stabilized (due to high system load, or requests by the user). This attribute has the same values as the MF\_VIDEODSP\_MODE attribute (**MFVideoDSPMode\_Stabilization** and **MFVideoDSPMode\_Passthrough**). To get the value of this attribute applications should call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32) on GUID **MFSampleExtension\_VideoDSPMode**.

## Remarks

An instance of the video stabilization DSP can be created in one of the following ways:

-   By calling [**MFTEnumEx**](/windows/desktop/api/mfapi/nf-mfapi-mftenumex). The video stabilization DSP is registered under the **MFT\_CATEGORY\_VIDEO\_EFFECT** category.
-   By calling the COM function **CoCreateInstance** passing it the CLSID **CLSID\_CMSVideoDSPMFT**. To use this method, you must include wmcodecdsp.h and link against wmcodecdspuuid.lib.

Additionally, the video stabilization DSP supports instantiation using Windows Runtime as a Windows Media Extension. It is defined on the [**Windows.Media.VideoEffects**](/uwp/api/Windows.Media.VideoEffects), and its full name is "Windows.Media.VideoEffects.VideoStabilization".

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Camerauicontrol.h</dt> </dl> |



## See also

<dl> <dt>

[Digital Signal Processors](windowsmediadigitalsignalprocessors.md)
</dt> <dt>

[**Windows.Media.VideoEffects**](/uwp/api/Windows.Media.VideoEffects)
</dt> </dl>

 

 
