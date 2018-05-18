---
Description: 'This topic describes how to write a custom Shell property handler for a Microsoft Media Foundation media source.'
ms.assetid: 'f8cf70ff-8324-4308-8adf-a145aa351ca9'
title: Custom Metadata Providers for Media Files
---

# Custom Metadata Providers for Media Files

This topic describes how to write a custom Shell property handler for a Microsoft Media Foundation media source.

> [!Note]  
> For background information about metadata providers in Media Foundation, see [Media Metadata](media-metadata.md). This topic discusses Shell property handlers; it does not describe the version 1 metadata interface, [**IMFMetadata**](imfmetadata.md).

 

Metadata is closely tied to the format of the file. In Media Foundation, file formats are represented by media sources. If you want to support metadata for a format that is not supported natively in Media Foundation, you must implement a custom media source with a property handler. The property handler enables the Shell property system to read and write metadata efficiently.

A property handler is a COM object that implements the following interfaces:

-   [**IInitializeWithStream**](shell.IInitializeWithStream)
-   [**IPropertyStore**](properties.IPropertyStore)

Optionally, it can also expose the following interface:

-   [**IPropertyStoreCapabilities**](properties.IPropertyStoreCapabilities)

If the Shell property system needs to get metadata for a file, it calls [**CoCreateInstance**](com.cocreateinstance) to create the property handler and then calls the appropriate read and write methods on the [**IPropertyStore**](properties.IPropertyStore) interface.

The Media Foundation pipeline uses a slightly different mechanism, because the pipeline gets the property handler directly from the media source. Instead of calling [**CoCreateInstance**](com.cocreateinstance) to create the property handler, the pipeline calls [**IMFGetService::GetService**](imfgetservice-getservice.md) on the media source, as described in the topic [Shell Metadata Providers](shell-metadata-providers.md).

To create a custom property handler, do the following:

-   Implement the [**IMFGetService**](imfgetservice.md) interface to expose [**IPropertyStore**](properties.IPropertyStore). The service GUID is **MF\_PROPERTY\_HANDLER\_SERVICE**.
-   If the media source will be used remotely, it must also expose the [**IPropertyStore**](properties.IPropertyStore) interface through the media source's **QueryInterface** method, in addition to [**IMFGetService**](imfgetservice.md).
-   To make the property handler available to the Shell property system, register the DLL for the property handler as described in [Registering and Distributing Property Handlers](properties.prophand_reg_dist).
-   The media source is registered separately, as described in [Scheme Handlers and Byte-Stream Handlers](scheme-handlers-and-byte-stream-handlers.md).

### Implementation Tips

For a list of metadata property keys, see [Metadata Properties for Media Files](metadata-properties-for-media-files.md).

Property handlers must be fast; they must provide efficient read and write access to the metadata. (Consider that the Shell may retrieve metadata from hundreds of files.) Therefore, do not call [**MFStartup**](mfstartup.md) from your property handler. The **MFStartup** function introduces startup latency, because it creates multiple work-queue threads and allocates global memory.

In a typical implementation, the property handler and the media source will share some of the same parsing code. However, a media source uses asynchronous [**IMFByteStream**](imfbytestream.md) calls for I/O, whereas the property handler uses the [**IStream**](stg.istream) interface. Media Foundation provides a helper object that wraps an **IStream**-based stream and exposes it as an **IMFByteStream** stream. To create the wrapper, call [**MFCreateMFByteStreamOnStream**](mfcreatemfbytestreamonstream.md).

When updating metadata, it is recommended to write the data directly to the original stream. This recommendation differs from the *copy-on-write* behavior of most property handlers, in which a copy of the data is modified. Media files can be very large, so copy-on-write is typically too slow for an efficient implementation. To disable copy-on-write, set the **ManualSafeSave** registry setting, as described in [Registering and Distributing Property Handlers](properties.prophand_reg_dist).

## Related topics

<dl> <dt>

[Media Metadata](media-metadata.md)
</dt> <dt>

[Media Sources](media-sources.md)
</dt> <dt>

[Writing a Custom Media Source](writing-a-custom-media-source.md)
</dt> </dl>

 

 



