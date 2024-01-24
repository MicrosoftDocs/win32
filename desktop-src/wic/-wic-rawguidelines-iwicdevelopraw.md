---
description: Support for IWICDevelopRaw
ms.assetid: 8e8ff65b-0849-42e0-924e-2a7c61d4b1bb
title: Support for IWICDevelopRaw
ms.topic: article
ms.date: 05/31/2018
---

# Support for IWICDevelopRaw

To enable applications to support RAW processing, codec authors are strongly encouraged to implement all of the parameters of [**IWICDevelopRaw**](/windows/desktop/api/Wincodec/nn-wincodec-iwicdevelopraw). For Windows 7, Windows Imaging Component (WIC) will require support for all of the [**IWICDevelopRaw**](/windows/desktop/api/Wincodec/nn-wincodec-iwicdevelopraw). If your file format doesn't support all of these parameters, then you should revise your image file format.

To enable basic RAW processing in applications, codecs must support adjustments to exposure (ExposureCompensationSupport) and color (such as KelvinWhitePointSupport and TintSupport). In addition, output to specific color spaces and pixel formats is highly recommended. Support for other adjustments is, of course, encouraged, and is required for Windows 7.

The RAW codec must provide basic support for image rotation and fast previewing. Rotation can be specified in two distinct ways:

-   [**IWICDevelopRaw**](/windows/desktop/api/Wincodec/nn-wincodec-iwicdevelopraw)::[**SetRotation**](/windows/desktop/api/Wincodec/nf-wincodec-iwicdevelopraw-setrotation) method. This method sets the desired rotation angle for the output of subsequent calls to [**CopyPixels**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapsource-copypixels).
-   [**IWICBitmapSourceTransform**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsourcetransform)::[**CopyPixels**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapsource-copypixels) method. The caller can set the dstTransform option to indicate the desired rotation angle.

These two approaches differ in the following ways:

-   Only [**IWICDevelopRaw**](/windows/desktop/api/Wincodec/nn-wincodec-iwicdevelopraw) settings can be persisted across instances of the decoder object.
-   [**IWICBitmapSourceTransform**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsourcetransform)::[**CopyPixels**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapsourcetransform-copypixels) applies only to that particular call; there is no persistence of any kind.
-   [**IWICDevelopRaw**](/windows/desktop/api/Wincodec/nn-wincodec-iwicdevelopraw) provides for much finer grained control in rotation. [**IWICBitmapSourceTransform**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsourcetransform)::[**CopyPixels**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapsourcetransform-copypixels) is constrained to 90-degree increments.

If rotation is specified in both [**IWICDevelopRaw**](/windows/desktop/api/Wincodec/nn-wincodec-iwicdevelopraw) and [**IWICBitmapSourceTransform**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsourcetransform), then the rotation effect is cumulative. For example, if [**IWICDevelopRaw**](/windows/desktop/api/Wincodec/nn-wincodec-iwicdevelopraw) specifies a 25-degree rotation and [**IWICBitmapSourceTransform**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsourcetransform) specifies a 90-degree rotation, then the following should happen:

-   Calls to [**IWICBitmapFrameDecode**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapframedecode)::[**CopyPixels**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapsource-copypixels) should apply a 25-degree rotation (that is, only the amount specified in [**IWICDevelopRaw**](/windows/desktop/api/Wincodec/nn-wincodec-iwicdevelopraw)).
-   Calls to [**IWICBitmapSourceTransform**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsourcetransform)::[**CopyPixels**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapsourcetransform-copypixels) with a dstTransform amount of 90 then result in a 115-degree rotation (25 + 90).
-   Again, only the 25-degree rotation specified via [**IWICDevelopRaw**](/windows/desktop/api/Wincodec/nn-wincodec-iwicdevelopraw)::[**SetRotation**](/windows/desktop/api/Wincodec/nf-wincodec-iwicdevelopraw-setrotation) can be persisted.

In Windows Vista, the [**IWICBitmapFrameDecode**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapframedecode)::[**GetThumbnail**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapframedecode-getthumbnail) and [**IWICBitmapDecoder**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapdecoder)::[**GetPreview**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapdecoder-getpreview) methods allow callers to get embedded thumbnails and preview images, respectively. These are intended to return precalculated previews and thumbnails from the image file stream. Generating previews or thumbnails "on the fly" results in poor performance in the Windows Explorer and Photo Viewer. The codec also must provide a way to return an updated screen resolution image quickly when users are doing interactive control of the processing settings.

Calls to [**IWICDevelopRaw**](/windows/desktop/api/Wincodec/nn-wincodec-iwicdevelopraw)::[**SetRenderMode**](/windows/desktop/api/Wincodec/nf-wincodec-iwicdevelopraw-setrendermode) will determine what subsequent calls to [**IWICBitmapFrameDecode**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapframedecode)::[**CopyPixels**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapsource-copypixels) return (favoring either speed or quality). Additionally, the IWICBitmapSourceTransform interface can be used to determine whether downsampling is necessary and can increase performance when it can be applied. The color fidelity of all the images should be comparable. When changes are made to the processing settings, all of these renderings should reflect the changes.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> <dt>

[WIC Guidelines for Camera RAW Image Formats](-wic-rawguidelines.md)
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> </dl>

 

 



