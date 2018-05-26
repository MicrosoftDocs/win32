---
Description: Interface Method Requirements
ms.assetid: 8c2afeb3-3e0b-4f8a-a2f4-df7c9ce4b098
title: Interface Method Requirements
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Interface Method Requirements

Not every method on every interface must have an implementation. For example, some codecs have global metadata, thumbnails, or color contexts, whereas other codecs provide these only on a per-frame basis. If codec authors provide these only on a per-frame basis, they need only implement the [**Get**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapdecoder-getthumbnail?branch=master)/[**SetThumbnail**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-setthumbnail?branch=master) or ColorContexts, or implement the [**GetMetadataQueryReader**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframedecode-getmetadataqueryreader?branch=master) or [**GetMetadataQueryWriter**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-getmetadataquerywriter?branch=master) methods on the [**IWICBitmapFrameDecode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframedecode?branch=master) and [**IWICBitmapFrameEncode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframeencode?branch=master) rather than on the [**IWICBitmapDecoder**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapdecoder?branch=master) and [**IWICBitmapEncoder**](/windows/win32/wincodec/nn-wincodec-iwicbitmapencoder?branch=master). Likewise, some codecs do not use indexed formats and so are not required to implement the [**CopyPalette**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapdecoder-copypalette?branch=master) and [**SetPalette**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-setpalette?branch=master) methods. These methods are therefore optional and are left to the discretion of the codec creator. Most other methods are required.

For Windows 7 [**Get**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapdecoder-getpreview?branch=master)/[**SetPreview**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-setpreview?branch=master) and [**Get**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapdecoder-getthumbnail?branch=master)/[**SetThumbnail**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-setthumbnail?branch=master) are required and must be implemented on either the contain-level classes or on the frame-level classes. If your image file format doesn't support previews or thumbnails in either of these locations, then you should revise your image file format to provide such support.

When a method is not implemented, it is important to return an appropriate error so the caller can determine that the requested feature is not supported. For example, if codec authors do not support container-level thumbnails, they should return [WINCODEC\_ERR\_CODECNOTHUMBNAIL](-wic-codec-error-codes.md) when an application calls [**GetThumbnail**](-wic-codec-iwicbitmapdecoder-getthumbnail-proxy.md), and if they don't have a palette, they should return [WINCODEC\_ERR\_PALETTEUNAVAILABLE](-wic-codec-error-codes.md). If no suitable [WINCODEC\_ERR](-wic-codec-error-codes.md) code exists, then the codec should return E\_NOTIMPL for unimplemented methods.

The following tables list the required and optional methods for each Windows Imaging Component (WIC) interfaces.

[**IWICBitmapDecoder**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapdecoder?branch=master)



Required

[**QueryCapability**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapdecoder-querycapability?branch=master)

[**Initialize**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapdecoder-initialize?branch=master)

[**GetContainerFormat**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapdecoder-getcontainerformat?branch=master)

[**GetDecoderInfo**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapdecoder-getdecoderinfo?branch=master)

[**GetFrameCount**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapdecoder-getframecount?branch=master)

[**GetFrame**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapdecoder-getframe?branch=master)

Optional

[**GetPreview**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapdecoder-getpreview?branch=master)¹

[**GetThumbnail**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapdecoder-getthumbnail?branch=master)²

[**GetColorContexts**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapdecoder-getcolorcontexts?branch=master)

[**GetMetadataQueryReader**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapdecoder-getmetadataqueryreader?branch=master)

[**CopyPalette**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapdecoder-copypalette?branch=master)



 

¹Required if your image file format supports container-level previews. If this is not the case you are strongly encouraged to revise your image file format to support this. If implemented here, then a corresponding [**SetPreview**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-setpreview?branch=master) is required on the container-level encode class.

²Required either here, or on the frame-level decode class, depending on where your image file format stores thumbnails. If implemented here, then a corresponding [**SetThumbnail**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-setthumbnail?branch=master) is required on the container-level encode class.

[**IWICBitmapFrameDecode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframedecode?branch=master)



Required

[**GetColorContexts**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframedecode-getcolorcontexts?branch=master)

[**GetMetadataQueryReader**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframedecode-getmetadataqueryreader?branch=master)

[**GetSize**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapsource-getsize?branch=master)

[**GetPixelFormat**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapsource-getpixelformat?branch=master)

[**GetResolution**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapsource-getresolution?branch=master)

[**CopyPixels**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapsource-copypixels?branch=master)

Optional

[**GetThumbnail**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframedecode-getthumbnail?branch=master)¹

[**CopyPalette**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapdecoder-copypalette?branch=master)



 

¹Required either here, or on the container-level decode class, depending on where you image file format stores thumbnails. If implemented here, then a corresponding [**SetThumbnail**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-setthumbnail?branch=master) is required on the frame-level encoder class.

[**IWICMetadataBlockReader**](/windows/win32/Wincodecsdk/nn-wincodecsdk-iwicmetadatablockreader?branch=master)



Required

[**GetContainerFormat**](/windows/win32/Wincodecsdk/nf-wincodecsdk-iwicmetadatablockreader-getcontainerformat?branch=master)

[**GetCount**](/windows/win32/Wincodecsdk/nf-wincodecsdk-iwicmetadatablockreader-getcount?branch=master)

[**GetReaderByIndex**](/windows/win32/Wincodecsdk/nf-wincodecsdk-iwicmetadatablockreader-getreaderbyindex?branch=master)

[**GetEnumerator**](/windows/win32/Wincodecsdk/nf-wincodecsdk-iwicmetadatablockreader-getenumerator?branch=master)



 

[**IWICBitmapSourceTransform**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsourcetransform?branch=master)



Required

[**DoesSupportTransform**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapsourcetransform-doessupporttransform?branch=master)

[**CopyPixels**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapsourcetransform-copypixels?branch=master)

Optional

[**GetClosestSize**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapsourcetransform-getclosestsize?branch=master)

[**GetClosestPixelFormat**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapsourcetransform-getclosestpixelformat?branch=master)



 

[**IWICDevelopRaw**](/windows/win32/Wincodec/nn-wincodec-iwicdevelopraw?branch=master)

See [Support for IWICDevelopRaw](wic._wic_rawguidelines_iwicdeveopraw), later in this document.

[**IWICBitmapEncoder**](/windows/win32/wincodec/nn-wincodec-iwicbitmapencoder?branch=master)



Required

[**Initialize**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-initialize?branch=master)

[**GetContainerFormat**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-getcontainerformat?branch=master)

[**GetEncoderInfo**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-getencoderinfo?branch=master)

[**CreateNewFrame**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-createnewframe?branch=master)

[**Commit**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-commit?branch=master)

Optional

[**SetPreview**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-setpreview?branch=master)¹

[**SetThumbnail**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-setthumbnail?branch=master)²

[**SetColorContexts**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-setcolorcontexts?branch=master)

[**GetMetadataQueryWriter**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-getmetadataquerywriter?branch=master)

[**SetPalette**](/windows/win32/Wincodec/nf-wincodec-iwicbitmap-setpalette?branch=master)



 

¹Required if your image file format supports frame-level previews.

²Required either here, or on the frame-level encode class, depending on where your image file format stores thumbnails. If implemented here, then a corresponding [**GetThumbnail**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapdecoder-getthumbnail?branch=master) is required on the container-level decode class.

[**IWICBitmapFrameEncode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframeencode?branch=master)



Required

[**Initialize**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-initialize?branch=master)

[**SetColorContexts**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-setcolorcontexts?branch=master)

[**SetColorContexts**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-setcolorcontexts?branch=master)

[**SetSize**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-setsize?branch=master)

[**SetPixelFormat**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-setpixelformat?branch=master)

[**SetResolution**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-setresolution?branch=master)

[**WritePixels**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-writepixels?branch=master)

[**WriteSource**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-writesource?branch=master)

[**Commit**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-commit?branch=master)

Optional

[**SetThumbnail**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-setthumbnail?branch=master)¹

[**CopyPalette**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapsource-copypalette?branch=master)



 

¹Required either here, or on the container-level encode class, depending on where your image file format stores thumbnails. If implemented here, then a corresponding [**GetThumbnail**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframedecode-getthumbnail?branch=master) is required on the frame-level decode class.

[**IWICMetadataBlockReader**](/windows/win32/Wincodecsdk/nn-wincodecsdk-iwicmetadatablockreader?branch=master)



Required

[**InitializeFromBlockReader**](/windows/win32/Wincodecsdk/nf-wincodecsdk-iwicmetadatablockwriter-initializefromblockreader?branch=master)

[**AddWriter**](/windows/win32/Wincodecsdk/nf-wincodecsdk-iwicmetadatablockwriter-addwriter?branch=master)

[**GetWriterByIndex**](/windows/win32/Wincodecsdk/nf-wincodecsdk-iwicmetadatablockwriter-getwriterbyindex?branch=master)

[**SetWriterByIndex**](/windows/win32/Wincodecsdk/nf-wincodecsdk-iwicmetadatablockwriter-setwriterbyindex?branch=master)

[**RemoveWriterByIndex**](/windows/win32/Wincodecsdk/nf-wincodecsdk-iwicmetadatablockwriter-removewriterbyindex?branch=master)



 

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

 

 



