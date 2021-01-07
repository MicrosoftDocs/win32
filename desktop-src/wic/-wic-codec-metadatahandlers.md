---
description: This topic introduces the requirements for creating custom metadata handlers for the Windows Imaging Component (WIC), including both metadata readers and writers.
ms.assetid: 08f1872b-6e4d-44ee-abc7-48685e435acc
title: Metadata Extensibility Overview
ms.topic: article
ms.date: 05/31/2018
---

# Metadata Extensibility Overview

This topic introduces the requirements for creating custom metadata handlers for the Windows Imaging Component (WIC), including both metadata readers and writers. It also discusses the requirements for extending WIC run-time component discovery to include your custom metadata handlers.

This topic contains the following sections.

-   [Prerequisites](#prerequisites)
-   [Introduction](#introduction)
-   [Creating a Metadata Reader](#creating-a-metadata-reader)
    -   [IWICMetadataReader Interface](#iwicmetadatareader-interface)
    -   [IWICPersistStream Interface](#iwicpersiststream-interface)
    -   [IWICStreamProvider Interface](#iwicstreamprovider-interface)
-   [Creating a Metadata Writer](#creating-a-metadata-writer)
    -   [IWICMetadataWriter Interface](#iwicmetadatawriter-interface)
    -   [IWICPersistStream Interface](#iwicpersiststream-interface)
    -   [IWICStreamProvider Interface](#iwicstreamprovider-interface)
-   [Installing and Registering a Metadata Handler](#installing-and-registering-a-metadata-handler)
    -   [Metadata Handler Registry Keys](#metadata-handler-registry-keys)
    -   [Metadata Readers](#metadata-readers)
    -   [Metadata Writers](#metadata-writers)
    -   [Signing a Metadata Handler](#signing-a-metadata-handler)
-   [Special Considerations](#special-considerations)
    -   [PROPVARIANTS](#propvariants)
    -   [8BIM Handlers](#8bim-handlers)
-   [Related topics](#related-topics)

## Prerequisites

To understand this topic you should have an in-depth understanding of WIC, its components, and metadata for images. For more information on WIC metadata, see the [WIC Metadata Overview](-wic-about-metadata.md). For more information on WIC components, see the [Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md).

## Introduction

As discussed in the [WIC Metadata Overview](-wic-about-metadata.md), there are often multiple blocks of metadata within an image, each exposing different types of information in different metadata formats. To interact with a metadata format embedded within an image, an application must use an appropriate metadata handler. WIC provides several metadata handlers (both metadata readers and writers) that enable you to read and write specific types of metadata such as Exif or XMP.

In addition to the native handlers provided, WIC provides APIs that enable you to create new metadata handlers that participate in WIC's run-time component discovery. This enables applications that use WIC to read and write your custom metadata formats.

The following steps enable your metadata handlers to participate in WIC's run-time metadata discovery.

-   Implement a metadata-reader handler class ([**IWICMetadataReader**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicmetadatareader)) that exposes the required WIC interfaces for reading your custom metadata format. This enables WIC-based applications to read your metadata format the same way they read native metadata formats.
-   Implement a metadata-writer handler class ([**IWICMetadataWriter**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicmetadatawriter)) that exposes the required WIC interfaces for encoding your custom metadata format. This enables WIC-based applications to serialize your metadata format into supported image formats.
-   Digitally sign and register your metadata handlers. This enables your metadata handlers to be discovered at run time by matching the identifying pattern in the registry with the pattern embedded in the image file.

## Creating a Metadata Reader

The main access to metadata blocks within a codec is through the [**IWICMetadataBlockReader**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicmetadatablockreader) interface that each WIC codec implements. This interface enumerates each of the metadata blocks embedded in an image format so that the appropriate metadata handler can be discovered and instantiated for each block. The metadata blocks that are not recognized by WIC are considered unknown and are defined as the GUID CLSID\_WICUnknownMetadataReader. To have your metadata format recognized by WIC, you must create a class that implements three interfaces: [**IWICMetadataReader**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicmetadatareader), [**IWICPersistStream**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicpersiststream), and [**IWICStreamProvider**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicstreamprovider).

> [!Note]  
> If your metadata format has restrictions that render some methods of the required interfaces inappropriate, such methods should return WINCODEC\_ERR\_UNSUPPORTEDOPERATION.

 

### IWICMetadataReader Interface

The [**IWICMetadataReader**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicmetadatareader) interface must be implemented when creating a metadata reader. This interface provides access to the underling metadata items within the data stream of a metadata format.

The following code shows the definition of the metadata reader interface as defined in the wincodecsdk.idl file.

``` syntax
interface IWICMetadataReader : IUnknown
{
    HRESULT GetMetadataFormat(
        [out] GUID *pguidMetadataFormat
        );

    HRESULT GetMetadataHandlerInfo(
        [out] IWICMetadataHandlerInfo **ppIHandler
        );

    HRESULT GetCount(
        [out] UINT *pcCount
        );

    HRESULT GetValueByIndex(
        [in] UINT nIndex,
        [in, out, unique] PROPVARIANT *pvarSchema,
        [in, out, unique] PROPVARIANT *pvarId,
        [in, out, unique] PROPVARIANT *pvarValue
        );

    HRESULT GetValue(
        [in, unique] const PROPVARIANT *pvarSchema,
        [in] const PROPVARIANT *pvarId,
        [in, out, unique] PROPVARIANT *pvarValue
        );

    HRESULT GetEnumerator(
        [out] IWICEnumMetadataItem **ppIEnumMetadata
        );
};
```

The **GetMetadataFormat** method returns the GUID of your metadata format.

The **GetMetadataHandlerInfo** method returns an [**IWICMetadataHandlerInfo**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicmetadatahandlerinfo) interface that provides information about your metadata handler. This includes information such as what image formats support the metadata format and whether your metadata reader requires access to the full metadata stream.

The **GetCount** method returns the number of individual metadata items (including embedded metadata blocks) found within the metadata stream.

The **GetValueByIndex** method returns a metadata item by an index value. This method enables applications to loop through each metadata item in a metadata block. The following code demonstrates how an application can use this method to retrieve each metadata item in a metadata block.


```C++
PROPVARIANT readerValue;
IWICMetadataBlockReader *blockReader = NULL;
IWICMetadataReader *reader = NULL;

PropVariantInit(&readerValue);

hr = pFrameDecode->QueryInterface(IID_IWICMetadataBlockReader, (void**)&blockReader);

if (SUCCEEDED(hr))
{
    // Retrieve the third block in the image. This is image specific and
    // ideally you should call this by retrieving the reader count
    // first.
    hr = blockReader->GetReaderByIndex(2, &reader);
}

if (SUCCEEDED(hr))
{
    UINT numValues = 0;

    hr = reader->GetCount(&numValues);

    // Loop through each item and retrieve by index
    for (UINT i = 0; SUCCEEDED(hr) && i < numValues; i++)
    {
        PROPVARIANT id, value;

        PropVariantInit(&id);
        PropVariantInit(&value);

        hr = reader->GetValueByIndex(i, NULL, &id, &value);

        if (SUCCEEDED(hr))
        {
            // Do something with the metadata item.
            //...
        }
        PropVariantClear(&id);
        PropVariantClear(&value);
    }               
}
```



The **GetValue** method retrieves a specific metadata item by schema and/or ID. This method is similar to the **GetValueByIndex** method except that it retrieves a metadata item that has a specific schema or ID.

The **GetEnumerator** method returns an enumerator of each metadata item in the metadata block. This enables applications to use an enumerator to navigate your metadata format.

If your metadata format does not have a notion of schemas for metadata items, the GetValue... methods should ignore this property. If, however, your format supports schema naming, you should anticipate a **NULL** value.

If a metadata item is an embedded metadata block, create a metadata handler from the substream of the embedded content and return the new metadata handler. If there is no metadata reader available for the nested block, instantiate and return an unknown metadata reader. To create a new metadata reader for the embedded block, call the component factory's **CreateMetadataReaderFromContainer** or **CreateMetadataReader** methods, or call the [**WICMatchMetadataContent**](/windows/desktop/api/wincodecsdk/nf-wincodecsdk-wicmatchmetadatacontent) function.

If the metadata stream contains big-endian content, the metadata reader is responsible for swapping any data values it processes. It is also responsible for informing any nested metadata readers that they are working with big-endian data stream. However, all values should be returned in little-endian format.

Implement support for namespace navigation by supporting queries where the metadata item ID is a `VT_CLSID` (a GUID) corresponding to a metadata format. If a nested metadata reader for that format is identified during parsing, it must be returned. This enables applications to use a metadata query reader to search your metadata format.

When getting a metadata item by ID, you should use [PropVariantChangeType Function](/windows/win32/api/propvarutil/nf-propvarutil-propvariantchangetype) to coerce the ID into the expected type. For example, the IFD reader will coerce an ID to type `VT_UI2` to coincide with the data type of an IFD tag ID USHORT. The input type and expected type must both be [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) to do this. This is not required, but doing this coercion simplifies code that calls the reader to query for metadata items.

### IWICPersistStream Interface

The [**IWICPersistStream**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicpersiststream) interface inherits from **IPersistStream** and provides additional methods for saving and loading objects by using the [**WICPersistOptions**](/windows/desktop/api/Wincodecsdk/ne-wincodecsdk-wicpersistoptions) enumeration.

The following code shows the definition of the [**IWICPersistStream**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicpersiststream) interface as defined in the wincodecsdk.idl file.

``` syntax
interface IWICPersistStream : IPersistStream
{
    HRESULT LoadEx(
        [in, unique] IStream *pIStream,
        [in, unique] const GUID *pguidPreferredVendor,
        [in] DWORD dwPersistOptions
        );

    HRESULT SaveEx(
        [in] IStream *pIStream,
        [in] DWORD dwPersistOptions,
        [in] BOOL fClearDirty
        );
};
```

The **LoadEx** method provides your metadata reader with a data stream containing your metadata block. Your reader parses this stream to access the underlying metadata items. Your metadata reader is initialized with a substream that is positioned at the beginning of the raw metadata content. If your reader does not require the full stream, the substream is limited in range to only the content of the metadata block; otherwise, the full metadata stream is provided with the position set at the beginning of your metadata block.

The **SaveEx** method is used by metadata writers to serialize your metadata block. When **SaveEx** is used in a metadata reader, it should return WINCODEC\_ERR\_UNSUPPORTEDOPERATION.

### IWICStreamProvider Interface

The [**IWICStreamProvider**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicstreamprovider) interface enables your metadata reader to provide references to its content stream, provide information about the stream, and refresh cached versions of the stream.

The following code shows the definition of the [**IWICStreamProvider**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicstreamprovider) interface as defined in the wincodecsdk.idl file.

``` syntax
interface IWICStreamProvider : IUnknown
{
    HRESULT GetStream(
        [out] IStream **ppIStream
        );

    HRESULT GetPersistOptions(
        [out] DWORD *pdwPersistOptions
        );

    HRESULT GetPreferredVendorGUID(
        [out] GUID *pguidPreferredVendor
        );

    HRESULT RefreshStream(
        );
};
```

The **GetStream** method retrieves a reference to your metadata stream. The stream you return should have the stream pointer reset to the start position. If your metadata format requires full stream access, the start position should be the start of your metadata block.

The **GetPersistOptions** method returns the stream's current options from the [**WICPersistOptions**](/windows/desktop/api/Wincodecsdk/ne-wincodecsdk-wicpersistoptions) enumeration.

The **GetPreferredVendorGUID** method returns the GUID of the vendor of the metadata reader.

The **RefreshStream** method refreshes the metadata stream. This method must call **LoadEx** with a **NULL** stream for any nested metadata blocks. This is necessary because nested metadata blocks and their items may no longer exist, due to in-place editing.

## Creating a Metadata Writer

A metadata writer is a type of metadata handler that provides a way to serialize a metadata block to an image frame, or outside an individual frame if the image format supports it. The main access to the metadata writers within a codec is through the [**IWICMetadataBlockWriter**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicmetadatablockwriter) interface that each WIC encoder implements. This interface enables applications to enumerate each of the metadata blocks embedded in an image so that the appropriate metadata writer can be discovered and instantiated for each metadata block. Metadata blocks that do not have a corresponding metadata writer are considered unknown, and are defined as the GUID CLSID\_WICUnknownMetadataReader. To enable WIC enabled applications to serialize and write your metadata format, you must create a class that implements the following interfaces: [**IWICMetadataWriter**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicmetadatawriter), [**IWICMetadataReader**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicmetadatareader), [**IWICPersistStream**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicpersiststream), and [**IWICStreamProvider**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicstreamprovider).

> [!Note]  
> If your metadata format has restrictions that render some methods of the required interfaces inappropriate, such methods should return WINCODEC\_ERR\_UNSUPPORTEDOPERATION.

 

### IWICMetadataWriter Interface

The [**IWICMetadataWriter**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicmetadatawriter) interface must be implemented by your metadata writer. Additionally, because **IWICMetadataWriter** inherits from [**IWICMetadataReader**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicmetadatareader), you must also implement all the methods of **IWICMetadataReader**. Because both handler types require the same interface inheritance, you might want to create a single class that provides both reading and writing functionality.

The following code shows the definition of the metadata writer interface as defined in the wincodecsdk.idl file.

``` syntax
interface IWICMetadataWriter : IWICMetadataReader
{
    HRESULT SetValue(
        [in, unique] const PROPVARIANT *pvarSchema,
        [in] const PROPVARIANT *pvarId,
        [in] const PROPVARIANT *pvarValue
        );

    HRESULT SetValueByIndex(
        [in] UINT nIndex,
        [in, unique] const PROPVARIANT *pvarSchema,
        [in] const PROPVARIANT *pvarId,
        [in] const PROPVARIANT *pvarValue
        );

    HRESULT RemoveValue(
        [in, unique] const PROPVARIANT *pvarSchema,
        [in] const PROPVARIANT *pvarId
        );

    HRESULT RemoveValueByIndex(
        [in] UINT nIndex
        );
};
```

The **SetValue** method writes the specified metadata item to the metadata stream.

The **SetValueByIndex** method writes the specified metadata item to the specified index in the metadata stream. The index does not refer to the ID but to the position of the item within the metadata block.

The **RemoveValue** method removes the specified metadata item from the metadata stream.

The **RemoveValueByIndex** method removes the metadata item at the specified index from the metadata stream. After removing an item, it is expected that the remaining metadata items will occupy the vacated index if the index is not the last index. It is also expected that the count will change after the item is removed.

It is the metadata writer's responsibility to convert the [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) items to the underlying structure required by your format. However, unlike the metadata reader, VARIANT types should not normally be coerced to different types as the caller is specifically indicating what data type to use.

Your metadata writer must commit all metadata items to the image stream, including hidden or unrecognized values. This includes unknown nested metadata blocks. However, it is the encoder's responsibility to set any critical metadata items prior to initiating the save operation.

If the metadata stream contains big-endian content, the metadata writer is responsible for swapping any data values it processes. It is also responsible for informing any nested metadata writers that they are working with a big-endian data stream when they save.

Implement support for namespace creation and removal by supporting set and remove operations on metadata items with a type of `VT_CLSID` (a GUID) corresponding to a metadata format. The metadata writer calls the [**WICSerializeMetadataContent**](/windows/desktop/api/wincodecsdk/nf-wincodecsdk-wicserializemetadatacontent) function to properly embed the nested metadata writer content into the parent metadata writer.

If your metadata format supports in-place encoding, you are responsible for managing the required padding. For more information on in-place encoding, see [WIC Metadata Overview](-wic-about-metadata.md) and [Overview of Reading and Writing Image Metadata](-wic-codec-readingwritingmetadata.md).

### IWICPersistStream Interface

The [**IWICPersistStream**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicpersiststream) interface inherits from **IPersistStream** and provides additional methods for saving and loading objects by using the [**WICPersistOptions**](/windows/desktop/api/Wincodecsdk/ne-wincodecsdk-wicpersistoptions) enumeration.

The following code shows the definition of the [**IWICPersistStream**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicpersiststream) interface as defined in the wincodecsdk.idl file.

``` syntax
interface IWICPersistStream : IPersistStream
{
    HRESULT LoadEx(
        [in, unique] IStream *pIStream,
        [in, unique] const GUID *pguidPreferredVendor,
        [in] DWORD dwPersistOptions
        );

    HRESULT SaveEx(
        [in] IStream *pIStream,
        [in] DWORD dwPersistOptions,
        [in] BOOL fClearDirty
        );
};
```

The **LoadEx** method provides your metadata handler with a data stream containing your metadata block.

The **SaveEx** method serializes the metadata into a stream. If the provided stream is the same as initialization stream, you should perform in-place encoding. If in-place encoding is supported, this method should return WINCODEC\_ERR\_TOOMUCHMETADATA when there is insufficient padding to perform in-place encoding. If in-place encoding is not supported, this method should return WINCODEC\_ERR\_UNSUPPORTEDOPERATION.

The **IPersistStream::GetSizeMax** method must be implemented and must return the exact size of the metadata content that would be written in subsequent save.

The **IPersistStream::IsDirty** method should be implemented if the metadata writer is initialized through a stream, so that an image can reliably determine whether its content has changed.

If your metadata format supports nested metadata blocks, your metadata writer should delegate to the nested metadata writers the serializing of its content when saving to a stream.

### IWICStreamProvider Interface

The implementation of the [**IWICStreamProvider**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicstreamprovider) interface for a metadata writer is the same as that of a metadata reader. For more information, see Creating a Metadata Reader section in this document.

## Installing and Registering a Metadata Handler

To install a metadata handler, you must provide the handler assembly and register it in the system registry. You can decide how and when the registry keys are populated.

> [!Note]  
> For readability, the actual hexadecimal GUIDs are not shown in the registry keys shown in the following sections of this document. To find the hexadecimal value for a specified friendly name, see the wincodec.idl and wincodecsdk.idl files.

 

### Metadata Handler Registry Keys

Each metadata handler is identified by a unique CLSID, and each handler is required to register its CLSID under the metadata handler's category ID GUID. Each handler type's category ID is defined in the wincodec.idl; the category ID name for readers is CATID\_WICMetadataReader, and the category ID name for writers is CATID\_WICMetadataWriter.

Each metadata handler is identified by a unique CLSID, and each handler is required to register its CLSID under the metadata handler's category ID GUID. Each handler type's category ID is defined in the wincodec.idl; the category ID name for readers is CATID\_WICMetadataReader, and the category ID name for writers is CATID\_WICMetadataWriter.

> [!Note]  
> In the following registry key listings, {Reader CLSID} refers to the unique CLSID that you provide for your metadata reader. {Writer CLSID} refers to the unique CLSID that you provide for your metadata writer. {Handler CLSID} refers to the reader's CLSID, the writer's CLSID, or both, depending on which handlers you are providing. {Container GUID} refers to the container object (image format or metadata format) that can contain the metadata block.

 

The following registry keys register your metadata handler with the other metadata handlers available:

``` syntax
[HKEY_CLASSES_ROOT\CLSID\{CATID_WICMetadataReaders}\Instance\{Reader CLSID}]
CLSID={Reader CLSID}
Friendly Name="Reader Name"

[HKEY_CLASSES_ROOT\CLSID\{CATID_ WICMetadataWriters}\Instance\{Writer CLSID}]
CLSID={Writer CLSID}
Friendly Name="Writer Name"
```

In addition to registering your handlers in their respective categories, you must also register additional keys that provide information specific to the handler. Readers and writers share similar registry key requirements. The following syntax shows how to register a handler. Both the reader handler and writer handler must be registered in this way, using their respective CLSIDs:

``` syntax
[HKEY_CLASSES_ROOT\CLSID\{CLSID}]
"Vendor"={VendorGUID}
"Date"="yyyy-mm-dd"
"Version"="Major.Minor.Build.Number"
"SpecVersion"="Major.Minor.Build.Number"
"MetadataFormat"={MetadataFormatGUID}
"RequiresFullStream"=dword:1|0
"SupportsPadding"= dword:1|0
"FixedSize"=0

[HKEY_CLASSES_ROOT\CLSID\{CLSID}\InProcServer32]
@="drive:\path\yourdll.dll"
"ThreadingModel"="Apartment"

[HKEY_CLASSES_ROOT\CLSID\{CLSID}\{LCID}]
Author="Author's Name"
Description = " Metadata Description"
DeviceManufacturer ="Manufacturer Name"
DeviceModels="Device,Device"
FriendlyName="Friendly Name"
```

### Metadata Readers

The metadata reader registration also includes keys that describe how the reader can be embedded in a container format. A container format can be an image format such as TIFF or JPEG; it can also be another metadata format such as an IFD metadata block. Natively supported image container formats are listed in wincodec.idl; each image container format is defined as a GUID with a name that begins with GUID\_ContainerFormat. Natively supported metadata container formats are listed in wincodecsdk.idl; each metadata container format is defined as a GUID with a name that begins with GUID\_MetadataFormat.

The following keys register a container that the metadata reader supports, and the data needed to read from that container. Each container supported by the reader must be registered in this way.

``` syntax
[HKEY_CLASSES_ROOT\CLSID\{Reader CLSID}\Containers\{Container GUID}\0]
"Position"=dword:00000000
"Pattern"=hex:ff,ff,ff,...
"Mask"=hex:ff,ff,ff,...
"DataOffset"=dword:00000006
```

The Pattern key describes the binary pattern that is used to match the metadata block to the reader. When defining a pattern for your metadata reader, it should be reliable enough that a positive match means the metadata reader can understand the metadata in the metadata block being processed.

The DataOffset key describes the fixed offset of the metadata from the block header. This key is optional and, if not specified, means that the actual metadata cannot be located using a fixed offset from the block header.

### Metadata Writers

The metadata writer registration also includes keys that describe how to write out the header preceding the metadata content embedded in a container format. As with the reader, a container format can be an image format or another metadata block.

The following keys register a container that the metadata writer supports, and the data needed to write the header and metadata. Each container supported by the writer must be registered in this way.

``` syntax
[HKEY_CLASSES_ROOT\CLSID\{Writer CLSID}\Containers\{Container GUID}]
"WritePosition"=dword:00000000
"WriteHeader"=hex:ff,ff,ff,...
"WriteOffset"=dword:00000000
```

The WriteHeader key describes the binary pattern of the metadata block header to be written. This binary pattern coincides with the metadata format's reader Pattern key.

The WriteOffset key describes the fixed offset from the block header at which the metadata should be written. This key is optional and, if not specified, means that the actual metadata should not be written out with the header.

### Signing a Metadata Handler

All metadata handlers must be digitally signed to participate in the WIC discovery process. WIC will not load any handler that is not signed by a trusted certificate authority. For more information on digital signing, see [Introduction to Code Signing](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms537361(v=vs.85)).

## Special Considerations

The following sections include additional information you must consider when creating your own metadata handlers.

### PROPVARIANTS

WIC uses a [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) to represent a metadata item for both reading and writing. A PROPVARIANT provides a data type and data value for a metadata item used within a metadata format. As the writer of a metadata handler, you have a lot of flexibility on how data is stored in the metadata format and how data is represented within a metadata block. The following table provides guidelines to help you decide on the appropriate PROPVARIANT type to use in different situations.



| Metadata type is...          | Use PROPVARIANT type      | PROPVARIANT Property                                                                                                                                                                                                                                                           |
|------------------------------|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Empty or non-existent.       | VT\_EMPTY                 | Not applicable.                                                                                                                                                                                                                                                                |
| Undefined.                   | VT\_BLOB                  | Use the blob property to set the size and pointer to the BLOB object allocated using CoTaskMemAlloc.                                                                                                                                                                           |
| A metadata block.            | VT\_UNKNOWN               | This type uses the punkVal property.                                                                                                                                                                                                                                           |
| An array of types.           | VT\_VECTOR \| VT\_{type}  | Use the ca{type} property to set the count and pointer to the array allocated using CoTaskMemAlloc.                                                                                                                                                                            |
| An array of metadata blocks. | VT\_VECTOR \| VT\_VARIANT | Use the capropvar property to set the array of variants.                                                                                                                                                                                                                       |
| A signed rational value.     | VT\_I8                    | Use the hVal property to set the value. Set the high word to the denominator and the low word to the numerator.                                                                                                                                                                |
| A rational value.            | VT\_UI8                   | Use the uhVal property to set the value. Set the HighPart to the denominator and the LowPart to the numerator. Note that the LowPart is an unsigned int. The numerator should be converted from an unsigned int to an int to ensure that the sign bit is preserved if present. |



 

To avoid redundancy in representing array items, do not use safe arrays; use only simple arrays. This reduces the work an application needs to perform when interpreting [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) types.

Avoid using `VT_BYREF` and store values inline whenever possible. `VT_BYREF` is inefficient for small types (common for metadata items) and does not provide size information.

Before using a [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant), always call **PropVariantInit** to initialize the value. When you are finished with the PROPVARIANT, always call **PropVariantClear** to release any memory allocated for the variable.

### 8BIM Handlers

When writing a metadata handler for an 8BIM metadata block, you must use a signature that encapsulates both the 8BIM signature and the ID. For example, the native 8BIMIPTC metadata reader provides the following registry information for reader discovery:

``` syntax
[HKEY_CLASSES_ROOT\CLSID\{0010668C-0801-4DA6-A4A4-826522B6D28F}\Containers\{16100D66-8570-4BB9-B92D-FDA4B23ECE67}\0]
"Position"=dword:00000000
"Pattern"=hex:38,42,49,4d,04,04
"Mask"=hex:ff,ff,ff,ff,ff,ff
"DataOffset"=dword:00000006
```

The 8BIMIPTC reader has a registered pattern of 0x38, 0x42, 0x49, 0x4D, 0x04, 0x04. The first four bytes (0x38, 0x42, 0x49, 0x4D) are the 8BIM signature, and the last two bytes (0x04, 0x04) are the ID for the IPTC record.

So, to write an 8BIM metadata reader for resolution information, you would need a registered pattern of 0x38, 0x42, 0x49, 0x4D, 0x03, 0xED. Again, the first four bytes (0x38, 0x42, 0x49, 0x4D) are the 8BIM signature. The last two bytes (0x03, 0xED), however, are the resolution information ID as defined by the PSD format.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> <dt>

[WIC Metadata Overview](-wic-about-metadata.md)
</dt> <dt>

[Metadata Query Language Overview](-wic-codec-metadataquerylanguage.md)
</dt> <dt>

[Overview of Reading and Writing Image Metadata](-wic-codec-readingwritingmetadata.md)
</dt> <dt>

[How-to: Re-encode a JPEG Image with Metadata](-wic-codec-jpegmetadataencoding.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> </dl>

 

 
