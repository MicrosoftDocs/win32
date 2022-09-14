---
title: Getting and Setting Metadata and Attributes
description: Getting and Setting Metadata and Attributes
ms.assetid: 83534998-4e7d-49b6-a160-ef9a0ddea5db
keywords:
- Windows Media Device Manager,attributes
- Device Manager,attributes
- desktop applications,attributes
- service providers,attributes
- programming guide,attributes
- attributes
- Windows Media Device Manager,metadata
- Device Manager,metadata
- desktop applications,metadata
- service providers,metadata
- programming guide,metadata
- metadata
ms.topic: article
ms.date: 05/31/2018
---

# Getting and Setting Metadata and Attributes

An application can get two kinds of information about a storage or device: attributes and metadata. Attributes are simpler Boolean values that generally describe file system information, such as whether a storage has child objects, whether it can be renamed, read, or deleted, and so on. Attributes are retrieved as flags values by calling [**IWMDMStorage::GetAttributes**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstorage-getattributes) or [**IWMDMStorage2::GetAttributes2**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstorage2-getattributes2). Attributes are set by calling [**IWMDMStorage3::SetMetadata**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstorage3-setmetadata).

An application can also request more complex data (numeric, string, or other data types) as *metadata*. Metadata values are identified by unique string names. Windows Media Device Manager defines a list of string constants that can be used to request values; these defined values are listed in [Metadata Constants](metadata-constants.md). A service provider can define its own constants, but a calling application must be aware of these definitions in order to request or set these custom metadata values. The application requests metadata by calling [**IWMDMStorage3::GetMetadata**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstorage3-getmetadata) or [**IWMDMStorage4::GetSpecifiedMetadata**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstorage4-getspecifiedmetadata).

An important aspect of getting and setting metadata and attributes is understanding where the retrieved values come from. The service provider or the device can get these values from many different places, including the following:

-   From the file header. For example, in an ASF file, the bit rate is stored in the file header.
-   From values set explicitly by the application when calling a method. These values may be saved in an external metadata store in the service provider or the device. This store may or may not persist when the device disconnects or turns off. For example, the play count and user star ratings are typically stored in external stores on the computer or device.
-   By examining information provided by the file system. For example, whether a file is read-only or whether a folder has children.
-   By opening and parsing the file data.

It is important to realize that a property might be stored in more than one location (within the file header and also in a local store), and that it may or may not be editable. For example, changing a file description may or may not be persistent; if the service provider stores the description locally, it will not persist on the device. Similarly, if the file description is taken from the file header, modifying this will only be persistent if the service provider or device opens and modifies the header data. Most applications make a best attempt by changing desired values, but do not depend on any properties to be persistently changed.

More information on getting and setting values is given in the appropriate sections for application developers and service provider developers later in the documentation.

## Related topics

<dl> <dt>

[**Tasks Common to Applications and Service Providers**](tasks-common-to-applications-and-service-providers.md)
</dt> </dl>

 

 




