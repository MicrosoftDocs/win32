---
description: Implementing IWICBitmapSourceTransform
ms.assetid: 6a3e682c-55c6-4728-9d14-5eb0290f3dcc
title: Implementing IWICBitmapSourceTransform
ms.topic: article
ms.date: 05/31/2018
---

# Implementing IWICBitmapSourceTransform

## IWICBitmapSourceTransform

Though optional, we highly recommend that every decoder implement this interface on your frame-level decoding class, because it can provide major performance benefits. When an application requests a specific region of interest, size, orientation, or pixel format, instead of just decoding the whole image at full resolution and then applying the requested transforms, Windows Imaging Component (WIC) calls [IUnknown::QueryInterface](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) for this interface on the [**IWICBitmapFrameDecode**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapframedecode) object. If the frame decoder supports it, WIC calls the appropriate method or methods to determine whether the frame decoder can perform the requested transform or determine the closest size or pixel format the decoder can provide to the one requested. If the decoder can perform the requested transform or transforms, WIC invokes [**CopyPixels**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapsourcetransform-copypixels) with the appropriate parameters. If the decoder can perform some, but not all of the requested transforms, WIC asks the decoder to perform those that it can, and uses the WIC transform objects ([**IWICBitmapScaler**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapscaler), [**IWICBitmapClipper**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapclipper), [**IWICBitmapFlipRotator**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapfliprotator), and [**IWICFormatConverter**](/windows/desktop/api/Wincodec/nn-wincodec-iwicformatconverter)) to perform the remaining transforms that could not be performed by the frame decoder on the result of the **CopyPixels** call. If the decoder doesn’t support [**IWICBitmapSourceTransform**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsourcetransform), then WIC must use the transform objects to perform all of the transforms. It’s usually much more efficient for the decoder to perform transforms during the decoding process than it is to decode the entire image and then perform the transforms. This is especially true for operations such as scaling to a much smaller size or pixel format conversions.


```C++
interface IWICBitmapSourceTransform : IUnknown
{
   // Required methods
   HRESULT DoesSupportTransform ( WICTransformOptions dstTransform,
              BOOL *pfIsSupported);
   HRESULT CopyPixels ( WICRect *prcSrc, 
      UINT uiWidth, 
      UINT uiHeight,
      WICPixelFormatGUID * pguidDstFormat,
      WICBitmapTransformOptions dstTransform, 
      UINT nStride, 
      UINT cbBufferSize, 
      BYTE *pbBuffer );

   // Optional methods
   HRESULT GetClosestSize ( UINT *puiWidth,
              UINT *puiHeight);
   HRESULT GetClosestPixelFormat ( WICPixelFormatGUID *pguidDstFormat);
}
```



-   [DoesSupportTransform](#doessupporttransform)
-   [CopyPixels](#copypixels)
-   [GetClosestSize](#getclosestsize)
-   [GetClosestPixelFormat](#getclosestpixelformat)

### DoesSupportTransform

[**DoesSupportTransform**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapsourcetransform-doessupporttransform) asks whether the decoder supports the requested rotation or flipping operation. The [**WICBitmapTransformOptions**](/windows/desktop/api/Wincodec/ne-wincodec-wicbitmaptransformoptions) that may be requested are:


```C++
enum WICBitmapTransformOptions
{   
   WICBitmapTransformRotate0,
   WICBitmapTransformRotate90,
   WICBitmapTransformRotate180,
   WICBitmapTransformRotate270,
   WICBitmapTransformFlipHorizontal,
   WICBitmapTransformFlipVertical
}
```



### CopyPixels

[**CopyPixels**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapsourcetransform-copypixels) performs the actual work of decoding the image bits, such as the [**CopyPixels**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapsource-copypixels) method on the [**IWICBitmapSource**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsource) interface, but the [**CopyPixels**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapsourcetransform-copypixels) method on [**IWICBitmapSourceTransform**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsourcetransform) is much more powerful, and can improve image processing performance significantly.

When multiple transform operations are requested, the result is dependent on the order in which the operations are performed. To ensure predictability and consistency across codecs, it’s important that all codecs perform these operations in the same order. This is the canonical order for performing these operations.

1.  Scale
2.  Crop
3.  Rotate

Pixel format conversion can be performed at any time, because it has no effect on the other transforms.

The first parameter, *prcSrc*, is used to specify the region of interest for clipping the image. Because scaling is performed before clipping by convention, if the image is to be scaled as well as clipped, the region of interest should be determined after the image has been scaled.

The second and third parameters indicate the size to which to scale the image.

The *pguidDstFormat* parameter indicates the requested pixel format for the decoded image. Because WIC has already called [**GetClosestPixelFormat**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapsourcetransform-getclosestpixelformat), this should be a pixel format that the decoder has indicated that it supports.

The *dstTransform* parameter indicates the requested rotation angle, and whether to flip the image vertically, horizontally, or both. Again, because WIC will have already called [**DoesSupportTransform**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapsourcetransform-doessupporttransform), the requested transform should be one that the decoder has already indicated that it supports. Remember that rotation should always be performed after scaling and clipping.

### GetClosestSize

[**GetClosestSize**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapsourcetransform-getclosestsize) takes two in/out parameters. The caller uses the *puiWidth* and *puiHeight* parameters to specify the size at which that the caller prefers the image to be decoded. However, a decoder can decode an image only to a size that’s a multiple of its DCT size, and different image formats can have different DCT sizes. The decoder should determine, based on its own DCT size, the closest it can come to the requested size, and set the *puiWidth* and *puiHeight* to those dimensions on return. If a larger size is requested, but the codec doesn’t support upscaling, the original should be returned.

### GetClosestPixelFormat

[**GetClosestPixelFormat**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapsourcetransform-getclosestpixelformat) is used to determine the closest pixel format to the requested pixel format that the decoder can provide without loss of data. It’s always preferable to convert to a wider pixel format than a narrower one, even though it will increase the size of the image, because it can always be reconverted to a more restrictive format if necessary. However, after the data is lost, it can’t be recovered.

## Continued Reading

To learn more about how to create a WIC-enabled codec, see [Implementing IWICDevelopRaw](-wic-imp-iwicdevelopraw.md).

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[**IWICBitmapSourceTransform**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsourcetransform)
</dt> <dt>

[**IWICMetadataBlockReader**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicmetadatablockreader)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Implementing IWICMetadataBlockReader](-wic-imp-iwicmetadatablockreader.md)
</dt> <dt>

[Implementing IWICDevelopRaw](-wic-imp-iwicdevelopraw.md)
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> </dl>

 

 
