---
description: Implementing IWICBitmapEncoder
ms.assetid: b671e941-ded6-4bde-bc4d-461f13feade0
title: Implementing IWICBitmapEncoder
ms.topic: article
ms.date: 05/31/2018
---

# Implementing IWICBitmapEncoder

-   [IWICBitmapEncoder](#implementing-iwicbitmapencoder)
    -   [Initialize](#initialize)
    -   [GetContainerFormat](#getcontainerformat)
    -   [GetEncoderInfo](#getencoderinfo)
    -   [CreateNewFrame](#createnewframe)
    -   [Commit](#commit)
    -   [SetPreview](#setpreview)
-   [Related topics](#related-topics)

## IWICBitmapEncoder

-   [Initialize](#initialize)
-   [GetContainerFormat](#getcontainerformat)
-   [GetEncoderInfo](#getencoderinfo)
-   [CreateNewFrame](#createnewframe)
-   [Commit](#commit)
-   [SetPreview](#setpreview)

This interface is the counterpart to the [**IWICBitmapDecoder**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapdecoder) interface and is the starting point for encoding an image file. Just as **IWICBitmapDecoder** is used for retrieving container-level properties and individual frames from the image container, [**IWICBitmapEncoder**](/windows/desktop/api/wincodec/nn-wincodec-iwicbitmapencoder) is used for setting container-level properties and serializing individual image frames into the container. You implement this interface on your container-level encoder class.

``` syntax
interface IWICBitmapEncoder : public IUnknown
{
   // Required methods
   HRESULT Initialize ( IStream *pIStream,
              WICBitmapEncoderCacheOption cacheOption );
   HRESULT GetContainerFormat ( GUID *pguidContainerFormat );
   HRESULT GetEncoderInfo ( IWICBitmapEncoderInfo **pIEncoderInfo );
   HRESULT CreateNewFrame ( IWICBitmapFrameEncode **ppIFrameEncode,
              IPropertyBag2 **ppIEncoderOptions );
   HRESULT Commit ( void );

   // Optional methods
   HRESULT SetPreview ( IWICBitmapSource *pIPreview );
   HRESULT SetThumbnail ( IWICBitmapSource *pIThumbnail );
   HRESULT SetColorContexts ( UINT cCount,
              IWICColorContext **ppIColorContext );
   HRESULT GetMetadataQueryWriter ( IWICMetadataQueryWriter 
              **ppIMetadataQueryWriter );
   HRESULT SetPalette ( IWICPalette *pIPalette);
};
```

As discussed in [Implementing IWICBitmapDecoder](-wic-imp-iwicbitmapdecoder.md), some image formats have global thumbnails, color contexts, or metadata, while many image formats provide these only on a per-frame basis. Therefore, the methods for setting these are optional on [**IWICBitmapEncoder**](/windows/desktop/api/wincodec/nn-wincodec-iwicbitmapencoder), but are required on [**IWICBitmapFrameEncode**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapframeencode). We’ll discuss the methods that are optional on **IWICBitmapEncoder** in the section on **IWICBitmapFrameEncode**, where they’re most commonly implemented.

If you don’t support global thumbnails, return WINCODEC\_ERR\_CODECNOTHUMBNAIL from the SetThumbnail method on [**IWICBitmapEncoder**](/windows/desktop/api/wincodec/nn-wincodec-iwicbitmapencoder). If you don’t support a container-level palette, or if the image you are encoding doesn’t have an indexed format, return WINCODEC\_ERR\_PALETTEUNAVAILABLE from the SetPalette method. For any other unsupported methods, return WINCODEC\_ERR\_UNSUPPORTEDOPERATION.

### Initialize

[**Initialize**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapencoder-initialize) is the first method invoked on an [**IWICBitmapEncoder**](/windows/desktop/api/wincodec/nn-wincodec-iwicbitmapencoder) after it has been instantiated. An image stream is passed to the encoder, and a caller may optionally specify a cache option. In the case of the decoder, the stream is read-only, but the stream passed to an encoder is a writeable stream, into which the encoder will serialize all of the image data and metadata. The cache options on the encoder are different as well.

``` syntax
enum WICBitmapEncoderCacheOption
{
   WICBitmapEncoderCacheInMemory,
   WICBitmapEncoderCacheTempFile,
   WICBitmapEncoderNoCache
}
```

The application has a choice of requesting the encoder to cache the image data in memory, cache it in a temporary file, or to write it directly into the disk file with no caching. When asked to cache the data in a temporary file, the encoder should create a temporary file on disk and write directly to that file without caching in memory. When the caller selects the no cache option, each frame must be committed in order before the next frame can be created.

### GetContainerFormat

[**GetContainerFormat**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapencoder-getcontainerformat) is implemented the same way as the [GetContainerFormat](-wic-imp-iwicbitmapdecoder.md) method in [Implementing IWICBitmapDecoder](-wic-imp-iwicbitmapdecoder.md).

### GetEncoderInfo

[**GetEncoderInfo**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapencoder-getencoderinfo) returns an [**IWICBitmapEncoderInfo**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapencoderinfo) object. To get the **IWICBitmapEncoderInfo** object, just pass the GUID of your encoder to the [**CreateComponentInfo**](/windows/desktop/api/Wincodec/nf-wincodec-iwicimagingfactory-createcomponentinfo) method on [**IWICImagingFactory**](/windows/desktop/api/Wincodec/nn-wincodec-iwicimagingfactory), and then request the **IWICBitmapEncoderInfo** interface on it.

See the example in [Implementing IWICBitmapDecoder](-wic-imp-iwicbitmapdecoder.md) under [GetDecoderInfo](-wic-imp-iwicbitmapdecoder.md).

### CreateNewFrame

[**CreateNewFrame**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapencoder-createnewframe) is the encoder counterpart of [**GetFrame**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapdecoder-getframe) on [**IWICBitmapDecoder**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapdecoder). This method returns an [**IWICBitmapFrameEncode**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapframeencode) object, which is the object that actually serializes the image data for a specific frame within the container.

One of the benefits of Windows Imaging Component (WIC) is that it provides a layer of abstraction for applications that enables them to work with all image formats in the same way. However, not all image formats are exactly the same. Some image formats have capabilities that others don’t have. For applications to be able to take advantage of those unique capabilities, it’s necessary to provide a way for the codec to expose them. This is the purpose of encoder options. If your codec supports any encoder options, you should create an [IPropertyBag2](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768192(v=vs.85)) object that exposes the encoder options you support, and return it in the *ppIEncoderOptions* parameter of this method. The caller can then use this IPropertyBag2 object to determine what encoder options your codec supports. If the caller wants to specify values for any of the supported encoder options, they will assign the value to the relevant property in the IPropertyBag2 object and pass it to the newly created [**IWICBitmapFrameEncode**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapframeencode) object in its Initialize method.

To instantiate an [IPropertyBag2](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768192(v=vs.85)) object, you first need to create a PROPBAG2 struct to specify each encoder option your encoder supports and its data type for each property. Then you must implement an IPropertyBag2 object that enforces the value ranges for each property on write, and reconciles any conflicting or overlapping values. For simple sets of non-conflicting encoder options, you can invoke the [**CreateEncoderPropertyBag**](/windows/desktop/api/Wincodecsdk/nf-wincodecsdk-iwiccomponentfactory-createencoderpropertybag) method, which will create a simple IPropertyBag2 object using the properties you specify in your PROPBAG2 struct. You must still enforce the value ranges. For more advanced encoder options, or if you need to reconcile conflicting values, you should write your own IPropertyBag2 implementation.


```C++
UINT cuiPropertyCount = 0;
IPropertyBag2* pPropertyBag = NULL;
PROPBAG2* pPropBagOptions;
HRESULT hr;

// Insert code here to initialize piPropertyBag with the 
// supported options for your encoder, and to initialize 
// cuiPropertyCount to the number of encoder option properties
// you are exposing.
...

hr = pComponentFactory->CreateEncoderPropertyBag( 
   pPropBagOptions, cuiPropertyCount, &pPropertyBag);
```



WIC provides a small set of canonical encoder options that are used by some of the common image formats. All of the canonical encoder options are optional, and codecs are not required to support any of them. The reason they are provided as canonical options is because many applications expose the user interface for users to specify these options when saving an image file in a format that supports them. Providing a canonical way to specify these options makes it easy for applications to communicate them to encoders in a consistent way. The canonical encoder options are listed in the following table.



| Encoder Option     | VARTYPE  | Value Range               |
|--------------------|----------|---------------------------|
| Lossless           | VT\_BOOL | True/False                |
| ImageQuality       | VT\_R4   | 0.0-1.0                   |
| CompressionQuality | VT\_R4   | 0.0-1.0                   |
| BitmapTransform    | VT\_UI1  | WICBitmapTransformOptions |



 

If your codec supports lossless encoding, you should expose the Lossless encoder option as a way for applications to request that an image be losslessly encoded. If a caller sets this property to True, you should ignore the ImageQuality option and encode the image losslessly.

The ImageQuality option allows an application to specify the degree of fidelity with which to encode the image. This option lets a user make a tradeoff between image quality versus speed and/or file size. JPEG is an example of an image format that supports this tradeoff. A value of 0.0 indicates that fidelity is of low importance and the encoder should use its most lossy algorithm. A value of 1.0 indicates that fidelity is the most important and the encoder should preserve the highest fidelity possible. (Depending on your codec, this may be synonymous with the Lossless option. However, if your codec supports lossless encoding, and if the Lossless option is set to True, the ImageQuality option should be ignored.)

The CompressionQuality option allows an application to specify the efficiency of compression to use when encoding the image. A very efficient algorithm may produce a smaller image file with the same quality as a less efficient compression algorithm, but may take longer to encode. This option lets a user specify a tradeoff between file size versus speed of encoding, while preserving the same level of quality. TIFF is an example of an image format that supports this tradeoff. (Note that a format such as JPEG supports different levels of compression, but a higher rate of compression results in lower image quality. Therefore, a JPEG image format would expose the ImageQuality option rather than the CompressionQuality option.) A value of 0.0 for this option indicates that you should compress the image as quickly as possible, without reducing fidelity, at the expense of a larger file size. A value of 1.0 indicates that you should create the smallest possible file size (at the same level of quality), regardless of how long it may take to encode it. A codec can support both the ImageQuality option and the CompressionQuality option, where the ImageQuality option specifies the acceptable degree of lossiness, and the CompressionQuality option offers a size/speed tradeoff at the specified quality level.

The BitmapTransform option provides a way for the caller to specify a rotation angle or vertical or horizontal flip orientation when encoding. The WICBitmapTransformOptions enum used to specify the requested transform is the same enum used when requesting a transform during decoding through the IWICBitmapSourceTransform interface.

Note that encoders are not limited to the canonical encoder options. The purpose of encoder options is to enable encoders to expose their capabilities, and there is no limit to the types of capabilities you can expose. Make sure your encoder options are well-documented. Even though an application can use the property bag you return from this method to discover the names, types, and value ranges for the options you support, the only way for them to find out their meanings, or how to expose them in the user interface, is from your documentation.

### Commit

[**Commit**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapencoder-commit) is the method you call after all the image data and metadata have been serialized into the stream. You should use this method to serialize the Preview image data into the stream, and any global thumbnails, metadata, palette, or other items, if applicable. This method should not close the file stream, because the application that opened the stream is expected to close it.

The section on the IWICBitmapFrameEncode:Commit method has details on how the IWICBitmapEncoderCacheOptions affect the behavior of this method.

### SetPreview

[**SetPreview**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapencoder-setpreview) is used to create a preview of the image. While it is not strictly required that every image have a preview, it is highly recommended. Modern digital cameras and scanners generate very high resolution images, which tend to be very large and, consequently, take significant processing time to decode. Images from the next generation of cameras will be even larger. It’s a good idea to provide a smaller, lower resolution version of an image, typically in JPEG format, that can be quickly decoded and displayed “instantly” when a user requests it. An application may request a preview before requesting the actual image to be decoded to provide a better experience for users, and show them a screen-size representation of the image while theyare waiting to decode the actual image. Although codecs should provide previews, codecs that do not support [**IWICBitmapSourceTransform**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsourcetransform) should definitely do so.

If you provide a JPEG preview, you don’t have to write a JPEG encoder to encode it. You should delegate to the JPEG encoder that ships with the WIC platform for encoding both previews and thumbnails.

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[**IWICBitmapEncoder**](/windows/desktop/api/wincodec/nn-wincodec-iwicbitmapencoder)
</dt> <dt>

[**IWICBitmapFrameEncode**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapframeencode)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Encoder Interfaces](-wic-encoderinterfaces.md)
</dt> <dt>

[Implementing IWICBitmapCodecProgressNotification (Encoder)](-wic-imp-iwicbitmapcodecprogressnotification-encoder.md)
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> </dl>

 

 
