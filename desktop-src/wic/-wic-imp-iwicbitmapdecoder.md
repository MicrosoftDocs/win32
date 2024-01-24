---
description: Implementing IWICBitmapDecoder
ms.assetid: 9e316bdd-803a-47af-b004-7675478eb829
title: Implementing IWICBitmapDecoder
ms.topic: article
ms.date: 05/31/2018
---

# Implementing IWICBitmapDecoder

## IWICBitmapDecoder

When an application requests a decoder, the first point of interaction with the codec is through the [**IWICBitmapDecoder**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapdecoder) interface. This is the container-level interface that provides access to the top-level properties of the container and, most importantly, the frames it contains. This is the primary interface on your container-level decoder class.

``` syntax
interface IWICBitmapDecoder : IUnknown
{
// Required methods
   HRESULT QueryCapability (IStream *pIStream, 
      DWORD *pdwCapabilities );
   HRESULT Initialize ( IStream *pIStream,
      WICDecodeOptions cacheOptions );
   HRESULT GetContainerFormat ( GUID *pguidContainerFormat );
   HRESULT GetDecoderInfo ( IWICBitmapDecoderInfo **pIDecoderInfo );
   HRESULT GetFrameCount ( UINT *pCount );
   HRESULT GetFrame ( UINT index, 
      IWICBitmapFrameDecode **ppIBitmapFrame );

// Optional methods
   HRESULT GetPreview ( IWICBitmapSource **ppIPreview );
   HRESULT GetThumbnail ( IWICBitmapSource **ppIThumbnail );
   HRESULT GetColorContexts ( UINT cCount, 
      IWICColorContext **ppIColorContexts, 
      UINT *pcActualCount );
   HRESULT GetMetadataQueryReader ( IWICMetadataQueryReader **ppIMetadataQueryReader);
   HRESULT CopyPalette ( IWICPalette *pIPalette );
}
```

Some image formats have global thumbnails, color contexts, or metadata, while many image formats provide these only on a per-frame basis. The methods for accessing these items are optional on [**IWICBitmapDecoder**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapdecoder), but are required on [**IWICBitmapFrameDecode**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapframedecode). Likewise, some codecs do not use indexed pixel formats and so do not need to implement the [CopyPalette](-wic-imp-iwicbitmapframedecode.md) methods on either interface. For more information on the optional **IWICBitmapDecoder** methods, see [Implementing IWICBitmapFrameDecode](-wic-imp-iwicbitmapframedecode.md), where they are most commonly implemented.

### QueryCapability

[**QueryCapability**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapdecoder-querycapability) is the method used for codec arbitration. (See [Discovery and Arbitration](-wic-howwicworks.md) in the [How The Windows Imaging Component Works](-wic-howwicworks.md) topic). If two codecs are capable of decoding the same image format, or if a pattern collision occurs in which two codecs use the same identifying pattern, this method allows you to select the codec that can best handle any specific image.

When invoking this method, Windows Imaging Component (WIC) passes you the actual stream containing the image. You must verify whether you can decode each frame within the image and enumerate through the metadata blocks, to accurately declare what capabilities this decoder has with respect to the specific file stream passed to it. This is important for all decoders, but particularly important for image formats based on Tagged Image File Format (TIFF) containers. The discovery process works by matching patterns associated with decoders in the registry to patterns in the actual image file. Declaring your identifying pattern in the registry guarantees that your decoder will always be detected for images in your image format. However, your decoder could still be detected for images in other formats. For example, all TIFF containers include the TIFF pattern, which is a valid identifying pattern for the TIFF image format. This means that, during discovery, at least two identifying patterns will be found in image files for any image format that’s based on a TIFF-style container. One will be the TIFF pattern and the other will be the actual image format pattern. While less likely, there could be pattern collisions between other unrelated image formats as well. This is why discovery and arbitration is a two-stage process. Always verify that the image stream passed to [**QueryCapability**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapdecoder-querycapability) is actually a valid instance of your own image format. Also, if your codec decodes an image format for which you don’t own the specification, your **QueryCapability** implementation should check for the presence of any feature that may be valid under the image format specification that your codec doesn’t implement. This will ensure that users do not experience unnecessary decoding failures or get unexpected results with your codec.

Before performing any operation on the image, you must save the current position of the stream, so you can restore it to its original position before returning from the method. The [**WICBitmapDecoderCapabilities**](/windows/desktop/api/Wincodec/ne-wincodec-wicbitmapdecodercapabilities) enumeration that specifies the capabilities is defined as follows:

``` syntax
enum WICBitmapDecoderCapabilities
{   
   WICBitmapDecoderCapabilitySameEncoder,
   WICBitmapDecoderCapabilityCanDecodeAllImages,
   WICBitmapDecoderCapabilityCanDecodeSomeImages,
   WICBitmapDecoderCapabilityCanEnumerateMetadata,
   WICBitmapDecoderCapabilityCanDecodeThumbnail
}
```

You should declare **WICBitmapDecoderCapabilitySameEncoder** only if your encoder was the one that encoded the image. After verifying whether you can decode each frame in the container, declare either **WICBitmapDecoderCapabilityCanDecodeSomeImages** if you can decode some but not all of the frames, **WICBitmapDecoderCapabilityCanDecodeAllImages** if you can decode all of the frames, or neither if you cannot decode any of them. (These two enums are mutually exclusive; if you return **WICBitmapDecoderCapabilityCanDecodeAllImages**, **WICBitmapDecoderCapabilityCanDecodeSomeImages** will be ignored.) Declare **WICBitmapDecoderCapabilityCanEnumerateMetadata** after verifying that you can enumerate through the metadata blocks in the image container. You don’t have to check for a thumbnail in every frame. If there is a global thumbnail and you can decode it, you can declare **WICBitmapDecoderCapabilityCanDecodeThumbnail**. If there is no global thumbnail, then attempt to decode the thumbnail for Frame 0. If there is no thumbnail in either of these places, do not declare this capability.

After determining the capabilities of the decoder with respect to the image stream passed to this method, perform an OR operation with the [**WICBitmapDecoderCapabilities**](/windows/desktop/api/Wincodec/ne-wincodec-wicbitmapdecodercapabilities) you have verified that this decoder can perform on this image, and return the result. Remember to restore the stream to its original position before returning.

### Initialize

[**Initialize**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapdecoder-initialize) is invoked by an application after a decoder has been selected to decode a specific image. The image stream is passed to the decoder, and a caller may optionally specify the [**WICDecodeOptions**](/windows/desktop/api/Wincodec/ne-wincodec-wicdecodeoptions) cache option for dealing with the metadata in the file.

``` syntax
enum WICDecodeOptions
{
   WICDecodeMetadataCacheOnDemand,
   WICDecodeMetadataCacheOnLoad
}
```

Some applications use metadata more than others. Most applications don’t need to access all the metadata in an image file, and will request specific metadata as they need it. Other applications would rather cache all the metadata up front than keep the file stream open and perform disk I/O every time they need to access metadata. If the caller doesn’t specify a metadata cache option, the default caching behavior should be cache on demand. This means no metadata should be loaded into memory until the application makes a specific request for that metadata. If the application specifies **WICDecodeMetadataCacheOnLoad**, the metadata should be loaded in memory immediately and cached. When metadata is cached on load, the file stream may be released after the metadata has been cached.

### GetContainerFormat

To implement [**GetContainerFormat**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapdecoder-getcontainerformat), just return the GUID of the image format of the image for which the decoder is instantiated. This method is also implemented on [**IWICMetadataBlockReader**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicmetadatablockreader) and [**IWICBitmapEncoder**](/windows/desktop/api/wincodec/nn-wincodec-iwicbitmapencoder).

### GetDecoderInfo

[**GetDecoderInfo**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapdecoder-getdecoderinfo) returns an [**IWICBitmapDecoderInfo**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapdecoderinfo) object. To get the **IWICBitmapDecoderInfo** object, just pass the GUID of your decoder to the [**CreateComponentInfo**](/windows/desktop/api/Wincodec/nf-wincodec-iwicimagingfactory-createcomponentinfo) method on [**IWICImagingFactory**](/windows/desktop/api/Wincodec/nn-wincodec-iwicimagingfactory), and then request the **IWICBitmapDecoderInfo** interface on it, as shown in the following example.


```C++
IWICComponentInfo* pComponentInfo = NULL;
HRESULT hr;
 
hr = m_pImagingFactory->CreateComponentInfo(CLSID_This, &pComponentInfo);

hr = pComponentInfo->QueryInterface(IID_IWICBitmapDecoderInfo, (void**)ppIDecoderInfo);

```



### GetFrameCount

[**GetFrameCount**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapdecoder-getframecount) just returns the number of frames in the container. Some container formats support multiple frames, and others support only one frame per container.

### GetFrame

[**GetFrame**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapdecoder-getframe) is an important method on the [**IWICBitmapDecoder**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapdecoder) interface because the frame contains the actual image bits, and the frame decoder object returned from this method is the object that does the actual decoding of the requested image. That is the other object you need to implement when writing a decoder. For more information on frame decoders, see [Implementing IWICBitmapFrameDecode](-wic-imp-iwicbitmapframedecode.md).

### GetPreview

[**GetPreview**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapdecoder-getpreview) returns a preview of the image. For a detailed discussion of previews, see the [Implementing IWICBitmapEncoder](-wic-imp-iwicbitmapencoder.md) method on the [Implementing IWICBitmapEncoder](-wic-imp-iwicbitmapencoder.md) interface.

If your image format contains an embedded JPEG preview, it is strongly recommend that, instead of writing a JPEG decoder to decode it, you delegate to the JPEG decoder that ships with the WIC platform for decoding previews and thumbnails. To do this, seek to the beginning of the preview image data in the stream and invoke the [**CreateDecoderFromStream**](/windows/desktop/api/Wincodec/nf-wincodec-iwicimagingfactory-createdecoderfromstream) method on the [**IWICImagingFactory**](/windows/desktop/api/Wincodec/nn-wincodec-iwicimagingfactory).


```C++
IWICBitmapDecoder* pPreviewDecoder = NULL;
IWICBitmapFrameDecode* pPreviewFrame = NULL;
IWICBitmapSource* pPreview = NULL;
HRESULT hr;

hr = m_pImagingFactory->CreateDecoderFromStream(
                               m_pStream, NULL, 
                               WICDecodeMetadataCacheOnDemand, &pPreviewDecoder);
hr = pPreviewDecoder->GetFrame(0, pPreviewFrame);
hr = pPreviewFrame->QueryInterface(IID_IWICBitmapSource, (void**)&pPreview);

```



## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[**IWICBitmapDecoder**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapdecoder)
</dt> <dt>

[**IWICBitmapFrameDecode**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapframedecode)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Decoder Interfaces](-wic-decoderinterfaces.md)
</dt> <dt>

[Implementing IWICBitmapCodecProgressNotification (Decoder)](-wic-imp-iwicbitmapcodecprogressnotification-decoder.md)
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> </dl>

 

 



