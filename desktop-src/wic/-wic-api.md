---
description: The Windows Imaging Component (WIC) provides a Component Object Model (COM) based API for use in C and C++.
ms.assetid: 74b14b5e-70e9-410f-a6e6-d8873a5f4fa4
title: WIC API Overview
ms.topic: article
ms.date: 05/31/2018
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
| [**IWICImagingFactory**](/windows/desktop/api/Wincodec/nn-wincodec-iwicimagingfactory)     | Primary class factory for application development using WIC components. This factory creates components such as image decoders, encoders and streams.   |
| [**IWICComponentFactory**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwiccomponentfactory) | Class factory targeted for WIC component developers. Components created from this factory are primarily used in codec and metadata handler development. |



 

To create either class factory, use the [CoCreateInstance](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) COM function. The following example demonstrates the creation of the WIC imaging factory.


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
    IID_PPV_ARGS(&pFactory)
);
```



## Imaging Components

The WIC APIs provide several types of imaging components. The following table describes some of the common WIC components. For a full list of available components, see [WIC interfaces](-wic-codec-ifaces.md).



| Component Type                                                      | Description                                                                                                   |
|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [**Bitmap**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmap)                             | Represents a writable in-memory representation of an [**IWICBitmapSource**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsource). |
| [**Decoder**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapdecoder)                     | Used to decode image data from a stream into a format that is useful for image processing.                    |
| [**Encoder**](/windows/desktop/api/wincodec/nn-wincodec-iwicbitmapencoder)                     | Writes image data to a stream.                                                                                |
| [**Stream**](/windows/desktop/api/Wincodec/nn-wincodec-iwicstream)                             | Used to read and write data from a file, network resource, a block of memory, and so on.                      |
| [**Format Converter**](/windows/desktop/api/Wincodec/nn-wincodec-iwicformatconverter)          | Used to convert from one pixel format to another.                                                             |
| [**Metadata Query Reader**](/windows/desktop/api/Wincodec/nn-wincodec-iwicmetadataqueryreader) | Used to read metadata of an image or image frame.                                                             |
| [**Metadata Query Writer**](/windows/desktop/api/Wincodec/nn-wincodec-iwicmetadataquerywriter) | Used to write metadata to an image or image frame.                                                            |



 

## See Also

[References](-wic-codec-reference.md)


[Samples and Code Examples](-wic-samples.md)


 

 
