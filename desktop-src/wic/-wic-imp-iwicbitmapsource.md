---
Description: Implementing IWICBitmapSource
ms.assetid: 'd092e9e5-c041-42f5-84c8-0af52bb5c810'
title: Implementing IWICBitmapSource
---

# Implementing IWICBitmapSource

## IWICBitmapSource

[**IWICBitmapSource**](-wic-codec-iwicbitmapsource.md) is important for working with images from an application perspective. It represents the highest level abstraction for an image source, and all Windows Imaging Component (WIC) interfaces that represent an image, including [**IWICBitmapFrameDecode**](-wic-codec-iwicbitmapframedecode.md), [**IWICBitmap**](-wic-codec-iwicbitmap.md), and all the transform interfaces ([**IWICBitmapScaler**](-wic-codec-iwicbitmapscaler.md), [**IWICBitmapClipper**](-wic-codec-iwicbitmapclipper.md), [**IWICBitmapFlipRotator**](-wic-codec-iwicbitmapfliprotator.md), and [**IWICFormatConverter**](-wic-codec-iwicformatconverter.md)) are derived from it. At any specific time, an **IWICBitmapSource** object may or may not be backed by an actual bitmap in memory. This enables very efficient processing by an application, because an image can be dealt with as an abstraction. Transform operations can be chained in a transform pipeline without consuming memory resources until the application is ready to render or print the image, at which time it invokes the [**CopyPixels**](-wic-codec-iwicbitmapsource-copypixels.md) method on the final transform to get a bitmap in memory of the image with the selected transforms applied.

``` syntax
interface IWICBitmapSource : IUnknown
{
   // Required methods
   HRESULT GetSize ( UINT *puiWidth, UINT *puiHeight );
   HRESULT GetPixelFormat ( WICPixelFormatGUID *pPixelFormat );
   HRESULT GetResolution ( double *pDpiX, double *pDpiY );
   HRESULT CopyPixels ( const WICRect *prc,
      UINT cbStride,
      UINT cbBufferSize, 
      BYTE *pbBuffer );
   // Optional method
   HRESULT CopyPalette ( IWICPalette *pIPalette );
}
```

From a codec perspective, the [**IWICBitmapSource**](-wic-codec-iwicbitmapsource.md) methods are implemented on the frame decoder object. These methods are described in Implementing IWICBitmapSource, along with the other methods on [**IWICBitmapFrameDecode**](-wic-codec-iwicbitmapframedecode.md), which is derived from **IWICBitmapSource**.

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[**IWICBitmapDecoder**](-wic-codec-iwicbitmapdecoder.md)
</dt> <dt>

[**IWICBitmapSource**](-wic-codec-iwicbitmapsource.md)
</dt> <dt>

[**IWICBitmapFrameDecode**](-wic-codec-iwicbitmapframedecode.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Implementing IWICBitmapCodecProgressNotification (Decoder)](-wic-imp-iwicbitmapcodecprogressnotification-decoder.md)
</dt> <dt>

[Implementing IWICBitmapFrameDecode](-wic-imp-iwicbitmapframedecode.md)
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> </dl>

 

 



