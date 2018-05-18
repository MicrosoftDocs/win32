---
Description: Interface Method Requirements
ms.assetid: '8c2afeb3-3e0b-4f8a-a2f4-df7c9ce4b098'
title: Interface Method Requirements
---

# Interface Method Requirements

Not every method on every interface must have an implementation. For example, some codecs have global metadata, thumbnails, or color contexts, whereas other codecs provide these only on a per-frame basis. If codec authors provide these only on a per-frame basis, they need only implement the [**Get**](-wic-codec-iwicbitmapdecoder-getthumbnail.md)/[**SetThumbnail**](-wic-codec-iwicbitmapencoder-setthumbnail.md) or ColorContexts, or implement the [**GetMetadataQueryReader**](-wic-codec-iwicbitmapframedecode-getmetadataqueryreader.md) or [**GetMetadataQueryWriter**](-wic-codec-iwicbitmapframeencode-getmetadataquerywriter.md) methods on the [**IWICBitmapFrameDecode**](-wic-codec-iwicbitmapframedecode.md) and [**IWICBitmapFrameEncode**](-wic-codec-iwicbitmapframeencode.md) rather than on the [**IWICBitmapDecoder**](-wic-codec-iwicbitmapdecoder.md) and [**IWICBitmapEncoder**](-wic-codec-iwicbitmapencoder.md). Likewise, some codecs do not use indexed formats and so are not required to implement the [**CopyPalette**](-wic-codec-iwicbitmapdecoder-copypalette.md) and [**SetPalette**](-wic-codec-iwicbitmapencoder-setpalette.md) methods. These methods are therefore optional and are left to the discretion of the codec creator. Most other methods are required.

For Windows 7 [**Get**](-wic-codec-iwicbitmapdecoder-getpreview.md)/[**SetPreview**](-wic-codec-iwicbitmapencoder-setpreview.md) and [**Get**](-wic-codec-iwicbitmapdecoder-getthumbnail.md)/[**SetThumbnail**](-wic-codec-iwicbitmapencoder-setthumbnail.md) are required and must be implemented on either the contain-level classes or on the frame-level classes. If your image file format doesn't support previews or thumbnails in either of these locations, then you should revise your image file format to provide such support.

When a method is not implemented, it is important to return an appropriate error so the caller can determine that the requested feature is not supported. For example, if codec authors do not support container-level thumbnails, they should return [WINCODEC\_ERR\_CODECNOTHUMBNAIL](-wic-codec-error-codes.md) when an application calls [**GetThumbnail**](-wic-codec-iwicbitmapdecoder-getthumbnail-proxy.md), and if they don't have a palette, they should return [WINCODEC\_ERR\_PALETTEUNAVAILABLE](-wic-codec-error-codes.md). If no suitable [WINCODEC\_ERR](-wic-codec-error-codes.md) code exists, then the codec should return E\_NOTIMPL for unimplemented methods.

The following tables list the required and optional methods for each Windows Imaging Component (WIC) interfaces.

[**IWICBitmapDecoder**](-wic-codec-iwicbitmapdecoder.md)



Required

[**QueryCapability**](-wic-codec-iwicbitmapdecoder-querycapability.md)

[**Initialize**](-wic-codec-iwicbitmapdecoder-initialize.md)

[**GetContainerFormat**](-wic-codec-iwicbitmapdecoder-getcontainerformat.md)

[**GetDecoderInfo**](-wic-codec-iwicbitmapdecoder-getdecoderinfo.md)

[**GetFrameCount**](-wic-codec-iwicbitmapdecoder-getframecount.md)

[**GetFrame**](-wic-codec-iwicbitmapdecoder-getframe.md)

Optional

[**GetPreview**](-wic-codec-iwicbitmapdecoder-getpreview.md)¹

[**GetThumbnail**](-wic-codec-iwicbitmapdecoder-getthumbnail.md)²

[**GetColorContexts**](-wic-codec-iwicbitmapdecoder-getcolorcontexts.md)

[**GetMetadataQueryReader**](-wic-codec-iwicbitmapdecoder-getmetadataqueryreader.md)

[**CopyPalette**](-wic-codec-iwicbitmapdecoder-copypalette.md)



 

¹Required if your image file format supports container-level previews. If this is not the case you are strongly encouraged to revise your image file format to support this. If implemented here, then a corresponding [**SetPreview**](-wic-codec-iwicbitmapencoder-setpreview.md) is required on the container-level encode class.

²Required either here, or on the frame-level decode class, depending on where your image file format stores thumbnails. If implemented here, then a corresponding [**SetThumbnail**](-wic-codec-iwicbitmapencoder-setthumbnail.md) is required on the container-level encode class.

[**IWICBitmapFrameDecode**](-wic-codec-iwicbitmapframedecode.md)



Required

[**GetColorContexts**](-wic-codec-iwicbitmapframedecode-getcolorcontexts.md)

[**GetMetadataQueryReader**](-wic-codec-iwicbitmapframedecode-getmetadataqueryreader.md)

[**GetSize**](-wic-codec-iwicbitmapsource-getsize.md)

[**GetPixelFormat**](-wic-codec-iwicbitmapsource-getpixelformat.md)

[**GetResolution**](-wic-codec-iwicbitmapsource-getresolution.md)

[**CopyPixels**](-wic-codec-iwicbitmapsource-copypixels.md)

Optional

[**GetThumbnail**](-wic-codec-iwicbitmapframedecode-getthumbnail.md)¹

[**CopyPalette**](-wic-codec-iwicbitmapdecoder-copypalette.md)



 

¹Required either here, or on the container-level decode class, depending on where you image file format stores thumbnails. If implemented here, then a corresponding [**SetThumbnail**](-wic-codec-iwicbitmapframeencode-setthumbnail.md) is required on the frame-level encoder class.

[**IWICMetadataBlockReader**](-wic-codec-iwicmetadatablockreader.md)



Required

[**GetContainerFormat**](-wic-codec-iwicmetadatablockreader-getcontainerformat.md)

[**GetCount**](-wic-codec-iwicmetadatablockreader-getcount.md)

[**GetReaderByIndex**](-wic-codec-iwicmetadatablockreader-getreaderbyindex.md)

[**GetEnumerator**](-wic-codec-iwicmetadatablockreader-getenumerator.md)



 

[**IWICBitmapSourceTransform**](-wic-codec-iwicbitmapsourcetransform.md)



Required

[**DoesSupportTransform**](-wic-codec-iwicbitmapsourcetransform-doessupporttransform.md)

[**CopyPixels**](-wic-codec-iwicbitmapsourcetransform-copypixels.md)

Optional

[**GetClosestSize**](-wic-codec-iwicbitmapsourcetransform-getclosestsize.md)

[**GetClosestPixelFormat**](-wic-codec-iwicbitmapsourcetransform-getclosestpixelformat.md)



 

[**IWICDevelopRaw**](-wic-codec-iwicdevelopraw.md)

See [Support for IWICDevelopRaw](wic._wic_rawguidelines_iwicdeveopraw), later in this document.

[**IWICBitmapEncoder**](-wic-codec-iwicbitmapencoder.md)



Required

[**Initialize**](-wic-codec-iwicbitmapencoder-initialize.md)

[**GetContainerFormat**](-wic-codec-iwicbitmapencoder-getcontainerformat.md)

[**GetEncoderInfo**](-wic-codec-iwicbitmapencoder-getencoderinfo.md)

[**CreateNewFrame**](-wic-codec-iwicbitmapencoder-createnewframe.md)

[**Commit**](-wic-codec-iwicbitmapencoder-commit.md)

Optional

[**SetPreview**](-wic-codec-iwicbitmapencoder-setpreview.md)¹

[**SetThumbnail**](-wic-codec-iwicbitmapencoder-setthumbnail.md)²

[**SetColorContexts**](-wic-codec-iwicbitmapencoder-setcolorcontexts.md)

[**GetMetadataQueryWriter**](-wic-codec-iwicbitmapencoder-getmetadataquerywriter.md)

[**SetPalette**](-wic-codec-iwicbitmap-setpalette.md)



 

¹Required if your image file format supports frame-level previews.

²Required either here, or on the frame-level encode class, depending on where your image file format stores thumbnails. If implemented here, then a corresponding [**GetThumbnail**](-wic-codec-iwicbitmapdecoder-getthumbnail.md) is required on the container-level decode class.

[**IWICBitmapFrameEncode**](-wic-codec-iwicbitmapframeencode.md)



Required

[**Initialize**](-wic-codec-iwicbitmapencoder-initialize.md)

[**SetColorContexts**](-wic-codec-iwicbitmapframeencode-setcolorcontexts.md)

[**SetColorContexts**](-wic-codec-iwicbitmapframeencode-setcolorcontexts.md)

[**SetSize**](-wic-codec-iwicbitmapframeencode-setsize.md)

[**SetPixelFormat**](-wic-codec-iwicbitmapframeencode-setpixelformat.md)

[**SetResolution**](-wic-codec-iwicbitmapframeencode-setresolution.md)

[**WritePixels**](-wic-codec-iwicbitmapframeencode-writepixels.md)

[**WriteSource**](-wic-codec-iwicbitmapframeencode-writesource.md)

[**Commit**](-wic-codec-iwicbitmapencoder-commit.md)

Optional

[**SetThumbnail**](-wic-codec-iwicbitmapframeencode-setthumbnail.md)¹

[**CopyPalette**](-wic-codec-iwicbitmapsource-copypalette.md)



 

¹Required either here, or on the container-level encode class, depending on where your image file format stores thumbnails. If implemented here, then a corresponding [**GetThumbnail**](-wic-codec-iwicbitmapframedecode-getthumbnail.md) is required on the frame-level decode class.

[**IWICMetadataBlockReader**](-wic-codec-iwicmetadatablockreader.md)



Required

[**InitializeFromBlockReader**](-wic-codec-iwicmetadatablockwriter-initializefromblockreader.md)

[**AddWriter**](-wic-codec-iwicmetadatablockwriter-addwriter.md)

[**GetWriterByIndex**](-wic-codec-iwicmetadatablockwriter-getwriterbyindex.md)

[**SetWriterByIndex**](-wic-codec-iwicmetadatablockwriter-setwriterbyindex.md)

[**RemoveWriterByIndex**](-wic-codec-iwicmetadatablockwriter-removewriterbyindex.md)



 

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

 

 



