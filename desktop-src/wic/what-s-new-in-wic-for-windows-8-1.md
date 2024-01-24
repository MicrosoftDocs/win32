---
description: Windows Imaging Component (WIC) has been updated with new releases of Windows. This topic provides a quick introduction to these new features.
ms.assetid: 710B71CE-6FCC-46DA-A65C-6E4FC6A04275
title: What's New in WIC
ms.topic: article
ms.date: 05/31/2018
---

# What's New in WIC

Windows Imaging Component (WIC) has been updated with new releases of Windows. This topic provides a quick introduction to these new features.

## What's new for Windows 10, version 1507

### Access to low level JPEG data for WIC decoding and encoding

Starting in Windows 10, version 1507, WIC provides access to low level JPEG data structures, including Huffman and quantization tables. For more information, see the following topics:

-   [**IWICJpegFrameDecode**](/windows/win32/api/Wincodec/nn-wincodec-iwicjpegframedecode) interface
-   [**IWICJpegFrameEncode**](/windows/win32/api/Wincodec/nn-wincodec-iwicjpegframeencode) interface

### JPEG indexing

JPEG indexing is a technique that significantly improves the performance of randomly accessing small sub regions of a large JPEG image, at the cost of some additional memory usage. JPEG indexing can be leveraged by any caller of WIC.

The [**ID2D1ImageSourceFromWic**](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1imagesourcefromwic) interface is designed to leverage JPEG indexing if it is turned on. For example, the ID2D1ImageSource API will only request the needed sections of the image in a scenario such as pan and zoom for a large resolution image. For more information, see the following topics:

-   [**IWICJpegFrameDecode::SetIndexing**](/windows/win32/api/Wincodec/nf-wincodec-iwicjpegframedecode-setindexing) method
-   [**ID2D1ImageSourceFromWic**](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1imagesourcefromwic) interface

## What's new for Windows 8.1

### Support for JPEG YCbCr images

Starting in Windows 8.1, WIC provides support for decoding, transforming and encoding JPEG Y'CbCr image data in its native format. This allows apps to significantly decrease processing time and memory consumption for certain imaging operations when working with Y'CbCr encoded JPEGs. For more information, see the following topics:

-   [Direct2D](-wic-sample-d2d-viewer.md)[YCbCr effect](../direct2d/ycbcr-effect.md)
-   [**IWICPlanarBitmapSourceTransform**](/windows/win32/api/Wincodec/nn-wincodec-iwicplanarbitmapsourcetransform) interface
-   [**IWICPlanarBitmapFrameEncode**](/windows/win32/api/Wincodec/nn-wincodec-iwicplanarbitmapframeencode) interface

### Support for block compressed formats (DDS files)

Starting in Windows 8.1, WIC adds a new codec that supports DDS images encoded in the following formats: DXGI\_FORMAT\_BC1\_UNORM, DXGI\_FORMAT\_BC2\_UNORM, and DXGI\_FORMAT\_BC3\_UNORM. DDS block compressed data can be accessed in a decoded form using standard WIC interfaces, or directly accessed using new DDS specific interfaces. For more information, see the following topics:

-   [**IWICDdsDecoder**](/windows/win32/api/Wincodec/nn-wincodec-iwicddsdecoder) interface
-   [**IWICDdsEncoder**](/windows/win32/api/Wincodec/nn-wincodec-iwicddsencoder) interface

## What's new for Windows 8

In Windows 8, WIC has been updated with several new features. The updated version of WIC is also available on Windows 7 and Windows Server 2008 R2 via the [Platform Update for Windows 7](../direct3darticles/platform-update-for-windows-7.md), which is available through the [Platform Update for Windows 7](https://support.microsoft.com/kb/2670838).

### Improved Direct2D integration

WIC in Windows 8 provides these APIs to improve Direct2D integration with WIC:

-   [**IWICImageEncoder**](/windows/win32/api/Wincodec/nn-wincodec-iwicimageencoder) - A new interface which can encode Direct2D[**ID2D1Image**](/windows/win32/api/d2d1/nn-d2d1-id2d1image) content to an [IWICBitmapFrameEncode](-wic-imp-iwicbitmapframeencode.md). The methods of this interface take a pointer to [**WICImageParameters**](/windows/win32/api/Wincodec/ns-wincodec-wicimageparameters), which are parameters to control encoding.
-   [**IWICImagingFactory2**](/windows/win32/api/Wincodec/nn-wincodec-iwicimagingfactory2) - New WIC factory with the [**CreateImageEncoder**](/windows/win32/api/Wincodec/nf-wincodec-iwicimagingfactory2-createimageencoder) method. This interface inherits from the original WIC factory, [**IWICImagingFactory**](/windows/win32/api/Wincodec/nn-wincodec-iwicimagingfactory), and is created the same way.

### Changes to BMP codec alpha support

WIC in Windows 8 supports loading [**BITMAPV5HEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapv5header) image files as [WICPixelFormat32bppBGRA](-wic-codec-native-pixel-formats.md)-formatted images. In addition, the BMP encoder supports a new Boolean ,encoder option "EnableV5Header32bppBGRA", which instructs the encoder to write a **BITMAPV5HEADER** with the 32bppBGRA image data.

For more info about BMP formats, see [BMP Format Overview](bmp-format-overview.md).

### New pixel formats

WIC in Windows 8 defines these new pixel formats:

-   GUID\_WICPixelFormat32bppRGB
-   GUID\_WICPixelFormat64bppRGB
-   GUID\_WICPixelFormat96bppRGBFloat
-   GUID\_WICPixelFormat64bppPRGBAHalf

> [!Note]  
> The TIFF built-in codec will return GUID\_WICPixelFormat96bppRGBFloat data. The other three formats are not used by built-in codecs.

 

### Restrictions to component extensibility in AppContainer

When running in an AppContainer process, which includes all Windows Store apps, WIC will only use Windows-provided components, regardless of whether additional components are installed on the system. App that are not running in AppContainer are not affected.

Apps don't need to make any code changes to run in an AppContainger, but the [**WICComponentEnumerateOptions**](/windows/win32/api/Wincodec/ne-wincodec-wiccomponentenumerateoptions) flag and vendor GUID parameters will have no effect. WIC will fail to load an image if it cannot be decoded by a Windows provided codec, and calling the [**CreateComponentEnumerator**](/windows/win32/api/Wincodec/nf-wincodec-iwicimagingfactory-createcomponentenumerator) method will only return Windows provided components.

### Changes to CLSID\_WICPngDecoder and PNG decoder color context support

**CLSID\_WICPngDecoder1** has been added with the same GUID as **CLSID\_WICPngDecoder**, and **CLSID\_WICPngDecoder2** has been added.

When compiled against the Windows 8 SDK, **CLSID\_WICPngDecoder** is \#defined to **CLSID\_WICPngDecoder2** to promote newly compiled apps using the new PNG decoder behavior. Apps should continue to specify **CLSID\_WICPngDecoder**.

Specifying **CLSID\_WICPngDecoder2** will create a version of the WIC PNG decoder that will generate an [**IWICColorContext**](/windows/win32/api/Wincodec/nn-wincodec-iwiccolorcontext) from cHRM and gAMA chunks. This allows this color space metadata to be used with other Windows APIs for color managing the source image. An **IWICColorContext** is not generated from the gAMA and cHRM chunks if an iCCP chunk is present, if an sRGB chunk is present, or if the gAMA and cHRM chunks indicate an sRGB color space.

An app can specify **CLSID\_WICPngDecoder1** to create a version of the WIC PNG decoder that does not generate an [**IWICColorContext**](/windows/win32/api/Wincodec/nn-wincodec-iwiccolorcontext) from the gAMA and cHRM chunks. This matches the behavior of the PNG decoder in previous versions of Windows.

### Changes to WINCODEC\_SDK\_VERSION

When compiled against the Windows 8 SDK, **WINCODEC\_SDK\_VERSION** is \#defined to **WINCODEC\_SDK\_VERSION2** to promote newly compiled apps using the new PNG decoder behavior. Otherwise, it is \#defined to **WINCODEC\_SDK\_VERSION1**. Apps should continue to specify **WINCODEC\_SDK\_VERSION**.

Specifying **WINCODEC\_SDK\_VERSION** when calling [**WICCreateImagingFactory\_Proxy**](-wic-codec-wiccreateimagingfactory-proxy.md) to create the imaging factory causes **CLSID\_WICPngDecoder2** to be created instead of **CLSID\_WICPngDecoder1** from the [**CreateDecoder**](/windows/win32/api/Wincodec/nf-wincodec-iwicimagingfactory-createdecoder) method and its variants. Also, a decoder component info enumerator will return **CLSID\_WICPngDecoder2** component info, but not **CLSID\_WICPngDecoder1** info.

Specifying **WINCODEC\_SDK\_VERSION1** will cause **CLSID\_WICPngDecoder1** to be used instead of **CLSID\_WICPngDecoder2** in the above cases.

### Changes to CLSID\_WICImagingFactory

**CLSID\_WICImagingFactory1** has been added with the same GUID as **CLSID\_WICImagingFactory**, and **CLSID\_WICImagingFactory2** has been added.

When compiled against the Windows 8 SDK, **CLSID\_WICImagingFactory** is \#defined to **CLSID\_WICImagingFactory2** to promote newly compiled apps using the new PNG decoder behavior. Apps should continue to specify **CLSID\_WICImagingFactory**.

Specifying **CLSID\_WICImagingFactory2** when calling [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) to create the imaging factory causes **CLSID\_WICPngDecoder2** to be created instead of **CLSID\_WICPngDecoder1** from the [**CreateDecoder**](/windows/win32/api/Wincodec/nf-wincodec-iwicimagingfactory-createdecoder) method and its variants. Also, a decoder component info enumerator will return **CLSID\_WICPngDecoder2** component info, but not **CLSID\_WICPngDecoder1** info.

Specifying **CLSID\_WICImagingFactory1** will cause **CLSID\_WICPngDecoder1** to be used instead of **CLSID\_WICPngDecoder2** in the above cases.

## What's new for Windows 7

In Windows 7, WIC has been updated with several new features. This topic provides a quick introduction to these new features.

### Updates to the TIFF Codec

The WIC TIFF codec has been updated for Windows 7 to support several features not supported by the previous version of WIC.

-   Support for large TIFF files.
-   Decode tiled TIFF images.
-   Decode flat (planar) TIFF images.
-   Decode JPEG encoded TIFF images.

### Progressive Decoding

Progressive decoding provides the ability to incrementally decode and render portions of an image before the entire image has finished downloading. This feature greatly improves the user experience when viewing images from the Internet, because the user does not have to wait for the entire image to download before decoding can begin. With progressive decoding, users are able to see an image preview with available data long before the entire image is downloaded. This feature is essential for any application used to view images from the Internet or from data sources with limited bandwidth.

For more information, see the [Progressive Decoding Overview](-wic-progressive-decoding.md).

### Extended Metadata Support for JPEG, PNG, and GIF

In Windows 7, WIC has extended its metadata support for JPEG, PNG, and GIF images.

-   Added support for animated GIF and GIF properties.
-   Expanded JPG metadata handlers to support chrominance, luminance, and comment metadata.
-   Expanded PNG metadata handlers to support tIME, sRGB, iCCP, hIST, cHRM, iTXt, bKGD, and gAMA metadata.
-   Added new 8BIM metadata handlers for ResolutionInfo metadata and IPTC digest metadata.
-   Added new metadata handlers for Logical Screen Descriptor (LSD), Image Descriptor (IMD), Graphic Control Extensions (GCE), and Application Extensions (APE) metadata.
-   Support for metadata that spans APPn blocks.

### Multi Threaded Apartment Support

Objects within a multithreaded apartment (MTA) may be called concurrently by any number of threads within the MTA, allowing for better performance on multicore systems and certain server scenarios. In addition, WIC codecs that live within an MTA can call other objects that live within the MTA without the marshaling cost associated of calling between threads that live in different STA apartments. In Windows 7, all in-box WIC codecs have been updated to support MTA, including JPEG, TIFF, PNG, GIF, ICO, and BMP. It is highly recommended that codecs be written to support MTA. Codecs that do not support MTA will cause significant performance degredation in multithreaded applications due to marshaling. Enabling MTA support requires proper synchronization to be implemented in the codec. Exact implementation of these synchronization techniques is beyond the scope of this paper. A general reference for synchronizing Component Object Model (COM) objects is provided below.

### Metadata Working Group Implementations

There are currently a variety of metadata storage formats that contain overlapping properties, without any clear industry standard or guidance on consistent methods for reading and writing these metadata formats. To help with this variety of formats and properties, the Metadata Working Group (MWG) was formed. The aim of the MWG is to provide guidelines that ensure interoperability among a wide variety of platforms, applications, and devices. The guidelines established by the MWG apply to the XMP, Exif, and IPTC metadata fields, and to the JPEG, TIFF, and PSD image formats.

In Windows 7, the photo metadata handler and the metadata policy layer have been updated to read and write image metadata according to the guidelines established by the MWG. For more information on the Metadata Working Group (MWG), view the [established metadata guidelines](https://s3.amazonaws.com/software.tagthatphoto.com/docs/mwg_guidance.pdf).

### Windows 7 features supported on Windows Vista and Windows Server 2008

The [Platform Update for Windows Vista](../win7ip/platform-update-for-windows-vista-portal.md) is a set of run-time libraries that enables developers to target applications to both Windows 7 and Windows Vista. The Platform Update for Windows Server 2008 is a set of run-time libraries that enables developers to target applications to both Windows Server 2008 R2 and Windows Server 2008. The Platform Update for Windows Vista and the Platform Update for Windows Server 2008 will be available to all Windows Vista and Windows Server 2008 customers through Windows Update. Third-party applications that require Platform Update for Windows Vista or Platform Update for Windows Server 2008 can have Windows Update detect whether the required updated is installed; if it is not, Windows Update will download and install it in the background. For more information about both updates, see Platform Update for Windows Vista

 

 
