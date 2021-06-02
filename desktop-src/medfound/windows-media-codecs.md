---
description: The Windows Media Audio and Video codecs are a collection of objects that you can use to compress and decompress digital media data.
ms.assetid: '74de2e75-b1ee-436d-8d78-efe366ab7aa6'
title: Windows Media Codecs
ms.topic: article
ms.date: 05/31/2018
---

# Windows Media Codecs

The Windows Media Audio and Video codecs are a collection of objects that you can use to compress and decompress digital media data. Each codec consists of two objects, an encoder and a decoder. This part of the documentation describes how to use the features of the Windows Media Audio and Video codecs to produce and consume compressed data streams.

> [!Note]  
> This documentation is primarily for developers who want to use Windows Media codecs in their C++-based media applications. For a technical overview of the features of the Windows Media codecs, see [About the Windows Media Codecs](about-the-windows-media-codecs.md).

 

The term *codec* is an amalgamation of the terms compressor and decompressor. A codec is usually implemented as a pair of COM objects: one for encoding content, and another for decoding content. In some cases the COM objects occupy the same dynamically linked library (DLL).

Every codec object implements two separate but similar interfaces:



| Interface                              | Description                                 |
|----------------------------------------|---------------------------------------------|
| [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform)   | Compatible with Microsoft Media Foundation. |
| [**IMediaObject**](/previous-versions/windows/desktop/api/mediaobj/nn-mediaobj-imediaobject) | Compatible with DirectShow.                 |



 

Not only are there different codecs for audio and for video, but also different codecs for different kinds of content that you might want to put into an audio or video file. The algorithms used to compress and decompress data for spoken words differ from the algorithms used to compress and decompress music data.

## Codec Descriptions

The following table describes the intended uses of the Windows Media codecs.



| Codec                                                                     | Description                                                                                                                                                                                                                                                                                  |
|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Windows Media Audio](windowsmediaaudioencoder.md)                       | An audio codec that supports three categories of encoded content: Standard, Professional, and Lossless.                                                                                                                                                                                      |
| [Windows Media Audio Voice](windowsmediaaudiovoiceencoder.md)            | Audio codec optimized for encoding the human voice at high compression ratios. This is the preferred codec for streams consisting mostly of spoken words. For content that is mixed music and speech, this codec can dynamically change the encoding algorithm used, to get optimal quality. |
| [Windows Media Video 9](windowsmediavideo9encoder.md)                    | A video codec that supports four categories of encoded content: Simple Profile, Main Profile, Advanced Profile, and Image..                                                                                                                                                                  |
| [Windows Media Video 9 Screen](usingthewindowsmediavideo9screencodec.md) | Video codec optimized for encoding sequential screen shots from computer monitors. This codec is often used for software training or support by recording monitor images while computer applications are being used.                                                                         |



 

The most recent versions of the codec objects also enable access to some legacy codecs, including Windows Media Video 7 and 8, Windows Media Screen 7, the older Microsoft MPEG-4 codecs, and the Microsoft ISO MPEG-4 codecs.

> [!Note]  
> This documentation does not cover these legacy codecs; it covers only the current versions of codecs.

 

For older codecs, use the same procedures as when using the current codecs; however, remember that not all features are supported in all codecs.

## In this section

-   [About the Windows Media Codecs](about-the-windows-media-codecs.md)
-   [Using the Codec and DSP Objects](decidinghowtousethewindowsmediaaudioandvideocodecs.md)
-   [Encoding Methods](encodingmethods.md)
-   [Codec Implementation](codecimplementation.md)
-   [The Leaky Bucket Buffer Model](the-leaky-bucket-buffer-model.md)
-   [Working with Codec DMOs](workingwithcodecdmos.md)
-   [Working with Codec MFTs](workingwithcodecmfts.md)
-   [Working with Audio](workingwithaudio.md)
-   [Working with Video](workingwithvideo.md)
-   [Storing Compressed Media in AVI Files](storingcompressedmediainavifiles.md)
-   [Using VBR Encoding](usingvbrencoding.md)
-   [Using Two-Pass Encoding](usingtwoencodingpasses.md)
-   [Getting Encoding Statistics](gettingencodingstatistics.md)
-   [Using Data Unit Extensions](usingdataunitextensions.md)
-   [Codec and DSP IPropertyBag Constants](codecanddspproperties.md)
-   [Table of Contents Parser](toc-parser.md)
-   [Windows Media Codec FAQ](frequentlyaskedquestions.md)

## Related topics

<dl> <dt>

[Media Foundation Programming Guide](media-foundation-programming-guide.md)
</dt> <dt>

[Media Technologies for Windows](/previous-versions/bg125389(v=msdn.10))
</dt> </dl>

 

 
