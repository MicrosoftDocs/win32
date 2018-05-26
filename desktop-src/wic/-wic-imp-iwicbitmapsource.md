---
Description: Implementing IWICBitmapSource
ms.assetid: d092e9e5-c041-42f5-84c8-0af52bb5c810
title: Implementing IWICBitmapSource
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Implementing IWICBitmapSource

## IWICBitmapSource

[**IWICBitmapSource**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsource?branch=master) is important for working with images from an application perspective. It represents the highest level abstraction for an image source, and all Windows Imaging Component (WIC) interfaces that represent an image, including [**IWICBitmapFrameDecode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframedecode?branch=master), [**IWICBitmap**](/windows/win32/Wincodec/nn-wincodec-iwicbitmap?branch=master), and all the transform interfaces ([**IWICBitmapScaler**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapscaler?branch=master), [**IWICBitmapClipper**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapclipper?branch=master), [**IWICBitmapFlipRotator**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapfliprotator?branch=master), and [**IWICFormatConverter**](/windows/win32/Wincodec/nn-wincodec-iwicformatconverter?branch=master)) are derived from it. At any specific time, an **IWICBitmapSource** object may or may not be backed by an actual bitmap in memory. This enables very efficient processing by an application, because an image can be dealt with as an abstraction. Transform operations can be chained in a transform pipeline without consuming memory resources until the application is ready to render or print the image, at which time it invokes the [**CopyPixels**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapsource-copypixels?branch=master) method on the final transform to get a bitmap in memory of the image with the selected transforms applied.

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

From a codec perspective, the [**IWICBitmapSource**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsource?branch=master) methods are implemented on the frame decoder object. These methods are described in Implementing IWICBitmapSource, along with the other methods on [**IWICBitmapFrameDecode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframedecode?branch=master), which is derived from **IWICBitmapSource**.

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[**IWICBitmapDecoder**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapdecoder?branch=master)
</dt> <dt>

[**IWICBitmapSource**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsource?branch=master)
</dt> <dt>

[**IWICBitmapFrameDecode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframedecode?branch=master)
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

 

 



