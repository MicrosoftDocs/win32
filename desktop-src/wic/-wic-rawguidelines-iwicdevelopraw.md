---
Description: Support for IWICDevelopRaw
ms.assetid: 8e8ff65b-0849-42e0-924e-2a7c61d4b1bb
title: Support for IWICDevelopRaw
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Support for IWICDevelopRaw

To enable applications to support RAW processing, codec authors are strongly encouraged to implement all of the parameters of [**IWICDevelopRaw**](/windows/win32/Wincodec/nn-wincodec-iwicdevelopraw?branch=master). For Windows 7, Windows Imaging Component (WIC) will require support for all of the [**IWICDevelopRaw**](/windows/win32/Wincodec/nn-wincodec-iwicdevelopraw?branch=master). If your file format doesn't support all of these parameters, then you should revise your image file format.

To enable basic RAW processing in applications, codecs must support adjustments to exposure (ExposureCompensationSupport) and color (such as KelvinWhitePointSupport and TintSupport). In addition, output to specific color spaces and pixel formats is highly recommended. Support for other adjustments is, of course, encouraged, and is required for Windows 7.

The RAW codec must provide basic support for image rotation and fast previewing. Rotation can be specified in two distinct ways:

-   [**IWICDevelopRaw**](/windows/win32/Wincodec/nn-wincodec-iwicdevelopraw?branch=master)::[**SetRotation**](/windows/win32/Wincodec/nf-wincodec-iwicdevelopraw-setrotation?branch=master) method. This method sets the desired rotation angle for the output of subsequent calls to [**CopyPixels**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapsource-copypixels?branch=master).
-   [**IWICBitmapSourceTransform**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsourcetransform?branch=master)::[**CopyPixels**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapsource-copypixels?branch=master) method. The caller can set the dstTransform option to indicate the desired rotation angle.

These two approaches differ in the following ways:

-   Only [**IWICDevelopRaw**](/windows/win32/Wincodec/nn-wincodec-iwicdevelopraw?branch=master) settings can be persisted across instances of the decoder object.
-   [**IWICBitmapSourceTransform**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsourcetransform?branch=master)::[**CopyPixels**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapsourcetransform-copypixels?branch=master) applies only to that particular call; there is no persistence of any kind.
-   [**IWICDevelopRaw**](/windows/win32/Wincodec/nn-wincodec-iwicdevelopraw?branch=master) provides for much finer grained control in rotation. [**IWICBitmapSourceTransform**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsourcetransform?branch=master)::[**CopyPixels**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapsourcetransform-copypixels?branch=master) is constrained to 90-degree increments.

If rotation is specified in both [**IWICDevelopRaw**](/windows/win32/Wincodec/nn-wincodec-iwicdevelopraw?branch=master) and [**IWICBitmapSourceTransform**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsourcetransform?branch=master), then the rotation effect is cumulative. For example, if [**IWICDevelopRaw**](/windows/win32/Wincodec/nn-wincodec-iwicdevelopraw?branch=master) specifies a 25-degree rotation and [**IWICBitmapSourceTransform**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsourcetransform?branch=master) specifies a 90-degree rotation, then the following should happen:

-   Calls to [**IWICBitmapFrameDecode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframedecode?branch=master)::[**CopyPixels**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapsource-copypixels?branch=master) should apply a 25-degree rotation (that is, only the amount specified in [**IWICDevelopRaw**](/windows/win32/Wincodec/nn-wincodec-iwicdevelopraw?branch=master)).
-   Calls to [**IWICBitmapSourceTransform**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsourcetransform?branch=master)::[**CopyPixels**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapsourcetransform-copypixels?branch=master) with a dstTransform amount of 90 then result in a 115-degree rotation (25 + 90).
-   Again, only the 25-degree rotation specified via [**IWICDevelopRaw**](/windows/win32/Wincodec/nn-wincodec-iwicdevelopraw?branch=master)::[**SetRotation**](/windows/win32/Wincodec/nf-wincodec-iwicdevelopraw-setrotation?branch=master) can be persisted.

In Windows Vista, the [**IWICBitmapFrameDecode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframedecode?branch=master)::[**GetThumbnail**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframedecode-getthumbnail?branch=master) and [**IWICBitmapDecoder**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapdecoder?branch=master)::[**GetPreview**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapdecoder-getpreview?branch=master) methods allow callers to get embedded thumbnails and preview images, respectively. These are intended to return precalculated previews and thumbnails from the image file stream. Generating previews or thumbnails "on the fly" results in poor performance in the Windows Explorer and Photo Viewer. The codec also must provide a way to return an updated screen resolution image quickly when users are doing interactive control of the processing settings.

Calls to [**IWICDevelopRaw**](/windows/win32/Wincodec/nn-wincodec-iwicdevelopraw?branch=master)::[**SetRenderMode**](/windows/win32/Wincodec/nf-wincodec-iwicdevelopraw-setrendermode?branch=master) will determine what subsequent calls to [**IWICBitmapFrameDecode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframedecode?branch=master)::[**CopyPixels**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapsource-copypixels?branch=master) return (favoring either speed or quality). Additionally, the IWICBitmapSourceTransform interface can be used to determine whether downsampling is necessary and can increase performance when it can be applied. The color fidelity of all the images should be comparable. When changes are made to the processing settings, all of these renderings should reflect the changes.

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

 

 



