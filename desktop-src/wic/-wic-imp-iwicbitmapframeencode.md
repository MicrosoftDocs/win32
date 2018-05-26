---
Description: Implementing IWICBitmapFrameEncode
ms.assetid: 509fa49c-c90d-4270-a338-6ce638ccd89a
title: Implementing IWICBitmapFrameEncode
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Implementing IWICBitmapFrameEncode

## IWICBitmapFrameEncode

[**IWICBitmapFrameEncode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframeencode?branch=master) is the encoder’s counterpart to the [**IWICBitmapFrameDecode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframedecode?branch=master) interface. You can implement this interface on your frame-level encoding class, which is the class that does the actual encoding of the image bits for each frame.


```C++
interface IWICBitmapFrameEncode : public IUnknown
{
   // Required methods
   HRESULT Initialize ( IPropertyBag2 *pIEncoderOptions );
   HRESULT SetSize ( UINT width,
               UINT height );
   HRESULT SetResolution ( double dpiX,
               double dpiY );
   HRESULT SetPixelFormat (WICPixelFormatGUID *pPixelFormat);
   HRESULT SetColorContexts ( UINT cCount,
               IWICColorContext **ppIColorContext );
   HRESULT GetMetadataQueryWriter ( IWICMetadataQueryWriter 
               **ppIMetadataQueryWriter );
   HRESULT SetThumbnail ( IWICBitmapSource *pIThumbnail );
   HRESULT WritePixels ( UINT lineCount,
               UINT cbStride,
               UINT cbBufferSize,
               BYTE *pbPixels );
   HRESULT WriteSource ( IWICBitmapSource *pIWICBitmapSource,
               WICRect *prc );
   HRESULT Commit ( void );

// Optional method
   HRESULT SetPalette ( IWICPalette *pIPalette );
};
```



-   [Initialize](#initialize)
-   [SetSize and SetResolution](#setsize-and-setresolution)
-   [SetPixelFormat](#setpixelformat)
-   [SetColorContexts](#setcolorcontexts)
-   [GetMetadataQueryWriter](#getmetadataquerywriter)
-   [SetThumbnail](#setthumbnail)
-   [WritePixels](#writepixels)
-   [WriteSource](#writesource)
-   [Commit](#commit)
-   [SetPalette](#setpalette)

### Initialize

[**Initialize**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-initialize?branch=master) is the first method invoked on an [**IWICBitmapFrameEncode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframeencode?branch=master) object after it has been instantiated. This method has one parameter, which may be set to **NULL**. This parameter represents the encoder options, and is the same [IPropertyBag2](http://msdn.microsoft.com/en-us/library/Aa768192(VS.85).aspx) instance that you created in the [**CreateNewFrame**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-createnewframe?branch=master) method on the container-level decoder, and passed back to the caller in the pIEncoderOptions parameter of that method. At that time, you populated the IPropertyBag2 struct with properties that represent the encoding options supported by your frame-level encoder. The caller has now provided values for those properties to indicate certain encoding option parameters, and is passing the same object back to you to initialize the **IWICBitmapFrameEncode** object. You should apply the specified options when encoding the image bits.

### SetSize and SetResolution

[**SetSize**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-setsize?branch=master) and [**SetResolution**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-setresolution?branch=master) are self-explanatory. The caller uses these methods to specify the size and resolution for the encoded image.

### SetPixelFormat

[**SetPixelFormat**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-setpixelformat?branch=master) is used to request a pixel format in which to encode the image. If the requested pixel format is not supported, you should return the GUID of the closest pixel format that is supported in *pPixelFormat*, which is an in/out parameter.

### SetColorContexts

[**SetColorContexts**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-setcolorcontexts?branch=master) is used to specify one or more valid color contexts (also known as color profiles) for this image. It’s important to specify the color contexts, so an application that decodes the image at a later time can convert from the source color profile to the destination profile of the device being used to display or print the image. Without a color profile, it is not possible to get consistent colors across different devices. This can be frustrating for end users when their photos look different on different monitors, and they can’t get the prints to match what they see on screen.

### GetMetadataQueryWriter

[**GetMetadataQueryWriter**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-getmetadataquerywriter?branch=master) returns an [**IWICMetadataQueryWriter**](/windows/win32/Wincodec/nn-wincodec-iwicmetadataquerywriter?branch=master) that an application can use to insert or edit specific metadata properties in a metadata block on the image frame.

You can instantiate an [**IWICMetadataQueryWriter**](/windows/win32/Wincodec/nn-wincodec-iwicmetadataquerywriter?branch=master) from the [**IWICComponentFactory**](/windows/win32/Wincodecsdk/nn-wincodecsdk-iwiccomponentfactory?branch=master) in several ways. You can either create it from your [**IWICMetadataBlockWriter**](/windows/win32/Wincodecsdk/nn-wincodecsdk-iwicmetadatablockwriter?branch=master), the same way [**IWICMetadataQueryReader**](/windows/win32/Wincodec/nn-wincodec-iwicmetadataqueryreader?branch=master) was created from an [**IWICMetadataBlockReader**](/windows/win32/Wincodecsdk/nn-wincodecsdk-iwicmetadatablockreader?branch=master) in the [**GetMetadataQueryReader**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframedecode-getmetadataqueryreader?branch=master) method on the [**IWICBitmapFrameDecode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframedecode?branch=master) interface.


```C++
IWICMetadataQueryWriter* piMetadataQueryWriter = NULL;
HRESULT hr;

hr = m_piComponentFactory->CreateQueryWriterFromBlockWriter( 
      static_cast<IWICMetadataBlockWriter*>(this), 
      &amp;piMetadataQueryWriter);

```



You can also create it from an existing [**IWICMetadataQueryReader**](/windows/win32/Wincodec/nn-wincodec-iwicmetadataqueryreader?branch=master), such as the one obtained using the previous method.


```C++
hr = m_piComponentFactory->CreateQueryWriterFromReader( 
      piMetadataQueryReader, pguidVendor, &amp;piMetadataQueryWriter);
```



The *pguidVendor* parameter allows you to specify a particular vendor for the query writer to use when instantiating a metadata writer. For example, if you provide your own metadata writers, you may want to specify your own vendor GUID. You can pass **NULL** to this parameter if you don’t have a preference.

### SetThumbnail

[**SetThumbnail**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-setthumbnail?branch=master) is used to provide a thumbnail. All images should provide a thumbnail either globally, on each frame, or both. The **GetThumbnail** and **SetThumbnail** methods are optional at the container-level but, if a codec returns WINCODEC\_ERR\_CODECNOTHUMBNAIL from the [**GetThumbnail**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapdecoder-getthumbnail?branch=master) method, Windows Imaging Component (WIC) will invoke the [**GetThumbnail**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframedecode-getthumbnail?branch=master) method for Frame 0. If no thumbnail is found in either place, WIC must decode the full image and scale it to thumbnail size, which could incur a large performance penalty for larger images.

The thumbnail should be of a size and resolution that makes it quick to decode and display. For this reason, thumbnails are most commonly JPEG images. Note that, if you use JPEG for your thumbnails, you don’t have to write a JPEG encoder to encode them, or a JPEG decoder to decode them. You should always delegate to the JPEG codec that ships with the WIC platform for encoding and decoding thumbnails.

### WritePixels

[**WritePixels**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-writepixels?branch=master) is the method used to pass in scan lines from a bitmap in memory for encoding. The method will be called repeatedly until all of the scan lines have been passed in. The *lineCount* parameter indicates how many scan lines are to be written in this call. The *cbStride* parameter indicates the number of bytes per scan line. *cbBufferSize* indicates the size of the buffer passed in the pbPixels parameter, which contains the actual image bits to be encoded. If the combined height of the scan lines from cumulative calls is greater than the height specified in [**SetSize**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-setsize?branch=master) method, return WINCODEC\_ERR\_TOOMANYSCANLINES.

When the [**WICBitmapEncoderCacheOption**](/windows/win32/Wincodec/ne-wincodec-wicbitmapencodercacheoption?branch=master) is **WICBitmapEncoderCacheInMemory**, the scan lines should be cached in memory until all scan lines have been passed in. If the encoder cache option is **WICBitmapEncoderCacheTempFile**, the scan lines should be cached in a temporary file, created when initializing the object. In either of these cases, the image should not be encoded until the caller calls [**Commit**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-commit?branch=master). In the case where the cache option is **WICBitmapEncoderNoCache**, the encoder should encode the scan lines as they’re received, if possible. (In some formats, this is not possible, and the scan lines must be cached until Commit is called.)

Most raw codecs will not implement [**WritePixels**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-writepixels?branch=master), because they don’t support altering the image bits in the raw file. Raw codecs should still implement **WritePixels**, however, because when metadata is added, it may increase the size of the file, requiring the file to be rewritten on the disk. In that case, it’s necessary to be able to copy the existing image bits, which is what the **WritePixels** method does.

### WriteSource

[**WriteSource**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-writesource?branch=master) is used to encode an [**IWICBitmapSource**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsource?branch=master) object. The first parameter is a pointer to an **IWICBitmapSource** object. The second parameter is a WICRect that specifies the region of interest to encode. This method may be called multiple times in succession, as long as the width of each rectangle is the same width of the final image to be encoded. If the width of the rectangle passed in the prc parameter is different than the width specified in the SetSize method, return WINCODEC\_ERR\_SOURCERECTDOESNOTMATCHDIMENSIONS. If the combined height of the scan lines from cumulative calls is greater than the height specified in SetSize method, return WINCODEC\_ERR\_TOOMANYSCANLINES.

The cache options work the same way with this method as with the [**WritePixels**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-writepixels?branch=master) method described previously.

### Commit

[**Commit**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-commit?branch=master) is the method that serializes the encoded image bits to the file stream, and iterates through all the metadata writers for the frame requesting them to serialize their metadata to the stream. In the case where the encoder cache option is WICBitmapEncoderCacheInMemory or WICBitmapEncoderCacheTempFile, this method is also responsible for encoding the image, and when the cache option is WICBitmapEncoderCacheTempFile, the **Commit** method should also delete the temporary file used to cache the image data before encoding.

This method is always invoked after all the scan lines or rectangles that make up the image have been passed in using either the [**Commit**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-commit?branch=master) or [**WriteSource**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-writesource?branch=master) method. The size of the final rectangle that is composed through the accumulated calls to WritePixels or WriteSource must be the same size as was specified in the SetSize method. If the size does not match the expected size, this method should return WINCODECERROR\_UNEXPECTEDSIZE.

To iterate through the metadata writers and tell each metadata writer to serialize its metadata go the stream, invoke GetWriterByIndex to iterate through the writers for each block, and invoke IWICPersistStream.Save on each metadata writer.


```C++
IWICMetadataWriter* piMetadataWRiter = NULL;
IWICPersistStream* piPersistStream = NULL;
HRESULT hr;

for (UINT x=0; x < m_blockCount; x++) 
{
    hr = GetWriterByIndex(x, & piMetadataWriter);
hr = piMetadataWriter->QueryInterface(
IID_IWICPersistStream,(void**)&amp;piPersistStream);

hr = piPersistStream->Save(m_piStream, 
WICPersistOptions.WicPersistOptionDefault, 
true);
...
}
```



### SetPalette

Only codecs that have indexed formats need to implement the [**SetPalette**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-setpalette?branch=master) method. If an image uses an indexed format, use this method to specify the palette of colors used in the image. If your codec doesn’t have an indexed format, return WINCODEC\_ERR\_PALETTEUNAVAILABLE from this method.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Implementing IWICBitmapCodecProgressNotification (Encoder)](-wic-imp-iwicbitmapcodecprogressnotification-encoder.md)
</dt> <dt>

[Implementing IWICMetadataBlockWriter](-wic-imp-iwicmetadatablockwriter.md)
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> </dl>

 

 



