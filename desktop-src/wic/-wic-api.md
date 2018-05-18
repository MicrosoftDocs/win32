---
Description: 'The Windows Imaging Component (WIC) provides a Component Object Model (COM) based API for use in C and C++.'
ms.assetid: '74b14b5e-70e9-410f-a6e6-d8873a5f4fa4'
title: WIC API Overview
---

# WIC API Overview

The Windows Imaging Component (WIC) provides a Component Object Model (COM) based API for use in C and C++. The WIC API exposes a variety of image-related functionality, including:

-   Built-in codecs for the standard web image formats.
-   Built-in support for standard metadata formats.
-   Wide range of pixel format support.
-   High-color support; including 30-bit extended range, 30-bit high precision, and 48-bit high precision and wide gamut pixel formats.
-   Extensible framework for image codecs, pixel formats, and metadata formats.

This topic contains the following topics.

-   [WIC Header Files](#wic-header-files)
-   [Library Files](#library-files)
-   [Class Factories](#class-factories)
-   [Imaging Components](#imaging-components)
-   [See Also](#see-also)

## WIC Header Files

The WIC APIs are defined in the following header and Interface Definition Language (IDL) files:



| File              | Description                                          |
|-------------------|------------------------------------------------------|
| wincodec.h        | Defines C and C++ versions of the primary WIC APIs.  |
| wincodec.idl      | Defines the primary WIC interfaces.                  |
| wincodecsdk.h     | Defines C and C++ versions of the metadata WIC APIs. |
| wincodecsdk.idl   | Defines the WIC metadata interfaces.                 |
| wincodec\_proxy.h | Defines the WIC proxy exports.                       |



 

To use WIC, your applications must include wincodec.h and/or wincodecsdk.h, depending on the API your application needs.

## Library Files

The WIC library files:



| File              | Description                                                            |
|-------------------|------------------------------------------------------------------------|
| windowscodecs.lib | Import library provided by the Windows Software Development Kit (SDK). |
| windowscodecs.dll | Stock implementation library provided by the operating system.         |



 

To link to WIC APIs, your application must include windowscodec.lib as an additional linker dependency.

## Class Factories

The following table describes the two COM class factories the WIC APIs provide for creating WIC components.



| Factory Interface                                               | Description                                                                                                                                             |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWICImagingFactory**](-wic-codec-iwicimagingfactory.md)     | Primary class factory for application development using WIC components. This factory creates components such as image decoders, encoders and streams.   |
| [**IWICComponentFactory**](-wic-codec-iwiccomponentfactory.md) | Class factory targeted for WIC component developers. Components created from this factory are primarily used in codec and metadata handler development. |



 

To create either class factory, use the [CoCreateInstance](http://msdn.microsoft.com/en-us/library/ms686615(VS.85).aspx) COM function. The following example demonstrates the creation of the WIC imaging factory.


```C++
// Initialize COM
CoInitialize(NULL);

// The factory pointer
IWICImagingFactory *pFactory = NULL;

// Create the COM imaging factory
HRESULT hr = CoCreateInstance(
    CLSID_WICImagingFactory,
    NULL,
    CLSCTX_INPROC_SERVER,
    IID_PPV_ARGS(&amp;pFactory)
);
```



## Imaging Components

The WIC APIs provide several types of imaging components. The following table describes some of the common WIC components. For a full list of available components, see [WIC interfaces](-wic-codec-ifaces.md).



| Component Type                                                      | Description                                                                                                   |
|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [**Bitmap**](-wic-codec-iwicbitmap.md)                             | Represents a writable in-memory representation of an [**IWICBitmapSource**](-wic-codec-iwicbitmapsource.md). |
| [**Decoder**](-wic-codec-iwicbitmapdecoder.md)                     | Used to decode image data from a stream into a format that is useful for image processing.                    |
| [**Encoder**](-wic-codec-iwicbitmapencoder.md)                     | Writes image data to a stream.                                                                                |
| [**Stream**](-wic-codec-iwicstream.md)                             | Used to read and write data from a file, network resource, a block of memory, and so on.                      |
| [**Format Converter**](-wic-codec-iwicformatconverter.md)          | Used to convert from one pixel format to another.                                                             |
| [**Metadata Query Reader**](-wic-codec-iwicmetadataqueryreader.md) | Used to read metadata of an image or image frame.                                                             |
| [**Metadata Query Writer**](-wic-codec-iwicmetadataquerywriter.md) | Used to write metadata to an image or image frame.                                                            |



 

## See Also

[References](-wic-codec-reference.md)


[Samples and Code Examples](-wic-samples.md)


 

 



