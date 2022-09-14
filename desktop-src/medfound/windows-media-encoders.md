---
description: An encoder converts uncompressed audio or video into compressed packets in the format specified by the application. For converting media files into ASF format, you can use the Windows Media audio and video codecs.
ms.assetid: 6dcf12d0-ea37-446b-a807-2b27fd1f6124
title: Windows Media Encoders
ms.topic: article
ms.date: 05/31/2018
---

# Windows Media Encoders

An encoder converts uncompressed audio or video into compressed packets in the format specified by the application. For converting media files into ASF format, you can use the Windows Media audio and video codecs.

An encoder is identified by the GUID that represents the category: audio or video. The encoder's output type is represented by a media type's major and the sub type GUID.

-   Windows Media audio codecs

    Category: **MFT\_CATEGORY\_AUDIO\_ENCODER**

    Major type: MFMediaType\_Audio

    SubType: MFAudioFormat\_WMAudioV9, MFAudioFormat\_WMAudioV8, MFAudioFormat\_WMAudio\_Lossless, MFAudioFormat\_WMASPDIF

-   Windows Media video codecs

    Category: **MFT\_CATEGORY\_VIDEO\_ENCODER**

    Major type: MFMediaType\_Video

    SubType: MFVideoFormat\_WVC1, MFVideoFormat\_WMV3, MFVideoFormat\_WMV2, MFVideoFormat\_WMV1

These encoders are implemented as [Media Foundation transform](media-foundation-transforms.md) (MFT) and Media Foundation provides access to the application through the [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) interface of the encoder. If you are using pipeline layer components for ASF encoding, the encoder MFT is inserted into the pipeline as a transform node because it is responsible for transforming media data that flows through the source to the sink. If the source is a compressed type, then the pipeline adds the required decoders to convert the source into an uncompressed type. An encoder has one input stream and one output stream. The encoder receives input data and produces encoded data according to the configuration and format set by the application prior to the encoding session. The format of the output stream is described by a media type.

This section contains the following topics.



| Topic                                                                              | Description                                                                                 |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [Instantiating an Encoder MFT](instantiating-the-encoder-mft.md)                  | Explains how to create the encoder.                                                         |
| [Encoding Properties](configuring-the-encoder.md)                                 | Explains how to configure the encoder by setting appropriate properties on the encoder MFT. |
| [Media Type Negotiation on the Encoder](media-type-negotiation-on-the-encoder.md) | Explains how to set input and output media types on the encoder.                            |
| [Configuring a WMV Encoder](configuring-a-wmv-encoder.md)                         | Explains how to configure a Windows Media Video (WMV) encoder.                              |
| [Setting an Output Type for a WMA Encoder](configuring-a-wma-encoder.md)          | Explains how to set an output type on a Windows Media Audio (WMA) encoder.                  |



 

## Related topics

<dl> <dt>

[Pipeline Layer ASF Components](pipeline-layer-asf-components.md)
</dt> </dl>

 

 



