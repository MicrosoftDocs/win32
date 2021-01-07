---
description: The topic introduces the bitmap decoder, a core Windows Imaging Component (WIC) codec component used to decode image files from a stream.
ms.assetid: 9dc8d2ec-5cc5-45fa-8a4d-5bdc3072c90c
title: Decoding Overview
ms.topic: article
ms.date: 05/31/2018
---

# Decoding Overview

The topic introduces the bitmap decoder, a core Windows Imaging Component (WIC) codec component used to decode image files from a stream.

This topic contains the following sections.

-   [Introduction](#introduction)
-   [Native Bitmap Decoders](#native-bitmap-decoders)
-   [Creating a Bitmap Decoder](#creating-a-bitmap-decoder)
-   [Decoder Extensibility](#decoder-extensibility)
-   [Related topics](#related-topics)

## Introduction

Bitmap decoders can be viewed as the outer container of a digital image and provides access to global properties and image frames. Some image formats support global thumbnails, previews, color contexts, or metadata, while others provide these properties only at the frame level. Note, however, many of the standard image formats do not support these global properties. As such, many of the native codec implementations provided by WIC do not support the majority of these global properties. See the table in the Native Bitmap Decoders section of this topic for information about global property support.

In WIC, bitmap decoders are represented by the [**IWICBitmapDecoder**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapdecoder) interface and provides access to these global properties of the bitmap and, more importantly, the frames it contains. The [**IWICBitmapFrameDecode**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapframedecode) interface represents an individual bitmap frame and is discussed in detail in the [Bitmap Sources Overview](-wic-bitmapsources.md).

## Native Bitmap Decoders

WIC provides several native implementations of the [**IWICBitmapDecoder**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapdecoder) interface for the standard web image formats and the high dynamic range HD Photo format. The following table lists the available native decoders, class identifier name, and support for global properties. Though a feature may not support a property such as thumbnails at the global level, the image format may support such properties at the individual frame level.



| Image Format | CLSID Name            | Thumbnails | Previews | Color Contexts | Metadata |
|--------------|-----------------------|------------|----------|----------------|----------|
| BMP          | CLSID\_WICBmpDecoder  | No         | No       | No             | No       |
| GIF          | CLSID\_WICGifDecoder  | No         | No       | No             | Yes      |
| ICO          | CLSID\_WICIcoDecoder  | No         | No       | No             | No       |
| JPEG         | CLSID\_WICJpegDecoder | No         | No       | No             | No       |
| PNG          | CLSID\_WICPngDecoder  | No         | No       | No             | No       |
| TIFF         | CLSID\_WICTiffDecoder | No         | No       | No             | No       |
| HD Photo     | CLSID\_WICWmpDecoder  | No         | Yes      | No             | No       |



 

## Creating a Bitmap Decoder

To decode an image using WIC, you first need to create an instance of the [**IWICBitmapDecoder**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapdecoder) for the targeted image format. The decoder instance enables you to access the global properties and metadata, if supported, as well as the image frames. The WIC imaging factory, [**IWICImagingFactory**](/windows/desktop/api/Wincodec/nn-wincodec-iwicimagingfactory), provides several methods for creating bitmap decoders. The following factory methods are provided to create bitmap decoders.

-   [**CreateDecoder**](/windows/desktop/api/Wincodec/nf-wincodec-iwicimagingfactory-createdecoder)
-   [**CreateDecoderFromFileHandle**](/windows/desktop/api/Wincodec/nf-wincodec-iwicimagingfactory-createdecoderfromfilehandle)
-   [**CreateDecoderFromFilename**](/windows/desktop/api/Wincodec/nf-wincodec-iwicimagingfactory-createdecoderfromfilename)
-   [**CreateDecoderFromStream**](/windows/desktop/api/Wincodec/nf-wincodec-iwicimagingfactory-createdecoderfromstream)

The following code demonstrates the how to create a bitmap decoder using an image filename and retrieve the first frame of the image.


```C++
   // Create a decoder
   IWICBitmapDecoder *pDecoder = NULL;

   hr = m_pIWICFactory->CreateDecoderFromFilename(
       szFileName,                      // Image to be decoded
       NULL,                            // Do not prefer a particular vendor
       GENERIC_READ,                    // Desired read access to the file
       WICDecodeMetadataCacheOnDemand,  // Cache metadata when needed
       &pDecoder                        // Pointer to the decoder
       );

   // Retrieve the first frame of the image from the decoder
   IWICBitmapFrameDecode *pFrame = NULL;

   if (SUCCEEDED(hr))
   {
       hr = pDecoder->GetFrame(0, &pFrame);
   }
```



## Decoder Extensibility

One of the core features of WIC is an extensibility framework that enables codec developers to develop their own image codecs and get the same platform support as the native implementations of image codecs. A single, consistent set of interfaces is used for all image processing, regardless of image format. Any application using WIC gets automatic support for new image formats as soon as the codec is installed. For more information on codec development, see the topics in [Component Development](-wic-component-development.md). For more information on decoder development, see [Implementing a WIC-Enabled Decoder](-wic-implementingwicdecoder.md).

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> <dt>

[Encoding Overview](-wic-creating-encoder.md)
</dt> <dt>

[Component Development](-wic-component-development.md)
</dt> </dl>

 

 



