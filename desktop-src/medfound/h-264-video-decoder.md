---
description: The Media Foundation H.264 video decoder is a Media Foundation Transform that supports decoding of Baseline, Main, and High profiles, up to level 5.1.
ms.assetid: 783a3618-981a-4573-9e9e-ebf5eeb75d06
title: H.264 Video Decoder
ms.topic: reference
ms.date: 05/31/2018
---

# H.264 Video Decoder

The Media Foundation H.264 video decoder is a [Media Foundation Transform](media-foundation-transforms.md) that supports decoding of Baseline, Main, and High profiles, up to level 5.1.

The H.264 video decoder exposes the following interfaces.

-   [**ICodecAPI**](/windows/win32/api/strmif/nn-strmif-icodecapi) (supported in Windows 8)
-   [**IMFGetService**](/windows/desktop/api/mfidl/nn-mfidl-imfgetservice)
-   [**IMFQualityAdvise**](/windows/desktop/api/mfidl/nn-mfidl-imfqualityadvise)
-   [**IMFQualityAdvise2**](/windows/desktop/api/mfidl/nn-mfidl-imfqualityadvise2)
-   [**IMFRateControl**](/windows/desktop/api/mfidl/nn-mfidl-imfratecontrol)
-   [**IMFRateSupport**](/windows/desktop/api/mfidl/nn-mfidl-imfratesupport)
-   [**IMFRealTimeClient**](/windows/desktop/api/mfidl/nn-mfidl-imfrealtimeclient)
-   [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform)

To create an instance of the decoder, do one of the following:

-   Call the [**MFTEnum**](/windows/desktop/api/mfapi/nf-mfapi-mftenum) or [**MFTEnumEx**](/windows/desktop/api/mfapi/nf-mfapi-mftenumex) function.
-   Call [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance). The CLSID for the decoder is **CLSID\_CMSH264DecoderMFT**, declared in wmcodecdsp.h.

## Input Types

The input type must contain at least the following two attributes:



| Attribute                                                 | Description                                                                                   |
|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| [**MF\_MT\_MAJOR\_TYPE**](mf-mt-major-type-attribute.md) | **MFMediaType\_Video**                                                                        |
| [**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md)        | [MFVideoFormat\_H264](video-subtype-guids.md) or MFVideoFormat\_H264\_ES |



 

If the input type contains only these two attributes, the decoder will offer a default output type, which acts as a placeholder. When the decoder receives enough input samples to produce an output frame, it signals a format change by returning **MF\_E\_TRANSFORM\_STREAM\_CHANGE** from [**IMFTransform::ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput). See the **ProcessOutput** documentation for details about handling format changes.

To avoid an initial format change, provide as much information in the input type as possible, including:




| Attribute | Description | 
|-----------|-------------|
| <a href="mf-mt-frame-rate-attribute.md"><strong>MF_MT_FRAME_RATE</strong></a> | Frame rate. | 
| <a href="mf-mt-frame-size-attribute.md"><strong>MF_MT_FRAME_SIZE</strong></a> | Frame dimensions. | 
| <a href="mf-mt-interlace-mode-attribute.md"><strong>MF_MT_INTERLACE_MODE</strong></a> | Interlace mode.<blockquote>[!Note]<br />In H.264 video, the interlace structure can change dynamically, so the recommended value of this attribute is <strong>MFVideoInterlace_MixedInterlaceOrProgressive</strong>. Interlace information in the video elementary stream takes precedence over the media type. For more information, see <a href="video-interlacing.md">Video Interlacing</a>.</blockquote><br /><br /> | 
| <a href="mf-mt-pixel-aspect-ratio-attribute.md"><strong>MF_MT_PIXEL_ASPECT_RATIO</strong></a> | Pixel aspect ratio. | 




 

The input type must be set before the output type. Until the input type is set, the encoder's [**IMFTransform::SetOutputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setoutputtype) method returns **MF\_E\_TRANSFORM\_TYPE\_NOT\_SET**.

## Output Types

The decoder supports the following output subtypes:

-   **MFVideoFormat\_I420**
-   **MFVideoFormat\_IYUV**
-   **MFVideoFormat\_NV12**
-   **MFVideoFormat\_YUY2**
-   **MFVideoFormat\_YV12**

For more information about these subtypes, see [Video Subtype GUIDs](video-subtype-guids.md).

## Transform Attributes

The H.264 decoder implements the [**IMFTransform::GetAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getattributes) method. Applications can use this method to get or set the following attributes.



| Attribute                                                                                       | Description                                                                                |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [CODECAPI\_AVDecVideoAcceleration\_H264](../directshow/avdecvideoacceleration-h264-property.md)            | Enables or disables hardware acceleration.                                                 |
| [CODECAPI\_AVDecVideoThumbnailGenerationMode](../directshow/avdecvideothumbnailgenerationmode-property.md) | Enables or disables thumbnail generation mode.                                             |
| [MF\_SA\_D3D\_AWARE](mf-sa-d3d-aware-attribute.md)                                             | Indicates that the decoder supports DirectX Video Acceleration (DXVA). Treat as read-only. |



 

In Windows 8, the H.264 decoder also supports the following attributes.



| Attribute                                                                                                     | Description                                                                                                 |
|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [CODECAPI\_AVLowLatencyMode](codecapi-avlowlatencymode.md)                                                   | Enables or disables low-latency decoding mode.                                                              |
| [CODECAPI\_AVDecNumWorkerThreads](codecapi-avdecnumworkerthreads.md)                                         | Sets the number of worker threads used by the decoder.                                                      |
| [CODECAPI\_AVDecVideoMaxCodedWidth](codecapi-avdecvideomaxcodedwidth.md)                                     | Sets the maximum picture width that the decoder will accept as an input type.                               |
| [CODECAPI\_AVDecVideoMaxCodedHeight](codecapi-avdecvideomaxcodedheight.md)                                   | Sets the maximum picture height that the decoder will accept as an input type.                              |
| [MF\_SA\_MINIMUM\_OUTPUT\_SAMPLE\_COUNT](mf-sa-minimum-output-sample-count.md)                               | Specifies the maximum number of output samples.                                                             |
| [MFT\_DECODER\_EXPOSE\_OUTPUT\_TYPES\_IN\_NATIVE\_ORDER](mft-decoder-expose-output-types-in-native-order.md) | Specifies whether a decoder exposes IYUV/I420 output types (suitable for transcoding) before other formats. |



 

In Windows 8, the H.264 decoder supports the [**ICodecAPI**](/windows/win32/api/strmif/nn-strmif-icodecapi) interface. This interface provides an alternativate API for setting the following codec properties.

-   [CODECAPI\_AVDecVideoMaxCodedWidth](codecapi-avdecvideomaxcodedwidth.md)
-   [CODECAPI\_AVDecVideoAcceleration\_H264](../directshow/avdecvideoacceleration-h264-property.md)
-   [CODECAPI\_AVDecVideoMaxCodedHeight](codecapi-avdecvideomaxcodedheight.md)
-   [CODECAPI\_AVDecVideoMaxCodedWidth](codecapi-avdecvideomaxcodedwidth.md)
-   [CODECAPI\_AVDecVideoThumbnailGenerationMode](../directshow/avdecvideothumbnailgenerationmode-property.md)

## Format Constraints

The decoder supports the following formats:




|Setting|Format|
|----|-----|
|Profiles/Levels| Baseline, Main, and High profiles, up to level 5.1. (See ITU-T H.264 specification for details.) | 
| Chroma Formats | 4:2:0 chroma or monochrome | 
| Minimum Resolution | 48 × 48 pixels | 
| Maximum Resolution | 4096 × 2304 pixels<br /> The maximum guaranteed resolution for DXVA acceleration is 1920 × 1088 pixels; at higher resolutions, decoding is done with DXVA, if it is supported by the underlying hardware, otherwise, decoding is done with software.<br /><blockquote>[!Note]<br />In Windows 7, the maximum supported resolution is 1920 × 1088 pixels for both software and DXVA decoding.</blockquote><br /><br /> | 
| DXVA | The decoder supports DXVA version 2, but not DXVA version 1. DXVA decoding is supported only for Main-compatible Baseline, Main, and High profile bitstreams. (Main-compatible Baseline bitstreams are defined as <strong>profile_idc</strong>=66 and <strong>constrained_set1_flag</strong>=1.)| 




 

Input data must conform to Annex B of ISO/IEC 14496-10. The data must include the start codes. The decoder skips bytes until it finds a valid sequence parameter set (SPS) and picture parameter set (PPS) in the byte stream.

The decoder does not support Film Grain Technology.

> [!Note]  
> A previous version of the documentation incorrectly stated that the decoder is supported on Windows Server 2008 R2.

 

If Platform Update Supplement for Windows Vista is installed, the H.264 video decoder is available on Windows Vista, but is accessible on Windows Vista only by using the [Source Reader](source-reader.md).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                  |
| DLL<br/>                      | <dl> <dt>Msmpeg2vdec.dll</dt> </dl> |



## See also

<dl> <dt>

[Codec Objects](codecobjects.md)
</dt> <dt>

[MPEG-4 Support in Media Foundation](mpeg-4-support-in-media-foundation.md)
</dt> <dt>

[Supported Media Formats in Media Foundation](supported-media-formats-in-media-foundation.md)
</dt> <dt>

[Video Media Types](video-media-types.md)
</dt> </dl>

 

 
