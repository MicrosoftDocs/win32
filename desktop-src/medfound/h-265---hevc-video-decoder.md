---
Description: The Media Foundation H.265 video decoder is a Media Foundation Transform that supports decoding H.265/HEVC content in Annex B format and can be used in playback of mp4 and m2ts files.
ms.assetid: BBE754E4-2AAD-4CFD-B53F-2B66693502EE
title: H.265 / HEVC Video Decoder
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# H.265 / HEVC Video Decoder

The Media Foundation H.265 video decoder is a [Media Foundation Transform](media-foundation-transforms.md) that supports decoding H.265/HEVC content in Annex B format and can be used in playback of mp4 and m2ts files.

The H.265 video decoder exposes the following interfaces.

-   [**ICodecAPI**](https://msdn.microsoft.com/en-us/library/Dd311953(v=VS.85).aspx) (supported in Windows 8)
-   [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes)
-   [**IMFGetService**](/windows/desktop/api/mfidl/nn-mfidl-imfgetservice)
-   [**IMFQualityAdvise**](/windows/desktop/api/mfidl/nn-mfidl-imfqualityadvise)
-   [**IMFQualityAdvise2**](/windows/desktop/api/mfidl/nn-mfidl-imfqualityadvise2)
-   [**IMFRateControl**](/windows/desktop/api/mfidl/nn-mfidl-imfratecontrol)
-   [**IMFRateSupport**](/windows/desktop/api/mfidl/nn-mfidl-imfratesupport)
-   [**IMFRealTimeClient**](/windows/desktop/api/mfidl/nn-mfidl-imfrealtimeclient)
-   [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform)

To create an instance of the decoder, do one of the following:

-   Call the [**MFTEnum**](/windows/desktop/api/mfapi/nf-mfapi-mftenum) or [**MFTEnumEx**](/windows/desktop/api/mfapi/nf-mfapi-mftenumex) function.
-   Call [**CoCreateInstance**](https://msdn.microsoft.com/en-us/library/ms686615(v=VS.85).aspx). The CLSID for the decoder is **CLSID\_CMSH265EncoderMFT**, declared in wmcodecdsp.h.

## Input Types

The input type must contain at least the following two attributes:



| Attribute                                                 | Description                                                                                   |
|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| [**MF\_MT\_MAJOR\_TYPE**](mf-mt-major-type-attribute.md) | **MFMediaType\_Video**                                                                        |
| [**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md)        | [MFVideoFormat\_HEVC](video-subtype-guids.md) or MFVideoFormat\_HEVC\_ES |



 

The first media subtype, MFVideoFormat\_HEVC, indicates that the media samples carry H.265 bitstream with start codes, and the stream has interleaved SPS/PPS. It assumes one frame per sample.

The media subtype MFVideoFormat\_ HEVC\_ES is to indicate the media samples carry elementary H.265 bitstream, where each sample may contain a partial picture, multiple pictures, some pictures plus a partial picture.

The input media types cannot change dynamically between two types. The decoder can detect in-flight output format changes based on the elementary stream syntax (aspect ratio, dimension, interlace flags, colorimetry information) and trigger corresponding output media type changes.

For input media type, the decoder expects the source to set the correct Profile. For example if the content is going to be 10bit, input media type should specify the profile as Main10.

## Output Types

The decoder supports the following output subtypes:

-   **MFVideoFormat\_NV12**
-   **MFVideoFormat\_P010**

For more information about these subtypes, see [Video Subtype GUIDs](video-subtype-guids.md).

## Transform Attributes

The H.265 decoder implements the [**IMFTransform::GetAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getattributes) method. Applications can use this method to get or set the following attributes.



| Attribute                                                                                       | Description                                                                                                                   |
|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [CODECAPI\_AVLowLatencyMode](codecapi-avlowlatencymode.md)                                     | Enables or disables low-latency decoding mode.                                                                                |
| [CODECAPI\_AVDecNumWorkerThreads](codecapi-avdecnumworkerthreads.md)                           | Sets the number of worker threads used by the decoder.                                                                        |
| [CODECAPI\_AVDecVideoThumbnailGenerationMode](https://msdn.microsoft.com/en-us/library/Dd742718(v=VS.85).aspx) | Enables or disables thumbnail generation mode.                                                                                |
| [MF\_NALU\_LENGTH\_SET](mf-nalu-length-set.md)                                                 | Indicates that NALU length information will be sent as a BLOB with each compressed H.265 sample.                              |
| [MF\_NALU\_LENGTH\_INFORMATION](mf-nalu-length-information.md)                                 | Indicates the lengths of NALUs in the sample. This is a MF BLOB that is set on compressed input samples to the H.265 decoder. |
| [MF\_SA\_MINIMUM\_OUTPUT\_SAMPLE\_COUNT](mf-sa-minimum-output-sample-count.md)                 | Specifies the maximum number of output samples.                                                                               |



 

The H.265 decoder supports the [**ICodecAPI**](https://msdn.microsoft.com/en-us/library/Dd311953(v=VS.85).aspx) interface. This interface provides an alternativate API for setting the following codec properties.

-   [CODECAPI\_AVDecNumWorkerThreads](codecapi-avdecnumworkerthreads.md)
-   [CODECAPI\_AVDecVideoThumbnailGenerationMode](https://msdn.microsoft.com/en-us/library/Dd742718(v=VS.85).aspx)
-   [CODECAPI\_AVLowLatencyMode](codecapi-avlowlatencymode.md)

## Format Constraints

The decoder supports the following formats:



|                    |                                                                                                                                                                                                                                                                      |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Profiles/Levels    | Main, Main Still Picture, and Main10 profiles                                                                                                                                                                                                                        |
| Chroma Formats     | 4:2:0 chroma                                                                                                                                                                                                                                                         |
| Minimum Resolution | 48 × 48 pixels                                                                                                                                                                                                                                                       |
| Maximum Resolution | 4096 × 2304 pixels<br/> The maximum guaranteed resolution for DXVA acceleration is 1920 × 1088 pixels; at higher resolutions, decoding is done with DXVA, if it is supported by the underlying hardware, otherwise, decoding is done with software.<br/> |
| DXVA               | The decoder supports DXVA version 2, but not DXVA version 1.                                                                                                                                                                                                         |



 

Input data must conform to Annex B of ITU-T H.265 \| ISO/IEC 23008-2. The data must include the start codes. The decoder skips bytes until it finds a valid sequence parameter set (SPS) and picture parameter set (PPS) in the byte stream.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | None supported<br/>                                                                |
| DLL<br/>                      | <dl> <dt>Mshevcdec.dll</dt> </dl> |



## See also

<dl> <dt>

[Codec Objects](codecobjects.md)
</dt> </dl>

 

 




