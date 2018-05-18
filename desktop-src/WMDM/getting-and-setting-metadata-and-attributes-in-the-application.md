---
title: Getting and Setting Metadata and Attributes in the Application
description: Getting and Setting Metadata and Attributes in the Application
ms.assetid: '308a722d-1c65-41eb-a0e2-21171eb410d5'
keywords: ["Windows Media Device Manager,metadata", "Device Manager,metadata", "programming guide,metadata", "desktop applications,metadata", "creating Windows Media Device Manager applications,metadata", "metadata", "Windows Media Device Manager,attributes", "Device Manager,attributes", "programming guide,attributes", "desktop applications,attributes", "creating Windows Media Device Manager applications,attributes", "attributes"]
---

# Getting and Setting Metadata and Attributes in the Application

A general discussion of metadata and attributes is available in [Getting and Setting Metadata and Attributes](getting-and-setting-metadata-and-attributes.md). This section covers specific application method calls to retrieve or set values.

Applications can retrieve attributes or metadata about a specific storage by calling [**IWMDMStorage::GetAttributes**](iwmdmstorage-getattributes.md), [**IWMDMStorage2::GetAttributes2**](iwmdmstorage2-getattributes2.md), [**IWMDMStorage3::GetMetadata**](iwmdmstorage3-getmetadata.md) or [**IWMDMStorage4::GetSpecifiedMetadata**](iwmdmstorage4-getspecifiedmetadata.md). **GetMetadata** retrieves a full collection of all the metadata associated with a storage, and the application can then enumerate through all values or request specific values from the collection. **GetSpecifiedMetadata** creates a metadata object on behalf of the caller. The caller may request a subset of the available data by filling in the *ppwszPropNames* parameter with an array of the desired Windows Media Device Manager property strings, and the count of that array. The returned metadata object will be filled with those properties that could be retrieved. Those properties that couldn't be retrieved will be absent. Metadata is returned on a best-effort basis.

A device can set attributes or metadata on a storage by calling [**IWMDMStorage::SetAttributes**](iwmdmstorage-setattributes.md), [**IWMDMStorage2::SetAttributes2**](iwmdmstorage2-setattributes2.md), or [**IWMDMStorage3::SetMetadata**](iwmdmstorage3-setmetadata.md). Note that there is no guarantee that any values set will persist, because they may be stored in a non-persistent external file store, the values may not be supported, or, the device may not support the properties as writeable.

You can also get or set metadata about a device by calling [**IWMDMDevice3::GetProperty**](iwmdmdevice3-getproperty.md) or [**IWMDMDevice3::SetProperty**](iwmdmdevice3-setproperty.md). There is a separate table of device metadata constants listed at the end of [Metadata Constants](metadata-constants.md).

Examples of using these methods are given in each method's reference documentation.

## Related topics

<dl> <dt>

[**Creating a Windows Media Device Manager Application**](creating-a-windows-media-device-manager-application.md)
</dt> <dt>

[**Getting and Setting Metadata and Attributes**](getting-and-setting-metadata-and-attributes.md)
</dt> </dl>

 

 




