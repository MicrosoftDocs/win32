---
description: Configuring Audio Encoding
ms.assetid: 40004f07-0b8c-49cd-9e17-1f6ad7604fbb
title: Configuring Audio Encoding (Microsoft Media Foundation)
ms.topic: article
ms.date: 05/31/2018
---

# Configuring Audio Encoding (Microsoft Media Foundation)

The Windows Media Audio encoder enumerates all of its supported output types in their complete form. Retrieve the type that you want by calling **IMediaObject::GetOutputType** or **IMFTransform::GetAvailableOutputType**, and then set the retrieved type, unaltered, as the output type by calling **IMediaObject::SetOutputType** or **IMFTransform::SetOutputType**.

The output media types supported by the audio encoder change as encoder properties are configured. You must configure all of the encoder properties you want to use before you enumerate the output type.

Two-pass and VBR modes are supported by the audio encoders, but are configured differently than for video. For more information, see [Enumerating Audio Types for Specific Encoding Modes](enumeratingaudiotypesforspecificencodingmodes.md).

The input types supported by the audio encoder are not available until you set the output type. If you call **IMediaObject::GetInputType** or **IMFTransform::GetInputType** before setting an output type, the method returns DMO\_E\_NO\_MORE\_ITEMS or MFT\_E\_NO\_MORE\_TYPES respectively. After the output type is set, the encoder enumerates the input types that it supports for the selected output type.

No audio resampling is performed by the Windows Media Audio encoder. This means that the encoder output type and the encoder input type must have the same number of channels, bits per sample, and sample rate. For more information, see [Finding Audio Encoder Output Types](findingaudioencoderoutputtypes.md).

> [!Note]  
>    Each output type enumerated by the audio encoder contains a **WAVEFORMATEX** structure (pointed to by **AM\_MEDIA\_TYPE.pbFormat**) with extended data appended to it. The size of the extended data is specified by **WAVEFORMATEX.cbSize**. This data must be kept with the encoded content so that it can be delivered to the decoder. The content cannot be decompressed without the extended format data.

 

## Related topics

<dl> <dt>

[Working with Audio](workingwithaudio.md)
</dt> </dl>

 

 



