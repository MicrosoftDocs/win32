---
description: This topic introduces bitmap sources, a core Windows Imaging Component (WIC) component that represents the bitmap pixels of an image.
ms.assetid: cff0c088-ca22-4d55-9cf0-9cbe9803923e
title: Bitmap Sources Overview
ms.topic: article
ms.date: 05/31/2018
---

# Bitmap Sources Overview

This topic introduces bitmap sources, a core Windows Imaging Component (WIC) component that represents the bitmap pixels of an image.

This topic contains the following sections.

-   [Bitmap Sources](#bitmap-sources-overview)
-   [Bitmap Frames](#bitmap-frames)
-   [Bitmaps](#bitmap-sources-overview)
-   [Transform Bitmap Sources](#transform-bitmap-sources)
-   [Pixel Format and Color Context Converters](#pixel-format-and-color-context-converters)
-   [Drawing Bitmap Sources](#drawing-bitmap-sources)
-   [Related topics](#related-topics)

## Bitmap Sources

The [**IWICBitmapSource**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsource) component is the basic building block of WIC and represents a single set of pixels. A bitmap source can be an individual frame of a multiframe image, or it can be the result of a transform performed on a bitmap source. The **IWICBitmapSource** interface is the base of many of the primary WIC interfaces such as the decoder frame [**IWICBitmapFrameDecode**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapframedecode) and transform bitmap sources such as the [**IWICBitmapFlipRotator**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapfliprotator).

The following table describes the different bitmap source components provided by WIC.



| Bitmap Sources                                                    | Description                                                          |
|-------------------------------------------------------------------|----------------------------------------------------------------------|
| [**IWICBitmapFrameDecode**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapframedecode) | Represents a decoder image frame.                                    |
| [**IWICBitmap**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmap)                       | Provides writability and in-memory representation to bitmap sources. |
| [**IWICBitmapClipper**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapclipper)         | Clips a bitmap source to a desired rectangle.                        |
| [**IWICBitmapFlipRotator**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapfliprotator) | Flips and/or rotates a bitmap source to a desired orientation.       |
| [**IWICBitmapScaler**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapscaler)           | Scales a bitmap source to a desired size.                            |
| [**IWICColorTransform**](/windows/desktop/api/Wincodec/nn-wincodec-iwiccolortransform)       | Transforms the color context of a bitmap source.                     |
| [**IWICFormatConverter**](/windows/desktop/api/Wincodec/nn-wincodec-iwicformatconverter)     | Converts the pixel format of a bitmap source.                        |



 

## Bitmap Frames

The most common [**IWICBitmapSource**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsource) is the [**IWICBitmapFrameDecode**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapframedecode). This interface is used to access the actual bitmap data of an image format. Many image formats only support a single bitmap frame, while other formats such as GIF and TIFF support multiple frames per image.

For an example on obtaining bitmap frames from an image, see the [How to Retrieve the Frames of an Image](https://www.bing.com/search?q=How+to+Retrieve+the+Frames+of+an+Image) topic.

## Bitmaps

An [**IWICBitmap**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmap) adds the concepts of writability and static in-memory to bitmap sources. WIC bitmaps enables users to directly access the pixels of a bitmap source. This direct access is provided by the [**Lock**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmap-lock) method and supports any combination of read and/or write access to the bitmap pixels. **Lock** method locks the specified bitmap rectangle and provides an [**IWICBitmapLock**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmaplock) object to access the pixels.

For an example using [**IWICBitmap**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmap) and [**IWICBitmapLock**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmaplock) objects, see the [How to Modify the Pixels of a Bitmap Source](-wic-bitmapsources-howto-modifypixels.md) topic.

## Transform Bitmap Sources

WIC provides several [**IWICBitmapSource**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsource) interfaces that transform the pixel data. Specifically, WIC provides bitmap source transforms for scaling, clipping, rotating, and flipping pixel data. These bitmap source transforms are [**IWICBitmapClipper**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapclipper), [**IWICBitmapScaler**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapscaler), and [**IWICBitmapFlipRotator**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapfliprotator). Each of these bitmap sources have a method to initialize and create a new transformed bitmap source. For example, the **IWICBitmapClipper** includes the [**Initialize**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapclipper-initialize) method. This method initializes the clipper bitmap source with the clipped pixel data of the input bitmap source at the given [**WICRect**](/windows/desktop/api/Wincodec/ns-wincodec-wicrect).

The following how-to topics demonstrate different uses of the transform bitmap sources.

-   [How to Scale a Bitmap Source](-wic-bitmapsources-howto-scale.md)
-   [How to Clip a Bitmap Source](-wic-bitmapsources-howto-clip.md)
-   [How to Flip and Rotate a Bitmap Source](-wic-bitmapsources-howto-flipandrotate.md)

## Pixel Format and Color Context Converters

WIC also provides bitmap sources converting the pixel format and color context of a bitmap source. WIC provides the [**IWICFormatConverter**](/windows/desktop/api/Wincodec/nn-wincodec-iwicformatconverter) and [**IWICColorTransform**](/windows/desktop/api/Wincodec/nn-wincodec-iwiccolortransform) for these operations.

[**IWICFormatConverter**](/windows/desktop/api/Wincodec/nn-wincodec-iwicformatconverter) converts a given bitmap source from one pixel format to another.

For an example using the [**IWICFormatConverter**](/windows/desktop/api/Wincodec/nn-wincodec-iwicformatconverter), see the [How to Draw a Bitmap Source Using Direct2D](-wic-bitmapsources-howto-drawusingd2d.md) topic.

## Drawing Bitmap Sources

WIC is a still image codec technology and is used to manage image data and metadata and does not inherently provide a way to render images. However, bitmap sources can be drawn using several Windows graphics technology such as Direct2D, Windows Graphics Device Interface (GDI), and Windows GDI+. Each of these technologies has a different level of interoperability with WIC. Direct2D provides direct interoperability through the [ID2D1Bitmap](../direct2d/render-targets-overview.md) interface and the [ID2D1RenderTarget::CreateBitmapFromWicBitmap](../direct2d/id2d1rendertarget-createbitmapfromwicbitmap.md) method while GDI and GDI+ require users to copy the bitmap source pixels into an [Bitmaps](../gdi/bitmaps.md).

The following example demonstrate how to draw bitmap sources by using Direct2D.

-   [How to Draw a Bitmap Source Using Direct2D](-wic-bitmapsources-howto-drawusingd2d.md)

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> <dt>

[Encoding Overview](-wic-creating-encoder.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> </dl>

 

 
