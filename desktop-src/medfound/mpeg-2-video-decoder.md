---
description: The MPEG-2 Video Decoder is a Media Foundation transform that decodes MPEG-1 and MPEG-2 video.
ms.assetid: 3E7FAE14-932D-44A3-997B-567C0D2EAE7B
title: MPEG-2 Video Decoder
ms.topic: reference
ms.date: 05/31/2018
---

# MPEG-2 Video Decoder

The MPEG-2 Video Decoder is a [Media Foundation transform](media-foundation-transforms.md) that decodes MPEG-1 and MPEG-2 video. The decoder supports MPEG-2 Simple and Main profile video (H.262, ISO/IEC 13818-2) and MPEG-1 video (ISO/IEC 11172-2).

## Input Types

The decoder supports the following input media types.

| Attribute                                                 | Description                                                             |
|-----------------------------------------------------------|-------------------------------------------------------------------------|
| [**MF\_MT\_MAJOR\_TYPE**](mf-mt-major-type-attribute.md) | **MFMediaType\_Video**                                                  |
| [**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md)        | **MFVideoFormat\_MPEG1**<br/> **MFVideoFormat\_MPEG2**<br/> |



 

## Output Types

The decoder supports the following output types.

| Attribute                                                 | Description                                                                                                                                                                    |
|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MF\_MT\_MAJOR\_TYPE**](mf-mt-major-type-attribute.md) | **MFMediaType\_Video**                                                                                                                                                         |
| [**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md)        | **MFVideoFormat\_I420**<br/> **MFVideoFormat\_IYUV**<br/> **MFVideoFormat\_NV12**<br/> **MFVideoFormat\_YUY2**<br/> **MFVideoFormat\_YV12**<br/> |



 

## Remarks

The MPEG-2 video decoder exposes the following interfaces:

-   [**ICodecAPI**](/windows/win32/api/strmif/nn-strmif-icodecapi)
-   [**IMFGetService**](/windows/desktop/api/mfidl/nn-mfidl-imfgetservice)
-   [**IMFQualityAdvise**](/windows/desktop/api/mfidl/nn-mfidl-imfqualityadvise)
-   [**IMFQualityAdvise2**](/windows/desktop/api/mfidl/nn-mfidl-imfqualityadvise2)
-   [**IMFRateControl**](/windows/desktop/api/mfidl/nn-mfidl-imfratecontrol)
-   [**IMFRateSupport**](/windows/desktop/api/mfidl/nn-mfidl-imfratesupport)
-   [**IMFRealTimeClient**](/windows/desktop/api/mfidl/nn-mfidl-imfrealtimeclient)
-   [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform)

The input to the decoder must be an elementary stream. The maximum supported resolution is 1920 × 1088 pixels.

The decoder supports DirectX Video Acceleration (DXVA) using either Microsoft Direct3D 9 or Microsoft Direct3D 11.

### Special Decoding Modes

-   **Low latency mode.** This mode is appropriate for scenarios such as real-time communications. It reduces start-up latency, so the decoder produces the first output sample sooner. However, the decoder buffers fewer samples in this mode, which can potentially lead to glitches, because the decoder does not decode as many frames in advance. To enable low latency mode, set the [CODECAPI\_AVLowLatencyMode](codecapi-avlowlatencymode.md) attribute.
-   **Seeking.** For precise seeking, call the [**IMFTransform::SetOutputBounds**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setoutputbounds) method. When this method is called, the decoder outputs only frames that fall within the range of time stamps specified by the caller.
-   **Thumbnail generation mode**. This mode is intended for quick generation of thumbnail images. In this mode, the decoder initially decodes only I frames. If no I frame is found within a certain number of frames, the decoder starts decoding P frames and outputs non–I frames at a fixed interval (one per *N* pictures) until an I frame is reached. To enable thumbnail generation mode, set the [CODECAPI\_AVDecVideoThumbnailGenerationMode](../directshow/avdecvideothumbnailgenerationmode-property.md) property.
-   **Trick play.** The decoder can decode at rates faster than real time. At higher playback rates, the decoder will switch to decoding only I frames. For reverse playback, only I frames are decoded.

### Codec Properties

The decoder supports the following properties through the [**IMFTransform::GetAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getattributes) method.



| Property                                                                                                      | Description                                                                                                |
|---------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [CODECAPI\_AVDecVideoThumbnailGenerationMode](../directshow/avdecvideothumbnailgenerationmode-property.md)               | Enables or disables thumbnail generation mode.                                                             |
| [CODECAPI\_AVDecVideoAcceleration\_MPEG2](../directshow/avdecvideoacceleration-mpeg2-property.md)                        | Enables or disables hardware accelerated decoding.                                                         |
| [CODECAPI\_AVLowLatencyMode](codecapi-avlowlatencymode.md)                                                   | Enables or disables low-latency mode.                                                                      |
| [MFT\_DECODER\_EXPOSE\_OUTPUT\_TYPES\_IN\_NATIVE\_ORDER](mft-decoder-expose-output-types-in-native-order.md) | Specifies whether the decoder exposes output types that are suitable for transcoding before other formats. |



 

Of these properties, the following can also be set through the [**ICodecAPI**](/windows/win32/api/strmif/nn-strmif-icodecapi) interface:

-   [CODECAPI\_AVDecVideoThumbnailGenerationMode](../directshow/avdecvideothumbnailgenerationmode-property.md)
-   [CODECAPI\_AVDecVideoAcceleration\_MPEG2](../directshow/avdecvideoacceleration-mpeg2-property.md)
-   [CODECAPI\_AVLowLatencyMode](codecapi-avlowlatencymode.md)

### Limitations

-   The decoder is not supported on IA-64–based platforms.
-   The decoder does not support CSS decryption or playback of encrypted DVDs.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                       |
| DLL<br/>                      | <dl> <dt>Msmpeg2vdec.dll</dt> </dl> |



## See also

<dl> <dt>

[Codec Objects](codecobjects.md)
</dt> </dl>

 

 
