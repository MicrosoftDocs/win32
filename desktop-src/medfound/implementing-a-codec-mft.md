---
Description: 'This topic provides some guidelines for implementing a decoder or encoder as a Media Foundation Transform (MFT) .'
ms.assetid: 'b15bda0a-0fdd-4601-975d-a71c47c974bf'
title: Implementing a Codec MFT
---

# Implementing a Codec MFT

This topic provides some guidelines for implementing a decoder or encoder as a Media Foundation Transform (MFT) .

-   [Encoders](#encoders)
    -   [Encoder Format Negotiation](#encoder-format-negotiation)
-   [Decoders](#decoders)
    -   [Transcode-Only Decoders](#transcode-only-decoders)
    -   [Telecine Attributes](#telecine-attributes)
-   [Related topics](#related-topics)

## Encoders

### Encoder Format Negotiation

The following procedure is used to initialize an encoder:

1.  Query the MFT for the [**ICodecAPI**](dshow.icodecapi) interface.
2.  Call [**ICodecAPI::SetValue**](dshow.icodecapi_setvalue) to set encoding properties.
3.  Call [**IMFTransform::SetOutputType**](imftransform-setoutputtype.md) to set the encoding format.
4.  Call [**IMFTransform::GetInputAvailableType**](imftransform-getinputavailabletype.md) to get a list of compatible input types. (This step might be skipped.)
5.  Call [**IMFTransform::SetInputType**](imftransform-setinputtype.md) to set the uncompressed input format.

After the output type is set in step 3, the [**GetInputAvailableType**](imftransform-getinputavailabletype.md) method must return a list of input types that are compatible with the current output type. In other words, any types returned by **GetInputAvailableType** at this point must be valid for [**SetInputType**](imftransform-setinputtype.md).

For decoders, the order in which types are set is reversed: The input type is set first, followed by the output type. After the input type is set, the [**IMFTransform::GetOutputAvailableType**](imftransform-getoutputavailabletype.md) method must return a list of types that can be passed to the [**IMFTransform::SetOutputType**](imftransform-setoutputtype.md) method.

Encoders and decoders should support NV12 as a common uncompressed format. This ensures that pipeline components can interoperate with minimal colorspace conversions. Of course, other formats can be supported as well.

## Decoders

### Transcode-Only Decoders

Some decoders are optimized for transcoding (decoding and then re-encoding a stream) and are not suitable for use during playback.

If a decoder MFT is intended only for transcoding, set the **MFT\_ENUM\_FLAG\_TRANSCODE\_ONLY** flag when you register the MFT. (See [**MFTRegister**](mftregister.md).)

By default, transcode decoders are not returned by the [**MFTEnumEx**](mftenumex.md) function. To enumerate transcode decoders, call **MFTEnumEx** and set the **MFT\_ENUM\_FLAG\_TRANSCODE\_ONLY** flag in *Flags* parameter. When used in the **MFTEnumEx** function, this flag enumerated both transcode decoders and other decoders.



| MFTRegister **MFT\_ENUM\_FLAG\_TRANSCODE\_ONLY** | MFTEnumEx **MFT\_ENUM\_FLAG\_TRANSCODE\_ONLY** | Is MFT Enumerated? |
|--------------------------------------------------|------------------------------------------------|--------------------|
| 1                                                | 1                                              | Yes                |
| 1                                                | 0                                              | No                 |
| 0                                                | 1                                              | Yes                |
| 0                                                | 0                                              | Yes                |



 

### Telecine Attributes

The media source might attach the following telecine attributes to the media samples that it delivers.



| Attribute                                                                                   | Description                                    |
|---------------------------------------------------------------------------------------------|------------------------------------------------|
| [**MFSampleExtension\_RepeatFirstField**](mfsampleextension-repeatfirstfield-attribute.md) | Equivalent to "repeat first field" (RFF) flag. |
| [**MFSampleExtension\_BottomFieldFirst**](mfsampleextension-bottomfieldfirst-attribute.md) | Inverse of "top field first" (TFF) flag.       |



 

These flags provide a hint to the enhanced video renderer (EVR) when it performs deinterlacing. A decoder should propagate these flags downstream by copying them to the output samples, so that they reach the EVR.

## Related topics

<dl> <dt>

[Writing a Custom MFT](writing-a-custom-mft.md)
</dt> </dl>

 

 



