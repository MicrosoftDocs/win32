---
description: Media Type Negotiation on the Encoder
ms.assetid: c8ae543e-68f7-4c74-9cb7-2a200bd51820
title: Media Type Negotiation on the Encoder
ms.topic: article
ms.date: 05/31/2018
---

# Media Type Negotiation on the Encoder

In Microsoft Media Foundation, encoders are implemented as [Media Foundation transforms](media-foundation-transforms.md) (MFTs) with one input and one output. Before an encoding session, an encoder needs to know the characteristics of the stream it will receive as input and the format of the stream it will produce as output. You must set the input and output media types and related characteristics before you pass data through the encoder. You must supply the input and output formats by specifying the appropriate [Media Type GUIDs](media-type-guids.md) and set the characteristics of the output stream by setting the relevant [Media Type Attributes](media-type-attributes.md) on the output media type. A newly instantiated encoder does not have any set media types.

The input media type is an uncompressed format, such as PCM audio or RGB video. The format types that are used by the encoder are limited to those described by the **VIDEOINFOHEADER** and **WAVEFORMATEX** structures. For more information about these structures, see the Windows SDK documentation.Media foundation provides helper functions to create media types from format structures. For example, the [**MFInitMediaTypeFromVideoInfoHeader**](/windows/desktop/api/mfapi/nf-mfapi-mfinitmediatypefromvideoinfoheader) function initializes a video type from a **VIDEOINFOHEADER** structure, and the [**MFInitMediaTypeFromWaveFormatEx**](/windows/desktop/api/mfapi/nf-mfapi-mfinitmediatypefromwaveformatex) function initializes a video type from a **WAVEFORMATEX** or **WAVEFORMATEXTENSIBLE** structure. For more information, see [Media Type Conversions](media-type-conversions.md). You must set the input media type on the encoder by calling [**IMFTransform::SetInputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setinputtype).

The output media type is the compression format used in the final source stream or file. You can set the available output media type only after setting the input media type. You can retrieve the supported output types by calling [**IMFTransform::GetOutputAvailableType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputavailabletype) in a loop until the encoder returns **MF\_E\_NO\_MORE\_TYPES**. Increment the type index with each iteration. When you find an appropriate media type, set the output media type by calling [**IMFTransform::SetOutputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setoutputtype).

The deciding factor in choosing the output media type depends on the type of encoding and your encoding requirements. For example, for audio streams that are CBR-encoded, you want to find a media type that matches your input and has a bit rate that is as close as possible to a target value.

If you want to use an encoding mode other than CBR, you must set the mode and then enumerate the output types for that mode, because the encoder changes the supported output types depending upon the mode set. The properties that control the encoding mode are [**MFPKEY\_VBRENABLED**](mfpkey-vbrenabledproperty.md) and [**MFPKEY\_PASSESUSED**](mfpkey-passesusedproperty.md). For example, if you are enumerating output types for VBR-quality encoding, the media type depends on the quality value you decide to use. For information about setting these properties, see [Encoding Properties](configuring-the-encoder.md).

## Related topics

<dl> <dt>

[Instantiating an Encoder MFT](instantiating-the-encoder-mft.md)
</dt> <dt>

[Windows Media Encoders](windows-media-encoders.md)
</dt> </dl>

 

 



