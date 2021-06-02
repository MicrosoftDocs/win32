---
description: Describes how to add data-unit extensions when using Windows Media encoders.
ms.assetid: fdadcb85-c564-4d05-a4d7-af53a0107455
title: Using Data Unit Extensions (Microsoft Media Foundation)
ms.topic: article
ms.date: 05/31/2018
---

# Using Data Unit Extensions (Microsoft Media Foundation)

The Windows Media Audio and Video codecs are designed to work well with the Advanced Systems Format (ASF) container. ASF is the structured format used for Windows Media Audio (WMA) files and Windows Media Video (WMV) files. It is an extensible format designed for streaming data. One of the unusual characteristics of the ASF structure is the ability to attach metadata to individual samples, and to embed that data with the samples in the bit stream. An item of metadata stored in this way is called a data *unit extension*, or *sample extension*.

A data unit extension can contain information that is required by the encoder, the decoder, or the player application. Most of the data-unit-extension types that are implemented in the Windows Media 9 Series of codecs contain data intended for the application that decodes and renders the media. For example, you can maintain SMPTE time codes from source data by adding them as data unit extensions. However, the following codec features require data unit extensions:

-   [Forced Key Frame Insertion](forcedkeyframeinsertion.md)
-   [Interlaced Video Encoding](interlacedvideoencoding.md)
-   The difficulty in using data unit extensions when accessing the codec directly is the mechanism by which the object receives the extension data. This is achieved by the objects of the Windows Media Format SDK by using buffer objects designed to support this feature. It is recommended that you use the Windows Media Format SDK to activate the codec features that require data unit extensions, but you can make these features work with the standalone codec objects.

## Passing Extended Samples to the Codec Objects

The Windows Media Format SDK uses buffer objects that expose [**INSSBuffer**](/previous-versions/windows/desktop/api/wmsbuffer/nn-wmsbuffer-inssbuffer) interfaces. The latest interface is [**INSSBuffer4**](/previous-versions/windows/desktop/api/wmsbuffer/nn-wmsbuffer-inssbuffer4). To pass samples to a codec object with data unit extensions, you must use a buffer object that implements the [**IMediaBuffer**](/previous-versions/windows/desktop/api/mediaobj/nn-mediaobj-imediabuffer) or [**IMFMediaBuffer**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediabuffer) interface and the **INSSBuffer** interface. You can use buffer objects created by the Windows Media Format SDK or Microsoft Media Foundation to accomplish this, or you can make your own buffer class that meets the requirements. To create your own buffer class, you must conform to the method prototypes for the **INSSBuffer** interfaces. These interface definitions can be found in the wmsbuffer.h header file that is installed with the Windows Media Format SDK.

## Related topics

<dl> <dt>

[Windows Media Codecs](windows-media-codecs.md)
</dt> </dl>

 

 
