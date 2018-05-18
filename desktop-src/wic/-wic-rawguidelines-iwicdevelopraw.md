---
Description: Support for IWICDevelopRaw
ms.assetid: '8e8ff65b-0849-42e0-924e-2a7c61d4b1bb'
title: Support for IWICDevelopRaw
---

# Support for IWICDevelopRaw

To enable applications to support RAW processing, codec authors are strongly encouraged to implement all of the parameters of [**IWICDevelopRaw**](-wic-codec-iwicdevelopraw.md). For Windows 7, Windows Imaging Component (WIC) will require support for all of the [**IWICDevelopRaw**](-wic-codec-iwicdevelopraw.md). If your file format doesn't support all of these parameters, then you should revise your image file format.

To enable basic RAW processing in applications, codecs must support adjustments to exposure (ExposureCompensationSupport) and color (such as KelvinWhitePointSupport and TintSupport). In addition, output to specific color spaces and pixel formats is highly recommended. Support for other adjustments is, of course, encouraged, and is required for Windows 7.

The RAW codec must provide basic support for image rotation and fast previewing. Rotation can be specified in two distinct ways:

-   [**IWICDevelopRaw**](-wic-codec-iwicdevelopraw.md)::[**SetRotation**](-wic-codec-iwicdevelopraw-setrotation.md) method. This method sets the desired rotation angle for the output of subsequent calls to [**CopyPixels**](-wic-codec-iwicbitmapsource-copypixels.md).
-   [**IWICBitmapSourceTransform**](-wic-codec-iwicbitmapsourcetransform.md)::[**CopyPixels**](-wic-codec-iwicbitmapsource-copypixels.md) method. The caller can set the dstTransform option to indicate the desired rotation angle.

These two approaches differ in the following ways:

-   Only [**IWICDevelopRaw**](-wic-codec-iwicdevelopraw.md) settings can be persisted across instances of the decoder object.
-   [**IWICBitmapSourceTransform**](-wic-codec-iwicbitmapsourcetransform.md)::[**CopyPixels**](-wic-codec-iwicbitmapsourcetransform-copypixels.md) applies only to that particular call; there is no persistence of any kind.
-   [**IWICDevelopRaw**](-wic-codec-iwicdevelopraw.md) provides for much finer grained control in rotation. [**IWICBitmapSourceTransform**](-wic-codec-iwicbitmapsourcetransform.md)::[**CopyPixels**](-wic-codec-iwicbitmapsourcetransform-copypixels.md) is constrained to 90-degree increments.

If rotation is specified in both [**IWICDevelopRaw**](-wic-codec-iwicdevelopraw.md) and [**IWICBitmapSourceTransform**](-wic-codec-iwicbitmapsourcetransform.md), then the rotation effect is cumulative. For example, if [**IWICDevelopRaw**](-wic-codec-iwicdevelopraw.md) specifies a 25-degree rotation and [**IWICBitmapSourceTransform**](-wic-codec-iwicbitmapsourcetransform.md) specifies a 90-degree rotation, then the following should happen:

-   Calls to [**IWICBitmapFrameDecode**](-wic-codec-iwicbitmapframedecode.md)::[**CopyPixels**](-wic-codec-iwicbitmapsource-copypixels.md) should apply a 25-degree rotation (that is, only the amount specified in [**IWICDevelopRaw**](-wic-codec-iwicdevelopraw.md)).
-   Calls to [**IWICBitmapSourceTransform**](-wic-codec-iwicbitmapsourcetransform.md)::[**CopyPixels**](-wic-codec-iwicbitmapsourcetransform-copypixels.md) with a dstTransform amount of 90 then result in a 115-degree rotation (25 + 90).
-   Again, only the 25-degree rotation specified via [**IWICDevelopRaw**](-wic-codec-iwicdevelopraw.md)::[**SetRotation**](-wic-codec-iwicdevelopraw-setrotation.md) can be persisted.

In Windows Vista, the [**IWICBitmapFrameDecode**](-wic-codec-iwicbitmapframedecode.md)::[**GetThumbnail**](-wic-codec-iwicbitmapframedecode-getthumbnail.md) and [**IWICBitmapDecoder**](-wic-codec-iwicbitmapdecoder.md)::[**GetPreview**](-wic-codec-iwicbitmapdecoder-getpreview.md) methods allow callers to get embedded thumbnails and preview images, respectively. These are intended to return precalculated previews and thumbnails from the image file stream. Generating previews or thumbnails "on the fly" results in poor performance in the Windows Explorer and Photo Viewer. The codec also must provide a way to return an updated screen resolution image quickly when users are doing interactive control of the processing settings.

Calls to [**IWICDevelopRaw**](-wic-codec-iwicdevelopraw.md)::[**SetRenderMode**](-wic-codec-iwicdevelopraw-setrendermode.md) will determine what subsequent calls to [**IWICBitmapFrameDecode**](-wic-codec-iwicbitmapframedecode.md)::[**CopyPixels**](-wic-codec-iwicbitmapsource-copypixels.md) return (favoring either speed or quality). Additionally, the IWICBitmapSourceTransform interface can be used to determine whether downsampling is necessary and can increase performance when it can be applied. The color fidelity of all the images should be comparable. When changes are made to the processing settings, all of these renderings should reflect the changes.

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

 

 



